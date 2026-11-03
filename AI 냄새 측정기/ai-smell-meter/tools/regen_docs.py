#!/usr/bin/env python3
"""생성 문서(docs/rules.md, references/chat-prompts.md)를 다시 만든다.

규칙이나 프롬프트를 고친 뒤 실행한다: python3 tools/regen_docs.py
tests/test_docs.py가 두 파일이 최신인지 확인한다.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LAUNCHER = os.path.join(ROOT, "skills", "ai-smell-polish", "scripts", "ai-smell")
CHAT = os.path.join(ROOT, "skills", "ai-smell-polish", "references", "chat-prompts.md")
RULES = os.path.join(ROOT, "docs", "rules.md")

HEAD = """# 셸 없이 쓰는 프롬프트

> `python3 bin/ai-smell prompt --chat ko|en`이 만든 것이다. 직접 고치지 말고 `ai_smell/prompt.py`를 고친 뒤 `python3 tools/regen_docs.py`로 다시 만든다.
> 웹 채팅(ChatGPT, Claude, Gemini 등)에 그대로 붙여 넣고 마지막 `{{...}}` 자리에 글을 넣는다.
> 이 방식에는 **점수 계산과 대조 검증이 없다.** 모델이 검토 항목을 목록으로 뽑고 고칠 뿐이므로, 보고할 때 "측정 없음"이라고 쓴다.
> 숫자·주소·고유명사는 고친 글과 원문을 눈으로 대조한다.
"""


def run(*args):
    return subprocess.run([sys.executable, "-I", LAUNCHER, *args], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


def main():
    ko = run("prompt", "--chat", "ko").rstrip("\n")
    en = run("prompt", "--chat", "en").rstrip("\n")
    with open(CHAT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"{HEAD}\n## 한국어\n\n````text\n{ko}\n````\n\n## English\n\n````text\n{en}\n````\n")
    with open(RULES, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(run("rules", "--format", "md"))
    print("갱신:", os.path.relpath(CHAT, ROOT), os.path.relpath(RULES, ROOT))


if __name__ == "__main__":
    main()
