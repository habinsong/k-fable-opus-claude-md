"""교정안(Edit)을 모아 글에 적용하고, 지운 자리를 다듬는다. 새 낱말을 만들어 넣지 않는다."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Sequence, Tuple

from .detect import analyze
from .model import TIER_RANK, Analysis, Edit


@dataclass
class PolishResult:
    original: str
    text: str
    tier: str
    edits: List[Edit]
    skipped: int
    before: Analysis
    after: Analysis
    notes: List[str] = field(default_factory=list)
    eol: str = "\n"

    @property
    def output(self) -> str:
        """원래 줄바꿈 방식(LF 또는 CRLF)을 되살린 교정문."""
        return self.text.replace("\n", self.eol) if self.eol != "\n" else self.text


def collect(analysis: Analysis, tier: str) -> List[Edit]:
    limit = TIER_RANK[tier]
    edits = [f.edit for f in analysis.findings if f.edit and TIER_RANK[f.edit.tier] <= limit]
    return sorted(edits, key=lambda e: (e.start, -(e.end - e.start)))


def resolve(edits: Sequence[Edit]) -> Tuple[List[Edit], int]:
    """겹치는 교정안은 앞에 온 긴 것을 남긴다."""
    kept: List[Edit] = []
    last = -1
    skipped = 0
    for e in edits:
        if e.start < last or (kept and e.start == kept[-1].start and e.end == kept[-1].end):
            skipped += 1
            continue
        kept.append(e)
        last = e.end
    return kept, skipped


def apply(text: str, edits: Sequence[Edit]) -> Tuple[str, List[int]]:
    """교정안을 적용하고, 바뀐 자리의 새 위치 목록도 돌려준다."""
    out: List[str] = []
    sites: List[int] = []
    pos = 0
    nxt = {i: (edits[i + 1].start if i + 1 < len(edits) else len(text) + 1) for i in range(len(edits))}
    length = 0
    for i, e in enumerate(edits):
        piece = text[pos:e.start]
        out.append(piece)
        length += len(piece)
        out.append(e.replacement)
        sites.append(length)
        length += len(e.replacement)
        pos = e.end
        if e.recap and e.replacement == "" and nxt[i] > e.end and e.end < len(text) and text[e.end].islower():
            out.append(text[e.end].upper())
            length += 1
            pos = e.end + 1
    out.append(text[pos:])
    return "".join(out), sites


_FENCE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
_EMPTY_ITEM = re.compile(r"^[ \t]*(?:[-*+•]|\d+[.)])[ \t]*$")


def tidy(text: str, sites: Sequence[int], *, lead_newlines: bool) -> str:
    """지운 자리 근처의 공백, 문장 부호 앞 공백, 빈 글머리, 연속 빈 줄을 정리한다.

    공백 정리는 교정이 일어난 자리 둘레에서만 한다. 그 밖의 글은 건드리지 않는다.
    """
    chars = list(text)
    for p in sorted(set(sites), reverse=True):
        n = len(chars)
        p = min(p, n)
        a = p
        while a > 0 and chars[a - 1] in " \t":
            a -= 1
        b = p
        while b < n and chars[b] in " \t":
            b += 1
        left = chars[a - 1] if a > 0 else "\n"
        right = chars[b] if b < n else "\n"
        if left == "\n":
            new = chars[a:p]                       # 들여쓰기는 두고, 지운 뒤에 남은 공백만 걷는다
        elif right == "\n":
            new = []                               # 줄 끝 공백
        elif right in ",.;:!?)]}":
            new = []                               # 문장 부호 앞 공백
        elif left in "([{\"'\u201c\u2018":
            new = []
        elif b - a > 0:
            new = [" "]                            # 공백 여러 개는 하나로
        else:
            new = []
        chars[a:b] = new
    lines = "".join(chars).split("\n")
    out: List[str] = []
    in_fence = False
    for line in lines:
        if _FENCE.match(line):
            in_fence = not in_fence
        if not in_fence and _EMPTY_ITEM.match(line):
            continue
        out.append(line)
    joined = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return joined if lead_newlines else joined.lstrip("\n")


def polish(text: str, *, tier: str = "standard", genre: str = "general", lang: str = "auto",
           ban=()) -> PolishResult:
    if tier not in TIER_RANK or tier == "none":
        raise ValueError(f"tier는 safe, standard, strong 중 하나여야 한다: {tier}")
    crlf = text.count("\r\n") * 2 > text.count("\n") > 0
    eol = "\r\n" if crlf else "\n"
    text = text.replace("\r\n", "\n") if crlf else text
    before = analyze(text, genre=genre, lang=lang, ban=ban)
    edits, skipped = resolve(collect(before, tier))
    if not edits:
        return PolishResult(text, text, tier, [], skipped, before, before,
                            ["이 단계에서 자동으로 고칠 것이 없다."], eol)
    new, sites = apply(text, edits)
    new = tidy(new, sites, lead_newlines=text.startswith("\n"))
    new = new.rstrip("\n ") + ("\n" if text.endswith("\n") else "")
    if text.strip() and not new.strip():
        return PolishResult(text, text, tier, [], len(edits), before, before,
                            ["교정하면 글이 모두 사라져서 원문을 그대로 두었다."], eol)
    after = analyze(new, genre=genre, lang=lang, ban=ban)
    return PolishResult(text, new, tier, edits, skipped, before, after, [], eol)
