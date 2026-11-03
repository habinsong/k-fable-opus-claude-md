# docs — 조사·검증 기록

이 폴더는 **사람이 직접 읽고 검토하는 조사 기록**입니다. LLM 컨텍스트에는 포함하지 않습니다. 프롬프트 컨텍스트에 넣는 작업 지침은 범용 지침인 [`universal/`](../universal/)과 모델별 지침인 [`md/`](../md/)에만 배치합니다.

각 모델의 사양, 가격, 벤치마크 지표, 독립 평가와의 비교 분석, 비판적 평가, 운용상 주의사항, 출처 URL, 미확인 사항을 이곳에 정리해 두었습니다. 이러한 메타데이터가 프롬프트 컨텍스트에 섞이면 모델이 핵심 지침을 해석하는 데 방해가 될 수 있어, `universal/`과 `md/`에서는 모두 제외했습니다.

## 디렉터리 구조

```text
docs/
├── README.md                         조사 기록 전체 안내 (본 문서)
├── _common/                          계열 및 모델 공통 조사 기록
│   ├── domain-rules/분야.md          분야별 규칙의 근거 수준 (행 단위 대조 표, 9개 분야)
│   └── korean-writing/               한국어 문체 조사 기록 (측정 도구, 실측, 문장 원리, 서지)
└── 계열/모델/
    ├── README.md                     해당 모델 조사 기록의 색인
    ├── overview.md                   모델 위치, 연혁, 사양, 라이선스
    ├── performance.md                성능 근거 (벤더 자체 수치 및 독립 평가 해석)
    ├── operations.md                 실제 운용 (행동 특성, API·하네스·로컬 구동, 데이터 정책)
    ├── critique.md                   비판적 평가 및 적합/부적합 상황
    ├── sources.md                    출처 URL, 확인 수준, 조사상 한계
    ├── xcheck.md                     공식 문서 외 복수 출처와의 교차 검증 결과
    ├── domains/분야.md               웹·앱·하드웨어 등 분야별 운용 조사와 출처
    └── korean-writing.md             한국어 윤문 3개 분야의 모델별 조사 기록 (주요 4대 계열)
```

분석 대상 내용이 없거나 실측 수치가 없는 파일(예: 성능 근거가 확인되지 않은 모델의 `performance.md`)은 무리하게 만들지 않았습니다. 실질적인 분석 내용이 있는 항목만 `README.md`를 통해 안내합니다.

## md 지침 문서와의 대응 관계

| `md/계열/모델/` 지침 문서 | 대응하는 `docs/계열/모델/` 조사 문서 |
|---|---|
| `general.md` | `overview.md`, `performance.md`, `operations.md`, `critique.md`, `sources.md`, `xcheck.md` |
| `web.md`, `app.md`, `native.md`, `hardware.md`, `firmware.md`, `web-research.md`, `research.md`, `tech-research.md` | `domains/동일-명칭.md` |
| `ko-academic.md`, `ko-everyday.md`, `ko-literary.md` | `korean-writing.md` (세 분야의 모델 조사를 하나로 통합) |

소제목 번호(2.x)는 주제별 분리 이전의 초기 일반 조사 기록 번호를 승계한 체계입니다. `domains/` 문서의 절 번호는 대응하는 지침 문서의 번호 체계(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙)와 일치합니다.

## 지원 계열과 모델

| 폴더 | 개발사 | 대상 모델 |
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

## 근거 수준 표기 체계

- `[확인]`: 1차 출처(공식 기술 문서, API 명세, 소스 코드)를 직접 열람하여 교차 확인을 마친 내용입니다.
- `[부분]`: 검색 결과 요약문, 2차 인용 기사, 벤더 자체 주장, 집계 사이트만을 통해 파악한 내용입니다.
- `[미확인]`: 조사 환경에서 확인하지 못했거나 출처 간 내용이 서로 충돌하는 항목입니다.
- `[추정]`: 이미 검증된 사실들을 바탕으로 논리적으로 이끌어낸 분석적 추론입니다.

모델 개발사가 직접 발표한 벤치마크는 객관적 사실이 아닌 일방의 주장으로 다룹니다. 독립 평가 지표의 버전이 다를 경우 무리하게 값을 비교하지 않고 충돌 항목으로 분류했습니다.

## 한계와 주의사항

- 본 조사는 조사 시점의 최신 공개 자료를 바탕으로 작성되었습니다. 검색 및 수집 범위는 주로 2026년 9월 말부터 10월까지이며, 이후 발표된 최신 변경 사항은 온전히 반영하지 못했을 수 있습니다.
- 조사 당시 일부 공식 기술 웹사이트에 직접 접근하기 어려워 다수의 항목이 `[부분]` 수준에 머물러 있습니다. 본 폴더의 사실을 의사결정의 근거로 삼으실 때는 공식 1차 출처를 직접 한 번 더 확인해 주시기 바랍니다.
- 문서 형식과 정합성은 `scripts/docs_tool.py`를 통해 기계적으로 검사하지만, 기재된 사실 관계의 정확성까지 스스로 보증하지는 않습니다.
