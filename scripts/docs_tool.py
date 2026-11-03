#!/usr/bin/env python3
"""모델별 지침 문서의 공통 블록 주입(sync)과 구조 검사(check).

사용법:
  python3 -I scripts/docs_tool.py sync            # 공통 블록을 정본에서 각 문서로 주입
  python3 -I scripts/docs_tool.py check           # 구조 검사 (누락 분야 문서는 경고)
  python3 -I scripts/docs_tool.py check --complete  # 모델 폴더마다 분야 문서 9개 필수

문서 위치: <계열>/<모델>/<분야>.md   정본: _shared/contract.md, _shared/domains/<분야>.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAMILIES = ["gpt", "claude", "gemini", "deepseek", "glm", "muse", "grok", "kimi", "qwen", "gemma", "minimax"]
DOMAINS = ["general", "web", "app", "native", "hardware", "firmware",
           "web-research", "research", "tech-research"]
CONTRACT_KEYWORDS = ["복명복창", "변경 요약", "수정 파일", "실행한 명령", "검증 결과",
                     "남은 리스크", "God-object", "500줄", "한국어", "비판", "재귀",
                     "라이선스", "저작권", "특허", "출처", "[확인]", "[미확인]"]
HARD_LIMIT = 500
SOFT_LIMIT = 260


def block_re(name):
    return re.compile(
        rf"(<!-- BEGIN:{name} -->\n)(.*?)(<!-- END:{name} -->)", re.S)


def canonical():
    contract = (ROOT / "_shared" / "contract.md").read_text(encoding="utf-8").strip("\n")
    domains = {}
    for d in DOMAINS:
        p = ROOT / "_shared" / "domains" / f"{d}.md"
        if p.exists():
            domains[d] = p.read_text(encoding="utf-8").strip("\n")
    return contract, domains


def docs():
    for fam in FAMILIES:
        for p in sorted((ROOT / fam).glob("*/*.md")):
            yield p


def sync():
    contract, domains = canonical()
    changed = 0
    for p in docs():
        dom = p.stem
        if dom not in domains:
            print(f"SKIP  {p.relative_to(ROOT)} (정본 없음: {dom})")
            continue
        text = p.read_text(encoding="utf-8")
        new = text
        for name, body in (("contract", contract), ("domain", domains[dom])):
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


def check(complete):
    errors, warns = [], []
    contract_path = ROOT / "_shared" / "contract.md"
    if not contract_path.exists():
        print("ERROR _shared/contract.md 없음")
        return 1
    contract, domains = canonical()
    for kw in CONTRACT_KEYWORDS:
        if kw not in contract:
            errors.append(f"_shared/contract.md: 필수 키워드 누락 '{kw}'")
    for d in DOMAINS:
        if d not in domains:
            errors.append(f"_shared/domains/{d}.md 없음")
        elif not domains[d].startswith("## 3. 분야 규칙"):
            errors.append(f"_shared/domains/{d}.md: '## 3. 분야 규칙'으로 시작해야 함")
    for f in [contract_path, *(ROOT / "_shared" / "domains").glob("*.md")]:
        n = len(f.read_text(encoding="utf-8").splitlines())
        if n > HARD_LIMIT:
            errors.append(f"{f.relative_to(ROOT)}: {n}줄 > {HARD_LIMIT}")

    count = 0
    for p in docs():
        count += 1
        rel = str(p.relative_to(ROOT))
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        if p.stem not in DOMAINS:
            errors.append(f"{rel}: 허용되지 않은 분야 이름 '{p.stem}'")
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
        for name, body in (("contract", contract), ("domain", domains.get(p.stem, ""))):
            m = block_re(name).search(text)
            if not m:
                errors.append(f"{rel}: {name} 블록 마커 없음")
            elif m.group(2).strip("\n") != body:
                errors.append(f"{rel}: {name} 블록이 정본과 다름 (sync 필요)")
        outside = block_re("contract").sub("", block_re("domain").sub("", text))
        for h in ("## 2. ", "## 4. 근거와 한계"):
            if h not in outside:
                errors.append(f"{rel}: '{h.strip()}' 섹션 없음")
        tail = outside.split("## 4. 근거와 한계")[-1] if "## 4. 근거와 한계" in outside else ""
        if "http" not in tail:
            errors.append(f"{rel}: '근거와 한계'에 출처 URL 없음")
        for bad in ("TODO", "TBD", "[PROJECT_NAME]"):
            if bad in outside:
                errors.append(f"{rel}: 자리표시자 '{bad}' 남아 있음")

    models = {p.parent for p in docs()}
    for m in sorted(models):
        have = {f.stem for f in m.glob("*.md")}
        miss = [d for d in DOMAINS if d not in have]
        if miss:
            msg = f"{m.relative_to(ROOT)}: 분야 문서 {len(miss)}개 누락 ({', '.join(miss)})"
            (errors if complete else warns).append(msg)

    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"check: 문서 {count}개, 모델 폴더 {len(models)}개, 경고 {len(warns)}, 오류 {len(errors)}")
    return 1 if errors else 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "sync":
        return sync()
    if len(argv) >= 2 and argv[1] == "check":
        return check("--complete" in argv)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
