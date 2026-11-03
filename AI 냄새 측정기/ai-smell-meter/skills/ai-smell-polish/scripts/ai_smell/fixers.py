"""규칙이 가리키는 교정 함수(repl)와 조건 함수(guard). 함수는 (match, ctx)를 받는다.

repl은 새 문자열을 돌려주거나, None을 돌려주어 이번 자리는 고치지 않는다.
guard는 False를 돌려주면 그 자리를 신호로 세지 않는다.
"""
from __future__ import annotations

import re
from typing import Callable, Dict, Optional

from .model import Ctx
from .textutil import case_like

# ---------------------------------------------------------------- guard

_DET = {"a", "an", "the", "this", "that", "these", "those", "our", "its", "their", "my", "your",
        "his", "her", "of", "for", "in", "on", "as"}


_LINE_MARK = re.compile(r"\s*(?:[-*+•>]|\d+[.)]|#{1,6})?\s*[\"'“‘(\[*_]*")
_LIST_LINE = re.compile(r"\s*(?:[-*+•]|\d+[.)]|#{1,6})\s")


def at_sentence_start(m: "re.Match[str]", ctx: Ctx) -> bool:
    """매치가 문장 첫머리인가. 따옴표, 괄호, 글머리 표지 바로 뒤도 첫머리로 본다."""
    text = ctx.masked
    ls = text.rfind("\n", 0, m.start()) + 1
    prefix = text[ls:m.start()]
    if _LINE_MARK.fullmatch(prefix):
        if ls == 0:
            return True
        j = ls - 1
        while j > 0 and text[j - 1] in " \t":
            j -= 1
        if j == 0 or text[j - 1] == "\n":
            return True                       # 빈 줄 뒤는 새 문단
        prev_end = j
        k = text.rfind("\n", 0, j - 1) + 1
        last = text[k:prev_end]
        prev = last
        return (prev[-1] in ".!?…:。" or bool(_LIST_LINE.match(last)) or last.lstrip().startswith("|"))
    tail = re.sub(r"[\"'”’)\]]+$", "", prefix.rstrip())
    return bool(tail) and tail[-1] in ".!?…:。"


_LEAD_ADVERB = re.compile(r"\W*(?:[A-Za-z']+(?: [A-Za-z']+){0,2}),\s*")


def at_clause_start(m: "re.Match[str]", ctx: Ctx) -> bool:
    """문장 첫머리이거나, 문장 첫머리의 짧은 접속부사(Furthermore, ...) 바로 뒤인가."""
    if at_sentence_start(m, ctx):
        return True
    ls = max(ctx.masked.rfind(c, 0, m.start()) for c in ".!?\n") + 1
    return bool(_LEAD_ADVERB.fullmatch(ctx.masked[ls:m.start()]))


def in_tail(m: "re.Match[str]", ctx: Ctx) -> bool:
    """글 끝부분(마지막 20%, 최소 240자 안)에 있는가. 맺음 인사는 끝에서만 군더더기로 본다."""
    return len(ctx.text) - m.end() <= max(240, int(len(ctx.text) * 0.2))


def tail_sentence(m: "re.Match[str]", ctx: Ctx) -> bool:
    """글 끝부분에서 문장 첫머리에 놓인 매치만 센다. 맺음 인사 규칙이 쓴다."""
    return in_tail(m, ctx) and at_sentence_start(m, ctx)


def no_digits_or_names(m: "re.Match[str]", ctx: Ctx) -> bool:
    """매치에 숫자, 따옴표, 고유명사 후보가 없으면 True. 사실이 들어 있는 꼬리절은 건드리지 않는다."""
    s = m.group(0)
    if re.search(r"\d|[\"“”‘’]", s):
        return False
    words = re.findall(r"\b[A-Z][a-z]+\b", s[1:])
    return len(words) == 0


def no_cite_after(m: "re.Match[str]", ctx: Ctx) -> bool:
    """뒤따르는 25자 안에 인용 표시([1], (Kim, 2020), et al.)가 있으면 출처 있는 서술이므로 센다 하지 않는다."""
    tail = ctx.masked[m.end():m.end() + 40]
    return not re.search(r"\[\d|\(\w+[^)]{0,20}\d{4}|et al\.|\u0000", tail)


def verb_context(m: "re.Match[str]", ctx: Ctx) -> bool:
    """앞 낱말이 관사나 소유격이면 명사 용법이므로 동사 교체 대상이 아니다."""
    prev = re.search(r"([A-Za-z']+)\s+$", ctx.masked[max(0, m.start() - 40):m.start()])
    return not (prev and prev.group(1).lower() in _DET)


# ---------------------------------------------------------------- repl: 영어

