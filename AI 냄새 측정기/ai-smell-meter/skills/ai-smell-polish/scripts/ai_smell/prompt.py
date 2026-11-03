"""LLM에게 맡길 윤문 프롬프트를 만든다. 엔진이 못 고치는 구조 습관을 사람 대신 모델이 고치게 하는 단계다.

모델에 상관없이 쓰도록 마크다운 틀이 기본이고, target='claude'는 같은 내용을 XML 태그로 감싼다.
프롬프트는 '탐지기를 속이라'는 지시를 담지 않는다. 오히려 그런 조작을 금지한다.
"""
from __future__ import annotations

from typing import List

from .model import CATEGORIES, Analysis, Finding
from .textutil import excerpt
from .verify import facts_for_prompt

KO_RULES = """\
1. 사실을 만들지 않는다. 「바꾸지 말 것」의 숫자, 주소, 코드, 인용, 고유명사는 그대로 둔다. 새 사실, 인용, 통계, 속담을 보태지 않는다.
2. 필자의 목소리를 지키고 빼기 중심으로 고친다. 격식을 올리지 않고, 구어 종결과 의도된 문체를 지우지 않는다.
3. 변경률은 원문의 5~30%가 권장이다. 30%를 넘으면 경고하고, 50%를 넘으면 멈추고 필자에게 묻는다.
4. 「걸린 신호」만 국소 수정한다. 문단을 통째로 다시 쓰지 않는다. 같은 유형이 두 번 고쳐도 남으면 접근을 바꾼다.
5. 구체적 내용이 없는 글은 지어내서 채우지 않는다. 필자에게 알맹이(수치, 사례, 고유명사)를 묻는다."""

KO_FIX = """\
- 부정 대구("A가 아니라 B"): B만 말하거나 한 문장 안에서 정정한다. 독자가 실제로 가질 오해를 바로잡는 한두 개는 남긴다.
- 의미 부풀리기("시사하는 바가 크다", "주목할 만하다", "중요한 역할"): 구체적 사실로 바꾸거나 지운다.
- 번역투: 어색한 곳에만 고친다. "~에 대해"는 을/를로, "~에 있어서"는 "~에서"로, 이중 피동은 단순 피동이나 능동으로. 일괄 치환하지 않는다.
- 문두 접속어: 한 문단에 3번 이상일 때 절반만 덜고, 앞 문장 끝말을 다음 문장이 받게 한다.
- 3항 나열: 뜻이 요구하는 개수만 남긴다.
- 감정 직접 서술: 행동, 사물, 말로 드러내거나 한 문단에 하나만 남긴다.
- 챗봇식 서두, 맺음, 예고, 되풀이 요약: 지운다.
- 같은 종결이 4문장 넘게 이어지면 구조를 바꾼다. 억지로 변주하지 않는다.
- 서술어 후치("했다, 조용히")와 분열문("중요한 것은 ~이다")은 평서 어순으로 되돌린다. 한 글에 한 번 이하.
- 한 문단 안에서 존댓말과 평어가 섞였으면 하나로 맞춘다. 필자가 보인 의도된 섞임은 따른다.
- 느낌표와 이모지로 감정을 대신하지 않는다. 필자가 그 문체를 쓸 때만 맞춘다.
- 학술은 한다체와 피동을 일률 제거하지 않는다. 일상은 사과와 감사를 한 번씩만. 문학은 도치와 반전 문장을 장면당 하나 이하."""

KO_BAN = """\
- 오타, 비문, 속어를 일부러 넣어 사람처럼 보이게 하는 것, 동의어로 낱말만 바꾸는 것(새 신호가 생긴다), 탐지기 회피를 노린 모든 조작은 하지 않는다."""

