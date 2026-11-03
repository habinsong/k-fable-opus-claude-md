"""입력 읽기, 보호 구간 가리기, 문장·문단 나누기, 단위 세기. 규칙은 알지 못한다."""
from __future__ import annotations

import bisect
import re
import sys
from typing import List, Optional, Sequence, Tuple

MAX_BYTES = 2_000_000
IGNORE_START = "ai-smell:ignore-start"
IGNORE_END = "ai-smell:ignore-end"

HANGUL = re.compile(r"[가-힣]")
LATIN = re.compile(r"[A-Za-z]")
WORDISH = re.compile(r"[A-Za-z0-9가-힣]")
EMOJI_CLASS = ("[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF☀-➿⭐⬆⬅⬇"
               "✅❌✨❗❓❤‼⁉]️?")
EMOJI = re.compile(EMOJI_CLASS)

_PROTECT = [
    re.compile(r"\A---\n.*?\n---[ \t]*(?:\n|\Z)", re.S),                # 앞머리(front matter)
    re.compile(r"^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?(?:^[ \t]*\1[ \t]*$|\Z)", re.S | re.M),  # 코드 울타리
    re.compile(r"<!--.*?-->", re.S),
    re.compile(r"`[^`\n]+`"),
    re.compile(r"https?://[^\s<>\"')\]]+"),
    re.compile(r"(?<=\]\()[^)\s]+(?=\))"),
    re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    re.compile(r"<[A-Za-z/][^>\n]*>"),
    re.compile(r"\$\$.*?\$\$", re.S),
    re.compile(r"^>.*$", re.M),                                        # 인용 블록
]
_ABBREV = {"mr", "mrs", "ms", "dr", "prof", "sr", "jr", "st", "vs", "etc", "e.g", "i.e", "fig", "no",
           "inc", "ltd", "co", "u.s", "u.k", "cf", "approx", "al", "vol", "pp", "ca", "est"}
_END = re.compile(r"[.!?…。！？]+[\"'”’)\]」』]*")


def read_input(path: Optional[str], text: Optional[str]) -> str:
    """파일, 표준 입력('-'), 직접 문자열 중 하나에서 읽는다."""
    if text is not None:
        return text
    if path in (None, "-"):
        return sys.stdin.read(MAX_BYTES)
    with open(path, "rb") as fh:
        raw = fh.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError(f"입력이 {MAX_BYTES}바이트를 넘는다: {path}")
    return raw.decode("utf-8", errors="replace")


def detect_lang(text: str) -> str:
    """'ko', 'en', 'mixed' 중 하나. 한글과 라틴 글자 수로 정한다."""
    h, e = len(HANGUL.findall(text)), len(LATIN.findall(text))
    if h + e == 0:
        return "en"
    share = h / (h + e)
    return "ko" if share >= 0.7 else "en" if share <= 0.15 else "mixed"


def protected_spans(text: str, extra_quotes: bool = False) -> List[Tuple[int, int]]:
    """고치거나 세지 않을 구간(코드, URL, 인용 블록, 무시 표시 등)을 합쳐 돌려준다."""
    spans: List[Tuple[int, int]] = []
    for rx in _PROTECT:
        spans.extend(m.span() for m in rx.finditer(text))
    pos = 0
    while True:
        s = text.find(IGNORE_START, pos)
        if s < 0:
            break
        e = text.find(IGNORE_END, s)
        e = len(text) if e < 0 else e + len(IGNORE_END)
        spans.append((s, e))
        pos = e
    if extra_quotes:
        spans.extend(m.span() for m in re.finditer(r"\"[^\"\n]{20,}\"|“[^”\n]{20,}”", text))
    return SpanList(merge_spans(spans))


def merge_spans(spans: Sequence[Tuple[int, int]]) -> List[Tuple[int, int]]:
    out: List[List[int]] = []
    for s, e in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [(a, b) for a, b in out]


def mask(text: str, spans: Sequence[Tuple[int, int]]) -> str:
    """보호 구간을 같은 길이의 \\x00으로 바꾼다(줄바꿈은 남겨 줄 번호를 지킨다)."""
    if not spans:
        return text
    chars = list(text)
    for s, e in spans:
        for i in range(s, e):
            if chars[i] != "\n":
                chars[i] = "\x00"
    return "".join(chars)


class SpanList(list):
    """보호 구간 목록. 시작 위치 색인을 한 번만 만들어 둔다."""

    def __init__(self, items=()):
        super().__init__(items)
        self.starts = [x[0] for x in self]


