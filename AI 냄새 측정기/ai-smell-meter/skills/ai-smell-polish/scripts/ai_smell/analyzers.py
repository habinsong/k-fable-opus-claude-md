"""정규식 한 줄로 잡히지 않고 '밀도'와 '연속'으로 판단하는 신호들.

각 함수는 Finding 목록을 돌려준다. 줄·열은 detect가 채운다. 문서 전체에 대한 신호는
길이 0인 구간(start == end)으로 두어 다른 신호와 겹쳐 가려지지 않게 한다.
"""
from __future__ import annotations

import re
import bisect
from typing import List, Optional, Sequence, Tuple

from .model import Edit, Finding, weigh

Span = Tuple[int, int]

EN_TRANS = re.compile(r"(?P<w>Moreover|Furthermore|Additionally|In addition|Consequently|Nevertheless|Nonetheless|"
                      r"Thus|Hence|Accordingly|Subsequently|Likewise|Similarly|Conversely|Meanwhile|Indeed|"
                      r"Overall|Ultimately)\b,?[ \t]*", re.I)
EN_ADDITIVE = {"moreover", "furthermore", "additionally", "in addition", "likewise", "similarly"}
KO_TRANS = re.compile(r"(?P<w>또한|아울러|더불어|나아가|게다가|뿐만\s*아니라|이와\s*함께|이에\s*따라|이를\s*통해|특히|"
                      r"무엇보다|한편|따라서|결과적으로|결국|즉|다시\s*말해|요컨대|반면|그럼에도)(?![가-힣])[,，]?[ \t]*")
KO_ADDITIVE = {"또한", "아울러", "더불어", "나아가", "게다가"}
EN_TRIPLE = re.compile(r"\b(?:the |a |an )?[\w'’-]+(?: [\w'’-]+)?, (?:the |a |an )?[\w'’-]+(?: [\w'’-]+)?,? "
                       r"(?:and|or) (?:the |a |an )?[\w'’-]+(?: [\w'’-]+)?\b")
EN_INTENS = re.compile(r"\b(?:very|really|truly|genuinely|incredibly|extremely|highly|deeply|profoundly|"
                       r"absolutely|undoubtedly|remarkably|exceptionally|tremendously)\b[ \t]?", re.I)
EN_INTENS_DROP = {"truly", "genuinely", "incredibly", "extremely", "remarkably", "exceptionally",
                  "tremendously", "profoundly", "undoubtedly"}
KO_INTENS = re.compile(r"(?<![가-힣])(?:매우|정말|굉장히|상당히|아주|너무|엄청|대단히|극도로|무척)(?![가-힣])[ \t]?")
EMOTION = ("기뻤", "슬펐", "행복했", "외로웠", "두려웠", "불안했", "벅차", "벅찼", "먹먹", "울컥", "뭉클", "철렁",
           "눈물이 흘렀", "숨이 멎", "가슴이 아렸", "가슴이 미어", "감동", "설렜", "서글펐", "그리웠", "뿌듯",
           "애틋", "저릿", "찡했", "눈시울", "가슴이 뛰", "심장이 뛰", "숨이 막", "온몸이 떨", "마음이 무거웠",
           "슬퍼졌", "외로워졌", "행복해졌")
DASH = re.compile("[—―]|(?<=[A-Za-z가-힣]) -- (?=[A-Za-z가-힣])|(?<=[A-Za-z가-힣]) – (?=[A-Za-z가-힣])")


def _mk(rid: str, cat: str, grade: str, start: int, end: int, w: float, genre: str, note: str, *,
        gmap=None, sugg: str = "", text: str = "", lang: str = "any", edit: Optional[Edit] = None) -> Finding:
    return Finding(rule_id=rid, category=cat, grade=grade, start=start, end=end, text=text, line=0, col=0,
                   weight=weigh(cat, grade, w, gmap or {}, genre), note=note, sugg=sugg,
                   tier=edit.tier if edit else "none", fixable=edit is not None, lang=lang, edit=edit)


