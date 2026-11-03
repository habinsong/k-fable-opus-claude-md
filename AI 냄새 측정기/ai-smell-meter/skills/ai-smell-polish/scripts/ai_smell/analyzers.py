"""정규식 한 줄로 잡히지 않고 '밀도'와 '연속'으로 판단하는 신호들.

각 함수는 Finding 목록을 돌려준다. 줄·열은 detect가 채운다. 문서 전체에 대한 신호는
길이 0인 구간(start == end)으로 두어 다른 신호와 겹쳐 가려지지 않게 한다.
"""
from __future__ import annotations

import bisect
import math
import re
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
_T_BAN = r"(?!(?:so|but|while|because|although|if|when|that|which|where|as|since|though|with|without|from|into|to|for|after|before)\b)"
_T_WORD = r"(?:[\w'’/-]+(?:[&/][\w'’/-]+)?)"
_T_ITEM = rf"(?:{_T_BAN}{_T_WORD}(?:\s+{_T_WORD}){{0,2}})"
TRAILING_PREP = re.compile(r"\s+(?:in|on|at|to|for|with|from|by|about|instead|across|through|before|after|without|into)\b.*$", re.I)
EN_TRIPLE = re.compile(rf"\b(?P<first>{_T_ITEM}),\s+(?P<second>{_T_ITEM}),?\s+(?:and|or)\s+(?P<third>{_T_ITEM})\b", re.I)
EN_INTENS = re.compile(r"\b(?:very|really|truly|genuinely|incredibly|extremely|highly|deeply|profoundly|"
                       r"absolutely|undoubtedly|remarkably|exceptionally|tremendously)\b[ \t]?", re.I)
EN_INTENS_DROP = {"truly", "genuinely", "incredibly", "extremely", "remarkably", "exceptionally",
                  "tremendously", "profoundly", "undoubtedly"}
KO_INTENS = re.compile(r"(?<![가-힣])(?:매우|정말|굉장히|상당히|아주|너무|엄청|대단히|극도로|무척)(?![가-힣])[ \t]?")
EMOTION = ("기뻤", "슬펐", "행복했", "외로웠", "두려웠", "불안했", "벅차", "벅찼", "먹먹", "울컥", "뭉클", "철렁", "눈물이 흘렀",
           "숨이 멎", "가슴이 아렸", "가슴이 미어", "감동", "설렜", "서글펐", "그리웠", "뿌듯", "애틋", "저릿", "찡했", "눈시울",
           "가슴이 뛰", "심장이 뛰", "숨이 막", "온몸이 떨", "마음이 무거웠", "슬퍼졌", "외로워졌", "행복해졌")
