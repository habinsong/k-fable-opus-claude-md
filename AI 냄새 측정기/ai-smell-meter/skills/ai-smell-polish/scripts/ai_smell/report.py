"""분석, 교정, 대조, 규칙 목록을 사람이 읽는 글과 JSON으로 그린다."""
from __future__ import annotations

import difflib
from typing import Any, Dict, List, Sequence

from .fix import PolishResult
from .i18n import t
from .model import CATEGORIES, Analysis, Finding, Rule
from .textutil import excerpt
from .verify import VerifyResult, to_dict as verify_dict

BAR = 10


def _cat_name(key: str, ui: str) -> str:
    c = CATEGORIES[key]
    return c.ko if ui == "ko" else c.en


def _bar(value: float, cap: float) -> str:
    if cap <= 0:
        return "·" * BAR
    n = max(0, min(BAR, round(BAR * value / cap)))
    return "█" * n + "░" * (BAR - n)


def _line_range(text: str, start: int, end: int) -> str:
    a = text.count("\n", 0, start) + 1
    b = text.count("\n", 0, end) + 1
    return f"{a}" if a == b else f"{a}~{b}"


def _rank(f: Finding) -> tuple:
    return (-f.weight, f.start)


def finding_dict(f: Finding, text: str) -> Dict[str, Any]:
    return {"rule": f.rule_id, "category": f.category, "grade": f.grade, "line": f.line, "col": f.col,
            "start": f.start, "end": f.end, "text": f.text, "weight": f.weight, "shadowed": f.shadowed,
            "note": f.note, "suggestion": f.sugg, "autofix_tier": f.tier if f.fixable else None,
            "context": excerpt(text, f.start, f.end)}


def analysis_dict(a: Analysis, text: str) -> Dict[str, Any]:
    return {"version": 1, "score": a.score, "label": {"ko": a.label_ko, "en": a.label_en}, "lang": a.lang,
            "genre": a.genre, "units": a.units, "sentences": a.sentences, "paragraphs": a.paragraphs,
            "density": a.density, "residue": a.residue, "categories": a.categories, "metrics": a.metrics,
            "notes": a.notes, "paragraph_scores": a.paragraph_scores,
            "findings": [finding_dict(f, text) for f in a.findings],
            "disclaimer": t("en", "disclaimer")}


def render_analysis(a: Analysis, text: str, ui: str = "ko", top: int = 12, show_all: bool = False) -> str:
    out: List[str] = []
    label = a.label_ko if ui == "ko" else a.label_en
    out.append(f"{t(ui, 'title')} {a.score}/100 — {label}")
    out.append(f"  {t(ui, 'target')}: {t(ui, 'lang_' + a.lang)} · {a.units}{t(ui, 'units')} · "
               f"{a.sentences}{t(ui, 'sentences')} · {a.paragraphs}{t(ui, 'paragraphs')} · "
               f"{t(ui, 'genre')} {t(ui, 'genre_' + a.genre)}")
    out.append(f"  ※ {t(ui, 'disclaimer')}")
    for n in a.notes:
        out.append(f"  ! {n}")
    scored = [f for f in a.findings if not f.shadowed and f.weight > 0]
    if a.categories:
        out.append("")
        out.append(t(ui, "categories"))
        for key, val in sorted(a.categories.items(), key=lambda kv: -kv[1]):
            cap = CATEGORIES[key].cap or max(val, 1.0)
            out.append(f"  {_cat_name(key, ui):<14}{_bar(val, cap)}  {val}")
    if scored:
        shown = sorted(scored, key=_rank)[: (len(scored) if show_all else top)]
        out.append("")
        out.append(f"{t(ui, 'findings')} ({len(shown)}/{len(scored)})")
        for f in shown:
            mark = f"  ✎{f.tier}" if f.fixable else ""
            ctx = f.text.replace("\n", " ")[:60]
            out.append(f"  {_line_range(text, f.start, f.end):>5} [{f.grade}] {_cat_name(f.category, ui)} · "
                       f"{ctx!r}{mark}")
            out.append(f"        {f.note}" + (f"  → {f.sugg}" if f.sugg else ""))
    elif not a.notes:
        out.append("")
        out.append(t(ui, "none_found"))
    paras = sorted((p for p in a.paragraph_scores if p["score"] > 0), key=lambda p: -p["score"])[:5]
    if len(a.paragraph_scores) > 1 and paras:
        out.append("")
        out.append(t(ui, "paragraphs_h"))
        for p in paras:
            out.append(f"  ¶{p['index']} ({_line_range(text, p['start'], p['end'])}) "
                       f"{p['score']}  [{p['findings']}]")
    info = [f for f in a.findings if f.category == "info" or (f.weight == 0 and not f.shadowed)]
    if info:
        names = sorted({f.rule_id for f in info})
        out.append("")
        out.append(f"{t(ui, 'info_h')}: " + ", ".join(f"{n}×{sum(1 for f in info if f.rule_id == n)}" for n in names))
    out.append("")
    out.append(f"{t(ui, 'next')}: {t(ui, 'next_polish')}")
    return "\n".join(out)


