"""문서를 읽어 검출 항목(Finding) 목록과 분석 점수(Analysis)를 만든다. 교정은 하지 않고 교정안(Edit)만 붙인다."""
from __future__ import annotations

import bisect
import re
import statistics
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from . import analyzers, score as scoring
from .model import Analysis, Ctx, Edit, Finding, Rule, TIER_RANK, line_starts, weigh
from .rules import load_rules
from .textutil import (count_units, detect_lang, excerpt, in_spans, locate, mask, paragraph_spans,
                       protected_spans, sentence_spans)

CLUSTER_WINDOW = 400


def user_rules(phrases: Iterable[str]) -> List[Rule]:
    """작성자가 직접 정한 금지어. 글자 그대로 찾는다(정규식 아님)."""
    out = []
    for i, p in enumerate(x.strip() for x in phrases if x and x.strip()):
        out.append(Rule(id=f"user.ban.{i + 1}", lang="any", category="vocab", grade="A",
                        pattern=re.compile(re.escape(p), re.I), note=f"작성자가 지정한 금지어: {p}", weight=1.0))
    return out


def _sentence_at(sents: Sequence[Tuple[int, int]], starts: Sequence[int], pos: int) -> Optional[Tuple[int, int]]:
    i = bisect.bisect_right(starts, pos) - 1
    if i >= 0 and sents[i][0] <= pos <= sents[i][1]:
        return sents[i]
    return None


def _build_edit(rule: Rule, m: "re.Match[str]", ctx: Ctx, spans, sents, sent_starts) -> Optional[Edit]:
    if rule.tier == "none" or rule.repl is None:
        return None
    if rule.fix_guard and not rule.fix_guard(m, ctx):
        return None
    text = ctx.text
    if rule.scope == "sentence":
        lead = len(m.group(0)) - len(m.group(0).lstrip())
        sp = _sentence_at(sents, sent_starts, m.start() + lead)
        if sp is None or m.start() + lead - sp[0] > 3:
            return None
        start, end, repl = sp[0], sp[1], ""
        while end < len(text) and text[end] in " \t":
            end += 1
    else:
        start, end = m.span()
        repl = rule.repl(m, ctx) if callable(rule.repl) else m.expand(rule.repl)
        if repl is None:
            return None
    if rule.protect and in_spans(spans, start, end):
        return None
    recap = bool(rule.recap and repl == "" and _starts_sentence(rule, m, ctx))
    return Edit(start, end, repl, rule.id, rule.tier, recap=recap, before=text[start:end])


def _starts_sentence(rule: Rule, m, ctx: Ctx) -> bool:
    from .fixers import at_sentence_start
    return at_sentence_start(m, ctx)


def _apply_filters(found: List[Tuple[Rule, Finding]]) -> List[Finding]:
    """min_count와 cluster 조건을 적용한다."""
    counts: Dict[str, int] = {}
    for r, f in found:
        counts[r.id] = counts.get(r.id, 0) + 1
    kept = [(r, f) for r, f in found if counts[r.id] >= r.min_count]
    clustered = sorted(((r, f) for r, f in kept if r.cluster > 0), key=lambda x: x[1].start)
    positions = [f.start for _, f in clustered]
    drop = set()
    for r, f in clustered:
        lo = bisect.bisect_left(positions, f.start - CLUSTER_WINDOW)
        hi = bisect.bisect_right(positions, f.start + CLUSTER_WINDOW)
        if hi - lo - 1 < r.cluster:
            drop.add(id(f))
    return [f for r, f in kept if id(f) not in drop]


def _shadow(findings: List[Finding]) -> None:
    """겹치는 검출 항목은 가장 가중치가 큰 하나만 점수에 반영한다. 가려진 항목의 교정안은 그대로 둔다."""
    items = sorted((f for f in findings if f.end > f.start), key=lambda f: (f.start, -f.end))
    group: List[Finding] = []
    group_end = -1

    def close() -> None:
        if len(group) > 1:
            best = max(group, key=lambda f: (f.weight, f.fixable, f.end - f.start))
            for f in group:
                if f is not best:
                    f.shadowed = True
    for f in items:
        if group and f.start >= group_end:
            close()
            group.clear()
            group_end = -1
        group.append(f)
        group_end = max(group_end, f.end)
    close()


def _metrics(masked: str, sents: Sequence[Tuple[int, int]], units: int) -> Dict[str, object]:
    lens = [len(masked[a:b].split()) for a, b in sents]
    return {
        "avg_sentence_units": round(statistics.mean(lens), 1) if lens else 0,
        "sentence_length_cv": round(statistics.pstdev(lens) / statistics.mean(lens), 2) if len(lens) > 1 and statistics.mean(lens) else 0,
        "em_dashes_per_1000_units": round(1000 * len(re.findall("[—―]", masked)) / max(units, 1), 1),
        "note": "문장 길이 변동(burstiness)은 약한 지표라 점수에 넣지 않는다(docs/research.md 6절).",
    }


def analyze(text: str, *, genre: str = "general", lang: str = "auto", ban: Iterable[str] = (),
            quotes: bool = False) -> Analysis:
    spans = protected_spans(text, quotes)
    masked = mask(text, spans)
    sents = sentence_spans(masked)
    sent_starts = [s[0] for s in sents]
    paras = paragraph_spans(masked)
    units = count_units(masked)
    ctx = Ctx(text, masked, genre)
    starts = line_starts(text)
    found: List[Tuple[Rule, Finding]] = []
    for rule in load_rules(lang) + user_rules(ban):
        src = masked if rule.protect else text
        gmult = rule.genre
        for m in rule.pattern.finditer(src):
            if m.start() == m.end() or (rule.guard and not rule.guard(m, ctx)):
                continue
            edit = _build_edit(rule, m, ctx, spans, sents, sent_starts)
            ln, col = locate(starts, m.start())
            f = Finding(rule_id=rule.id, category=rule.category, grade=rule.grade, start=m.start(), end=m.end(),
                        text=text[m.start():m.end()][:90], line=ln, col=col,
                        weight=weigh(rule.category, rule.grade, rule.weight, gmult, genre), note=rule.note,
                        sugg=rule.sugg, tier=rule.tier if edit else "none", fixable=edit is not None,
                        lang=rule.lang, edit=edit)
            found.append((rule, f))
    findings = _apply_filters(found)
    for f in analyzers.run_all(text, masked, sents, paras, units, genre):
        f.line, f.col = locate(starts, f.start)
        findings.append(f)
    _shadow(findings)
    findings.sort(key=lambda f: (f.start, -f.weight))
    res = scoring.compute(findings, units)
    notes: List[str] = []
    if units < 40:
        notes.append("표본이 짧아(40단위 미만) 점수가 불안정하다.")
    if not findings:
        notes.append("검출된 항목이 없다. 검출 항목이 없다고 사람이 쓴 글이라는 보증은 아니다.")
    return Analysis(lang=detect_lang(masked), genre=genre, units=units, sentences=len(sents),
                    paragraphs=len(paras), score=int(res["score"]), label_ko=str(res["label_ko"]),
                    label_en=str(res["label_en"]), density=float(res["density"]), residue=float(res["residue"]),
                    categories=dict(res["categories"]), findings=findings,
                    paragraph_scores=scoring.paragraph_scores(findings, masked, paras),
                    metrics=_metrics(masked, sents, units), notes=notes)


def excerpt_of(text: str, f: Finding) -> str:
    return excerpt(text, f.start, f.end)


def tier_ok(edit: Edit, tier: str) -> bool:
    return TIER_RANK[edit.tier] <= TIER_RANK[tier]
