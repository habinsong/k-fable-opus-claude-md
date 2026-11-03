# docs — 조사·검증 기록

이 폴더는 **사람이 읽는 조사 기록**입니다. LLM 컨텍스트에 넣지 않습니다. 컨텍스트에 넣는 지침은 [`universal/`](../universal/)(범용)과 [`md/`](../md/)(모델별)에만 있습니다.

모델의 사양, 가격, 벤치마크, 독립 평가와의 비교, 비판적 평가, 운용상의 주의, 출처 URL, 확인하지 못한 것을 여기에 둡니다. 이런 내용이 컨텍스트에 섞이면 모델이 지침을 읽는 데 방해가 되므로 `universal/`과 `md/`에서는 모두 뺐습니다.

## 구조

```
docs/
├── README.md
├── _common/                          제공자·모델에 공통인 조사 기록
│   ├── domain-rules/<분야>.md        분야 규칙의 "시점에 민감한 사실" 근거 수준 (행 단위 표, 분야 9개)
│   └── korean-writing/               한국어 윤문 조사 (AI 말투 도구, 실측, 한국어 원리, 서지)
└── <계열>/<모델>/
    ├── README.md                     이 모델 조사 기록의 색인
    ├── overview.md                   위치, 출시·연혁, 사양, 라이선스
    ├── performance.md                성능 근거 (벤더 수치와 독립 평가를 읽는 법)
    ├── operations.md                 운용 (행동 특성, API·하네스·로컬 실행, 데이터·정책)
    ├── critique.md                   비판적 평가, 쓸 때와 쓰지 않을 때
    ├── sources.md                    출처 URL, 확인 수준, 한계
    ├── xcheck.md                     사양을 공식 문서 말고 다른 출처(공식 저장소, 2차 여러 곳)로 교차 확인한 결과
    ├── domains/<분야>.md             웹·앱·네이티브·하드웨어·펌웨어·웹 리서치·리서치·기술 리서치에서의 이 모델 운용
    └── korean-writing.md             한국어 윤문 3분야의 모델별 조사와 지침 근거 (gpt·claude·gemini·gemma만)
```

해당 내용이 없는 주제 파일(예: 성능 근거가 없는 모델의 `performance.md`)은 만들지 않았습니다. `README.md`가 있는 파일만 안내합니다.

## md 문서와의 짝

| `md/<계열>/<모델>/` | `docs/<계열>/<모델>/` |
|---|---|
| `general.md` | `overview.md`, `performance.md`, `operations.md`, `critique.md`, `sources.md`, `xcheck.md` |
| `web.md`, `app.md`, `native.md`, `hardware.md`, `firmware.md`, `web-research.md`, `research.md`, `tech-research.md` | `domains/<같은 이름>.md` |
| `ko-academic.md`, `ko-everyday.md`, `ko-literary.md` | `korean-writing.md` 하나 (세 분야의 모델 조사가 같음) |

소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호입니다. `domains/` 문서의 절 번호는 짝이 되는 지침 문서의 번호를 따릅니다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).

## 계열과 모델

| 폴더 | 제공자 | 모델 |
|---|---|---|
| `gpt/` | OpenAI | `gpt-6-astra` · `gpt-6-luna` · `gpt-6.1-sol` · `gpt-6.1-terra` |
| `claude/` | Anthropic | `fable-5.1` · `fable-5.5` · `haiku-5.5` · `opus-5.5` · `sonnet-5.5` |
| `gemini/` | Google | `gemini-3.8-flash` · `gemini-4-argon` · `gemini-4-carbon` |
| `gemma/` | Google (로컬) | `gemma-4-12b` · `gemma-4-26b-a4b` · `gemma-4-31b` · `gemma-4-e2b` · `gemma-4-e4b` |
| `deepseek/` | DeepSeek | `v4.1-flash-1017` |
| `glm/` | Z.ai(Zhipu) | `glm-5.3` · `glm-5.3-flash` · `glm-5.5` |
| `muse/` | Meta | `muse-spark` · `muse-wonder` |
| `grok/` | xAI | `grok-4.7` · `grok-4.8` · `grok-5` |
| `kimi/` | Moonshot | `kimi-k3.1` |
| `qwen/` | Alibaba | `qwen3.6-27b` · `qwen3.6-35b-a3b` · `qwen3.7-max` · `qwen3.8-2.4t-a95b` · `qwen3.8-27b` · `qwen3.8-max` |
| `minimax/` | MiniMax | `minimax-m3` · `minimax-m3.1-flash` |

## 근거 수준 표기

- `[확인]`: 1차 출처(공식 문서, 명세, 소스)를 직접 읽고 확인했습니다.
- `[부분]`: 검색 결과 요약, 2차 출처, 벤더 주장, 집계 사이트에서만 확인했습니다.
- `[미확인]`: 확인하지 못했거나 출처끼리 충돌합니다.
- `[추정]`: 확인된 사실에서 제가 끌어낸 추론입니다.

벤더가 직접 낸 벤치마크는 주장으로만 다룹니다. 독립 지수의 버전이 다르면 값을 비교하지 않고 충돌로 적었습니다.

## 한계

- 조사 기준일은 2026-11-03입니다. 검색 범위는 대체로 2026년 9월 말~10월까지였고, 그 이후 발표는 반영하지 못했습니다.
- 공식 사이트 상당수가 조사 환경에서 열리지 않아 많은 내용이 `[부분]`입니다. 이 폴더의 사실을 근거로 삼기 전에 공식 출처로 다시 확인하세요.
- 형식은 `scripts/docs_tool.py`로 검사하지만, 사실 여부는 검사하지 않습니다.