def in_spans(spans: Sequence[Tuple[int, int]], start: int, end: int) -> bool:
    """[start, end)가 보호 구간과 겹치는가."""
    starts = getattr(spans, "starts", None)
    if starts is None:
        starts = [x[0] for x in spans]
    i = bisect.bisect_right(starts, end - 1) - 1
    while i >= 0:
        s, e = spans[i]
        if e <= start:
            return False
        if s < end and e > start:
            return True
        i -= 1
    return False


def paragraph_spans(masked: str) -> List[Tuple[int, int]]:
    """빈 줄로 나눈 문단의 (시작, 끝). 제목 줄은 따로 문단이 된다."""
    out: List[Tuple[int, int]] = []
    pos = 0
    for m in re.finditer(r"\n[ \t]*\n+", masked):
        if m.start() > pos:
            out.append((pos, m.start()))
        pos = m.end()
    if pos < len(masked):
        out.append((pos, len(masked)))
    split: List[Tuple[int, int]] = []
    for s, e in out:
        seg = masked[s:e]
        if "\n" in seg and re.search(r"^#{1,6}\s", seg, re.M):
            cur = s
            for m in re.finditer(r"^[^\n]*\n?", seg, re.M):
                line = m.group(0)
                if not line:
                    continue
                if re.match(r"#{1,6}\s", line):
                    if cur < s + m.start():
                        split.append((cur, s + m.start()))
                    split.append((s + m.start(), s + m.end()))
                    cur = s + m.end()
            if cur < e:
                split.append((cur, e))
        else:
            split.append((s, e))
    return [(a, b) for a, b in split if masked[a:b].strip()]


def _is_boundary(masked: str, term_start: int, after: int) -> bool:
    if after >= len(masked):
        return True
    if not masked[after].isspace():
        return False
    prev = masked[max(0, term_start - 40):term_start]
    if prev and (prev[-1].isascii() and (prev[-1].isalnum())):
        word = re.search(r"([A-Za-z.]+)$", prev)
        if word and word.group(1).lower().strip(".") in _ABBREV:
            return False
        if re.search(r"(?:^|\s)[A-Z]$", prev):
            return False
        if re.search(r"(?:^|\n)\s*\d{1,3}$", prev):          # '1. 항목' 같은 번호
            return False
        nxt = re.match(r"\s*(.)", masked[after:after + 8], re.S)
        if nxt and nxt.group(1).islower():
            return False
    return True


def sentence_spans(masked: str) -> List[Tuple[int, int]]:
    """문장의 (시작, 끝). 끝은 마침표와 닫는 따옴표까지이고 뒤 공백은 포함하지 않는다."""
    spans: List[Tuple[int, int]] = []
    for ps, pe in paragraph_spans(masked):
        seg = masked[ps:pe]
        cuts = [ps]
        for m in _END.finditer(seg):
            if _is_boundary(masked, ps + m.start(), ps + m.end()):
                cuts.append(ps + m.end())
        for m in re.finditer(r"\n(?=[ \t]*(?:[-*•+]\s|\d+[.)]\s|#{1,6}\s|\|))", seg):
            cuts.append(ps + m.start())
        for m in re.finditer(r"[:：]\n", seg):
            cuts.append(ps + m.end() - 1)
        cuts = sorted(set(cuts))
        if cuts[-1] != pe:
            cuts.append(pe)
        for a, b in zip(cuts, cuts[1:]):
            lo, hi = a, b
            while lo < hi and masked[lo].isspace():
                lo += 1
            while hi > lo and masked[hi - 1].isspace():
                hi -= 1
            if hi > lo and WORDISH.search(masked[lo:hi]):
                spans.append((lo, hi))
    return spans


def count_units(masked: str) -> int:
    """공백으로 나눈 덩어리 중 글자나 숫자가 있는 것의 수. 한국어는 어절, 영어는 낱말에 가깝다."""
    return sum(1 for t in masked.split() if WORDISH.search(t))


def locate(starts: Sequence[int], pos: int) -> Tuple[int, int]:
    """문자 위치를 (줄, 열)로. 둘 다 1부터."""
    i = bisect.bisect_right(starts, pos) - 1
    return i + 1, pos - starts[i] + 1


def excerpt(text: str, start: int, end: int, pad: int = 28, limit: int = 110) -> str:
    seg = text[max(0, start - pad):min(len(text), end + pad)]
    seg = re.sub(r"\s+", " ", seg).strip()
    return seg if len(seg) <= limit else seg[:limit - 1] + "…"


def case_like(original: str, replacement: str) -> str:
    """원문 첫 글자가 대문자면 교체어 첫 글자도 대문자로."""
    if replacement and original[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement
