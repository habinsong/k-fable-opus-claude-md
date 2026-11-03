# 에이전트 정의

| 파일 | 대상 | 쓰는 법 |
|---|---|---|
| `claude/ai-smell-polisher.md` | Claude Code 서브에이전트 | `python3 install.py`가 `.claude/agents/`(또는 `~/.claude/agents/`)에 복사한다. 설치 뒤 Claude Code를 다시 시작하거나 `/agents`로 불러온다 |
| `codex/AGENTS.snippet.md` | Codex CLI 등 `AGENTS.md`를 읽는 도구 | `python3 install.py --scope project --append-instructions`가 프로젝트의 `AGENTS.md` 끝에 덧붙인다(이미 있으면 건드리지 않는다) |
| `gemini/GEMINI.snippet.md` | Gemini CLI | 같은 옵션이 `GEMINI.md` 끝에 덧붙인다 |

스킬 자체(`skills/ai-smell-polish/`)가 세 도구의 공통 설치 대상이다. 위 정의는 스킬을 더 잘 찾아 쓰게 하는 얇은 안내다. 셸이 없는 웹 채팅에는 `skills/ai-smell-polish/references/chat-prompts.md`를 붙여 넣는다.

에이전트 정의의 단일 원본은 이 폴더다. 설치기는 설치할 때 이 폴더를 스킬 폴더 안(`agents/`)에도 복사해, 설치된 스킬만으로 다시 설치할 수 있게 한다.
