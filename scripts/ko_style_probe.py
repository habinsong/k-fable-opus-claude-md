#!/usr/bin/env python3
"""한국어 글의 문체 신호를 센다. 윤문 전후 비교용 휴리스틱이며 AI 탐지기가 아니다.

사용법:
  python3 -I scripts/ko_style_probe.py 파일.txt           # 표로 출력
  python3 -I scripts/ko_style_probe.py 파일.txt --json    # JSON 출력
  python3 -I scripts/ko_style_probe.py -                  # 표준 입력

한계: 정규식 기반이라 오탐·미탐이 있다. 수치가 낮아도 사람이 쓴 글이 되지는 않는다.
참고값은 im-not-ai 저자의 자체 보고(사람 60편 대 AI 60편, 편집된 전문 산문)이며
장르·분량에 따라 달라진다. 근거 수준과 한계는 docs/_common/korean-writing/empirical-validation.md를 본다.
"""
import json
import re
import statistics
import sys
from pathlib import Path

MAX_BYTES = 2_000_000
FENCE = re.compile(r"```.*?```", re.S)
MD_PREFIX = re.compile(r"^\s*(?:#{1,6}\s+|[-*+]\s+|\d+[.)]\s+|>\s?)", re.M)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
SENT_SPLIT = re.compile(r"(?<=[.!?…。])[\"'”’)\]]*\s+|\n+")
CONNECTORS = ("또한", "따라서", "즉", "나아가", "게다가")
EMOTION = ("기뻤", "슬펐", "행복했", "외로웠", "두려웠", "불안했", "벅차", "벅찼", "먹먹", "울컥",
           "뭉클", "철렁", "쿵", "눈물이 흘렀", "숨이 멎", "가슴이 아렸", "가슴이 미어", "감동", "설렜",
           "서글펐", "그리웠", "뿌듯", "애틋", "저릿", "찡했", "눈시울", "가슴이 뛰", "심장이 뛰",
           "숨이 막", "온몸이 떨", "마음이 무거웠", "슬퍼졌", "외로워졌", "행복해졌")
# (이름, 정규식, 설명). 설명은 출력에 그대로 붙는다.
STRONG = [
    ("부정 대구 후보", re.compile(r"(?<!뿐만 )(?<!뿐 )(?<!다름 )아니라|[이가]\s*아니다[.!]"),
     "사람 0.6 / AI 5.8 (1천자당, 자체 실측)"),
    ("당위 서술", re.compile(r"(?:해야|되어야|돼야|하여야)\s*(?:한다|합니다|하며|함)|필요가\s*(?:있다|있습니다)"),
     "AI가 사람의 3.7배(자체 실측)"),
    ("'~적' 표현", re.compile(r"[가-힣]적(?:인)?\s"), "'~적 N' 체인이 1.6배(자체 실측)"),
]
WEAK = [
    ("'를 통해' 류", re.compile(r"[을를]\s*통(?:해서?|하여)"), "사람이 더 많이 썼다. 금지 근거로 쓰지 않는다"),
    ("'것이다' 류", re.compile(r"것(?:이다|입니다)(?![가-힣])"), "사람이 약 2배 더 썼다. 금지 근거로 쓰지 않는다"),
]
TRANSLATIONESE = [
    ("에 대해/대한", re.compile(r"에\s*대(?:해서?|한)")),
    ("에 있어(서)", re.compile(r"에\s*있어(?:서)?")),
    ("에 의해/의한", re.compile(r"에\s*의(?:해서?|한)")),
    ("이중 피동", re.compile(r"되어진|보여진|불려진|쓰여진|잊혀지|생각되어")),
    ("가지고 있", re.compile(r"가지고\s*있")),
    ("할 수 있/없", re.compile(r"할\s*수\s*(?:있|없)")),
]
INVERSION = [
    ("분열문 후보('~것은')", re.compile(r"[가-힣]+\s*것은\s")),
    ("강조 도입('핵심은' 등)", re.compile(r"(?:핵심은|관건은|문제는|중요한\s*점은|결론은)\s")),
    ("서술어 뒤 후치('했다, 조용히.')", re.compile(r"(?:다|요|어|야|지)\s*,\s*[가-힣]{1,5}[.!?]\s*$", re.M)),
]


def clean(text):
    return MD_PREFIX.sub("", FENCE.sub(" ", text)).replace("**", "").replace("__", "")


def sentences(text):
    parts = [s.strip() for s in SENT_SPLIT.split(text)]
    return [s for s in parts if len(s) >= 2 and re.search(r"[가-힣]", s)]


def core(s):
    return re.sub(r"[^가-힣]+$", "", s)


def register(s):
    c = core(s)
    if re.search(r"(?<!아)(?:니다|니까)$", c):  # '아니다'는 합쇼체가 아니다
        return "합쇼체"
    if c.endswith("요"):
        return "해요체"
    if c.endswith("다"):
        return "평서(한다체)"
    if re.search(r"(?:어|아|야|지|네|까|냐|래|게|자|마|라|거든|잖아|군)$", c):
        return "반말"
    return "기타"


def per_k(n, chars):
    return round(n * 1000 / chars, 2) if chars else 0.0


def longest_run(items):
    best = run = 1 if items else 0
    for a, b in zip(items, items[1:]):
        run = run + 1 if a == b else 1
        best = max(best, run)
    return best


def longest_true_run(flags):
    best = run = 0
    for f in flags:
        run = run + 1 if f else 0
        best = max(best, run)
    return best


