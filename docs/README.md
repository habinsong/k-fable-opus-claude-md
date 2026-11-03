# docs — 조사·검증 기록

이 폴더는 **사람이 읽는 조사 기록**입니다. LLM 컨텍스트에 넣지 않습니다. 컨텍스트에 넣는 지침은 [`md/`](../md/)에만 있습니다.

모델의 사양, 가격, 벤치마크, 독립 평가와의 비교, 비판적 평가, 운용상의 주의, 출처 URL, 확인하지 못한 것을 여기에 둡니다. 이런 내용이 컨텍스트에 섞이면 모델이 지침을 읽는 데 방해가 되므로 `md/`에서는 모두 뺐습니다.

## 구조

```
docs/
├── README.md
├── _common/                          제공자·모델에 공통인 조사 기록
│   ├── domain-rules/<분야>.md        분야 규칙의 근거 수준 표기 원본 (분야 9개)
│   └── korean-writing/               한국어 윤문 조사 (AI 말투 도구, 실측, 한국어 원리, 서지)
└── <계열>/<모델>/
    ├── <분야>.md                     md/<계열>/<모델>/<분야>.md 의 조사 기록 (분야 9개)
    └── korean-writing.md             한국어 윤문 3분야(ko-*)의 모델별 조사 기록 (gpt·claude·gemini·gemma만)
```

`md/<계열>/<모델>/<분야>.md` 한 개마다 같은 경로의 `docs/<계열>/<모델>/<분야>.md`가 짝으로 있습니다. 한국어 윤문 분야 3개(`ko-academic`, `ko-everyday`, `ko-literary`)는 모델 조사 기록이 같아서 `korean-writing.md` 한 개를 함께 씁니다.

## 분야 문서 9개

`general`(범용), `web`, `app`, `native`, `hardware`, `firmware`, `web-research`, `research`, `tech-research`.

각 조사 기록의 절 번호는 짝이 되는 지침 문서의 번호를 따릅니다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙). 그래서 `§2`부터 시작하고 `§4 근거와 한계`로 끝납니다.

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