def _sentence_of(sents: Sequence[Span], starts: Sequence[int], pos: int) -> Optional[Span]:
    i = bisect.bisect_right(starts, pos) - 1
    if i >= 0 and sents[i][0] <= pos <= sents[i][1]:
        return sents[i]
    return None


def _by_para(sents: Sequence[Span], paras: Sequence[Span]) -> List[List[Span]]:
    """문단마다 그 안의 문장 목록. 둘 다 정렬돼 있으므로 한 번에 훑는다."""
    out: List[List[Span]] = []
    i, n = 0, len(sents)
    for ps, pe in paras:
        while i < n and sents[i][0] < ps:
            i += 1
        group: List[Span] = []
        while i < n and sents[i][1] <= pe:
            group.append(sents[i])
            i += 1
        out.append(group)
    return out


def dashes(masked: str, sents: Sequence[Span], units: int, genre: str) -> List[Finding]:
    """줄표가 3개 이상이면 센다. 한 문장의 한 쌍은 쉼표로(standard), 이어 붙이는 하나는 strong에서 쉼표로."""
    hits = list(DASH.finditer(masked))
    if len(hits) < 3:
        return []
    out: List[Finding] = []
    per_sentence = {}
    starts = [x[0] for x in sents]
    for m in hits:
        sp = _sentence_of(sents, starts, m.start())
        per_sentence.setdefault(sp, []).append(m)
    for sp, ms in per_sentence.items():
        for i, m in enumerate(ms):
            s, e = m.start(), m.end()
            while s > 0 and masked[s - 1] in " \t":
                s -= 1
            while e < len(masked) and masked[e] in " \t":
                e += 1
            nxt = masked[e:e + 1]
            edit = None
            if len(ms) == 2 and sp is not None:
                inner = masked[ms[0].end():ms[1].start()]
                if 2 <= len(inner.strip()) <= 80 and not re.search(r"[.!?\n]", inner):
                    edit = Edit(s, e, ", ", "any.format.em-dash", "standard", before=masked[s:e])
            elif len(ms) == 1 and nxt.islower() and s > 0 and masked[s - 1].isalnum():
                edit = Edit(s, e, ", ", "any.format.em-dash", "strong", before=masked[s:e])
            out.append(_mk("any.format.em-dash", "format", "B", m.start(), m.end(), 0.4, genre,
                           "줄표(em dash)가 여러 번 쓰였다.", text=m.group(0).strip(),
                           sugg="쉼표, 마침표, 괄호로 바꾼다.", edit=edit))
    return out


def _delete_edit(rid: str, start: int, end: int, tier: str, recap: bool, text: str) -> Edit:
    return Edit(start, end, "", rid, tier, recap=recap, before=text[start:end])


def transitions(text: str, masked: str, sents: Sequence[Span], paras: Sequence[Span], genre: str,
                gmap) -> List[Finding]:
    """문두 접속어가 문단 안에 3번 이상이면 절반(2번째, 4번째...)을 센다. 더하기 접속어만 지울 수 있다."""
    out: List[Finding] = []
    flagged: List[Tuple[Span, re.Match, str]] = []
    doc_hits: List[Tuple[Span, re.Match, str]] = []
    for group in _by_para(sents, paras):
        hits = []
        for sp in group:
            km = KO_TRANS.match(masked, sp[0])
            m = km or EN_TRANS.match(masked, sp[0])
            if m:
                hits.append((sp, m, "ko" if km else "en"))
        doc_hits.extend(hits)
        if len(hits) >= 3:
            flagged.extend(hits[1::2])
    if not flagged and len(doc_hits) >= 5 and len(doc_hits) / max(len(sents), 1) >= 0.3:
        flagged = doc_hits[1::2]
    for sp, m, lang in flagged:
        word = re.sub(r"\s+", " ", m.group("w").lower())
        additive = word in (EN_ADDITIVE if lang == "en" else KO_ADDITIVE)
        edit = _delete_edit(f"{lang}.transition.stack", sp[0], m.end(), "strong", lang == "en", text) if additive else None
        out.append(_mk(f"{lang}.transition.stack", "transition", "B", sp[0], m.end(), None, genre,
                       "문두 접속어가 겹쳤다." if lang == "ko" else "Stacked sentence-initial transitions.",
                       gmap={"academic": 0.6}, text=m.group(0).strip(), lang=lang, edit=edit,
                       sugg="앞 문장의 끝말을 다음 문장이 받게 해서 접속어를 줄인다."))
    return out