DASH = re.compile(r"[—―]|(?<=\S)\s*--\s*(?=\S)|(?<=[A-Za-z가-힣])\s*[–]\s*(?=[A-Za-z가-힣])|(?<=[A-Za-z가-힣])\s+-\s+(?=[A-Za-z가-힣])")


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
    """줄표(em dash) 남발을 센다. 한국어는 1개부터 번역투, 영어는 3개 이상부터 과다로 본다."""
    hits = list(DASH.finditer(masked))
    is_ko = bool(re.search(r"[가-힣]", masked))
    if len(hits) < (1 if is_ko else 3):
        return []
    out: List[Finding] = []
    per_sentence = {}
    starts = [x[0] for x in sents]
    for m in hits:
        per_sentence.setdefault(_sentence_of(sents, starts, m.start()), []).append(m)
    for sp, ms in per_sentence.items():
        for i, m in enumerate(ms):
            s, e = m.start(), m.end()
            while s > 0 and masked[s - 1] in " \t": s -= 1
            while e < len(masked) and masked[e] in " \t": e += 1
            nxt = masked[e:e + 1]
            edit = None
            rid = "ko.trans.em-dash" if is_ko else "any.format.em-dash"
            cat = "translationese" if is_ko else "format"
            if len(ms) == 2 and sp is not None:
                inner = masked[ms[0].end():ms[1].start()]
                if 2 <= len(inner.strip()) <= 80 and not re.search(r"[.!?\n]", inner):
                    edit = Edit(s, e, ", ", rid, "standard", before=masked[s:e])
            elif is_ko and s > 0 and masked[s - 1].isalnum():
                edit = Edit(s, e, ", ", rid, "standard", before=masked[s:e])
            elif len(ms) == 1 and nxt.islower() and s > 0 and masked[s - 1].isalnum():
                edit = Edit(s, e, ", ", rid, "strong", before=masked[s:e])
            note = ("한국어 산문에서 줄표(—)는 번역투이자 어색한 삽입구 흉내이다." if is_ko else "줄표(em dash)가 여러 번 쓰였다.")
            out.append(_mk(rid, cat, "A" if is_ko else "B", m.start(), m.end(), 0.8 if is_ko else 0.4, genre,
                           note, text=m.group(0).strip(), lang="ko" if is_ko else "any",
                           sugg="쉼표, 마침표, 괄호로 바꾼다.", edit=edit))
    if len(hits) >= 3:
        out.append(_mk("any.structure.em-dash-overuse", "structure", "A", 0, 0, 0.8, genre,
                       f"줄표(em dash)가 글 전체에 과다하게 남발된다 (총 {len(hits)}건)." if is_ko else
                       f"Em dashes are excessively used across the text ({len(hits)} occurrences).",
                       lang="any", sugg="줄표를 쉼표, 괄호, 또는 마침표로 나누어 정리한다."))
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
    """A, B, 그리고 C 꼴의 3항 나열. 문서에 2번 이상이거나 한 문단에 2번 이상일 때 센다."""
    found: List[Tuple[Span, int, int, str]] = []
    for sp in sents:
        seg = masked[sp[0]:sp[1]]
        if "\x00" in seg or seg.lstrip().startswith("|") or " | " in seg:
            continue
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
                first, second, third = m.group("first").strip(), m.group("second").strip(), m.group("third").strip()
                third_clean = TRAILING_PREP.sub("", third).strip()
                items = [first, second, third_clean]
                if all(re.match(r"^\d+$", i.strip()) for i in items) or all(i.strip()[:1].isupper() for i in items):
                    continue
                end_pos = m.start() + len(m.group(0)) - (len(third) - len(third_clean))
                found.append((sp, sp[0] + m.start(), sp[0] + end_pos, "en"))
    if not found or len(found) < 2:
        return []
    per_para = {}
    pstarts = [x[0] for x in paras]
    for item in found:
        i = bisect.bisect_right(pstarts, item[1]) - 1
        if i >= 0 and item[1] < paras[i][1]:
            per_para.setdefault(i, []).append(item)
    chosen: List[Tuple[Span, int, int, str]] = []
    if len(found) >= 4 or len(per_para) >= 3:
        chosen = found
    elif len(found) >= 3:
        chosen = found[1:]
    else:
        for items in per_para.values():
            if len(items) >= 2:
                chosen.extend(items[1:])
    out = [_mk(f"{lang}.structure.triple", "structure", "B", s, e, 0.6, genre,
               "3항 나열이 반복된다." if lang == "ko" else "Repeated lists of three.",
               gmap={"academic": 0.7}, text=text[s:e][:60], lang=lang,
               sugg="뜻이 요구하는 개수만 남긴다.") for _, s, e, lang in chosen]
    if len(found) >= 4 or len(per_para) >= 3:
        is_ko = any(lang == "ko" for _, _, _, lang in found)
        out.append(_mk("any.structure.triple-overuse", "structure", "B", 0, 0, 0.8, genre,
                       f"3항 나열이 글 전체에 걸쳐 과다하게 반복된다 (총 {len(found)}건)." if is_ko
                       else f"Lists of three are excessively repeated across the text ({len(found)} occurrences).",
                       lang="any", sugg="나열 항목을 2개로 줄이거나 서술식 문장으로 풀어 쓴다."))
    return out


def _core(s: str) -> str:
    return re.sub(r"[^가-힣]+$", "", s)


def rhythm(text: str, masked: str, sents: Sequence[Span], genre: str) -> List[Finding]:
    out: List[Finding] = []
    ko = [sp for sp in sents if re.search(r"[가-힣]", masked[sp[0]:sp[1]])]
    if len(ko) >= 4:
        ends = [(_core(masked[a:b])[-3:] if _core(masked[a:b]).endswith("니다") else _core(masked[a:b])[-2:])
                for a, b in ko]
        i = 0
        while i < len(ends):
            j = i
            while j + 1 < len(ends) and ends[j + 1] == ends[i] and ends[i]:
                j += 1
            if j - i + 1 >= (6 if ends[i].endswith("니다") else 4):
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
        if j - i + 1 >= 4:
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


_POLITE = re.compile(r"(?<!아)(?:니다|니까)$")
_PLAIN = re.compile(r"(?:어|아|야|지|네|까|냐|래|게|자|마|라|거든|잖아|군)$")


