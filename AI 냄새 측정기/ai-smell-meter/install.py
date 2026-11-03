#!/usr/bin/env python3
"""AI 냄새 측정기 설치 스크립트. 에이전트가 이 파일 하나로 점검, 설치, 시험, 시연까지 끝낸다.

  python3 install.py                      # 점검 + 설치(사용자 범위, 감지된 AI 도구) + 시험 + 시연
  python3 install.py --scope project      # 현재 프로젝트 폴더에만 설치
  python3 install.py --agents claude,agents --dry-run
  python3 install.py --doctor | --selftest | --demo | --uninstall

그 밖의 인자는 `ai-smell install`에 그대로 넘어간다(`ai-smell install --help`).
"""
import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(HERE, "skills", "ai-smell-polish", "scripts"))

from ai_smell.cli import main  # noqa: E402
from ai_smell.samples import AI_STRONG  # noqa: E402


def demo() -> int:
    print("\n== 시연: 한국어 AI풍 표본 ==")
    main(["analyze", "--text", AI_STRONG["ko"], "--top", "5"])
    print("\n== 교정문 (standard) ==")
    return main(["polish", "--text", AI_STRONG["ko"], "--text-only"])


def run(argv):
    flags = {"--doctor": lambda: main(["doctor"]), "--selftest": lambda: main(["selftest"]), "--demo": demo}
    if len(argv) == 1 and argv[0] in flags:
        return flags[argv[0]]()
    if argv in ([], ["--all"]):
        steps = [("점검", lambda: main(["doctor"])), ("설치", lambda: main(["install"])),
                 ("시험", lambda: main(["selftest"])), ("시연", demo)]
        rc = 0
        for name, fn in steps:
            print(f"\n=== {name} ===")
            code = fn()
            rc = rc or code
            if code and name in ("점검", "설치", "시험"):
                print(f"{name} 단계가 실패해 중단합니다.")
                return code
        return rc
    return main(["install", *argv])


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