def triples(text: str, masked: str, sents: Sequence[Span], paras: Sequence[Span], genre: str) -> List[Finding]:
    """A, B, 그리고 C 꼴의 3항 나열. 문서에 3번 이상이거나 한 문단에 2번 이상일 때만 센다."""
    found: List[Tuple[Span, int, int, str]] = []
    for sp in sents:
        seg = masked[sp[0]:sp[1]]
        if "\x00" in seg or seg.lstrip().startswith("|") or " | " in seg:
            continue                      # 코드·표는 산문 나열이 아니다
        if re.search(r"[가-힣]", seg):
            parts = [x.strip() for x in re.split(r"[,，]", seg.rstrip(".!?… "))]
            if len(parts) == 3 and not re.search(r"\d", seg):
                head = " ".join(parts[0].split()[-2:])
                tail = " ".join(parts[2].split()[:3])
                if (1 <= len(head) <= 18 and 1 <= len(parts[1]) <= 18 and
                        (len(tail) <= 18 or parts[2].startswith(("그리고", "및")))):
                    found.append((sp, sp[0], sp[1], "ko"))
        else:
            for m in EN_TRIPLE.finditer(seg):
                body = m.group(0)
                items = re.split(r",\s*(?:and |or )?|\s+(?:and|or)\s+", body)
                if re.search(r"\d", body) or all(i.strip()[:1].isupper() for i in items):
                    continue
                found.append((sp, sp[0] + m.start(), sp[0] + m.end(), "en"))
    if not found:
        return []
    per_para = {}
    pstarts = [x[0] for x in paras]
    for item in found:
        i = bisect.bisect_right(pstarts, item[1]) - 1
        if i >= 0 and item[1] < paras[i][1]:
            per_para.setdefault(i, []).append(item)
    chosen: List[Tuple[Span, int, int, str]] = []
    if len(found) >= 3:
        chosen = found[1:]
    else:
        for items in per_para.values():
            if len(items) >= 2:
                chosen.extend(items[1:])
    return [_mk(f"{lang}.structure.triple", "structure", "B", s, e, 0.5, genre,
                "3항 나열이 반복된다." if lang == "ko" else "Repeated lists of three.",
                gmap={"academic": 0.7}, text=text[s:e][:60], lang=lang,
                sugg="뜻이 요구하는 개수만 남긴다.") for _, s, e, lang in chosen]


def _core(s: str) -> str:
    return re.sub(r"[^가-힣]+$", "", s)


