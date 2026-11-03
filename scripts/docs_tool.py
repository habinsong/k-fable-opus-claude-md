#!/usr/bin/env python3
"""LLM 컨텍스트용 지침(universal/, md/)과 사람이 읽는 조사 기록(docs/)을 관리한다.

사용법:
  python3 -I scripts/docs_tool.py sync              # 공통 블록을 universal/·md/ 문서에 주입
  python3 -I scripts/docs_tool.py check             # 구조·분리 검사 (누락은 경고)
  python3 -I scripts/docs_tool.py check --complete  # 모델 폴더마다 분야 문서와 docs 짝을 필수로 검사
  python3 -I scripts/docs_tool.py check --skip-blocks  # 주입 전 초안: 블록 일치 비교 생략

루트 폴더:
  universal/                      모델에 상관없이 쓰는 범용 지침. 분야 문서 12개 + contract.md + ko-core.md
  md/<계열>/<모델>/<분야>.md      모델별 지침. 범용 지침 + 모델 전용 지침(§2)
  docs/<계열>/<모델>/             조사·검증·근거 기록. 컨텍스트에 넣지 않는다.
      README.md                  이 모델의 조사 기록 색인
      overview · performance · operations · critique .md   md의 general.md 짝(주제별로 나눔)
      sources.md                 출처와 한계
      domains/<분야>.md           md의 나머지 분야 8개의 짝
      korean-writing.md          한국어 윤문 3분야(ko-*)의 모델별 조사 기록
  universal/·md/ 문서에는 근거·출처·가격·벤치마크·비판을 두지 않는다. docs/에 둔다.

원본(정본)의 위치:
  계약            universal/contract.md          → 모든 범용·모델별 문서의 <!-- BEGIN:contract --> 블록
  한국어 공통 원리 universal/ko-core.md           → universal/ko-*.md 의 <!-- BEGIN:ko-core --> 블록
  분야 규칙       universal/<분야>.md            → md/<계열>/<모델>/<분야>.md 의 <!-- BEGIN:domain --> 블록
  모델 전용 지침  md/<계열>/<모델>/general.md 의 <!-- BEGIN:model --> 블록 → 같은 모델의 다른 분야 문서
                 (한국어 분야는 md/<계열>/<모델>/ko-academic.md 의 블록 → ko-everyday, ko-literary)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNIV = ROOT / "universal"
MD = ROOT / "md"
DOCS = ROOT / "docs"
FAMILIES = ["gpt", "claude", "gemini", "deepseek", "glm", "muse", "grok", "kimi", "qwen", "gemma", "minimax"]
DOMAINS = ["general", "web", "app", "native", "hardware", "firmware",
           "web-research", "research", "tech-research"]
KO_DOMAINS = ["ko-academic", "ko-everyday", "ko-literary"]
KO_FAMILIES = ["gpt", "claude", "gemini", "gemma"]
ALL_DOMAINS = DOMAINS + KO_DOMAINS
KO_DOC = "korean-writing"
MODEL_DOC_NAMES = {"README", "overview", "performance", "operations", "critique", "sources", "xcheck", KO_DOC}
MODEL_SOURCE = {"base": "general", "ko": "ko-academic"}
CONTRACT_KEYWORDS = ["복명복창", "변경 요약", "수정 파일", "실행한 명령", "검증 결과",
                     "남은 리스크", "God-object", "500줄", "한국어", "비판", "재귀",
                     "라이선스", "저작권", "특허", "출처", "[확인]", "[미확인]",
                     "웹 검색", "웹 페이지 가져오기"]
# 사용자가 요구한 항목이 한국어 공통 원리에서 빠지면 검사가 실패한다.
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


def block_of(text, name):
    m = block_re(name).search(text)
    return m.group(2).strip("\n") if m else None


def strip_blocks(text, names):
    for n in names:
        text = block_re(n).sub("", text)
    return text


def from_marker(text, marker):
    i = text.find(marker)
    return text[i:].strip("\n") if i >= 0 else ""


def contract_text():
    return from_marker(read(UNIV / "contract.md"), "## 0.")


def ko_core_text():
    t = read(UNIV / "ko-core.md")
    m = re.search(r"^### ", t, re.M)
    return t[m.start():].strip("\n") if m else ""


def domain_part(d):
    """범용 문서에서 계약 블록 뒤의 분야 규칙 본문. ko-core 표식은 걷어 낸다."""
    part = from_marker(read(UNIV / f"{d}.md"), "## 3. 분야 규칙")
    return re.sub(r"<!-- (?:BEGIN|END):ko-core -->\n?", "", part).strip("\n")


def md_files():
    for fam in FAMILIES:
        for p in sorted((MD / fam).glob("*/*.md")):
            yield p


def parts(p):
    return p.parent.parent.name, p.parent.name, p.stem


def model_source_path(fam, model, domain):
    kind = "ko" if domain in KO_DOMAINS else "base"
    return MD / fam / model / f"{MODEL_SOURCE[kind]}.md"


def model_text(fam, model, domain):
    p = model_source_path(fam, model, domain)
    return block_of(read(p), "model") if p.exists() else None


def research_hits(text, skip_tags=False):
    hits = []
    for rx, label in RESEARCH_MARKERS:
        if skip_tags and label == "근거 수준 태그":
            continue
        m = rx.search(text)
        if m:
            hits.append(f"{label} '{m.group(0)[:30]}'")
    return hits


def inject(text, name, body):
    rx = block_re(name)
    if not rx.search(text):
        return None
    return rx.sub(lambda m: m.group(1) + body + "\n" + m.group(3), text, count=1)


def sync():
    contract = contract_text()
    ko_core = ko_core_text() if (UNIV / "ko-core.md").exists() else ""
    changed = 0
    for d in ALL_DOMAINS:
        p = UNIV / f"{d}.md"
        if not p.exists():
            continue
        text = read(p)
        new = inject(text, "contract", contract)
        if new is None:
            print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:contract 마커 없음")
            return 1
        if d in KO_DOMAINS:
            new = inject(new, "ko-core", ko_core)
            if new is None:
                print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:ko-core 마커 없음")
                return 1
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    for p in md_files():
        fam, model, dom = parts(p)
        if dom not in ALL_DOMAINS or not (UNIV / f"{dom}.md").exists():
            print(f"SKIP  {p.relative_to(ROOT)} (범용 지침 없음: {dom})")
            continue
        mtext = model_text(fam, model, dom)
        if not mtext:
            print(f"ERROR {p.relative_to(ROOT)}: 모델 지침 원본 블록이 비어 있음 ({model_source_path(fam, model, dom).relative_to(ROOT)})")
            return 1
        text = read(p)
        new = text
        for name, body in (("contract", contract), ("model", mtext), ("domain", domain_part(dom))):
            new = inject(new, name, body)
            if new is None:
                print(f"ERROR {p.relative_to(ROOT)}: BEGIN/END:{name} 마커 없음")
                return 1
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"sync 완료: {changed}개 파일 갱신")
    return 0


def check_universal(errors, skip_blocks):
    for need in ["contract.md", "ko-core.md"] + [f"{d}.md" for d in ALL_DOMAINS]:
        if not (UNIV / need).exists():
            errors.append(f"universal/{need} 없음")
    if (UNIV / "contract.md").exists():
        contract = contract_text()
        for kw in CONTRACT_KEYWORDS:
            if kw not in contract:
                errors.append(f"universal/contract.md: 필수 키워드 누락 '{kw}'")
        for hit in research_hits(contract, skip_tags=True):
            errors.append(f"universal/contract.md: 리서치 표지 {hit}")
    else:
        contract = ""
    if (UNIV / "ko-core.md").exists():
        core = read(UNIV / "ko-core.md")
        for kw in KO_CORE_KEYWORDS:
            if kw not in core:
                errors.append(f"universal/ko-core.md: 필수 키워드 누락 '{kw}'")
        for hit in research_hits(core):
            errors.append(f"universal/ko-core.md: 컨텍스트 지침에 리서치 표지 {hit}")
        ko_core = ko_core_text()
    else:
        ko_core = ""
    for f in sorted(UNIV.glob("*.md")):
        n = len(read(f).splitlines())
        if n > HARD_LIMIT:
            errors.append(f"universal/{f.name}: {n}줄 > {HARD_LIMIT}")
    for d in ALL_DOMAINS:
        p = UNIV / f"{d}.md"
        if not p.exists():
            continue
        rel = f"universal/{d}.md"
        text = read(p)
        if "## 3. 분야 규칙" not in text:
            errors.append(f"{rel}: '## 3. 분야 규칙' 절 없음")
        if not text.startswith("# "):
            errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
        checks = [("contract", contract)] + ([("ko-core", ko_core)] if d in KO_DOMAINS else [])
        for name, body in checks:
            got = block_of(text, name)
            if got is None:
                errors.append(f"{rel}: {name} 블록 마커 없음")
            elif not skip_blocks and got != body:
                errors.append(f"{rel}: {name} 블록이 원본과 다름 (sync 필요)")
        for hit in research_hits(strip_blocks(text, ["contract"])):
            errors.append(f"{rel}: 컨텍스트 지침에 리서치 표지 {hit}")
    return contract


def check_md(errors, warns, contract, skip_blocks):
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
        src = model_source_path(fam, model, dom)
        if mtext is None:
            errors.append(f"{rel}: 모델 지침 원본 파일 없음 ({src.relative_to(ROOT)})")
        elif not mtext.startswith("## 2. "):
            errors.append(f"{src.relative_to(ROOT)}: 모델 지침 블록이 '## 2. '로 시작해야 함")
        domain = domain_part(dom) if (UNIV / f"{dom}.md").exists() else ""
        for name, body in (("contract", contract), ("model", mtext), ("domain", domain)):
            got = block_of(text, name)
            if got is None:
                errors.append(f"{rel}: {name} 블록 마커 없음")
            elif not skip_blocks and body is not None and got != body:
                errors.append(f"{rel}: {name} 블록이 원본과 다름 (sync 필요)")
        for hit in research_hits(strip_blocks(text, ["contract"])):
            errors.append(f"{rel}: 컨텍스트 문서에 리서치 표지 {hit} — docs/로 옮긴다")
        own = strip_blocks(text, ["contract", "model", "domain"])
        for bad in ("TODO", "TBD", "[PROJECT_NAME]"):
            if bad in own:
                errors.append(f"{rel}: 자리표시자 '{bad}' 남아 있음")
    return count


FACT_HEAD = "시점에 민감한 사실"
FACT_HEDGE = "확정된 사실이 아니라"
FACT_LEVELS = {"확인", "부분", "미확인", "추정"}


def fact_rows(text):
    """'시점에 민감한 사실' 절의 표 행을 {항목: 셀 목록}으로 돌려준다. 표가 없으면 빈 dict."""
    if FACT_HEAD not in text:
        return {}
    body = text.split(FACT_HEAD, 1)[1].split("\n### ", 1)[0]
    rows = {}
    for line in body.splitlines():
        if line.startswith("| ") and not line.startswith("| 항목"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows[cells[0]] = cells
    return rows


def check_fact_tables(errors):
    """universal의 사실 표와 docs/_common/domain-rules의 근거 수준 표가 행 단위로 같은지 본다."""
    for d in DOMAINS:
        up = UNIV / f"{d}.md"
        if not up.exists():
            continue
        utext = read(up)
        urows = fact_rows(utext)
        if not urows:
            continue
        rel = f"universal/{d}.md"
        if FACT_HEDGE not in utext:
            errors.append(f"{rel}: 사실 표 위에 '확정된 사실이 아니라 확인의 출발점'이라는 명령문이 없음")
        dp = DOCS / "_common" / "domain-rules" / f"{d}.md"
        if not dp.exists():
            errors.append(f"docs/_common/domain-rules/{d}.md 없음 ({rel}에 사실 표가 있음)")
            continue
        drows = {}  # docs 표는 절 제목이 없어 표 행을 직접 읽는다
        for line in read(dp).splitlines():
            if line.startswith("| ") and not line.startswith("| 항목"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                drows[cells[0]] = cells
        for item, cells in urows.items():
            got = drows.get(item)
            if got is None:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'의 근거 수준 행 없음")
            elif len(got) < 3 or got[2] != cells[1]:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'의 내용이 {rel}와 다름")
            elif got[1] not in FACT_LEVELS:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'의 근거 수준 '{got[1]}'이 허용값이 아님")
        for item in drows:
            if item not in urows:
                errors.append(f"docs/_common/domain-rules/{d}.md: 항목 '{item}'이 {rel}에 없음")


def check_docs(errors, warns, complete):
    if not (DOCS / "README.md").exists():
        errors.append("docs/README.md 없음")
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
        mdir = DOCS / fam / model
        want = ["README.md", "sources.md"] if "general" in have else []
        want += [f"domains/{d}.md" for d in have if d in DOMAINS and d != "general"]
        want += ["korean-writing.md"] if have & set(KO_DOMAINS) else []
        for rel_name in want:
            if not (mdir / rel_name).exists():
                (errors if complete else warns).append(f"docs/{fam}/{model}/{rel_name} 없음 (md의 조사 기록 짝)")
    for fam in FAMILIES:
        for mdir in sorted(p for p in (DOCS / fam).glob("*") if p.is_dir()):
            for dp in sorted([*mdir.glob("*.md"), *(mdir / "domains").glob("*.md")]):
                rel = str(dp.relative_to(ROOT))
                in_domains = dp.parent.name == "domains"
                text = read(dp)
                if not text.startswith("# "):
                    errors.append(f"{rel}: 첫 줄이 H1 제목이 아님")
                if in_domains and (dp.stem not in DOMAINS or dp.stem == "general"):
                    warns.append(f"{rel}: 짝이 되는 md 분야 이름이 아님")
                if not in_domains and dp.stem not in MODEL_DOC_NAMES:
                    warns.append(f"{rel}: 알려진 조사 기록 이름이 아님 ({', '.join(sorted(MODEL_DOC_NAMES))})")
                if (in_domains or dp.stem in ("sources", KO_DOC)) and "http" not in text:
                    errors.append(f"{rel}: 조사 기록에 출처 URL 없음")
                if len(text.splitlines()) > HARD_LIMIT:
                    errors.append(f"{rel}: {len(text.splitlines())}줄 > {HARD_LIMIT}")


def check(complete, skip_blocks=False):
    errors, warns = [], []
    for fam in FAMILIES:
        if (ROOT / fam).exists():
            errors.append(f"{fam}/: 옛 위치다. md/{fam}/ 와 docs/{fam}/ 로 나눈다")
    if (ROOT / "_shared").exists():
        errors.append("_shared/: 없앤 폴더다. 범용 지침은 universal/, 모델 지침은 md/에 둔다")
    contract = check_universal(errors, skip_blocks)
    count = check_md(errors, warns, contract_text() if (UNIV / "contract.md").exists() else contract, skip_blocks)
    check_docs(errors, warns, complete)
    check_fact_tables(errors)
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
