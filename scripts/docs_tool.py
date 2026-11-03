#!/usr/bin/env python3
"""LLM 컨텍스트용 지침(md/)과 사람이 읽는 조사 기록(docs/)을 관리한다.

사용법:
  python3 -I scripts/docs_tool.py sync              # 계약·모델·분야 블록을 md/ 문서에 주입
  python3 -I scripts/docs_tool.py check             # 구조·분리 검사 (누락은 경고)
  python3 -I scripts/docs_tool.py check --complete  # 모델 폴더마다 분야 문서와 docs 짝을 필수로 검사
  python3 -I scripts/docs_tool.py check --skip-blocks  # 주입 전 초안: 블록 일치 비교 생략

구조:
  md/<계열>/<모델>/<분야>.md      컨텍스트에 넣는 지침. 근거·출처·가격·벤치마크·비판을 두지 않는다.
  docs/<계열>/<모델>/<분야>.md    조사·검증·근거 기록. 컨텍스트에 넣지 않는다.
  docs/<계열>/<모델>/korean-writing.md   한국어 윤문 3분야(ko-*)의 모델별 조사 기록
  _shared/                       md 문서의 원본(계약, 분야 규칙, 모델 지침). 컨텍스트에 직접 넣지 않는다.
한국어 윤문 분야(ko-*)는 KO_FAMILIES 계열에만 있다. 분야 원본의 <!-- INCLUDE:ko-core -->는
_shared/ko-core.md 내용으로 펼쳐서 주입한다.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "md"
DOCS = ROOT / "docs"
SHARED = ROOT / "_shared"
FAMILIES = ["gpt", "claude", "gemini", "deepseek", "glm", "muse", "grok", "kimi", "qwen", "gemma", "minimax"]
DOMAINS = ["general", "web", "app", "native", "hardware", "firmware",
           "web-research", "research", "tech-research"]
KO_DOMAINS = ["ko-academic", "ko-everyday", "ko-literary"]
KO_FAMILIES = ["gpt", "claude", "gemini", "gemma"]
ALL_DOMAINS = DOMAINS + KO_DOMAINS
KO_DOC = "korean-writing"
INCLUDE_KO_CORE = "<!-- INCLUDE:ko-core -->"
CONTRACT_KEYWORDS = ["복명복창", "변경 요약", "수정 파일", "실행한 명령", "검증 결과",
                     "남은 리스크", "God-object", "500줄", "한국어", "비판", "재귀",
                     "라이선스", "저작권", "특허", "출처", "[확인]", "[미확인]",
                     "웹 검색", "웹 페이지 가져오기"]
# 사용자가 요구한 항목이 한국어 공통 지침에서 빠지면 검사가 실패한다.
KO_CORE_KEYWORDS = ["흐름", "호흡", "과서술", "대구", "도치", "감정", "번역투",
                    "윤문 순환", "측정", "라이선스"]
# 컨텍스트로 들어가는 글에 있으면 안 되는 리서치 표지. 계약의 근거 수준 정의(§1.3)만 예외다.
RESEARCH_MARKERS = [
    (re.compile(r"https?://"), "출처 URL"),
    (re.compile(r"\[(?:확인|부분|미확인|추정|권고)[^\]]*\]"), "근거 수준 태그"),
    (re.compile(r"근거와 한계|근거 표기"), "근거 절"),
    (re.compile(r"\$\s?\d"), "가격"),
    (re.compile(r"Artificial Analysis|SWE-bench|Terminal-Bench|LMArena|EQ-Bench|KatFishNet"), "벤치마크·연구 출처"),
]
HARD_LIMIT = 500
SOFT_LIMIT = 220


def block_re(name):
    return re.compile(rf"(<!-- BEGIN:{name} -->\n)(.*?)(<!-- END:{name} -->)", re.S)


def read(p):
    return p.read_text(encoding="utf-8")


def canonical():
    contract = read(SHARED / "contract.md").strip("\n")
    core_path = SHARED / "ko-core.md"
    core = read(core_path).strip("\n") if core_path.exists() else ""
    domains = {}
    for d in ALL_DOMAINS:
        p = SHARED / "domains" / f"{d}.md"
        if p.exists():
            domains[d] = read(p).strip("\n").replace(INCLUDE_KO_CORE, core)
    return contract, domains


def model_source(fam, model, domain):
    suffix = ".ko.md" if domain in KO_DOMAINS else ".md"
    return SHARED / "models" / fam / f"{model}{suffix}"


def model_text(fam, model, domain):
    p = model_source(fam, model, domain)
    return read(p).strip("\n") if p.exists() else None


def md_files():
    for fam in FAMILIES:
        for p in sorted((MD / fam).glob("*/*.md")):
            yield p


def parts(p):
    return p.parent.parent.name, p.parent.name, p.stem


def research_hits(text, skip_tags=False):
    hits = []
    for rx, label in RESEARCH_MARKERS:
        if skip_tags and label == "근거 수준 태그":
            continue
        m = rx.search(text)
        if m:
            hits.append(f"{label} '{m.group(0)[:30]}'")
    return hits


def sync():
    contract, domains = canonical()
    changed = 0
    for p in md_files():
        fam, model, dom = parts(p)
        if dom not in domains:
            print(f"SKIP  {p.relative_to(ROOT)} (분야 원본 없음: {dom})")
            continue
        mtext = model_text(fam, model, dom)
        if mtext is None:
            print(f"ERROR {p.relative_to(ROOT)}: 모델 지침 원본 없음 ({model_source(fam, model, dom).relative_to(ROOT)})")
            return 1
        text = read(p)
        new = text
        for name, body in (("contract", contract), ("model", mtext), ("domain", domains[dom])):
            rx = block_re(name)
            if not rx.search(new):
                print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:{name} 마커 없음")
                return 1
            new = rx.sub(lambda m: m.group(1) + body + "\n" + m.group(3), new, count=1)
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"sync 완료: {changed}개 파일 갱신")
    return 0


def check_shared(errors, contract, domains):
    contract_path = SHARED / "contract.md"
    for kw in CONTRACT_KEYWORDS:
        if kw not in contract:
            errors.append(f"_shared/contract.md: 필수 키워드 누락 '{kw}'")
    for hit in research_hits(contract, skip_tags=True):
        errors.append(f"_shared/contract.md: 리서치 표지 {hit}")
    for d in ALL_DOMAINS:
        rel = f"_shared/domains/{d}.md"
        if d not in domains:
            errors.append(f"{rel} 없음")
            continue
        if not domains[d].startswith("## 3. 분야 규칙"):
            errors.append(f"{rel}: '## 3. 분야 규칙'으로 시작해야 함")
        if INCLUDE_KO_CORE in domains[d]:
            errors.append(f"{rel}: ko-core 포함 마커가 펼쳐지지 않음")
        for hit in research_hits(domains[d]):
            errors.append(f"{rel}: 컨텍스트 지침에 리서치 표지 {hit}")
    core_path = SHARED / "ko-core.md"
    if not core_path.exists():
        errors.append("_shared/ko-core.md 없음")
    else:
        core = read(core_path)
        for kw in KO_CORE_KEYWORDS:
            if kw not in core:
                errors.append(f"_shared/ko-core.md: 필수 키워드 누락 '{kw}'")
    extra = [core_path] if core_path.exists() else []
    for f in [contract_path, *extra, *(SHARED / "domains").glob("*.md"), *(SHARED / "models").glob("*/*.md")]:
        n = len(read(f).splitlines())
        if n > HARD_LIMIT:
            errors.append(f"{f.relative_to(ROOT)}: {n}줄 > {HARD_LIMIT}")


def check_md(errors, warns, contract, domains, skip_blocks):
    count = 0
    for p in md_files():
        count += 1
        fam, model, dom = parts(p)
        rel = str(p.relative_to(ROOT))
        text = read(p)
        lines = text.splitlines()
        if dom not in ALL_DOMAINS:
            errors.append(f"{rel}: 허용되지 않은 분야 이름 '{dom}'")
            continue
        if dom in KO_DOMAINS and fam not in KO_FAMILIES:
            errors.append(f"{rel}: 한국어 윤문 분야는 {', '.join(KO_FAMILIES)} 계열에만 둔다")
            continue
        if len(lines) > HARD_LIMIT:
            errors.append(f"{rel}: {len(lines)}줄 > {HARD_LIMIT}")
        elif len(lines) > SOFT_LIMIT:
            warns.append(f"{rel}: {len(lines)}줄 (권장 {SOFT_LIMIT} 이하)")
        if not lines or not lines[0].startswith("# "):
            errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
        head = "\n".join(lines[:4])
        if "기준일" not in head or "모델 ID" not in head:
            errors.append(f"{rel}: 상단 메타 줄에 '모델 ID'와 '기준일' 필요")
        mtext = model_text(fam, model, dom)
        if mtext is None:
            errors.append(f"{rel}: 모델 지침 원본 없음 ({model_source(fam, model, dom).relative_to(ROOT)})")
        elif not mtext.startswith("## 2. "):
            errors.append(f"{model_source(fam, model, dom).relative_to(ROOT)}: '## 2. '로 시작해야 함")
        want = {"contract": contract, "model": mtext, "domain": domains.get(dom, "")}
        for name, body in want.items():
            m = block_re(name).search(text)
            if not m:
                errors.append(f"{rel}: {name} 블록 마커 없음")
            elif not skip_blocks and body is not None and m.group(2).strip("\n") != body:
                errors.append(f"{rel}: {name} 블록이 원본과 다름 (sync 필요)")
        outside_contract = block_re("contract").sub("", text)
        for hit in research_hits(outside_contract):
            errors.append(f"{rel}: 컨텍스트 문서에 리서치 표지 {hit} — docs/로 옮긴다")
        own = text
        for name in ("contract", "model", "domain"):
            own = block_re(name).sub("", own)  # 공통 블록 안의 지침 문장(예: TODO를 남기지 않는다)은 제외
        for bad in ("TODO", "TBD", "[PROJECT_NAME]"):
            if bad in own:
                errors.append(f"{rel}: 자리표시자 '{bad}' 남아 있음")
    return count


def check_docs(errors, warns, complete):
    if not (DOCS / "README.md").exists():
        errors.append("docs/README.md 없음")
    for d in DOMAINS:
        if not (DOCS / "_common" / "domain-rules" / f"{d}.md").exists():
            errors.append(f"docs/_common/domain-rules/{d}.md 없음")
    models = {}
    for p in md_files():
        fam, model, dom = parts(p)
        models.setdefault((fam, model), set()).add(dom)
    for (fam, model), have in sorted(models.items()):
        need = DOMAINS + (KO_DOMAINS if fam in KO_FAMILIES else [])
        miss = [d for d in need if d not in have]
        if miss:
            msg = f"md/{fam}/{model}: 분야 문서 {len(miss)}개 누락 ({', '.join(miss)})"
            (errors if complete else warns).append(msg)
        pairs = [d for d in have if d in DOMAINS] + ([KO_DOC] if have & set(KO_DOMAINS) else [])
        for name in pairs:
            dp = DOCS / fam / model / f"{name}.md"
            if not dp.exists():
                (errors if complete else warns).append(f"docs/{fam}/{model}/{name}.md 없음 (md의 조사 기록 짝)")
    allowed = set(DOMAINS) | {KO_DOC}
    for fam in FAMILIES:
        for dp in sorted((DOCS / fam).glob("*/*.md")):
            rel = str(dp.relative_to(ROOT))
            text = read(dp)
            if not text.startswith("# "):
                errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
            if dp.stem not in allowed:
                warns.append(f"{rel}: 짝이 되는 md 분야 이름이 아님")
            if "http" not in text:
                errors.append(f"{rel}: 조사 기록에 출처 URL 없음")
            if len(text.splitlines()) > HARD_LIMIT:
                errors.append(f"{rel}: {len(text.splitlines())}줄 > {HARD_LIMIT}")


def check(complete, skip_blocks=False):
    errors, warns = [], []
    if not (SHARED / "contract.md").exists():
        print("ERROR _shared/contract.md 없음")
        return 1
    for fam in FAMILIES:
        if (ROOT / fam).exists():
            errors.append(f"{fam}/: 옛 위치다. md/{fam}/ 와 docs/{fam}/ 로 나눈다")
    contract, domains = canonical()
    check_shared(errors, contract, domains)
    count = check_md(errors, warns, contract, domains, skip_blocks)
    check_docs(errors, warns, complete)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    models = {p.parent for p in md_files()}
    print(f"check: md 문서 {count}개, 모델 폴더 {len(models)}개, 경고 {len(warns)}, 오류 {len(errors)}")
    return 1 if errors else 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "sync":
        return sync()
    if len(argv) >= 2 and argv[1] == "check":
        return check("--complete" in argv, "--skip-blocks" in argv)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
