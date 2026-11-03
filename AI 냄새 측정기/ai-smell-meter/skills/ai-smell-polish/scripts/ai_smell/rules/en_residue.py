"""영어: 챗봇 잔재, 아첨, 자리표시자, 누출된 마크업. 글 내용이 아니라 대화의 껍데기를 잡는다."""
from __future__ import annotations

import re

from .. import fixers as fx
from .build import R

TAIL = r"[^.!?\n]*[.!?]"          # 문장 끝까지

RULES = [
    # ---- 챗봇 잔재 (대화체 인사, 서두, 맺음)
    R("en.residue.opener", "en", "residue", "A",
      r"^([ \t]*(?:[-*\u2022][ \t]+)?)(?:certainly|sure|absolutely|of course|definitely|sure thing)[!.,][ \t]+(?=[A-Z])",
      "Paragraph opens with a chatbot acknowledgement.", tier="standard", repl=r"\1",
      sugg="Delete the acknowledgement and start with the content."),
    R("en.residue.here-is-revised", "en", "residue", "A",
      r"(?:here(?:'s| is)|below is|i(?:'ve| have) (?:rewritten|revised|polished|updated)) "
      r"(?:a |an |the |your |my )?(?:revised|rewritten|polished|improved|updated|edited|final|cleaned[- ]up)"
      r"[^.\n]{0,60}[:.]",
      "Meta sentence introducing the edited text.", tier="standard", repl="", scope="sentence",
      sugg="Delete the lead-in."),
    R("en.residue.hope-helps", "en", "residue", "A",
      r"(?:i hope|hope) (?:this|that|these|it) (?:helps|was helpful|is helpful|clarifies|answers)" + TAIL,
      "Chatbot sign-off.", tier="standard", repl="", scope="sentence", guard=fx.tail_sentence,
      sugg="Delete the sign-off."),
    R("en.residue.let-me-know", "en", "residue", "A",
      r"(?:please )?(?:let me know|feel free to (?:ask|reach out|let me know)|don't hesitate to|"
      r"if you (?:have|need|want|would like)(?: any)?(?: further| more| additional)? "
      r"(?:questions|help|assistance|clarification|changes|adjustments|modifications)|"
      r"is there anything else)" + TAIL,
      "Offer of further help at the end.", tier="standard", repl="", scope="sentence", guard=fx.tail_sentence,
      sugg="Delete the closing offer unless this is a real email that needs it."),
    R("en.residue.happy-to-help", "en", "residue", "A",
      r"(?:i(?:'d| would) be (?:happy|glad|delighted) to help|i(?:'m| am) (?:happy|glad) to help)" + TAIL,
      "Eager-to-help line.", tier="standard", repl="", scope="sentence", guard=fx.at_sentence_start),
    R("en.residue.apology", "en", "residue", "A",
      r"(?:i apologi[sz]e for (?:any|the) (?:confusion|inconvenience|misunderstanding|oversight|error)|"
      r"apologies for (?:any|the) (?:confusion|inconvenience|misunderstanding))" + TAIL,
      "Stock apology.", tier="standard", repl="", scope="sentence", guard=fx.at_sentence_start),
    R("en.residue.as-an-ai", "en", "residue", "A",
      r"\bas an? (?:ai|artificial intelligence|large language model|language model|llm|ai assistant|"
      r"ai language model)(?: model)?,[ \t]*",
      "Model self-reference as a preamble.", tier="standard", repl="", recap=True,
      sugg="Delete the preamble."),
    R("en.residue.no-opinions", "en", "residue", "A",
      r"\bi (?:don't|do not|cannot|can't) (?:have|hold|form) (?:personal )?(?:opinions|feelings|beliefs|experiences)\b"
      r"|\bi (?:don't|do not|cannot|can't) (?:browse|access) (?:the internet|real-time|live|current)\b",
      "Model limitation disclaimer.", sugg="Remove it; check whether the claim it guards is still current."),
    R("en.residue.cutoff", "en", "residue", "A",
      r"\b(?:as of|up to) my (?:last )?(?:knowledge |training )?(?:cutoff|update|training)(?: date)?\b"
      r"|\bmy (?:knowledge|training) (?:cutoff|data) (?:is|ends)\b",
      "Knowledge-cutoff disclaimer.", sugg="Replace with a dated source or delete."),
    R("en.residue.generated-note", "en", "residue", "A",
      r"^[ \t]*(?:note|disclaimer)?:?[ \t]*this (?:response|text|content|article|essay) was "
      r"(?:generated|written|created|produced) (?:by|with|using) (?:an? )?(?:ai|chatgpt|gpt|claude|gemini|"
      r"a language model)[^\n]*\n?",
      "Self-label line.", tier="standard", repl=""),

    # ---- 아첨과 공치사
    R("en.sycophancy.praise", "en", "sycophancy", "A",
      r"(?:(?:what|such) an? |that(?:'s| is) an? |this is an? )?(?:great|excellent|fantastic|wonderful|"
      r"insightful|fascinating|thoughtful|good|interesting) (?:question|point|observation|catch|idea)[!.]",
      "Praises the question before answering.", tier="standard", repl="", scope="sentence",
      sugg="Delete it and answer."),
    R("en.sycophancy.right", "en", "sycophancy", "A",
      r"\byou(?:'re| are) (?:absolutely|completely|totally|entirely|quite) (?:right|correct)[!.,]?[ \t]*",
      "Agreement opener that agrees before checking.", tier="standard", repl="", recap=True),

    # ---- 채우지 않은 자리표시자, 누출된 마크업 (사람 글에서는 거의 없는 흔적)
    R("en.placeholder.bracket", "en", "placeholder", "A",
      r"\[(?:your|insert|add|company|recipient|client|customer|name|date|title|link|url|address|phone|email|"
      r"topic|city|brand|product)[^\]\n]{0,40}\]",
      "Template slot left unfilled.", flags=re.I | re.M,
      sugg="Fill it in or delete the line."),
    R("any.markup.utm", "any", "markup", "A",
      r"[?&]utm_source=(?:chatgpt\.com|openai|copilot\.com|perplexity)(?:&[^\s)\]>\"']*)?",
      "Chat tool tag in a URL.", tier="safe", repl=fx.utm_param, protect=False,
      sugg="Strip the tracking parameter."),
    R("en.residue.signpost-polish", "en", "residue", "B",
      r"^[ \t]*(?:revised|rewritten|polished|improved|edited) (?:version|text|draft)[ \t]*:[ \t]*\n+",
      "Label line for the edited text.", tier="standard", repl=""),
]

