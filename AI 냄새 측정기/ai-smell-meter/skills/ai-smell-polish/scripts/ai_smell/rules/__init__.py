"""규칙 모음. load_rules()가 모든 규칙을 한 번 모아 돌려주고 id 중복을 검사한다."""
from __future__ import annotations

from typing import List

from ..model import Rule
from . import (common, en_hedging, en_puffery, en_residue, en_structure, en_vocab, ko_lexicon,
               ko_residue, ko_style)
from .build import check_unique

_CACHE: List[Rule] = []


def load_rules(lang: str = "auto") -> List[Rule]:
    """lang이 'ko'나 'en'이면 그 언어와 공통(any) 규칙만, 'auto'면 전부."""
    if not _CACHE:
        for mod in (en_residue, en_puffery, en_structure, en_hedging, en_vocab,
                    ko_residue, ko_style, ko_lexicon, common):
            _CACHE.extend(mod.RULES)
        check_unique(_CACHE)
    if lang in ("ko", "en"):
        return [r for r in _CACHE if r.lang in (lang, "any")]
    return list(_CACHE)
