# AI 냄새 측정기: 에이전트용 안내

사용자가 "이거 설치하고 테스트해", "이 폴더 써 봐", "AI 티 빼 줘", "윤문해 줘"라고 하면 아래대로 **되묻지 않고** 스스로 한다. 이 파일을 읽은 에이전트가 설치, 시험, 사용, 보고까지 끝내는 것이 목표다.

## A. 설치하고 시험하라는 요청

이 폴더(`AI 냄새 측정기/ai-smell-meter/`)에서 실행한다. 경로에 한글과 공백이 있으니 따옴표로 감싼다. Windows는 `python3` 대신 `py -3`을 쓴다.

```bash
cd "AI 냄새 측정기/ai-smell-meter"
python3 install.py            # 점검, 설치, 시험, 시연을 차례로 한다
```

`install.py`가 하는 일: (1) `doctor`로 Python 3.9+와 내장 시험 확인, (2) 감지된 AI 도구 폴더(`~/.claude`, `~/.gemini`, `~/.codex`)와 공통 `~/.agents`에 스킬 설치, Claude Code에는 서브에이전트도 설치, (3) 설치본마다 `selftest` 실행, (4) 한국어 표본으로 측정과 교정문 시연.

| 상황 | 할 일 |
|---|---|
| 홈 디렉터리를 건드리면 안 되거나 쓰기 권한이 없다 | `python3 install.py --scope project` (현재 프로젝트의 `.agents`, `.claude` 아래에만 설치) |
| 특정 도구만 | `python3 install.py --agents claude,agents` |
| 무엇이 설치될지 먼저 보기 | `python3 install.py --dry-run` |
| 프로젝트의 `AGENTS.md`, `GEMINI.md`에도 사용 안내를 넣기 | `python3 install.py --scope project --append-instructions` |
| 제거 | `python3 install.py --uninstall` |
| 설치 없이 시험만 | `python3 skills/ai-smell-polish/scripts/ai-smell selftest` |
| Python이 없거나 3.9 미만 | 설치하지 말고 사용자에게 알린다. 셸이 없으면 `skills/ai-smell-polish/references/chat-prompts.md`의 프롬프트를 쓴다 |
| selftest 실패 | 출력 그대로 사용자에게 보여 주고 멈춘다. 고치려고 규칙 파일을 임의로 수정하지 않는다 |

설치 뒤 **사용자에게 보고할 것** (한국어 존댓말, 아래 순서):

1. 설치된 경로 목록과 각각의 selftest 결과(`26/26`)
2. 시연의 점수 변화(전 → 후)와 교정문 한 단락
3. 새로 시작해야 스킬 목록에 보인다는 점(도구가 설치 시점에 목록을 읽는 경우)
4. 한계 한 줄: 문체 특징를 줄이는 도구이며 저자 판정기도 탐지 회피 도구도 아니다

## B. 글을 윤문하라는 요청

설치되어 있으면 `ai-smell-polish` 스킬의 `SKILL.md`를 따른다. 설치되어 있지 않으면 A를 먼저 한다. 흐름은 다음과 같다.

```
analyze(측정) -> polish(교정문 출력) -> 남은 검토 항목는 prompt가 만든 지시대로 직접 수정 -> verify(대조) -> 재측정
```

- 입력이 붙여 넣은 글이면 임시 파일에 쓴다(인용된 heredoc). 원본 파일은 사용자가 `--in-place`를 요청하지 않는 한 고치지 않는다.
- **교정문을 먼저, 그대로** 보여 준다. 그다음 점수 변화, 바꾼 것, 남긴 것, 사용자가 채워야 할 구체적 정보를 쓴다.
- `verify`가 FAIL이면 되돌리고, CONFIRM이면 멈추고 묻는다.

## C. 하지 않는 일

- "사람이 쓴 것 같다", "AI 탐지기를 통과한다"고 단정하지 않는다. 외부 탐지기 점수에 맞춰 고치지 않는다.
- 사실, 숫자, 인용, 고유명사를 지어내지 않는다. 구체적 내용이 없으면 사용자에게 묻는다.
- 학교·학술지·회사의 AI 사용 규정을 피하려는 목적이면 돕지 않고 이유를 말한다.
- 사용자가 요청하지 않으면 커밋, 푸시, 외부 전송을 하지 않는다.

## D. 구조

```
ai-smell-meter/
  install.py                      설치 + 시험 + 시연 (이 파일 하나로 끝)
  bin/ai-smell                    저장소에서 바로 쓰는 진입점
  skills/ai-smell-polish/         스킬 폴더 = 엔진 + SKILL.md + references (설치할 때 통째로 복사)
    scripts/ai-smell              실행 파일
    scripts/ai_smell/             엔진 패키지 (표준 라이브러리만)
  agents/                         Claude 서브에이전트 정의, Codex·Gemini용 안내
  docs/                           설계, 근거, 한계, 규칙 목록
  tests/                          단위 시험
```

자세한 설명은 `README.md`, `docs/design.md`, `docs/limits.md`를 본다.
