"""영어: 구조 습관. 부정 대구, 분사 꼬리, be 동사 회피, 맺음 요약 같은 '틀'을 잡는다."""
from __future__ import annotations

from .. import fixers as fx
from .build import R, alt

SEP = r"(?:[,;:—–]|\s-\s|\s--\s)"
PIVOT = (r"(?:but\b|it(?:'s| is| also)\b|they(?:'re| are)\b|this is\b|that(?:'s| is)\b|rather\b|"
         r"it also\b|more\b)")
NEGATE = (r"(?:not|never|isn't|aren't|wasn't|weren't|is not|are not|was not|were not)")
PART = alt("highlighting", "underscoring", "showcasing", "emphasizing", "emphasising", "reflecting",
           "demonstrating", "illustrating", "ensuring", "fostering", "cementing", "solidifying",
           "reinforcing", "symbolizing", "signaling", "paving the way", "contributing to",
           "setting the stage", "positioning", "shaping", "empowering")
SUMMARY = alt("in conclusion", "in summary", "in short", "in essence", "to sum up", "to summarize",
              "to summarise", "to conclude", "to wrap up", "overall", "all in all", "ultimately",
              "at the end of the day", "in the end", "the bottom line", "taken together", "looking ahead",
              "moving forward")

RULES = [
    # ---- 부정 대구
    R("en.structure.neg-parallel", "en", "structure", "A",
      r"\b(?:it|this|that|these|they|he|she|we|there)(?:'s| is| are| was| were)?\s*" + NEGATE +
      r"\s+(?:(?:just|only|merely|simply|about|a mere)\b[^.!?\n]{1,110}?" + SEP + r"\s*" + PIVOT +
      r"|(?:just|merely|simply|a mere)\b[^.!?\n]{1,110}?\s+but\b)",
      "Negative parallelism: knocks down a view nobody held, then states the point.",
      tier="strong", repl=fx.neg_parallel_fix,
      sugg="State the point directly (the second half only)."),
    R("en.structure.neg-parallel-noun", "en", "structure", "A",
      r"(?<![\w'])[A-Za-z][\w-]*(?:\s+[\w-]+){0,3}?\s+(?:isn't|aren't|wasn't|weren't|is not|are not)\s+"
      r"(?:just|only|merely|simply)\b[^.!?\n]{1,110}?" + SEP + r"\s*" + PIVOT,
      "Negative parallelism with a noun subject.", sugg="State the point directly (the second half only)."),
    R("en.structure.isnt-x-but-y", "en", "structure", "B",
      r"\b(?:isn't|aren't|wasn't|weren't|is not|are not)\s+(?:the|a|an)\s+[^.!?\n]{1,50}?\s+but\s+(?:the|a|an)\b",
      "'isn't the X but the Y' contrast.", w=0.8, sugg="Say what it is."),
    R("en.structure.on-one-hand", "en", "structure", "C",
      r"\bon (?:the )?one hand\b[^.!?\n]{0,200}?\bon the other(?: hand)?\b",
      "Balanced both-sides frame.", w=0.5, sugg="Commit to the claim the evidence supports."),
    R("en.structure.neg-parallel-about", "en", "structure", "A",
      r"\b(?:isn't|aren't|is not|are not|wasn't) (?:really |just |only )?(?:about|a question of|a matter of)\b"
      r"[^.!?\n]{1,90}?[,;:—–.]\s*(?:it(?:'s| is)|but|they(?:'re| are)|rather)\b",
      "Negative parallelism ('isn't about X, it's about Y').", sugg="State the point directly."),
    R("en.structure.not-only", "en", "structure", "B",
      r"\bnot only\b[^.!?\n]{1,120}?\bbut(?: also)?\b", "'Not only X but also Y' frame.", w=0.7,
      sugg="Use it only when both halves matter equally."),
    R("en.structure.more-than-just", "en", "structure", "B",
      r"\bmore than (?:just|merely|simply|only) (?:an? |the )|\bno longer (?:just|merely|only|simply)\b",
      "Negative-parallel variant."),
    R("en.structure.less-more", "en", "structure", "B", r"\bless about\b[^.!?\n]{1,70}?,\s*more about\b",
      "Negative-parallel variant ('less about X, more about Y')."),
    R("en.structure.no-no-just", "en", "structure", "B", r"(?:\bno [^.!?\n]{1,40}\.\s+){2,}just\b",
      "'No X. No Y. Just Z.' triple."),
    R("en.structure.not-a-but-a", "en", "structure", "B",
      r"\bnot an? [^.!?\n]{1,50}?[,—–]\s*(?:but|rather) an? \b", "'Not a X, but a Y' frame."),

    # ---- 분사 꼬리와 be 동사 회피
    R("en.structure.participial-tail", "en", "structure", "B",
      r",\s+" + PART + r"\b[^.!?\n]{0,160}(?=[.!?])",
      "Tail clause that announces significance ('..., highlighting its importance').",
      tier="strong", repl="", fix_guard=fx.no_digits_or_names,
      sugg="Delete the tail unless it adds a checkable fact."),
    R("en.structure.copula", "en", "structure", "B",
      r"\b(?P<v>serves|serve|served|stands|stand|stood)\s+as\s+(?P<art>an?|the)\b",
      "Fancy verb where 'is' works.", tier="standard", repl=fx.copula),
    R("en.structure.boasts", "en", "structure", "B", r"\bboast(?:s|ed|ing)? (?=(?:an?|the|over|more|nearly|some|\d)\b)",
      "'Boasts' for 'has'.", tier="strong",
      repl=lambda m, c: {"boasts": "has ", "boast": "have ", "boasted": "had ", "boasting": "having "}.get(
          m.group(0).strip().lower())),
    R("en.structure.considered", "en", "structure", "C",
      r"\bis (?:widely |often |generally |commonly )(?:considered|regarded|seen|viewed) as\b",
      "Vague framing.", genre={"academic": 0.5}),

    # ---- 맺음과 거짓 양보
    R("en.structure.summary-open", "en", "structure", "B",
      r"^[ \t]*(?:#{1,6}[ \t]+)?" + SUMMARY + r"\b[,:]?",
      "Paragraph restates what was just said.", w=0.6, genre={"academic": 0.5},
      sugg="Delete if it only repeats; keep only a real decision or next step."),
    R("en.structure.summary-heading", "en", "structure", "C",
      r"^#{1,6}[ \t]*(?:conclusion|final thoughts|key takeaways|takeaways|the bottom line|wrapping up|"
      r"closing thoughts)[ \t]*$", "Template heading.", w=0.4),
    R("en.structure.false-concession", "en", "structure", "C",
      r"\bwhile [^.!?\n]{3,80}?(?:has|have|may have) (?:its |their |some )?(?:limitations|drawbacks|challenges|"
      r"downsides|flaws|shortcomings)[^.!?\n]{0,60},\s", "'While X has limits, it is still great' frame."),
    R("en.structure.false-range", "en", "structure", "C",
      r"\beverything from\b[^.!?\n]{3,60}\bto\b|\bfrom [A-Za-z ]{3,30} to [A-Za-z ]{3,30}, and everything in between",
      "Range with no real scale."),
    R("en.structure.staged-honest", "en", "structure", "C",
      r"\b(?:honestly|frankly|candidly|truthfully)\?[ \t]", "Staged candor."),
    # ---- 10개 상투 개념 대응
    R("en.structure.paired-with", "en", "structure", "B",
      r"\b(?:paired with|coupled with|hand in hand with|two sides of the same coin)\b",
      "Overused coupling phrase.", tier="standard", repl=fx.en_paired_with,
      sugg="Use 'with' or state the concrete relationship directly."),
]