EN_RULES = """\
1. Invent nothing. Keep every number, URL, code span, quotation, and proper noun listed under "Do not change". Add no new facts, sources, or statistics.
2. Preserve the author's voice. Prefer deleting to rewriting, and rewriting to adding. Do not raise the register or smooth out intentional style.
3. Aim to change 5-30% of the words. Above 30%, flag it; above 50%, stop and ask the author.
4. Fix only the flagged signals, locally. Do not regenerate whole paragraphs. If a pattern survives two passes, change approach.
5. If the text has no specifics, do not make them up. Ask the author for the concrete detail (a number, a case, a name)."""

EN_FIX = """\
- Negative parallelism ("not just X, but Y"): state Y directly; keep a contrast only when a reader would plausibly hold the mistaken view.
- Importance inflation ("plays a vital role", "stands as a testament", "-ing" tails like "highlighting its importance"): give the concrete fact or delete.
- Vague authority ("experts say", "studies show"): name the source or delete. Never invent one.
- Plain verbs: "is/has/uses" over "serves as/boasts/utilizes/leverages".
- Chatbot residue, signposting ("Let's dive in"), restating summaries, stacked transitions: delete.
- Lists of three: keep only the count the meaning needs.
- Hedging: keep one hedge where the uncertainty is real; delete throat-clearing ("It is important to note that").
- Formatting: drop emoji bullets, bold lead-ins, and decorative headings; keep an em dash only where it earns its place.
- Match the genre and register of the original (academic, business, casual, fiction)."""

EN_BAN = """\
- Do not add typos, slang, or randomness to seem human. Do not swap synonyms one-for-one (it creates new tells). Do not do anything aimed at evading AI detectors."""

KO_OUT = """\
1. 교정문만 `---` 두 줄 사이에 둔다.
2. 그 아래에 변경 요약을 5개 이내로 쓴다(무엇을 왜).
3. 필자에게 물을 것이 있으면 「확인 질문:」으로 따로 쓴다.
4. 사람이 쓴 것 같다고 단정하지 않는다."""

EN_OUT = """\
1. Put only the corrected text between two `---` lines.
2. Below it, list at most 5 changes (what and why).
3. If you need something from the author, add a separate "Questions:" line.
4. Do not claim the result "reads as human"."""


def _finding_lines(text: str, findings: List[Finding], limit: int, ui: str) -> List[str]:
    scored = sorted((f for f in findings if not f.shadowed and f.weight > 0), key=lambda f: (-f.weight, f.start))
    out = []
    for f in sorted(scored[:limit], key=lambda f: f.start):
        cat = CATEGORIES[f.category]
        name = cat.ko if ui == "ko" else cat.en
        ctx = excerpt(text, f.start, f.end, pad=10, limit=90)
        hint = f" → {f.sugg}" if f.sugg else ""
        out.append(f"- {f.line}{'행' if ui == 'ko' else ''} [{name}] \"{ctx}\" — {f.note}{hint}")
    if len(scored) > limit:
        out.append(f"- … +{len(scored) - limit}")
    return out


def _facts_block(text: str, ui: str) -> str:
    facts = facts_for_prompt(text)
    labels = {"numbers": ("숫자", "Numbers"), "urls": ("주소", "URLs"), "names": ("영문 고유명사 후보", "Proper nouns"),
              "code": ("코드", "Code"), "quotes": ("직접 인용", "Quotations")}
    lines = []
    for key, (ko, en) in labels.items():
        if facts[key]:
            lines.append(f"- {ko if ui == 'ko' else en}: " + ", ".join(str(x) for x in facts[key][:25]))
    return "\n".join(lines) if lines else ("- (없음)" if ui == "ko" else "- (none)")