def verify_lines(v: VerifyResult, ui: str = "ko") -> List[str]:
    out = [f"{t(ui, 'verify')}: {v.status}  ({t(ui, 'change_rate')} {v.change_rate:.0%}, "
           f"{t(ui, 'score_change')} {v.score_before} → {v.score_after})"]
    for lvl, msg in v.messages:
        out.append(f"  [{lvl}] {msg}")
    if v.dropped_terms:
        out.append(f"  [INFO] 사라진 낱말(참고): {', '.join(v.dropped_terms[:10])}" if ui == "ko"
                   else f"  [INFO] words that disappeared (reference): {', '.join(v.dropped_terms[:10])}")
    return out


def render_verify(v: VerifyResult, ui: str = "ko") -> str:
    return "\n".join(verify_lines(v, ui) + ["", t(ui, "limits")])


def render_polish_summary(res: PolishResult, ver: VerifyResult, ui: str = "ko") -> str:
    b, a = res.before, res.after
    lb, la = (b.label_ko, a.label_ko) if ui == "ko" else (b.label_en, a.label_en)
    remaining = len([f for f in a.findings if not f.shadowed and f.weight > 0])
    out = [f"{t(ui, 'summary')}: {t(ui, 'score_change')} {b.score} ({lb}) → {a.score} ({la}) · "
           f"{t(ui, 'edits')} {len(res.edits)}{t(ui, 'count')} ({t(ui, 'tier')} {res.tier}) · "
           f"{t(ui, 'change_rate')} {ver.change_rate:.0%}"]
    if remaining:
        out.append(f"  {t(ui, 'remaining')} {remaining}{t(ui, 'count')}: {t(ui, 'remaining_hint')}")
    for n in res.notes:
        out.append(f"  ! {n}")
    if res.edits:
        out.append(f"  {t(ui, 'changes')}:")
        for e in res.edits[:30]:
            line = res.original.count("\n", 0, e.start) + 1
            after = e.replacement.replace("\n", " ") or t(ui, "deleted")
            out.append(f"    {line:>4}행 {e.rule_id}: {e.before.strip()[:50]!r} → {after[:50]!r}")
        if len(res.edits) > 30:
            out.append(f"    … +{len(res.edits) - 30}")
        if any(e.tier == "strong" for e in res.edits):
            out.append(f"  ! {t(ui, 'needs_review')}")
    out += verify_lines(ver, ui)
    out.append(f"  {t(ui, 'limits')}")
    return "\n".join(out)


def polish_dict(res: PolishResult, ver: VerifyResult) -> Dict[str, Any]:
    return {"version": 1, "tier": res.tier, "corrected": res.output,
            "before": {"score": res.before.score, "label": res.before.label_ko},
            "after": {"score": res.after.score, "label": res.after.label_ko},
            "edits": [{"rule": e.rule_id, "tier": e.tier, "before": e.before, "after": e.replacement,
                       "start": e.start, "end": e.end} for e in res.edits],
            "remaining": [finding_dict(f, res.text) for f in res.after.findings
                          if not f.shadowed and f.weight > 0],
            "verify": verify_dict(ver)}


def unified_diff(a: str, b: str) -> str:
    return "".join(difflib.unified_diff(a.splitlines(True), b.splitlines(True), "original", "corrected"))


def render_rules(rules: Sequence[Rule], ui: str = "ko") -> str:
    out = [f"{t(ui, 'rules_h')} ({len(rules)})"]
    for r in rules:
        fix = r.tier if (r.tier != "none" and r.repl is not None) else t(ui, "no_fix")
        out.append(f"  {r.id:<36} {r.lang:<3} {_cat_name(r.category, ui):<12} {t(ui, 'grade')} {r.grade}  "
                   f"{t(ui, 'tier_h')} {fix}  {r.note}")
    return "\n".join(out)


def rules_markdown(rules: Sequence[Rule]) -> str:
    out = ["# 규칙 목록 (자동 생성)", "",
           "`ai-smell rules --format md`가 만든다. 직접 고치지 말고 `ai_smell/rules/`를 고친 뒤 다시 만든다.", "",
           "| id | 언어 | 범주 | 등급 | 가중치 | 교정 | 설명 |", "|---|---|---|---|---|---|---|"]
    for r in rules:
        w = CATEGORIES[r.category].weight if r.weight is None else r.weight
        fix = r.tier if (r.tier != "none" and r.repl is not None) else "-"
        note = r.note.replace("|", "/")
        out.append(f"| `{r.id}` | {r.lang} | {CATEGORIES[r.category].ko} | {r.grade} | {w} | {fix} | {note} |")
    return "\n".join(out) + "\n"