def _register(sentence: str) -> str:
    core = re.sub(r"[^가-힣]+$", "", sentence)
    if _POLITE.search(core) or core.endswith("요"):
        return "polite"
    if core.endswith("다") or _PLAIN.search(core):
        return "plain"
    return "other"


def register_mix(masked: str, sents: Sequence[Span], paras: Sequence[Span], genre: str) -> List[Finding]:
    """한 문단 안에 존댓말과 평어 종결이 섞이면 센다(universal/ko-everyday.md, ko-academic.md). 따옴표 문장은 뺀다."""
    out: List[Finding] = []
    for inside in _by_para(sents, paras):
        kinds = []
        for sp in inside:
            seg = masked[sp[0]:sp[1]]
            if ("|" in seg or seg.lstrip().startswith(("(", "[", "`", "#")) or
                    re.search(r"[\"\u201c\u300c]", seg) or len(re.findall(r"[가-힣]", seg)) < 6):
                continue
            kinds.append((_register(seg), sp))
        have = {k for k, _ in kinds}
        if {"polite", "plain"} <= have:
            first_other = next(sp for k, sp in kinds if k != kinds[0][0] and k in ("polite", "plain"))
            out.append(_mk("ko.register.mixed", "rhythm", "C", first_other[0], first_other[1], 0.5, genre,
                           "한 문단 안에 존댓말과 평어가 섞였다.", lang="ko", gmap={"literary": 0.3},
                           text=masked[first_other[0]:first_other[1]][:40],
                           sugg="문단의 말투를 하나로 맞춘다. 의도한 섞임이면 그대로 둔다."))
    return out


def exclamations(masked: str, sents: Sequence[Span], genre: str) -> List[Finding]:
    n = masked.count("!") + masked.count("\uff01")
    if n >= 3 and sents and n / len(sents) >= 0.25:
        pos = min(i for i in (masked.find("!"), masked.find("\uff01")) if i >= 0)
        around = next((sp for sp in sents if sp[0] <= pos < sp[1]), (pos, pos + 1))
        return [_mk("any.format.exclaim", "format", "C", pos, pos + 1, 0.4, genre,
                    f"느낌표가 문장 {len(sents)}개에 {n}개이다.", gmap={"everyday": 0.3},
                    text=masked[around[0]:around[1]][:40], sugg="느낌표로 감정을 대신하지 않는다.")]
    return []


def paragraph_cadence(text: str, masked: str, sents: Sequence[Span], paras: Sequence[Span], genre: str) -> List[Finding]:
    """문단마다 문장 수와 길이가 2~6문장으로 거의 일정하여 기계적인 정보 분배를 보이는 경우를 센다."""
    body_paras = [p for p in paras if not masked[p[0]:p[1]].strip().startswith(
        ("#", ">", "|", "```", "<!--", "- ", "* ", "1. ", "2. ", "3. "))]
    if len(body_paras) < 4:
        return []
    p_sents = _by_para(sents, body_paras)
    s_lens = [len(g) for g in p_sents]
    w_lens = [len(masked[ps:pe].split()) for ps, pe in body_paras]
    n = len(body_paras)
    if all(2 <= s <= 6 for s in s_lens) and all(8 <= w <= 120 for w in w_lens):
        mean_s = sum(s_lens) / n
        std_s = math.sqrt(sum((s - mean_s) ** 2 for s in s_lens) / n)
        if std_s <= 1.8:
            is_ko = bool(re.search(r"[가-힣]", text))
            msg = (f"{n}개 문단이 모두 2~6문장으로 분량이 균일하여 기계적 정보 분배를 보인다." if is_ko
                   else f"All {n} paragraphs are uniformly 2-6 sentences long with robotic cadence.")
            sugg = ("한 줄 문단이나 긴 문단을 섞는다." if is_ko
                    else "Vary paragraph lengths to create natural rhythm.")
            return [_mk("any.structure.uniform-cadence", "structure", "B", 0, 0, 0.8, genre,
                        msg, lang="any", sugg=sugg)]
    return []


def run_all(text: str, masked: str, sents: Sequence[Span], paras: Sequence[Span], units: int,
            genre: str) -> List[Finding]:
    return (dashes(masked, sents, units, genre) + transitions(text, masked, sents, paras, genre, {}) +
            triples(text, masked, sents, paras, genre) + rhythm(text, masked, sents, genre) +
            emotion(masked, paras, genre) + intensifiers(text, masked, units, genre) +
            layout(masked, units, genre) + summary_closers(masked, sents, paras, genre) +
            register_mix(masked, sents, paras, genre) + exclamations(masked, sents, genre) +
            paragraph_cadence(text, masked, sents, paras, genre))
