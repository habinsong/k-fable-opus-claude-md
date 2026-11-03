# AI 냄새 측정기 (ai-smell-meter)

한국어와 영어 글에서 **AI 냄새**(챗봇 잔재, 의미 부풀리기, 부정 대구, 번역투, 군더더기)를 재고, **교정된 글을 출력**하는 윤문 도구다. 하나의 코드로 세 가지 모양을 한다.

- **윤문 엔진**: `python3` 표준 라이브러리만 쓰는 명령줄 도구. 네트워크도 API 키도 필요 없다.
- **윤문 스킬**: Agent Skills 규격의 `ai-smell-polish`. Claude Code, Codex CLI, Gemini CLI 같은 에이전트가 읽는다.
- **윤문 에이전트**: Claude Code 서브에이전트 정의와 Codex·Gemini용 안내, 셸 없는 채팅 환경용 프롬프트.

> **이 도구는 AI 탐지기가 아니다.** 지수는 문체 신호의 밀도이고 'AI가 썼을 확률'이 아니다. 사람이 쓴 글이 높게, AI가 쓴 글이 낮게 나올 수 있다. 저자 판정, 평가, 징계에 쓰지 않는다. 탐지기를 속이는 기능은 없다. 한계는 [`docs/limits.md`](docs/limits.md).

## AI 에이전트에게 이렇게 말하면 된다

```text
AI 냄새 측정기/ai-smell-meter 폴더의 AGENTS.md를 읽고, 설치하고, 스스로 시험해서 결과를 알려 줘.
```

```text
(글을 붙여 넣고) 이 글에서 AI 티를 빼서 자연스럽게 윤문해 줘. 고친 글도 보여 줘.
```

에이전트는 [`AGENTS.md`](AGENTS.md)대로 점검, 설치, 시험, 시연까지 되묻지 않고 끝낸다.

## 직접 쓰기

저장소 루트에서 (경로에 한글과 공백이 있으니 따옴표를 쓴다. Windows는 `python3` 대신 `py -3`):

```bash
cd "AI 냄새 측정기/ai-smell-meter"
python3 install.py                                  # 점검 + 설치 + 시험 + 시연
python3 bin/ai-smell analyze 글.md                  # 지수와 신호 목록
python3 bin/ai-smell polish 글.md > 글.교정.md      # 교정문은 표준 출력, 요약은 표준 오류
python3 bin/ai-smell prompt 글.md --target claude   # 남은 신호를 LLM이 고칠 지시문
python3 bin/ai-smell verify 글.md 글.최종.md        # 사실 보존, 변경률, 새 신호 대조
```

| 명령 | 하는 일 |
|---|---|
| `analyze` | 지수(0~100), 범주별 신호, 문단별 지수. `--format json`, `--genre academic\|everyday\|literary` |
| `polish` | 교정문 출력. `--tier safe\|standard\|strong`, `--out`, `--in-place`(.bak 백업), `--diff`, `--format json` |
| `prompt` | 남은 신호를 고칠 LLM 프롬프트. `--target generic\|claude\|gpt\|gemini`, `--chat ko\|en`(셸 없는 환경용) |
| `verify` | 숫자·주소·코드·인용·영문 고유명사 보존, 변경률, 새 신호. PASS/WARN/CONFIRM/FAIL |
| `rules` | 규칙 목록 (등급, 교정 단계). 전체는 [`docs/rules.md`](docs/rules.md) |
| `selftest`, `doctor` | 설치 확인 |
| `install` | 스킬·에이전트 설치. `--scope user\|project\|both`, `--agents`, `--dry-run`, `--uninstall` |

작성자 금지어는 `--ban "구절"`, `--ban-file 목록.txt`로 넘긴다. 코드 블록, 인라인 코드, URL, 인용 블록(`>`), `<!-- ai-smell:ignore-start -->`와 `<!-- ai-smell:ignore-end -->` 사이는 보지도 고치지도 않는다.

## 실제 출력 예

영어 표본 (`polish`는 기본 standard 단계):

```text
원문: Certainly! In today's fast-paced digital world, AI plays a crucial role in shaping how teams work.
      It's not just a tool, it's a game-changer. Experts agree that organizations can leverage its robust
      capabilities to unlock their full potential. In order to get started, utilize the free tier. I hope this helps!

AI 냄새 지수 95/100 — 강함  →  standard 교정 후 78/100 (자동 교정 6건, 변경률 29%, 대조 PASS)

교정문: AI plays a crucial role in shaping how teams work. It's not just a tool, it's a game-changer. Experts agree
        that organizations can use its robust capabilities to unlock their full potential. To get started, use the free tier.

strong 단계: ... It's a game-changer. ...   ("It's not just a tool, it's"가 "It's"로, 뜻이 달라질 수 있어 읽고 확인한다)
```

한국어 표본:

