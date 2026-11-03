"""영어: 과다 어휘. 등급 A는 독립된 정량 연구가 있는 낱말, B는 편집자 합의, C는 실무자 목록이다.

낱말 하나는 AI의 증거가 못 된다. 그래서 흔한 낱말(C)은 군집(cluster)일 때만 센다.
모델 세대마다 목록이 바뀐다(docs/research.md 2절). 낡은 항목은 규칙 파일에서 지우면 된다.
"""
from __future__ import annotations

from .. import fixers as fx
from .build import R

UTIL = {"utilize": "use", "utilizes": "uses", "utilized": "used", "utilizing": "using", "utilise": "use",
        "utilises": "uses", "utilised": "used", "utilising": "using"}
SHOW = {"showcase": "show", "showcases": "shows", "showcased": "showed", "showcasing": "showing"}
DELVE = {"delve": "look", "delves": "looks", "delved": "looked", "delving": "looking"}
LEV = {"leverage": "use", "leverages": "uses", "leveraged": "used", "leveraging": "using"}
COMMENCE = {"commence": "start", "commences": "starts", "commenced": "started", "commencing": "starting"}

RULES = [
    # ---- A: 정량 근거가 있는 낱말 (Kobak 2024, Liang 2024, Juzek 2024-25 등)
    R("en.vocab.delve", "en", "vocab", "A", r"\bdelv(?:e|es|ed|ing)\b", "Peak 'LLM word' in academic prose.",
      sugg="'look into', 'examine', or cut."),
    R("en.vocab.delve-into", "en", "vocab", "A", r"\bdelv(?:e|es|ed|ing)\b(?=\s+(?:deeper\s+|further\s+)?into\b)",
      "Peak 'LLM word' in academic prose.", tier="strong", repl=fx.word_map(DELVE)),
    R("en.vocab.tapestry", "en", "vocab", "A", r"\btapestr(?:y|ies)\b", "Stock metaphor."),
    R("en.vocab.showcase", "en", "vocab", "A", r"\bshowcas(?:e|es|ed|ing)\b", "Overused verb ('show').",
      guard=fx.verb_context),
    R("en.vocab.showcase-fix", "en", "vocab", "A",
      r"\bshowcas(?:e|es|ed|ing)\b(?=\s+(?:how|that|the|a|an|its|their|our|your|his|her|these|those|this|"
      r"[A-Z0-9]))", "Overused verb ('show').", tier="strong", repl=fx.word_map(SHOW), guard=fx.verb_context),
    R("en.vocab.underscore", "en", "vocab", "A", r"\bunderscor(?:e|es|ed|ing)\b", "Overused verb ('show', 'stress').",
      guard=fx.verb_context),
    R("en.vocab.intricate", "en", "vocab", "A", r"\bintricate(?:ly)?\b|\bintricac(?:y|ies)\b",
      "Overused adjective."),
    R("en.vocab.pivotal", "en", "vocab", "A", r"\bpivotal\b", "Overused adjective ('key').",
      tier="strong", repl=fx.keep_case("key")),
    R("en.vocab.meticulous", "en", "vocab", "A", r"\bmeticulous(?:ly)?\b", "Overused adjective."),
    R("en.vocab.commendable", "en", "vocab", "A", r"\bcommendabl[ey]\b", "Overused adjective."),
    R("en.vocab.notably", "en", "vocab", "A", r"\bnotably\b", "Overused sentence adverb.", w=0.5),
    R("en.vocab.multifaceted", "en", "vocab", "A", r"\bmulti-?faceted\b", "Overused adjective."),
    # ---- B: 편집자 합의
    R("en.vocab.crucial", "en", "vocab", "B", r"\bcrucial(?:ly)?\b", "Overused intensifier.", w=0.5, cluster=1),
    R("en.vocab.comprehensive", "en", "vocab", "B", r"\bcomprehensive(?:ly)?\b", "Overused adjective.", w=0.5,
      cluster=1),
    R("en.vocab.enhance", "en", "vocab", "B", r"\benhanc(?:e|es|ed|ing)\b", "Overused verb.", w=0.5, cluster=1),
    R("en.vocab.foster", "en", "vocab", "B", r"\bfoster(?:s|ed|ing)?\b", "Overused verb.", cluster=1,
      guard=fx.verb_context),
    R("en.vocab.garner", "en", "vocab", "B", r"\bgarner(?:s|ed|ing)?\b", "Overused verb ('get', 'win')."),
    R("en.vocab.bolster", "en", "vocab", "B", r"\bbolster(?:s|ed|ing)?\b", "Overused verb ('strengthen')."),
    R("en.vocab.elevate", "en", "vocab", "B", r"\belevat(?:e|es|ed|ing)\b", "Overused verb.", cluster=1),
    R("en.vocab.streamline", "en", "vocab", "B", r"\bstreamlin(?:e|es|ed|ing)\b", "Overused verb.", cluster=1),
    R("en.vocab.revolutionize", "en", "vocab", "B", r"\brevolutioni[sz](?:e|es|ed|ing)\b", "Hype verb."),
    R("en.vocab.leverage", "en", "vocab", "B", r"\bleverag(?:e|es|ed|ing)\b", "Business jargon for 'use'.",
      guard=fx.verb_context, cluster=1),
    R("en.vocab.leverage-fix", "en", "vocab", "B",
      r"\bleverag(?:e|es|ed|ing)\b(?=\s+(?:the|a|an|our|their|its|your|his|her|these|those|this|that|existing|"
      r"modern|advanced|new)\b)", "Business jargon for 'use'.", tier="standard", repl=fx.word_map(LEV),
      guard=fx.verb_context),
    R("en.vocab.utilize", "en", "vocab", "C", r"\butili[sz](?:e|es|ed|ing)\b", "'Use' is enough.", w=0.4,
      tier="standard", repl=fx.word_map(UTIL)),
    R("en.vocab.commence", "en", "vocab", "C", r"\bcommenc(?:e|es|ed|ing)\b", "'Start' is enough.", w=0.4,
      tier="standard", repl=fx.word_map(COMMENCE)),
    R("en.vocab.facilitate", "en", "vocab", "B", r"\bfacilitat(?:e|es|ed|ing)\b", "Abstract verb.", w=0.5, cluster=1),
    R("en.vocab.empower", "en", "vocab", "B", r"\bempower(?:s|ed|ing|ment)?\b", "Hype verb.", cluster=1),
    R("en.vocab.unleash", "en", "vocab", "B", r"\bunleash(?:es|ed|ing)?\b", "Hype verb."),
    R("en.vocab.embark", "en", "vocab", "B", r"\bembark(?:s|ed|ing)?\b", "Journey metaphor."),
    R("en.vocab.holistic", "en", "vocab", "B", r"\bholistic(?:ally)?\b", "Abstract adjective.", cluster=1),
    R("en.vocab.synergy", "en", "vocab", "B", r"\bsynerg(?:y|ies|istic)\b", "Business jargon."),
    R("en.vocab.paradigm", "en", "vocab", "C", r"\bparadigms?\b", "Abstract noun.", cluster=1),
    R("en.vocab.myriad", "en", "vocab", "B", r"\bmyriad\b|\bplethora\b", "Grand quantity word ('many')."),
    R("en.vocab.nuanced", "en", "vocab", "C", r"\bnuanced\b", "Vague praise.", cluster=1),
    R("en.vocab.robust", "en", "vocab", "C", r"\brobust(?:ly|ness)?\b", "Vague praise.", cluster=1),
    R("en.vocab.seamless", "en", "vocab", "C", r"\bseamless(?:ly)?\b", "Vague praise.", cluster=1),
    R("en.vocab.vibrant", "en", "vocab", "C", r"\bvibrant\b", "Vague praise.", cluster=1),
    R("en.vocab.groundbreaking", "en", "vocab", "B", r"\bgroundbreaking\b|\bcutting[- ]edge\b",
      "Hype adjective.", cluster=1),
    R("en.vocab.invaluable", "en", "vocab", "B", r"\binvaluable\b|\bunparalleled\b|\bunprecedented\b",
      "Superlative with no number behind it.", cluster=1),
    R("en.vocab.interplay", "en", "vocab", "B", r"\binterplay\b", "Abstract noun."),
    R("en.vocab.ecosystem", "en", "vocab", "C", r"\becosystems?\b|\bframeworks?\b|\blandscapes?\b|\bjourneys?\b",
      "Abstract container noun.", cluster=2, w=0.5, protect=True),
    R("en.vocab.dynamic", "en", "vocab", "C", r"\bdynamic\b|\binnovative\b|\bprofound(?:ly)?\b|"
      r"\bremarkabl[ey]\b|\bessential\b|\bvital\b", "Vague intensifier.", cluster=2, w=0.4),
    R("en.vocab.era-2026", "en", "vocab", "C", r"\bload[- ]bearing\b|\bquietly\b",
      "Reported as a recent assistant tic (anecdotal).", cluster=1, w=0.5),
]
