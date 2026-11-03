"""규칙을 짧게 쓰기 위한 도우미. 규칙 파일은 R(...)과 lit/alt/kl만 부른다."""
from __future__ import annotations

import re
from typing import Dict, Iterable, Optional

from ..model import CATEGORIES, GRADES, LANGS, TIER_RANK, Rule


def lit(phrase: str) -> str:
    """영어 구절 -> 정규식 조각. 공백은 \\s+, 하이픈은 공백도 허용, '는 곡선 따옴표도 받는다."""
    out = []
    for part in re.split(r"(\s+|-)", phrase):
        if not part:
            continue
        if part.isspace():
            out.append(r"\s+")
        elif part == "-":
            out.append(r"[-‐‑\s]+")
        else:
            out.append(re.escape(part).replace("'", "['’]"))
    return "".join(out)


def alt(*phrases: str) -> str:
    """구절 여럿 -> (?:a|b|c). 긴 것을 먼저 둔다."""
    items = sorted({lit(p) for p in phrases}, key=len, reverse=True)
    return "(?:" + "|".join(items) + ")"


def kl(phrase: str) -> str:
    """한국어 구절 -> 정규식 조각. 띄어쓰기는 있어도 없어도 된다."""
    return r"\s*".join(re.escape(p) for p in phrase.split())


def kalt(*phrases: str) -> str:
    items = sorted({kl(p) for p in phrases}, key=len, reverse=True)
    return "(?:" + "|".join(items) + ")"


KB = r"(?<![가-힣])"      # 한글 낱말 앞 경계
KE = r"(?![가-힣])"       # 한글 낱말 뒤 경계


def R(rid: str, lang: str, cat: str, grade: str, pattern: str, note: str, *,
      w: Optional[float] = None, tier: str = "none", repl=None, scope: str = "match",
      sugg: str = "", genre: Optional[Dict[str, float]] = None, min_count: int = 1,
      cluster: int = 0, guard=None, fix_guard=None, protect: bool = True, recap: bool = False,
      flags: Optional[int] = None) -> Rule:
    if lang not in LANGS or cat not in CATEGORIES or grade not in GRADES or tier not in TIER_RANK:
        raise ValueError(f"규칙 정의가 잘못됐다: {rid}")
    if scope not in ("match", "sentence"):
        raise ValueError(f"scope가 잘못됐다: {rid}")
    if flags is None:
        flags = re.M | (re.I if lang == "en" else 0)
    return Rule(id=rid, lang=lang, category=cat, grade=grade, pattern=re.compile(pattern, flags),
                note=note, weight=w, tier=tier, repl=repl, scope=scope, sugg=sugg,
                genre=dict(genre or {}), min_count=min_count, cluster=cluster, guard=guard,
                fix_guard=fix_guard, protect=protect, recap=recap)


def check_unique(rules: Iterable[Rule]) -> None:
    seen = set()
    for r in rules:
        if r.id in seen:
            raise ValueError(f"규칙 id가 겹친다: {r.id}")
        seen.add(r.id)
