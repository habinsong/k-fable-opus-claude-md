"""엔진 전체가 공유하는 자료형과 상수. 이 모듈은 다른 엔진 모듈을 가져오지 않는다."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

VERSION = "1.0.0"

# 자동 교정 단계. none은 자동 교정이 없고 보고만 한다.
TIER_RANK = {"safe": 0, "standard": 1, "strong": 2, "none": 99}
TIERS = ("safe", "standard", "strong")
GRADES = ("A", "B", "C")
# 근거 등급 계수. A는 뚜렷한 잔재이거나 독립된 정량 근거가 둘 이상, B는 정량 근거 하나이거나
# 편집자 합의, C는 실무자 목록이나 일화다. 근거는 docs/research.md에 있다.
GRADE_FACTOR = {"A": 1.0, "B": 0.75, "C": 0.45}
GENRES = ("general", "academic", "everyday", "literary")
LANGS = ("ko", "en", "any")


@dataclass(frozen=True)
class Category:
    key: str
    ko: str
    en: str
    weight: float          # 규칙이 따로 정하지 않았을 때의 기본 가중치
    cap: float             # 100단위당 가중 밀도 상한. 한 범주가 점수를 독점하지 못하게 한다
    absolute: bool = False  # True면 길이와 무관하게 건수로 센다(챗봇 잔재 같은 것)


CATEGORIES: Dict[str, Category] = {c.key: c for c in (
    Category("residue", "챗봇 잔재", "chatbot residue", 1.0, 0.0, True),
    Category("sycophancy", "아첨·공치사", "sycophancy", 0.6, 0.0, True),
    Category("markup", "누출된 마크업", "leaked markup", 1.0, 0.0, True),
    Category("placeholder", "빈 자리표시자", "unfilled placeholder", 0.8, 0.0, True),
    Category("puffery", "의미 부풀리기", "puffery", 1.0, 6.0),
    Category("vocab", "과다 어휘", "overused words", 0.8, 5.0),
    Category("structure", "구조 습관", "structural habits", 1.2, 6.0),
    Category("hedging", "군더더기·유보", "filler and hedging", 0.7, 4.0),
    Category("transition", "접속어 남발", "stacked transitions", 0.6, 3.0),
    Category("signpost", "예고·안내", "signposting", 0.8, 3.0),
    Category("attribution", "출처 없는 권위", "vague attribution", 1.0, 3.0),
    Category("translationese", "번역투", "translationese", 0.6, 4.0),
    Category("emotion", "감정 직접 서술", "told emotion", 0.7, 3.0),
    Category("rhythm", "리듬 단조", "monotone rhythm", 0.8, 3.0),
    Category("format", "서식 신호", "formatting tells", 0.5, 3.0),
    Category("hygiene", "보이지 않는 문자", "invisible characters", 0.0, 0.0),
    Category("info", "참고(점수 제외)", "info (unscored)", 0.0, 0.0),
)}

LABELS = ((15, "거의 없음", "minimal"), (35, "약함", "weak"),
          (60, "뚜렷함", "noticeable"), (101, "강함", "strong"))


@dataclass
class Ctx:
    """규칙의 guard와 교정 함수가 보는 문맥."""
    text: str
    masked: str
    genre: str = "general"


Guard = Callable[["re.Match[str]", Ctx], bool]
Repl = Callable[["re.Match[str]", Ctx], Optional[str]]


@dataclass(frozen=True)
class Rule:
    id: str
    lang: str
    category: str
    grade: str
    pattern: "re.Pattern[str]"
    note: str
    weight: Optional[float] = None
    tier: str = "none"
    repl: Any = None                   # str(정규식 치환 틀) 또는 Repl 함수
    scope: str = "match"               # "match" 또는 "sentence"(문장 통째 삭제)
    sugg: str = ""
    genre: Dict[str, float] = field(default_factory=dict)
    min_count: int = 1                 # 문서 전체에서 이 횟수 이상일 때만 센다
    cluster: int = 0                   # 400자 안에 다른 cluster 규칙이 이만큼 있어야 센다
    guard: Optional[Guard] = None
    fix_guard: Optional[Guard] = None  # 신호로는 세되 자동 교정은 이 조건일 때만 한다
    protect: bool = True               # False면 URL 같은 보호 구간 안도 본다
    recap: bool = False                # 삭제한 뒤 문장 첫 글자를 대문자로 바꾼다


@dataclass
class Edit:
    start: int
    end: int
    replacement: str
    rule_id: str
    tier: str
    recap: bool = False
    before: str = ""


@dataclass
class Finding:
    rule_id: str
    category: str
    grade: str
    start: int
    end: int
    text: str
    line: int
    col: int
    weight: float                      # 가중치 x 근거 계수 x 장르 계수. 점수에 들어가는 값
    note: str
    sugg: str = ""
    tier: str = "none"                 # 이 단계 이상에서 자동 교정된다
    fixable: bool = False
    lang: str = "any"
    shadowed: bool = False             # 더 무거운 신호에 겹쳐 점수에서 빠졌다
    edit: Optional[Edit] = None        # 자동 교정이 있으면 그 내용


@dataclass
class Analysis:
    lang: str
    genre: str
    units: int
    sentences: int
    paragraphs: int
    score: int
    label_ko: str
    label_en: str
    density: float
    residue: float
    categories: Dict[str, float]
    findings: List[Finding]
    paragraph_scores: List[Dict[str, Any]]
    metrics: Dict[str, Any]
    notes: List[str] = field(default_factory=list)


def label_for(score: float) -> "tuple[str, str]":
    for limit, ko, en in LABELS:
        if score < limit:
            return ko, en
    return LABELS[-1][1], LABELS[-1][2]


def line_starts(text: str) -> List[int]:
    starts = [0]
    for m in re.finditer(r"\n", text):
        starts.append(m.end())
    return starts


def weigh(cat: str, grade: str, w: Optional[float], gmap: Dict[str, float], genre: str) -> float:
    """신호 하나의 점수 기여: (규칙 가중치 또는 범주 기본값) x 근거 계수 x 장르 계수."""
    base = CATEGORIES[cat].weight if w is None else w
    return round(base * GRADE_FACTOR[grade] * gmap.get(genre, 1.0), 4)