def rhythm(text: str, masked: str, sents: Sequence[Span], genre: str) -> List[Finding]:
    out: List[Finding] = []
    ko = [sp for sp in sents if re.search(r"[가-힣]", masked[sp[0]:sp[1]])]
    if len(ko) >= 4:
        ends = [_core(masked[a:b])[-2:] for a, b in ko]
        i = 0
        while i < len(ends):
            j = i
            while j + 1 < len(ends) and ends[j + 1] == ends[i] and ends[i]:
                j += 1
            if j - i + 1 >= 4:
                out.append(_mk("ko.rhythm.same-ending", "rhythm", "C", ko[j][0], ko[j][1], 0.8, genre,
                               f"같은 어미('{ends[i]}')가 {j - i + 1}문장 연속된다.", lang="ko",
                               text=masked[ko[j][0]:ko[j][1]][:40], sugg="종결 형태와 문장 구조를 바꾼다."))
            i = j + 1
    if len(ko) >= 6:
        handa = sum(1 for a, b in ko if _core(masked[a:b]).endswith("한다"))
        if handa / len(ko) >= 0.8:
            out.append(_mk("ko.rhythm.handa", "rhythm", "B", ko[0][0], ko[0][0], 0.6, genre,
                           f"'~한다'로 끝나는 문장이 {handa}/{len(ko)}이다.", lang="ko",
                           sugg="'~이다', '~였다', '~되었다' 등으로 다양하게. 억지로 바꾸지는 않는다."))
    if len(ko) >= 5:
        commas = sum(masked[a:b].count(",") + masked[a:b].count("，") for a, b in ko)
        if commas / len(ko) >= 2.2:
            out.append(_mk("ko.rhythm.commas", "rhythm", "B", ko[0][0], ko[0][0], 0.6, genre,
                           f"문장당 쉼표가 {commas / len(ko):.1f}개이다.", lang="ko",
                           sugg="숨을 고를 자리에만 쉼표를 둔다."))
        can = sum(1 for a, b in ko if re.search(r"수\s*(?:있|없)", masked[a:b]))
        if can >= 4 and can / len(ko) >= 0.3:
            out.append(_mk("ko.rhythm.can-do", "rhythm", "C", ko[0][0], ko[0][0], 0.5, genre,
                           f"'수 있다' 문장이 {can}/{len(ko)}이다.", lang="ko", gmap={"academic": 0.6},
                           sugg="단정할 수 있는 사실은 단정한다."))
    en = [sp for sp in sents if not re.search(r"[가-힣]", masked[sp[0]:sp[1]])]
    first = [re.match(r"\W*(\w+)", masked[a:b]) for a, b in en]
    firsts = [m.group(1).lower() if m else "" for m in first]
    i = 0
    while i < len(firsts):
        j = i
        while j + 1 < len(firsts) and firsts[j + 1] == firsts[i] and firsts[i]:
            j += 1
        if j - i + 1 >= 3:
            out.append(_mk("en.rhythm.same-start", "rhythm", "C", en[j][0], en[j][1], 0.5, genre,
                           f"{j - i + 1} sentences in a row start with '{firsts[i]}'.", lang="en",
                           text=masked[en[j][0]:en[j][1]][:40], sugg="Merge sentences or change the subject."))
        i = j + 1
    return out


def emotion(masked: str, paras: Sequence[Span], genre: str) -> List[Finding]:
    """한 문단에 감정을 직접 서술하는 말이 둘 이상이면 둘째부터 센다(universal/ko-core.md 3.7)."""
    out: List[Finding] = []
    for ps, pe in paras:
        seg = masked[ps:pe]
        hits = sorted((m.start() + ps, m.end() + ps, w) for w in EMOTION for m in re.finditer(re.escape(w), seg))
        merged: List[Tuple[int, int, str]] = []
        for h in hits:
            if merged and h[0] < merged[-1][1]:
                continue
            merged.append(h)
        for s, e, w in merged[1:]:
            out.append(_mk("ko.emotion.told", "emotion", "C", s, e, None, genre,
                           "한 문단에서 감정을 이름 붙여 서술하는 말이 겹친다.", lang="ko", text=w,
                           gmap={"literary": 1.4, "academic": 0.4},
                           sugg="행동, 사물, 말로 드러내거나 하나만 남긴다."))
    return out