def word_map(mapping: Dict[str, str]) -> Callable:
    """매치된 낱말(소문자)을 사전에서 찾아 바꾼다. 대문자로 시작했으면 맞춘다."""
    def fix(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
        word = m.group(0)
        out = mapping.get(re.sub(r"\s+", " ", word.lower()))
        return None if out is None else case_like(word, out)
    return fix


def keep_case(template: str) -> Callable:
    """매치 첫 글자 대소문자를 살린 채 template으로 바꾼다."""
    def fix(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
        return case_like(m.group(0), template)
    return fix


_COPULA = {"serves": "is", "serve": "are", "served": "was", "stands": "is", "stand": "are", "stood": "was"}


def copula(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    verb = m.group("v").lower()
    out = _COPULA.get(verb)
    return None if out is None else case_like(m.group("v"), out) + " " + m.group("art")


_UTM = re.compile(r"utm_source=(?:chatgpt\.com|openai|copilot\.com|perplexity)", re.I)


def utm_param(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """주소에 붙은 ?utm_source=chatgpt.com 꼬리표만 걷는다. 다른 매개변수는 남긴다."""
    s = m.group(0)
    lead = s[0]
    rest = _UTM.sub("", s[1:], count=1).lstrip("&")
    if not rest:
        return ""
    return ("?" if lead == "?" else "&") + rest


# ---------------------------------------------------------------- repl: 한국어

_JONG = {"ㄴ": 4, "ㄹ": 8, "ㅁ": 16}


def _add_jong(syllable: str, jong: str) -> str:
    code = ord(syllable) - 0xAC00
    if 0 <= code < 11172 and code % 28 == 0:
        return chr(ord(syllable) + _JONG[jong])
    return syllable + {"ㄴ": "ㄴ", "ㄹ": "ㄹ", "ㅁ": "ㅁ"}[jong]


_BASE = {"되어": "되", "돼": "되", "보여": "보이", "쓰여": "쓰이", "불리워": "불리", "불려": "불리",
         "잊혀": "잊히", "읽혀": "읽히", "닫혀": "닫히", "열려": "열리", "놓여": "놓이", "나뉘어": "나뉘",
         "섞여": "섞이", "바뀌어": "바뀌", "쌓여": "쌓이", "묶여": "묶이"}
_PAST = {"이": "였", "리": "렸", "히": "혔", "되": "되었"}
_PRESENT = {"이": "여", "리": "려", "히": "혀", "되": "되어"}


def _conj(base: str, ending: str) -> Optional[str]:
    head, last = base[:-1], base[-1]
    if ending == "진다":
        return head + _add_jong(last, "ㄴ") + "다"
    if ending == "진":
        return head + _add_jong(last, "ㄴ")
    if ending == "질":
        return head + _add_jong(last, "ㄹ")
    if ending == "짐":
        return head + _add_jong(last, "ㅁ")
    if ending == "졌":
        past = _PAST.get(last)
        return base + "었" if past is None else head + past
    if ending == "져":
        pres = _PRESENT.get(last)
        return base + "어" if pres is None else head + pres
    plain = {"지는": "는", "지며": "며", "지고": "고", "지면": "면", "지게": "게", "지도록": "도록", "지기": "기"}
    return base + plain[ending] if ending in plain else None


def double_passive(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """보여진다 -> 보인다, 되어진다 -> 된다처럼 '-어지다'가 겹친 피동을 단일 피동으로."""
    base = _BASE.get(m.group("stem"))
    return None if base is None else _conj(base, m.group("end"))


def nominal_verb(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'검토를 진행한다' -> '검토한다'. 명사는 화이트리스트에 있는 것만 온다."""
    return m.group("noun") + m.group("e")


_GANEUNG = {"하다": "있다", "합니다": "있습니다", "하며": "있으며", "하고": "있고", "하여": "있어",
            "하지": "있지", "하므로": "있으므로"}


def can_do(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'사용하는 것이 가능하다' -> '사용할 수 있다'."""
    tail = _GANEUNG.get(m.group("e"))
    return None if tail is None else m.group("stem") + "할 수 " + tail


def rago(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'요소라고 할 수 있다' -> '요소이다'. 필자가 유보한 정도를 올리므로 strong 단계에서만 쓴다."""
    polite = m.group("e").startswith("있습") or m.group("e").startswith("있겠습")
    return m.group("n") + ("입니다" if polite else "이다")


_PIVOT_CLAUSE = re.compile(r"(it(?:'s| is)|they(?:'re| are)|this is|that(?:'s| is))\s*$", re.I)
_NEG = re.compile(r"^(?P<subj>it|this|that|these|they|he|she|we|there)(?P<cop>'s| is| are| was| were)?\s*"
                  r"(?P<neg>not|never|isn't|aren't|wasn't|weren't|is not|are not|was not|were not)\b", re.I)
_COP = {"isn't": " is", "aren't": " are", "wasn't": " was", "weren't": " were", "is not": " is",
        "are not": " are", "was not": " was", "were not": " were"}


def neg_parallel_fix(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'It's not just X, it's Y' -> 'It's Y'. 앞 절을 걷고 뒤 절만 남긴다. 숫자와 고유명사가 있으면 하지 않는다."""
    s = m.group(0)
    if not no_digits_or_names(m, ctx) or re.search(r"\bnot\s+only\b", s, re.I) and not _PIVOT_CLAUSE.search(s):
        return None
    pc = _PIVOT_CLAUSE.search(s)
    if pc:
        if not _NEG.match(s):
            return None                    # 주어가 명사면 앞 절을 지울 때 주어가 사라진다
        return case_like(s[:1], pc.group(1))
    if re.search(r"\bbut\s*$", s, re.I):
        n = _NEG.match(s)
        if not n:
            return None
        cop = n.group("cop") or _COP.get(re.sub(r"\s+", " ", n.group("neg").lower()), "")
        return n.group("subj") + cop if cop else None
    return None
