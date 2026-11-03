# 에이전트 정의

| 파일 | 대상 | 설치 및 사용 안내 |
|---|---|---|
| `claude/ai-smell-polisher.md` | Claude Code 서브에이전트 | `python3 install.py` 실행 시 `.claude/agents/`(또는 `~/.claude/agents/`)에 복사됩니다. 설치 후 Claude Code를 재시작하거나 `/agents` 명령으로 불러옵니다 |
| `codex/AGENTS.snippet.md` | Codex CLI 등 `AGENTS.md`를 읽는 도구 | `python3 install.py --scope project --append-instructions` 실행 시 프로젝트의 `AGENTS.md` 끝에 덧붙입니다 (이미 있으면 변경하지 않습니다) |
| `gemini/GEMINI.snippet.md` | Gemini CLI | 동일한 옵션을 통해 `GEMINI.md` 끝에 덧붙입니다 |

스킬 자체(`skills/ai-smell-polish/`)가 주요 CLI 도구의 공통 설치 대상입니다. 위의 정의 파일들은 스킬을 적재적소에 연계하기 위한 안내 설정입니다. 터미널 환경이 없는 웹 채팅 인터페이스에서는 `skills/ai-smell-polish/references/chat-prompts.md`의 프롬프트를 활용하시면 됩니다.

에이전트 정의의 단일 원본은 본 폴더입니다. 설치 스크립트는 작업 시 이 폴더를 스킬 폴더 내부(`agents/`)로도 복사하여, 설치된 스킬 단독으로도 재설치가 가능하도록 구성합니다.