```text
원문: 물론입니다! 급변하는 AI 시대에 인공지능은 단순한 도구가 아니라 패러다임의 전환을 의미한다. 이는 다양한 측면에서
      시사하는 바가 크다. 분석을 진행한 결과, 비용이 감소되어진 것으로 나타났다. 도움이 되었기를 바랍니다.

AI 냄새 지수 87/100 — 강함  →  standard 교정 후 65/100 (자동 교정 4건, 변경률 26%, 대조 PASS)

교정문: 급변하는 AI 시대에 인공지능은 단순한 도구가 아니라 패러다임의 전환을 의미한다. 이는 다양한 측면에서
        시사하는 바가 크다. 분석한 결과, 비용이 감소된 것으로 나타났다.
```

남은 점수는 엔진이 일부러 자동으로 고치지 않는 구조 습관이다. 이 표본에는 구체적 내용이 거의 없어서, 에이전트가 `prompt` 지시대로 고치면 대부분 지워진다. 실제로 영어 표본을 `AI shapes how teams work. Organizations can use its capabilities. To get started, use the free tier.`로 줄였을 때 지수는 0이 되었지만 `verify`는 변경률 78%라 **CONFIRM**(필자 확인 필요)을 냈다. 지어내서 채우지 않고 필자에게 구체적 사례를 묻는 것이 맞다.

## 어떻게 동작하나

1. **보호**: 코드, URL, 인용 블록, 무시 구간을 가린다.
2. **측정**: 197개 규칙(영어 118, 한국어 66, 공통 13)과 분석기 열 가지가 신호를 찾는다. 신호마다 근거 등급(A/B/C)이 있고 등급이 가중치에 곱해진다.
3. **지수**: 범주별 상한을 둔 밀도 점수와 챗봇 잔재 점수를 합친다. 문장 길이 변동은 약한 신호라 점수에 넣지 않는다.
4. **교정**: `safe`(글자만), `standard`(군더더기·잔재·이중 피동 등 뜻이 거의 안 바뀌는 것), `strong`(뜻이 조금 달라질 수 있음). 구조 습관은 자동으로 고치지 않는다.
5. **대조**: 고친 글에서 숫자·주소·코드·인용이 바뀌면 FAIL, 변경률이 50%를 넘으면 CONFIRM, 새 신호가 생기면 WARN.

설계는 [`docs/design.md`](docs/design.md), 규칙의 근거와 출처는 [`docs/research.md`](docs/research.md)에 있다.

## 설치 위치

| 도구 | 사용자 범위 | 프로젝트 범위 |
|---|---|---|
| Claude Code | `~/.claude/skills/ai-smell-polish`, `~/.claude/agents/ai-smell-polisher.md` | `.claude/skills/...`, `.claude/agents/...` |
| 공통(Codex, Gemini CLI 등) | `~/.agents/skills/ai-smell-polish` | `.agents/skills/ai-smell-polish` |
| Gemini CLI | `~/.gemini/skills/ai-smell-polish` | `.gemini/skills/ai-smell-polish` |
| Codex (구 경로) | `~/.codex/skills/ai-smell-polish` | |

**각 도구가 이 경로를 실제로 읽는지는 직접 확인하지 못했다**(문서 요약 기준). 설치 뒤 도구의 스킬 목록에 `ai-smell-polish`가 보이는지 확인한다.

## 모델에 상관없이 쓰기

엔진은 LLM을 부르지 않으므로 어떤 모델이든 같다. 구조 습관을 고치는 단계만 에이전트 모델이 하는데, 지시문은 마크다운 틀(GPT·Gemini·일반)과 XML 태그 틀(Claude)로 만든다(`prompt --target`). 셸이 없는 웹 채팅에는 [`chat-prompts.md`](skills/ai-smell-polish/references/chat-prompts.md)의 한국어·영어 프롬프트를 붙여 넣는다(이때는 지수와 대조 검증이 없다).

## 폴더

```
install.py   bin/ai-smell   AGENTS.md
skills/ai-smell-polish/{SKILL.md, scripts/, references/}   스킬 = 엔진 + 지침
agents/{claude, codex, gemini}/                             에이전트 정의와 안내
docs/{design, research, limits, rules}.md
tests/
```

## English summary

`ai-smell-meter` measures and removes "AI smell" (chatbot residue, importance inflation, negative parallelism, translationese, filler) in **Korean and English** text and prints the corrected text. It is stdlib-only Python 3.9+, ships as an Agent Skill (`ai-smell-polish`) plus a Claude Code subagent definition, and an agent can install and self-test it from `AGENTS.md`. It is **not an AI detector**: the index is a density of style signals, not a probability of authorship, and it has no detector-evasion features. Mechanical fixes are tiered (`safe`/`standard`/`strong`); structural rewrites are delegated to the agent through `prompt`, then checked by `verify` (facts, change rate, new signals). Limits and unverified points: [`docs/limits.md`](docs/limits.md).

```bash
python3 install.py            # doctor + install + selftest + demo
python3 bin/ai-smell polish draft.md > draft.polished.md
```

## 라이선스

MIT. [`LICENSE`](LICENSE). 참고한 공개 프로젝트는 아이디어만 가져왔고 코드는 가져오지 않았다([`docs/research.md`](docs/research.md) 7절).
