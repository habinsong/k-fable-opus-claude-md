# Muse Spark — 교차 확인
> 제공자: Meta · 모델 ID: `muse-spark` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-spark/general.md`](../../../md/muse/muse-spark/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- 이 모델의 공식 문서나 공식 저장소는 이 환경에서 읽지 못했다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 최초 출시 | 2026-04-08 | [부분] 단일 출처 (2차 요약) | datanorth 외 |  |
| Muse Spark 1.1 (Meta Model API 유료 첫 모델) | 2026-07-09, 입력 $1.25 / 출력 $4.25, 컨텍스트 1,048,576 | [부분] 2차 3곳 일치 | implicator.ai, datanorth, developersdigest, t2online | 대기자 명단으로 개발자를 늘리고 신규 개발자에게 $20 크레딧, Meta 인프라 한정 |
| 1.2 / 1.3 | 2026-08-05 / 2026-09-02, 요금 같음, 1.3은 캐시 읽기 $0.15 | [부분] 단일 출처 (집계 사이트) | typingmind, llmgateway | Meta 공식 문서는 읽지 못했다 |
| 버전 표기 | 이 폴더 이름은 `muse-spark`이고 시장에는 1.1·1.2·1.3이 있다 | 해당 없음 | - | 수치를 인용할 때 어느 버전인지 확인한다 |

## 아직 못 올린 것
- Meta 공식 개발자 문서가 이 환경에서 열리지 않았다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [implicator.ai](https://www.implicator.ai/meta-prices-its-first-paid-ai-model-api-at-4-25-per-million-output-tokens/)
- [datanorth](https://datanorth.ai/news/meta-releases-muse-spark-1-1-agentic-ai-model)
- [developersdigest](https://www.developersdigest.tech/blog/meta-muse-spark-1-1-developer-guide-2026)
- [t2online](https://t2online.in/tech/tech-news/meta-unveils-muse-spark-1-1-as-it-enters-the-ai-pricing-war/2006371)
- [llmgateway (1.3)](https://llmgateway.io/models/muse-spark-1.3)