def intensifiers(text: str, masked: str, units: int, genre: str) -> List[Finding]:
    """겹친 강조어. 100단위당 밀도가 높고 4개 이상일 때, 앞의 둘을 빼고 센다."""
    out: List[Finding] = []
    for lang, rx in (("ko", KO_INTENS), ("en", EN_INTENS)):
        hits = list(rx.finditer(masked))
        if len(hits) < 4 or len(hits) * 100 / max(units, 60) < (2.0 if lang == "ko" else 1.5):
            continue
        for m in hits[2:]:
            word = m.group(0).strip().lower()
            edit = None
            if lang == "ko" or word in EN_INTENS_DROP:
                edit = _delete_edit(f"{lang}.hedging.intensifier", m.start(), m.end(), "strong", False, text)
            out.append(_mk(f"{lang}.hedging.intensifier", "hedging", "C", m.start(), m.end(), 0.3, genre,
                           "겹친 강조어." if lang == "ko" else "Stacked intensifiers.", lang=lang,
                           text=m.group(0).strip(), edit=edit, sugg="수치나 사실로 바꾸거나 지운다."))
    return out


def layout(masked: str, units: int, genre: str) -> List[Finding]:
    out: List[Finding] = []
    bold = len(re.findall(r"\*\*[^*\n]{1,80}\*\*", masked))
    if bold >= 5 and bold * 100 / max(units, 60) > 2.5:
        out.append(_mk("any.format.bold-density", "format", "C", 0, 0, 0.4, genre,
                       f"굵은 글씨가 100단위당 {bold * 100 / max(units, 60):.1f}개이다."))
    heads = len(re.findall(r"^#{1,6}[ \t]+\S", masked, re.M))
    if heads >= 4 and units / heads < 60:
        out.append(_mk("any.format.heading-density", "format", "C", 0, 0, 0.4, genre,
                       f"제목이 {heads}개로 문단보다 많다.", sugg="짧은 글에는 제목을 줄인다."))
    return out


SUMMARY_EN = re.compile(r"(?:In (?:conclusion|summary|short|essence)|To (?:sum up|summarize|summarise|conclude|wrap up)|"
                        r"Overall|All in all|Ultimately|At the end of the day|In the end|The bottom line|"
                        r"Taken together)\b,?", re.I)
SUMMARY_KO = re.compile(r"(?:결론적으로|요약하자면|요약하면|정리하자면|정리하면|종합하면|이처럼|이렇듯|이상으로|결국)(?![가-힣])[,，]?")


def summary_closers(masked: str, sents: Sequence[Span], paras: Sequence[Span], genre: str) -> List[Finding]:
    """문단의 마지막 문장이 '결론적으로', 'Ultimately' 같은 맺음 표지로 열리면 센다."""
    out: List[Finding] = []
    for inside in _by_para(sents, paras):
        if len(inside) < 2:
            continue
        sp = inside[-1]
        m = SUMMARY_KO.match(masked, sp[0]) or SUMMARY_EN.match(masked, sp[0])
        if m:
            lang = "ko" if SUMMARY_KO.match(masked, sp[0]) else "en"
            out.append(_mk(f"{lang}.structure.summary-closer", "structure", "B", sp[0], m.end(), 0.6, genre,
                           "문단의 마지막 문장이 앞 내용을 되풀이하는 맺음 표지로 열린다." if lang == "ko"
                           else "Last sentence of the paragraph opens with a summarising marker.",
                           gmap={"academic": 0.5}, text=m.group(0), lang=lang,
                           sugg="앞 문장과 같은 말이면 지운다."))
    return out


def run_all(text: str, masked: str, sents: Sequence[Span], paras: Sequence[Span], units: int,
            genre: str) -> List[Finding]:
    out: List[Finding] = []
    out += dashes(masked, sents, units, genre)
    out += transitions(text, masked, sents, paras, genre, {})
    out += triples(text, masked, sents, paras, genre)
    out += rhythm(text, masked, sents, genre)
    out += emotion(masked, paras, genre)
    out += intensifiers(text, masked, units, genre)
    out += layout(masked, units, genre)
    out += summary_closers(masked, sents, paras, genre)
    return out
