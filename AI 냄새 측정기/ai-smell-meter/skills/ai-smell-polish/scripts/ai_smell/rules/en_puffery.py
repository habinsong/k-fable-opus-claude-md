"""영어: 의미 부풀리기(puffery), 출처 없는 권위, 예고·안내. 근거는 docs/research.md 3절."""
from __future__ import annotations

from .. import fixers as fx
from .build import R, alt

ROLE = alt("vital", "crucial", "pivotal", "key", "significant", "important", "critical", "central",
           "essential", "integral", "major", "fundamental", "instrumental")
WORLD = alt("fast-paced", "digital", "modern", "ever-changing", "rapidly changing", "rapidly evolving",
            "interconnected", "competitive", "dynamic", "technology-driven", "globalized", "ever-evolving")
EVOLVING = alt("ever-evolving", "ever-changing", "rapidly evolving", "rapidly changing", "fast-paced",
               "ever-shifting", "ever-growing", "ever-expanding")
NOUN = alt("world", "age", "era", "landscape", "society", "environment", "economy", "marketplace")

RULES = [
    # ---- 의미 부풀리기
    R("en.puffery.testament", "en", "puffery", "B",
      r"\ba (?:powerful |enduring |living |true |clear |lasting |remarkable )?testament (?:to|of)\b",
      "Inflates a small fact into a symbol.", sugg="State the fact; drop the symbolism."),
    R("en.puffery.vital-role", "en", "puffery", "B",
      r"\bplay(?:s|ed|ing)? an? " + ROLE + r" role (?:in|as)\b",
      "Importance asserted instead of shown.", sugg="Say what it actually does."),
    R("en.puffery.underscores", "en", "puffery", "B",
      r"\b(?:underscor|highlight|emphasi[sz]|reinforc)(?:e|es|ed|ing) (?:the |its |their |an? )?"
      r"(?:importance|significance|need|value|role|power)\b",
      "Sentence announces its own significance.", sugg="Delete or replace with the concrete consequence."),
    R("en.puffery.tapestry", "en", "puffery", "B",
      r"\b(?:rich|vibrant|intricate|complex|diverse|woven) tapestry\b", "Stock metaphor.",
      sugg="Name the actual parts."),
    R("en.puffery.todays-world", "en", "puffery", "B",
      r"\bin (?:today's|the modern|this|our) (?:" + WORLD + r"[ \t]+){1,2}" + NOUN + r"\b,?[ \t]*",
      "Generic scene-setting opener.", tier="standard", repl="", recap=True, fix_guard=fx.at_sentence_start,
      sugg="Start with the actual subject."),
    R("en.puffery.evolving-landscape", "en", "puffery", "B",
      r"\b(?:the )?" + EVOLVING + r" (?:landscape|world|realm|field|space|environment|digital \w+)\b",
      "Stock phrase for change.", sugg="Use the specific change (what, when)."),
    R("en.puffery.navigate", "en", "puffery", "B",
      r"\bnavigat(?:e|es|ed|ing) (?:the |this |these |today's )?(?:complexit(?:y|ies)|challenges|intricacies|"
      r"landscape|nuances|waters|maze|terrain)\b", "Navigation metaphor.", sugg="Say what is being done."),
    R("en.puffery.beacon", "en", "puffery", "C",
      r"\b(?:a |the )?(?:beacon|cornerstone|bedrock|linchpin|hallmark) of\b", "Monument metaphor."),
    R("en.puffery.paving", "en", "puffery", "B", r"\bpav(?:e|es|ed|ing) the way (?:for|to)\b",
      "Stock phrase for 'enables'.", sugg="Use a plain verb and name the result."),
    R("en.puffery.unlock", "en", "puffery", "B",
      r"\bunlock(?:s|ed|ing)? (?:the |its |their |your )?(?:full |true |hidden |untapped |immense |incredible )?"
      r"(?:potential|power|possibilities|value|secrets?)\b", "Stock phrase."),
    R("en.puffery.game-changer", "en", "puffery", "B", r"\bgame[- ]chang(?:er|ing)\b", "Hype word."),
    R("en.puffery.future-bright", "en", "puffery", "B",
      r"\bthe future (?:looks|is|remains|seems) (?:incredibly |very )?(?:bright|promising|exciting)\b"
      r"|\bthe possibilities are (?:endless|limitless|boundless)\b|\bendless possibilities\b",
      "Empty forward-looking close.", sugg="Cut, or say what will be tested or decided next."),
    R("en.puffery.only-time", "en", "puffery", "C", r"\bonly time will tell\b|\bremains to be seen\b",
      "Empty forward-looking close."),
    R("en.puffery.lasting", "en", "puffery", "C",
      r"\b(?:lasting|indelible|profound|enduring) (?:impact|legacy|impression|mark)\b", "Legacy cliche."),
    R("en.puffery.travel", "en", "puffery", "C",
      r"\bnestled (?:in|within|among|at)\b|\bin the heart of\b|\bbreathtaking\b|\bmust[- ]visit\b|"
      r"\brich (?:cultural |historical )?(?:heritage|history|tradition)\b|\bbustling\b",
      "Brochure language."),
    R("en.puffery.unwavering", "en", "puffery", "B",
      r"\bunwavering (?:commitment|dedication|support|focus|determination)\b|"
      r"\brelentless (?:pursuit|focus|commitment)\b", "Intensified abstraction."),
    R("en.puffery.transformative", "en", "puffery", "B",
      r"\btransformative (?:power|potential|impact|journey|force|technology)\b", "Hype phrase."),
    R("en.puffery.new-era", "en", "puffery", "B",
      r"\bushers? in a new era\b|\ba new era of\b|\bmarks? an? (?:significant |pivotal |new |major |watershed )?"
      r"(?:turning point|milestone|chapter|moment|shift)\b", "Importance inflation."),
    R("en.puffery.metaphor-of", "en", "puffery", "C",
      r"\ba (?:symphony|mosaic|kaleidoscope|dance|journey|tapestry) of\b", "Stock metaphor."),
    R("en.puffery.realm", "en", "puffery", "C", r"\bin the (?:realm|domain|sphere) of\b",
      "Abstract container; 'in' is enough."),
    R("en.puffery.fragment-closer", "en", "puffery", "B",
      r"\blet that sink in\b\.?|\bread that again\b\.?|\bsound familiar\?|\bthis changes everything\b\.?|"
      r"\band that(?:'s| is) (?:okay|fine|the point)\b\.?", "Dramatic one-line closer.",
      sugg="Cut it; the preceding sentence already made the point."),
    R("en.puffery.the-real", "en", "puffery", "C",
      r"\bthe real (?:question|problem|issue|challenge|story|magic|power|secret|difference|reason|test)\b"
      r"|\bhere(?:'s| is) where it gets (?:interesting|tricky|complicated)\b",
      "Staged reveal."),
    R("en.puffery.honest-answer", "en", "puffery", "C",
      r"\bthe (?:honest|short|simple|truthful) (?:answer|truth|version)(?: is)?[:,]|\bsit with that\b",
      "Anecdotal tic reported for recent assistants; weak evidence."),

    # ---- 출처 없는 권위 (인용 표시가 뒤따르면 세지 않는다)
    R("en.attribution.vague", "en", "attribution", "B",
      r"\b(?:experts|researchers|scientists|analysts|observers|critics|historians|scholars|economists|"
      r"industry (?:experts|observers|analysts|insiders|leaders|reports?)|many (?:experts|people|scholars|"
      r"observers)|some (?:critics|experts|observers)|studies (?:show|suggest|indicate|have shown|have found|reveal)|"
      r"research (?:shows|suggests|indicates|has shown)|reports suggest|"
      r"it is (?:widely|generally|commonly|often) (?:believed|known|accepted|recognized|agreed|said|argued))\b",
      "Authority without a named source.", guard=fx.no_cite_after,
      sugg="Name the source (who, where, when) or drop the claim."),

    # ---- 예고와 안내
    R("en.signpost.lets-pure", "en", "signpost", "B",
      r"let(?:'s| us) (?:dive in|dive deeper|get started|break it down|unpack (?:this|that|it)|jump in|"
      r"dive into (?:it|the details))[.!:]?",
      "Content-free announcement.", tier="standard", repl="", scope="sentence",
      sugg="Delete the announcement."),
    R("en.signpost.lets", "en", "signpost", "B",
      r"^[ \t]*let(?:'s| us) (?:dive|delve|explore|take a (?:closer |deeper )?look|walk through|break)\b",
      "Announces what will be done instead of doing it.", w=0.6),
    R("en.signpost.in-this", "en", "signpost", "C",
      r"\bin this (?:article|post|guide|section|blog post|essay|piece|tutorial),? (?:we|i)(?:'ll| will)? "
      r"(?:explore|discuss|delve|examine|look at|cover|dive|walk through|break down|unpack)\b",
      "Table-of-contents sentence.", genre={"academic": 0.4}),
    R("en.signpost.stock", "en", "signpost", "C",
      r"\b(?:here(?:'s| is) (?:what|everything) you need to know|without further ado|buckle up|read on|"
      r"stay tuned|spoiler alert)\b", "Hook phrase."),
    R("en.signpost.heres-the-thing", "en", "signpost", "B",
      r"\bhere(?:'s| is) the (?:thing|kicker|catch|deal|truth|twist)[:,.][ \t]*",
      "Staged run-up.", tier="strong", repl="", recap=True, fix_guard=fx.at_sentence_start),
    R("en.signpost.the-x-question", "en", "signpost", "B",
      r"\b(?:the|here's the) (?:result|catch|kicker|twist|problem|upshot|punchline|bottom line|secret)\?",
      "Self-posed question answered at once.", sugg="State the point without the question."),
    R("en.signpost.question-opener", "en", "signpost", "C",
      r"^[ \t]*(?:ever|have you ever) (?:wondered|thought|asked yourself|noticed)\b[^?\n]*\?|"
      r"^[ \t]*(?:imagine|picture) (?:this|a world|if|yourself)\b|^[ \t]*what if (?:i told you|you could)\b",
      "Hook opening."),
    R("en.signpost.whether", "en", "signpost", "B",
      r"\bwhether you(?:'re| are) (?:an? |just |new |already |looking |trying )[^.!?\n]{0,60}?"
      r"(?:\bor\b|,)[^.!?\n]{0,60},", "'Whether you're A or B' audience sweep."),
]
