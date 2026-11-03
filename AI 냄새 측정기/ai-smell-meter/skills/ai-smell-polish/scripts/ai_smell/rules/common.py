"""두 언어 공통: 서식 신호와 보이지 않는 문자.

서식은 단독으로 AI의 증거가 아니다. 이모지 불릿, 굵은 라벨 불릿, 줄표(em dash)는 군집일 때만 센다.
줄표는 최신 모델에서 크게 줄었다는 보고가 있어(docs/research.md 2절) 가중치를 낮게 둔다.
"""
from __future__ import annotations

import re

from ..textutil import EMOJI_CLASS
from .build import R

# 보이지 않는 문자는 소스에 리터럴로 두지 않고 코드 포인트로 만든다.
PRIVATE = "[" + chr(0xE200) + "-" + chr(0xE2FF) + "]"
PRIVATE_CLS = chr(0xE200) + "-" + chr(0xE2FF)
SPACES = "".join(chr(c) for c in (0x00A0, 0x202F, 0x2007, 0x2009, 0x200A))
INVISIBLE = "".join(chr(c) for c in (0x200B, 0x2060, 0xFEFF, 0x00AD))
BULLET = r"(?:[-*•]|\d+[.)])"
EM = r"[—―]"          # em dash, horizontal bar

RULES = [
    R("any.markup.oaicite", "any", "markup", "A",
      r":?contentReference\[oaicite:\d+\]\{index=\d+\}|\boaicite:\d+\b", "누출된 인용 토큰.",
      tier="safe", repl=""),
    R("any.markup.turn-ref", "any", "markup", "A",
      r"\bturn\d+(?:search|view|news|image|file|forecast|product)\d+\b", "누출된 도구 참조 토큰.",
      tier="safe", repl=""),
    R("any.markup.private-use", "any", "markup", "A",
      PRIVATE + r"[^" + PRIVATE_CLS + r"\n]{0,80}" + PRIVATE + r"|" + PRIVATE,
      "비공개 영역 인용 표지.", tier="safe", repl="", flags=re.M),
    R("any.placeholder.lorem", "any", "placeholder", "A", r"\blorem ipsum\b", "더미 문구.", flags=re.M),

    R("any.format.emoji-lead", "any", "format", "B",
      r"^([ \t]*(?:" + BULLET + r"[ \t]+|#{1,6}[ \t]+)?)(?:" + EMOJI_CLASS + r"[ \t]*)+(?=\S)",
      "줄머리 이모지(불릿, 제목).", tier="standard", repl=r"\1", genre={"everyday": 0.3},
      sugg="이모지를 걷는다.", cluster=0, min_count=2, flags=re.M),
    R("any.format.emoji-any", "any", "format", "C", EMOJI_CLASS, "본문 이모지.", w=0.3, min_count=3,
      genre={"everyday": 0.2}, tier="strong", repl="", flags=re.M),
    R("any.format.bold-lead", "any", "format", "B",
      r"^([ \t]*" + BULLET + r"[ \t]+)\*\*([^*\n]{2,60})\*\*(?=[ \t]*[:：.\-–—]|[ \t]+\S)",
      "불릿마다 굵은 라벨로 시작한다.", w=0.5, min_count=3, tier="strong", repl=r"\1\2", flags=re.M,
      sugg="라벨 굵기를 걷거나 줄글로 푼다."),
    R("any.format.bold-line", "any", "format", "C", r"^[ \t]*\*\*[^*\n]{2,60}\*\*[ \t]*$",
      "굵은 글씨만 있는 줄이 제목 구실을 한다.", w=0.3, min_count=3, flags=re.M),
    R("any.format.hashtags", "any", "format", "C", r"(?<![\w#])#[A-Za-z가-힣][\w가-힣]{1,30}(?![\w])",
      "해시태그 묶음.", w=0.3, min_count=5, flags=re.M),
    R("any.format.heading-title-case", "any", "format", "C",
      r"^#{1,6}[ \t]+(?:[A-Z][a-z]+(?:[ \t]+(?:[A-Z][a-z]+|of|and|the|for|in|to|a|an|on|with)){3,})[ \t]*$",
      "제목이 모두 대문자로 시작한다(제목식 대문자).", w=0.3, flags=re.M),

    R("any.hygiene.nbsp", "any", "hygiene", "B", "[" + SPACES + "]",
      "줄바꿈 없는 공백 문자가 섞였다.", tier="safe", repl=" ", flags=re.M,
      sugg="복사, 검색, 코드에서 문제를 일으키는 문자라 일반 공백으로 바꾼다."),
    R("any.hygiene.zero-width", "any", "hygiene", "B", "[" + INVISIBLE + "]",
      "보이지 않는 문자(너비 0, 연자 부호)가 섞였다.", tier="safe", repl="", flags=re.M,
      sugg="복사, 검색, 코드에서 문제를 일으키는 문자라 지운다. 출처를 숨기려는 기능이 아니다."),
]
