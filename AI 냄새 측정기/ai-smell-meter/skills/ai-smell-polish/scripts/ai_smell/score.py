"""신호 목록 -> 0~100 지수. 이 지수는 문체 신호의 밀도이며 'AI가 썼을 확률'이 아니다.

공식(docs/design.md 3절):
  밀도 점수  S_d = 100 * (1 - exp(-D / 5))        D = 범주별 min(상한, 100 * 가중합 / max(단위, 60))의 합
  잔재 점수  S_r = 100 * (1 - exp(-R / 2.2))      R = 챗봇 잔재류(건수 기준) 가중합
  지수       S   = 100 - (100 - S_d)(100 - S_r) / 100
한 규칙이 한 문서에서 낼 수 있는 가중합은 그 규칙 최대 가중치의 4배까지다.
"""
from __future__ import annotations

import bisect
import math
from collections import defaultdict
from typing import Dict, List, Sequence, Tuple

from .model import CATEGORIES, Finding, label_for
from .textutil import count_units

D0 = 5.0
R0 = 2.2
MIN_UNITS = 60
RULE_CAP = 4.0


def compute(findings: Sequence[Finding], units: int) -> Dict[str, object]:
    active = [f for f in findings if not f.shadowed and f.weight > 0]
    by_rule: Dict[str, List[Finding]] = defaultdict(list)
    for f in active:
        by_rule[f.rule_id].append(f)
    by_cat: Dict[str, float] = defaultdict(float)
    for items in by_rule.values():
        total = min(sum(f.weight for f in items), RULE_CAP * max(f.weight for f in items))
        by_cat[items[0].category] += total
    density = 0.0
    residue = 0.0
    cats: Dict[str, float] = {}
    for key, w in by_cat.items():
        cat = CATEGORIES[key]
        if cat.absolute:
            residue += w
            cats[key] = round(w, 2)
        else:
            per100 = 100.0 * w / max(units, MIN_UNITS)
            density += min(cat.cap, per100)
            cats[key] = round(per100, 2)
    s_d = 100.0 * (1.0 - math.exp(-density / D0))
    s_r = 100.0 * (1.0 - math.exp(-residue / R0))
    score = 100.0 - (100.0 - s_d) * (100.0 - s_r) / 100.0
    ko, en = label_for(score)
    return {"score": int(round(score)), "label_ko": ko, "label_en": en, "density": round(density, 3),
            "residue": round(residue, 3), "categories": cats}


def paragraph_scores(findings: Sequence[Finding], masked: str,
                     paras: Sequence[Tuple[int, int]]) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    ordered = sorted(findings, key=lambda f: f.start)
    starts = [f.start for f in ordered]
    for i, (ps, pe) in enumerate(paras):
        lo, hi = bisect.bisect_left(starts, ps), bisect.bisect_left(starts, pe)
        inside = [f for f in ordered[lo:hi] if f.end > f.start]
        units = count_units(masked[ps:pe])
        res = compute(inside, units)
        out.append({"index": i + 1, "start": ps, "end": pe, "units": units, "score": res["score"],
                    "findings": len([f for f in inside if not f.shadowed and f.weight > 0])})
    return out