def build(text: str, analysis: Analysis, *, ui: str = "", target: str = "generic", limit: int = 25) -> str:
    lang = ui or ("en" if analysis.lang == "en" else "ko")
    ko = lang == "ko"
    h = {"role": "# 역할" if ko else "# Role", "rules": "# 원칙" if ko else "# Rules",
         "fix": "# 고치는 방법" if ko else "# How to fix", "ban": "# 하지 말 것" if ko else "# Do not",
         "facts": "# 바꾸지 말 것" if ko else "# Do not change",
         "found": f"# 걸린 신호 ({analysis.score}/100)" if ko else f"# Flagged signals ({analysis.score}/100)",
         "out": "# 출력 형식" if ko else "# Output format", "text": "# 원문" if ko else "# Text"}
    role = ("당신은 한국어 글을 윤문하는 편집자입니다. 목표는 읽는 사람이 걸리지 않고 읽는 글입니다. "
            "AI 탐지기를 통과시키는 것은 목표가 아닙니다. 장르: " + analysis.genre + "."
            if ko else "You are a line editor. The goal is text that reads naturally to a person, not text that "
            "passes an AI detector. Genre: " + analysis.genre + ". Reply in the language of the text.")
    findings = "\n".join(_finding_lines(text, analysis.findings, limit, lang)) or ("- (없음)" if ko else "- (none)")
    body = [(h["role"], role), (h["rules"], KO_RULES if ko else EN_RULES), (h["fix"], KO_FIX if ko else EN_FIX),
            (h["ban"], KO_BAN if ko else EN_BAN), (h["facts"], _facts_block(text, lang)), (h["found"], findings),
            (h["out"], KO_OUT if ko else EN_OUT)]
    if target == "claude":
        tags = ["role", "rules", "how_to_fix", "do_not", "do_not_change", "flagged_signals", "output_format"]
        parts = [f"<{tag}>\n{content}\n</{tag}>" for tag, (_, content) in zip(tags, body)]
        parts.append(f"<text>\n{text}\n</text>")
        return "\n\n".join(parts)
    parts = [f"{title}\n{content}" for title, content in body]
    parts.append(f"{h['text']}\n---\n{text}\n---")
    return "\n\n".join(parts)


CHAT_STEP_KO = """\
0. 먼저 글에서 AI 냄새 신호를 목록으로 뽑는다(줄 번호, 원문 일부, 유형). 신호가 없으면 "신호 없음"이라 쓰고 고치지 않는다.
1. 목록의 신호만 국소 수정한다."""

CHAT_STEP_EN = """\
0. First list the AI-sounding signals you find (line, quoted fragment, type). If there are none, say "no signals" and change nothing.
1. Fix only the listed signals, locally."""


def chat_prompt(lang: str) -> str:
    """셸이 없는 채팅 환경에 붙여 넣는 프롬프트. 엔진의 지수와 대조 검증이 없는 대신 신호 목록을 먼저 뽑게 한다."""
    ko = lang == "ko"
    out_rules = (KO_OUT if ko else EN_OUT)
    parts = [("# 역할" if ko else "# Role",
              "당신은 한국어 글을 윤문하는 편집자입니다. 목표는 읽는 사람이 걸리지 않고 읽는 글입니다. AI 탐지기를 "
              "통과시키는 것은 목표가 아닙니다." if ko else
              "You are a line editor. The goal is text that reads naturally to a person, not text that passes an AI "
              "detector. Reply in the language of the text."),
             ("# 순서" if ko else "# Steps", CHAT_STEP_KO if ko else CHAT_STEP_EN),
             ("# 원칙" if ko else "# Rules", (KO_RULES if ko else EN_RULES).replace("「바꾸지 말 것」의", "글 속의")
              .replace(' listed under "Do not change"', " in the text")),
             ("# 고치는 방법" if ko else "# How to fix", KO_FIX if ko else EN_FIX),
             ("# 하지 말 것" if ko else "# Do not", KO_BAN if ko else EN_BAN),
             ("# 출력 형식" if ko else "# Output format", out_rules),
             ("# 원문" if ko else "# Text", "---\n{{여기에 글을 붙여 넣는다}}\n---" if ko else
              "---\n{{paste the text here}}\n---")]
    return "\n\n".join(f"{h}\n{b}" for h, b in parts) + "\n"