def triple_lists(sents):
    """쉼표로 짧은 세 덩어리가 이어지는 문장(3항 나열 후보)의 수."""
    n = 0
    for s in sents:
        parts = [x.strip() for x in re.split(r"[,，]", s.rstrip(".!?… "))]
        if len(parts) != 3 or not all(1 <= len(x) <= 18 for x in parts[:2]):
            continue
        # 마지막 덩어리는 '그리고/및'으로 열리면 길어도 3항 나열로 본다
        if len(parts[2]) <= 18 or parts[2].startswith(("그리고", "및")):
            n += 1
    return n


def measure(raw):
    text = clean(raw)
    chars = len(re.sub(r"\s", "", text))
    sents = sentences(text)
    n = len(sents)
    lens = [len(s) for s in sents]
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    out = {"글자수(공백 제외)": chars, "문장수": n, "문단수": len(paras)}
    commas = text.count(",") + text.count("，")
    out["문장 길이"] = {
        "평균": round(statistics.mean(lens), 1) if lens else 0,
        "표준편차": round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0,
        "100자 이상 문장(1천자당)": per_k(sum(1 for x in lens if x >= 100), chars),
        "참고": "편집된 사람 글 91.3 / AI 8.1 (1천자당, 자체 실측, 편집 효과 가능)",
    }
    out["쉼표"] = {
        "문장당 쉼표": round(commas / n, 2) if n else 0,
        "쉼표 포함 문장 비율(%)": round(100 * sum(1 for s in sents if "," in s or "，" in s) / n, 1) if n else 0,
        "참고": "수필 기준 문장당 사람 1.13 / AI 2.56. 보고서·블로그는 기준 없음",
    }
    ends = [core(s)[-2:] for s in sents]
    out["종결"] = {
        "같은 어미 최대 연속": longest_run(ends),
        "'~한다' 종결 비율(%)": round(100 * sum(1 for s in sents if core(s).endswith("한다")) / n, 1) if n else 0,
        "참고": "같은 어미 4문장 연속은 점검. '~한다' 편중은 AI가 1.8배(자체 실측)",
    }
    out["근거 있는 신호(1천자당)"] = {
        name: {"횟수": len(rx.findall(text)), "1천자당": per_k(len(rx.findall(text)), chars), "참고": note}
        for name, rx, note in STRONG}
    out["연속 부정 뒤 결론 후보"] = {
        "'~아니다' 문장 연속 최대": longest_true_run([core(s).endswith("아니다") for s in sents])}
    out["참고용(근거 약함, 고치는 근거로 쓰지 않음)"] = {
        name: {"횟수": len(rx.findall(text)), "참고": note} for name, rx, note in WEAK}
    starts = [sum(1 for s in re.split(SENT_SPLIT, p) if s.strip().startswith(CONNECTORS)) for p in paras]
    out["참고용(근거 약함, 고치는 근거로 쓰지 않음)"]["문두 접속사 문단 최대"] = max(starts, default=0)
    out["번역투 후보(어색한 곳에만 고침)"] = {name: len(rx.findall(text)) for name, rx in TRANSLATIONESE}
    out["대구·도치 후보(사용자 관찰, 공개 근거 [미확인])"] = {
        name: len(rx.findall(text)) for name, rx in INVERSION}
    out["대구·도치 후보(사용자 관찰, 공개 근거 [미확인])"]["3항 나열 후보(짧은 쉼표 세 덩어리)"] = triple_lists(sents)
    emo = sum(text.count(w) for w in EMOTION)
    out["감정 직접 서술 후보(AI 특유 근거 없음)"] = {"횟수": emo, "1천자당": per_k(emo, chars)}
    regs = [register(s) for s in sents]
    mixed = sum(1 for p in paras if {register(s) for s in sentences(p)} & {"합쇼체", "해요체"}
                and {register(s) for s in sentences(p)} & {"평서(한다체)", "반말"})
    out["말투"] = {k: regs.count(k) for k in sorted(set(regs))}
    out["말투"]["존대와 평어가 섞인 문단"] = mixed
    out["서식 신호"] = {
        "이모지": len(EMOJI.findall(raw)), "줄표(—–―)": len(re.findall(r"[—–―]", raw)),
        "굵은 글씨 쌍": raw.count("**") // 2, "제목 줄": len(re.findall(r"^\s*#{1,6}\s", raw, re.M)),
        "불릿/번호 줄": len(re.findall(r"^\s*(?:[-*+]|\d+[.)])\s", raw, re.M)),
        "곡선 따옴표": len(re.findall(r"[“”‘’]", raw)), "물결표(~)": raw.count("~"),
    }
    return out


def render(d, indent=0):
    pad = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{pad}[{k}]" if indent == 0 else f"{pad}{k}")
            render(v, indent + 1)
        else:
            print(f"{pad}{k}: {v}")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1 or any(a not in ("--json",) for a in argv[1:] if a.startswith("--")):
        print(__doc__)
        return 2
    try:
        if args[0] == "-":
            raw = sys.stdin.read(MAX_BYTES)
        else:
            p = Path(args[0])
            if p.stat().st_size > MAX_BYTES:
                print(f"오류: 파일이 {MAX_BYTES}바이트를 넘는다")
                return 1
            raw = p.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"오류: {e}")
        return 1
    result = measure(raw)
    if "--json" in argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        render(result)
        print("\n이 수치는 판정이 아니다. 신호가 한 단락에 겹칠 때만 고치고, 자연스러움은 사람이 읽어 판단한다.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
