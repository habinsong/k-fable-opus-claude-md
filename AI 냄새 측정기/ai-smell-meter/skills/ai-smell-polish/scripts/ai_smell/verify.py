"""원문과 윤문본을 대조한다. 사실이 그대로인지, 얼마나 바뀌었는지, 새 신호가 생기지 않았는지 본다.

이 검증은 의미를 증명하지 못한다. 숫자, 주소, 코드, 인용, 영문 고유명사가 그대로인지와
변경 규모를 기계적으로 볼 뿐이다. 의미가 같은지는 사람이 읽어서 판단한다.
"""
from __future__ import annotations

import difflib
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from .detect import analyze
from .textutil import mask, protected_spans, sentence_spans

NUMBER = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*")
URL = re.compile(r"https?://[^\s<>\"')\]]+")
FENCE = re.compile(r"^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?(?:^[ \t]*\1[ \t]*$|\Z)", re.S | re.M)
INLINE = re.compile(r"`[^`\n]+`")
QUOTE = re.compile(r"\"([^\"\n]{8,})\"|“([^”\n]{8,})”|「([^」\n]{4,})」")
LATIN = re.compile(r"\b[A-Za-z][A-Za-z0-9]*(?:[-_.][A-Za-z0-9]+)*\b")
PARTICLE = re.compile(r"(?:에서는|에서의|에서|으로는|으로|에게|까지|부터|보다|처럼|께서|이다|입니다|은|는|이|가|을|를|의|에|로|와|과|도|만)$")
STOP_EN = {"The", "A", "An", "It", "This", "That", "These", "Those", "In", "On", "At", "We", "I", "He", "She",
           "They", "You", "There", "Here", "If", "When", "While", "As", "For", "And", "But", "Or", "So", "To",
           "Of", "By", "With", "From", "Our", "My", "Your", "Its", "Their", "His", "Her", "What", "Why", "How"}


@dataclass
class VerifyResult:
    status: str                      # PASS, WARN, CONFIRM, FAIL
    change_rate: float
    length_ratio: float
    score_before: int
    score_after: int
    numbers_missing: List[str] = field(default_factory=list)
    numbers_added: List[str] = field(default_factory=list)
    urls_missing: List[str] = field(default_factory=list)
    code_missing: List[str] = field(default_factory=list)
    quotes_missing: List[str] = field(default_factory=list)
    names_missing: List[str] = field(default_factory=list)
    names_added: List[str] = field(default_factory=list)
    new_signals: List[str] = field(default_factory=list)
    dropped_terms: List[str] = field(default_factory=list)
    messages: List[Tuple[str, str]] = field(default_factory=list)


def _norm_number(s: str) -> str:
    s = s.replace(",", "")
    if re.fullmatch(r"\d+", s):
        return str(int(s))
    return s.rstrip("0").rstrip(".") if "." in s else s


def numbers(text: str) -> Counter:
    return Counter(_norm_number(m.group(0)) for m in NUMBER.finditer(text))


def code_pieces(text: str) -> List[str]:
    fences = [m.group(0).strip() for m in FENCE.finditer(text)]
    rest = FENCE.sub(" ", text)
    return fences + [m.group(0) for m in INLINE.finditer(rest)]


def names(text: str) -> set:
    """영문 고유명사 후보: 전부 대문자, 안에 대문자, 숫자 포함, 문장 첫머리가 아닌 대문자 시작."""
    masked = mask(text, protected_spans(text))
    starts = {s for s, _ in sentence_spans(masked)}
    out = set()
    for m in LATIN.finditer(masked):
        w = m.group(0)
        if len(w) < 2:
            continue
        strong = w.isupper() or any(c.isupper() for c in w[1:]) or any(c.isdigit() for c in w)
        if strong or (w[0].isupper() and m.start() not in starts and w not in STOP_EN):
            out.add(w)
    return out


def _tokens(text: str) -> List[str]:
    return re.findall(r"\S+", text)


def change_rate(a: str, b: str) -> float:
    """원문 어절 중 바뀌거나 사라진 비율. 어절 단위로 전체를 맞춘다.

    아주 긴 글(곱이 4천만을 넘음)은 줄 단위로 먼저 맞추고 바뀐 덩어리만 어절 단위로 본다.
    """
    ta, tb = _tokens(a), _tokens(b)
    if not ta:
        return 0.0
    if len(ta) * len(tb) <= 40_000_000:
        ops = difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes()
        changed = sum(i2 - i1 for tag, i1, i2, _, _ in ops if tag != "equal")
        return min(1.0, changed / len(ta))
    la, lb = a.split("\n"), b.split("\n")
    changed = 0
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        x, y = _tokens(" ".join(la[i1:i2])), _tokens(" ".join(lb[j1:j2]))
        for t2, a1, a2, _, _ in difflib.SequenceMatcher(None, x, y, autojunk=False).get_opcodes():
            if t2 != "equal":
                changed += a2 - a1
    return min(1.0, changed / len(ta))


