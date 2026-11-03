"""영어: 군더더기와 유보(hedging), 장황한 구절. 장황한 구절의 가중치는 일부러 낮다.

장황함을 고쳤다고 해서 점수가 'AI 쪽'으로 몰리면 안 되므로 가중치를 낮게 둔다(docs/research.md 5절).
"""
from __future__ import annotations

from .. import fixers as fx
from .build import R, alt

NOTE_LEAD = alt("it is important to note that", "it's important to note that", "it is worth noting that",
                "it's worth noting that", "it should be noted that", "it is worth mentioning that",
                "it's worth mentioning that", "it bears mentioning that", "it is crucial to note that",
                "it is essential to note that", "it is important to remember that",
                "it is important to understand that", "it is important to recognize that",
                "it is worth pointing out that", "it must be noted that", "it goes without saying that",
                "needless to say", "as we all know", "it is no secret that", "it's no secret that")
STOCK = alt("at the end of the day", "in a nutshell", "simply put", "to put it simply", "let's face it",
            "the fact of the matter is that", "the fact of the matter is")
ADVERB = alt("importantly", "interestingly", "crucially", "significantly", "remarkably", "essentially",
             "fundamentally", "undoubtedly", "undeniably", "admittedly", "frankly", "basically")

WORDY = {
    "in order to": "to", "due to the fact that": "because", "despite the fact that": "although",
    "in spite of the fact that": "although", "at this point in time": "now", "at the present time": "now",
    "in the event that": "if", "for the purpose of": "for", "with regard to": "about",
    "in close proximity to": "near", "a large number of": "many", "has the ability to": "can",
    "have the ability to": "can", "is able to": "can", "are able to": "can", "make use of": "use",
    "makes use of": "uses", "made use of": "used", "making use of": "using", "prior to": "before",
    "subsequent to": "after", "in conjunction with": "with", "on a regular basis": "regularly",
    "each and every": "every", "first and foremost": "first", "in the near future": "soon",
    "in light of the fact that": "because", "take into consideration": "consider",
    "takes into consideration": "considers", "give consideration to": "consider",
    "come to the conclusion that": "conclude that", "is indicative of": "shows",
    "are indicative of": "show",
}

RULES = [
    R("en.hedging.note-that", "en", "hedging", "B", NOTE_LEAD + r",?[ \t]*",
      "Throat-clearing before the actual statement.", genre={"academic": 0.7},
      tier="standard", repl="", recap=True, fix_guard=fx.at_clause_start,
      sugg="Delete it; say the point."),
    R("en.hedging.potentially", "en", "hedging", "B", r"\b(may|might|could|can|would|should) potentially\b",
      "Stacked hedge.", tier="standard", repl=r"\1", genre={"academic": 0.7}, sugg="Keep one hedge."),
    R("en.hedging.stock-lead", "en", "hedging", "C", STOCK + r",?[ \t]*",
      "Filler lead-in.", tier="strong", repl="", recap=True, fix_guard=fx.at_sentence_start),
    R("en.hedging.adverb-lead", "en", "hedging", "C", r"^[ \t]*" + ADVERB + r",[ \t]+",
      "Sentence adverb that comments on itself.", w=0.5, genre={"academic": 0.6},
      tier="strong", repl="", recap=True, flags=None),
    R("en.hedging.when-it-comes", "en", "hedging", "C", r"\bwhen it comes to\b",
      "Wordy topic marker; 'for' or 'with' is usually enough.", w=0.4),
    R("en.hedging.arguably", "en", "hedging", "C", r"\barguably\b|\bin many ways\b", "Weasel hedge.", w=0.4,
      cluster=1),
    R("en.hedging.wordy", "en", "hedging", "C", r"\b" + alt(*WORDY) + r"\b",
      "Wordier than the plain phrase.", w=0.3, tier="standard", repl=fx.word_map(WORDY),
      genre={"academic": 0.6}),
    R("en.vocab.notably-lead", "en", "vocab", "A", r"^[ \t]*notably,[ \t]+",
      "Sentence adverb that comments on itself.", tier="strong", repl="", recap=True),
]
