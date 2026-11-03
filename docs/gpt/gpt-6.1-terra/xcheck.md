# GPT-6.1 Terra — 교차 확인
> 제공자: OpenAI · 모델 ID: `gpt-6.1-terra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-terra/general.md`](../../../md/gpt/gpt-6.1-terra/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- openai-python 3.39.0 (2026-10-26): "add gpt-6.1-terra model identifier".

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 (GA) | 2026-10-26 | [확인] 1차 + [부분] 2차 4곳 일치 | SDK 변경 기록; aiweekly, letsdatascience, yourstory, forkast |  |
| 가격 (입력/출력) | $1 / $5 | [부분] 2차 5곳 일치 | aiweekly, letsdatascience, yourstory, llmgateway, vals.ai | '50% 인하'의 비교 대상이 Sol(aiweekly)과 GPT-5.6 Terra(다른 기사)로 엇갈린다 |
| 컨텍스트 / 최대 출력 | 약 1.05M (일부 1.1M) / 128K | [부분] 2차 3곳 일치 | aicybr, llmgateway, vals.ai |  |
| 제공 범위 | ChatGPT Work·Codex + API(`gpt-6.1-terra`) | [부분] 상충 | 한 기사는 ChatGPT·Codex 중심, 다른 기사는 API 별도 발표가 없다고 적음 | SDK에 식별자가 추가된 것은 API 노출을 시사하지만 가용성은 확인하지 못했다 [추정] |

## 아직 못 올린 것
- openai.com, developers.openai.com 본문이 이 환경에서 열리지 않아 공식 모델 페이지와 요금표는 읽지 못했다. 열리면 컨텍스트, 요금, 기본 effort를 [확인]으로 올릴 수 있다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [openai/openai-python CHANGELOG](https://raw.githubusercontent.com/openai/openai-python/main/CHANGELOG.md)
- [aiweekly](https://aiweekly.co/alerts/openai-ships-gpt-61-terra-at-15-per-million-half-of-sol)
- [letsdatascience](https://letsdatascience.com/news/openai-releases-gpt-61-terra-cutting-price-50-and-benchmark-bc892dc4)
- [yourstory](https://yourstory.com/ai-story/gpt-6-1-terra-lower-api-pricing-developers)
- [llmgateway](https://llmgateway.io/models/gpt-6.1-terra)
- [forkast](https://forkast.news/gpt-6-1-terra-arrives-at-1-5-half-the-rate-of-a-model-openai-shipped-27-days-ago/)