def _stems(text: str) -> Counter:
    c: Counter = Counter()
    for t in re.findall(r"[가-힣]{2,}|[A-Za-z]{7,}", text):
        c[PARTICLE.sub("", t) if re.match(r"[가-힣]", t) else t.lower()] += 1
    return c


def dropped_terms(a: str, b: str, limit: int = 12) -> List[str]:
    sa, sb = _stems(a), _stems(b)
    gone = [w for w in sa if w not in sb and len(w) >= 2]
    return gone[:limit]


def verify(original: str, revised: str, *, genre: str = "general", lang: str = "auto") -> VerifyResult:
    na, nb = numbers(original), numbers(revised)
    miss_n = sorted((na - nb).elements())
    add_n = sorted((nb - na).elements())
    urls_a, urls_b = set(URL.findall(original)), set(URL.findall(revised))
    code_missing = [c for c in code_pieces(original) if c not in revised]
    quotes = [next(g for g in m.groups() if g) for m in QUOTE.finditer(original)]
    quotes_missing = [q for q in quotes if q not in revised]
    la, lb = names(original), names(revised)
    before, after = analyze(original, genre=genre, lang=lang), analyze(revised, genre=genre, lang=lang)
    ids_before = {f.rule_id for f in before.findings if f.weight > 0 and not f.shadowed}
    new_signals = sorted({f.rule_id for f in after.findings if f.weight > 0 and not f.shadowed} - ids_before)
    rate = change_rate(original, revised)
    ratio = len(re.sub(r"\s", "", revised)) / max(1, len(re.sub(r"\s", "", original)))
    r = VerifyResult("PASS", round(rate, 3), round(ratio, 3), before.score, after.score,
                     miss_n, add_n, sorted(urls_a - urls_b), code_missing, quotes_missing,
                     sorted(la - lb), sorted(lb - la), new_signals, dropped_terms(original, revised))
    msgs: List[Tuple[str, str]] = []
    if miss_n or add_n:
        msgs.append(("FAIL", f"숫자가 달라졌다: 빠짐 {miss_n[:8]}, 늘어남 {add_n[:8]}"))
    if r.urls_missing:
        msgs.append(("FAIL", f"주소가 빠졌다: {r.urls_missing[:4]}"))
    if code_missing:
        msgs.append(("FAIL", f"코드가 바뀌거나 빠졌다: {[c[:40] for c in code_missing[:3]]}"))
    if quotes_missing:
        msgs.append(("FAIL", f"직접 인용이 바뀌었다: {[q[:40] for q in quotes_missing[:3]]}"))
    if rate > 0.5:
        msgs.append(("CONFIRM", f"변경률 {rate:.0%}가 50%를 넘는다. 지워진 것이 군더더기뿐인지 필자 확인이 필요하다."))
    elif rate > 0.3:
        msgs.append(("WARN", f"변경률 {rate:.0%}가 30%를 넘는다."))
    if r.names_missing or r.names_added:
        msgs.append(("WARN", f"영문 고유명사 후보가 달라졌다: 빠짐 {r.names_missing[:6]}, 새로 생김 {r.names_added[:6]}"))
    if new_signals:
        msgs.append(("WARN", f"원문에 없던 신호가 생겼다: {new_signals[:6]}"))
    if ratio < 0.6:
        msgs.append(("WARN", f"분량이 {1 - ratio:.0%} 줄었다. 의미가 빠졌는지 확인한다."))
    if after.score >= before.score and before.score > 0:
        msgs.append(("WARN", "지수가 줄지 않았다."))
    order = {"PASS": 0, "WARN": 1, "CONFIRM": 2, "FAIL": 3}
    r.messages = msgs
    for lvl, _ in msgs:
        if order[lvl] > order[r.status]:
            r.status = lvl
    return r


def to_dict(r: VerifyResult) -> Dict[str, object]:
    return dict(r.__dict__)


def facts_for_prompt(text: str, limit: int = 40) -> Dict[str, List[str]]:
    """프롬프트에 '바꾸지 말 것'으로 실어 보낼 항목."""
    nums = [n for n, _ in numbers(text).most_common(limit)]
    return {"numbers": nums, "urls": sorted(set(URL.findall(text)))[:limit],
            "names": sorted(names(text))[:limit], "code": [c[:60] for c in code_pieces(text)[:limit]],
            "quotes": [next(g for g in m.groups() if g)[:60] for m in QUOTE.finditer(text)][:limit]}

