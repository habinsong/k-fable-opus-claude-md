---
name: ai-smell-polish
description: "한국어·영어 글에서 AI 냄새(챗봇 잔재, 의미 부풀리기, 부정 대구, 번역투, 군더더기)를 측정하고 교정된 글을 출력하는 윤문 스킬. 'AI 티 빼 줘', '윤문해 줘', '자연스럽게 다듬어 줘', 'AI 냄새 측정', 'de-slop this', 'humanize this text', 'remove AI-sounding phrases' 같은 요청에 쓴다. 측정과 기계적 교정은 python3 표준 라이브러리만 쓰는 엔진이 하고, 구조적 문제의 재작성은 에이전트가 하며, 고친 뒤에는 사실 보존과 변경률을 다시 검증한다. 탐지기를 속이거나 저자를 숨기는 용도로는 쓰지 않는다."
license: MIT
compatibility: "Python 3.9 이상, 표준 라이브러리만 필요. 셸을 실행할 수 있는 에이전트(Claude Code, Codex CLI, Gemini CLI 등)에서 동작한다. 셸이 없으면 references/chat-prompts.md의 프롬프트를 쓴다."
---

# AI 냄새 측정 · 윤문

글의 **문체 신호**를 세고(지수 0~100), **교정된 글**을 출력한다. 지수는 'AI가 썼을 확률'이 아니다. 사람이 쓴 글도 높게, AI가 쓴 글도 낮게 나올 수 있으므로 저자 판정에 쓰지 않는다.

## 역할 분담

| 단계 | 누가 | 하는 일 |
|---|---|---|
| 측정 | 엔진 | 챗봇 잔재, 의미 부풀리기, 부정 대구, 번역투 등 신호를 세고 지수를 낸다 |
| 기계적 교정 | 엔진 | 잔재와 군더더기 삭제, 장황한 구절 단순화, 이중 피동 등 뜻이 안 바뀌는 것만 고친다 |
| 구조적 재작성 | **에이전트(당신)** | 엔진이 못 고치는 대구, 부풀린 서술, 3항 나열을 playbook대로 최소 수정한다 |
| 대조 검증 | 엔진 | 숫자·주소·코드·인용·고유명사 보존, 변경률, 새로 생긴 신호를 확인한다 |

## 실행 파일 찾기

이 SKILL.md가 있는 폴더의 `scripts/ai-smell`이다(아래 `S`). 없으면 저장소의 `AI 냄새 측정기/ai-smell-meter/skills/ai-smell-polish/scripts/ai-smell`을 쓴다. Windows에서는 `python3` 대신 `py -3` 또는 `python`을 쓴다.

```bash
S="<이 폴더>/scripts/ai-smell"
python3 "$S" selftest        # 처음 한 번. 26개 모두 통과해야 한다
```

## 작업 순서

1. **입력을 파일로 만든다.** 사용자가 글을 붙여 넣었으면 따옴표가 깨지지 않게 인용된 heredoc으로 임시 파일에 쓴다(`cat > /tmp/draft.md <<'EOF'`). 파일이면 그대로 쓴다. 원본은 고치지 않는다.
2. **측정한다.** `python3 "$S" analyze /tmp/draft.md` (장르는 `--genre academic|everyday|literary`). 지수와 상위 신호를 사용자에게 짧게 보인다.
3. **기계적 교정.** `python3 "$S" polish /tmp/draft.md > /tmp/draft.polished.md` 교정문은 표준 출력, 요약은 표준 오류다. 단계는 `--tier safe|standard|strong`이다. 기본 standard로 시작하고, strong은 뜻이 조금 달라질 수 있으니 사용자에게 알린다.
4. **남은 신호를 고친다.** `python3 "$S" prompt /tmp/draft.md --target claude|gpt|gemini|generic`이 만든 지시를 읽고, 걸린 곳만 국소 수정한다. 규칙은 `references/ko-playbook.md`, `references/en-playbook.md`다. 새 사실을 지어내지 않는다. 구체적 내용이 없으면 사용자에게 묻는다.
5. **대조 검증.** `python3 "$S" verify /tmp/draft.md /tmp/draft.final.md` 가 FAIL이면 숫자·주소·코드·인용이 바뀐 것이니 되돌린다. CONFIRM(변경률 50% 초과)이면 멈추고 사용자에게 알린다. 새 신호가 생겼으면 그 부분을 다시 고친다.
6. **재측정하고 반복한다.** 최대 3회. 같은 신호가 두 번 고쳐도 남으면 접근을 바꾸거나 사용자에게 묻는다.
7. **보고한다.** 교정문을 **먼저, 그대로** 보인다. 이어서 3~5줄로 지수 변화, 바꾼 것, 남긴 것과 이유, 사용자가 채워야 할 구체적 정보를 쓴다.

## 정직 규칙

- "사람이 쓴 것 같다", "탐지되지 않는다"고 단정하지 않는다. 말할 수 있는 것은 "측정된 신호가 N에서 M으로 줄었다"까지다.
- 외부 AI 탐지기 점수를 맞추려고 고치지 않는다. 오타·속어·무작위성을 넣어 사람처럼 보이게 하지 않는다.
- 학교·학술지·회사가 AI 사용 표기나 금지를 요구하면 그 규정이 먼저다. 저자를 속이거나 규정을 피하는 것이 목적이면 돕지 않고 이유를 말한다.
- 필자의 말버릇과 문체는 오류가 아니다. 이미 자연스러운 글은 건드리지 않는다.
- 표본이 40단위보다 짧으면 지수가 불안정하다고 알린다.

## 도구를 실행할 수 없을 때

셸이 없는 채팅 환경이면 `references/chat-prompts.md`의 프롬프트(한국어·영어)를 붙여 넣어 같은 규칙으로 고친다. 이때는 지수 계산과 대조 검증이 없으므로 보고에 "측정 없음"이라고 쓴다.

## 참조

- `references/ko-playbook.md`: 한국어 윤문 규칙 (학술·일상·문학)
- `references/en-playbook.md`: 영어 윤문 규칙
- `references/workflow.md`: 반복 루프, 중단 조건, 명령 모음
- `references/chat-prompts.md`: 셸 없이 쓰는 프롬프트
- `references/limits.md`: 한계와 근거 수준
- 규칙 전체: `python3 "$S" rules --ui ko`
