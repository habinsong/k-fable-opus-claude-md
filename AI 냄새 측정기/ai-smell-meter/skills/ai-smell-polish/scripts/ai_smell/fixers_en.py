"""영어 AI 냄새 규칙의 자동 교정 함수(repl).

'더하다', '짝/쌍', '재다', '신호', '전파', '자동', '지수', '밀도', '박는다' 등
영문 LLM 특유의 상투구(cliche)를 간결한 자연어로 바꾼다.
"""
from __future__ import annotations

import re
from typing import Optional

from .model import Ctx
from .textutil import case_like


def en_adds_depth(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'adds depth to' -> 'deepens', 'adds a touch of' -> 'brings'."""
    s = m.group(0)
    m_depth = re.search(r"\b(?P<v>add|adds|added|adding)\s+depth\s+to\b", s, re.I)
    if m_depth:
        vmap = {"add": "deepen", "adds": "deepens", "added": "deepened", "adding": "deepening"}
        rep = vmap.get(m_depth.group("v").lower(), "deepen")
        return case_like(s, rep)
    m_touch = re.search(r"\b(?P<v>add|adds|added|adding)\s+a\s+touch\s+of\b", s, re.I)
    if m_touch:
        vmap = {"add": "bring", "adds": "brings", "added": "brought", "adding": "bringing"}
        rep = vmap.get(m_touch.group("v").lower(), "bring")
        return case_like(s, rep)
    m_nuance = re.search(r"\b(?P<v>add|adds|added|adding)\s+nuance\s+to\b", s, re.I)
    if m_nuance:
        vmap = {
            "add": "deepen nuance in",
            "adds": "deepens nuance in",
            "added": "deepened nuance in",
            "adding": "deepening nuance in",
        }
        rep = vmap.get(m_nuance.group("v").lower(), "deepen nuance in")
        return case_like(s, rep)
    return None


def en_paired_with(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'paired with' / 'coupled with' -> 'with', 'two sides of the same coin' -> 'closely related'."""
    s = m.group(0)
    low = s.lower()
    if "two sides of the same coin" in low:
        return case_like(s, "closely related")
    if any(p in low for p in ("paired with", "coupled with", "hand in hand with")):
        return case_like(s, "with")
    return None


def en_gauge(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'gauge the impact' -> 'assess the impact'."""
    s = m.group(0)
    vmap = {"gauge": "assess", "gauges": "assesses", "gauged": "assessed", "gauging": "assessing"}
    return re.sub(
        r"\b(gauge|gauges|gauged|gauging)\b",
        lambda match: case_like(match.group(0), vmap.get(match.group(0).lower(), "assess")),
        s,
        flags=re.I,
    )


def en_signal(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'sends a clear signal that' -> 'indicates that', 'a clear signal that' -> 'a sign that'."""
    s = m.group(0)
    low = s.lower()
    if "a clear signal that" in low and not any(k in low for k in ("send", "sent", "serve")):
        return case_like(s, "a sign that")
    if "send" in low or "sent" in low:
        vmap = {"sends": "indicates that", "send": "indicate that", "sent": "indicated that", "sending": "indicating that"}
        m_verb = re.search(r"\b(sends|send|sent|sending)\b", s, re.I)
        if m_verb:
            return case_like(s, vmap.get(m_verb.group(0).lower(), "indicates that"))
    if "serve" in low:
        vmap = {"serves": "shows that", "serve": "show that", "served": "showed that", "serving": "showing that"}
        m_verb = re.search(r"\b(serves|serve|served|serving)\b", s, re.I)
        if m_verb:
            return case_like(s, vmap.get(m_verb.group(0).lower(), "shows that"))
    return None


def en_propagate(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'propagate across' -> 'spread across', 'dissemination of' -> 'distribution of'."""
    s = m.group(0)
    if "dissemination of" in s.lower():
        return case_like(s, "distribution of")
    vmap = {"propagate": "spread", "propagates": "spreads", "propagated": "spread", "propagating": "spreading"}
    return re.sub(
        r"\b(propagate|propagates|propagated|propagating)\b",
        lambda match: case_like(match.group(0), vmap.get(match.group(0).lower(), "spread")),
        s,
        flags=re.I,
    )


def en_seamless_action(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'seamlessly integrates' -> 'integrates', 'seamless automation' -> 'automation'."""
    s = m.group(0)
    if s.lower() == "seamless automation":
        return case_like(s, "automation")
    m_verb = re.match(r"seamlessly\s+(.+)", s, re.I)
    if m_verb:
        return case_like(s, m_verb.group(1))
    return None


def en_automatically(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'automatically generates' -> 'generates', 'automatically creates' -> 'creates'."""
    v = m.group("v")
    return case_like(m.group(0), v)


def en_abstract_index(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'happiness index' -> 'happiness level', 'trust score' -> 'trust level'."""
    s = m.group(0)
    return re.sub(r"\b(index|score)\b", lambda match: case_like(match.group(0), "level"), s, flags=re.I)


def en_density(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'high information density' -> 'rich detail', 'dense with X' -> 'rich in X'."""
    s = m.group(0)
    low = s.lower()
    if "higher information density" in low:
        return case_like(s, "richer detail")
    if "high information density" in low:
        return case_like(s, "rich detail")
    m_noun = re.match(r"dense\s+with\s+(.+)", s, re.I)
    if m_noun:
        return case_like(s, f"rich in {m_noun.group(1)}")
    return None


def en_hardcode(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'hardcoded directly into' -> 'written directly into', 'baked into' -> 'built into'."""
    s = m.group(0)
    if "baked into" in s.lower():
        return case_like(s, "built into")
    vmap = {"hardcode": "write", "hardcodes": "writes", "hardcoded": "written", "hardcoding": "writing"}
    return re.sub(
        r"\b(hardcode|hardcodes|hardcoded|hardcoding)\b",
        lambda match: case_like(match.group(0), vmap.get(match.group(0).lower(), "write")),
        s,
        flags=re.I,
    )


def en_tapestry(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'rich tapestry of' -> 'diversity of', 'a rich tapestry' -> 'a diverse mixture'."""
    s = m.group(0)
    low = s.lower()
    if "tapestry of" in low:
        return case_like(s, re.sub(r"\b(?:rich|vibrant|intricate|complex|diverse|woven)\s+tapestry\s+of\b", "diversity of", s, flags=re.I))
    return case_like(s, re.sub(r"\b(?:rich|vibrant|intricate|complex|diverse|woven)\s+tapestry\b", "diverse mix", s, flags=re.I))


def en_testament(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'a testament to' -> 'evidence of'."""
    s = m.group(0)
    return case_like(s, re.sub(r"\ba\s+(?:powerful\s+|enduring\s+|living\s+|true\s+|clear\s+|lasting\s+|remarkable\s+)?testament\s+to\b", "evidence of", s, flags=re.I))


def en_navigate(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'navigate the complexities of' -> 'handle the complexities of'."""
    s = m.group(0)
    vmap = {"navigate": "handle", "navigates": "handles", "navigated": "handled", "navigating": "handling"}
    return re.sub(r"\b(navigate|navigates|navigated|navigating)\b", lambda match: case_like(match.group(0), vmap.get(match.group(0).lower(), "handle")), s, flags=re.I)


def en_game_changer(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'game-changer' -> 'turning point', 'game-changing' -> 'transformative'."""
    s = m.group(0)
    low = s.lower()
    if "game-changing" in low or "game changing" in low:
        return case_like(s, "transformative")
    return case_like(s, "turning point")


def en_paradigm_shift(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'paradigm shift' -> 'major shift'."""
    s = m.group(0)
    return case_like(s, "major shift")


def en_unlock(m: "re.Match[str]", ctx: Ctx) -> Optional[str]:
    """'unlock the full potential' -> 'reach full potential'."""
    s = m.group(0)
    return re.sub(r"\b(unlock|unlocks|unlocked|unlocking)\s+(?:the\s+|its\s+|their\s+|your\s+)?(?:full\s+|true\s+|hidden\s+)?potential\b",
                  lambda match: case_like(match.group(0), "reach full potential"), s, flags=re.I)
