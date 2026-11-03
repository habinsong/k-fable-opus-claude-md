# Grok 4.7 — 교차 확인
> 제공자: xAI · 모델 ID: `grok-4.7` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/grok/grok-4.7/general.md`](../../../md/grok/grok-4.7/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- xai-org/grok-build의 model.rs 테스트에 `grok-4.7`(컨텍스트 [256K, 500K]), effort `xhigh`~`low`가 있다. 시험용 값이라 실제 제공 사양의 증거로는 약하지만 500K와 4단계 effort는 2차와 맞는다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-09-21 | [부분] 2차 2곳 일치 | letsdatascience, vpsranking |  |
| 컨텍스트 | 500K | [부분] 2차 4곳 일치 + 코드 시험값 | letsdatascience, llmgateway, devtk.ai, 기존 문서 / grok-build 시험 픽스처 |  |
| 가격 (입력/출력) | $2 / $6 | [부분] 2차 4곳 일치 | llmgateway, anotherwrapper, pricepertoken, usagepricing | AIML API 경유는 $2.6/$7.8, 지역 엔드포인트는 10% 가산 |
| 장문 요금 (입력 200K 이상) | $4 / $12 (요청 전체) | [부분] 단일 출처 | 한 가격 사이트 | AIML API는 200K 초과 $5.2/$15.6으로 다르다 |
| 추론 단계 | `low` / `medium` / `high` / `xhigh` | [부분] 2차 2곳 일치 + 코드 시험값 | letsdatascience, devtk.ai / grok-build | `none`은 시험에서 거부값 |
| 기본 effort / 추론 끄기 | 기본 `high`, 추론을 끌 수 없음 | [부분] 단일 출처 | Oracle OCI 문서 요약(검색 결과) | Oracle 문서는 이 환경에서 열리지 않아 요약만 봤다 |
| 최대 출력 | 미공개 / 450K / 500K | [부분] 상충 | CometAPI('xAI가 한도를 적지 않음'), OrcaRouter(450K), pi.dev(500K) | 컨텍스트와 같은 값을 적은 곳도 있어 믿기 어렵다 |
| 제공 경로 | Amazon Bedrock에서 500K 컨텍스트로 제공 | [부분] 단일 출처 | aiweekly |  |
| Fast 변형 | Cursor·Grok Build 한정, 공개 API에는 없음 | [부분] 단일 출처 | 한 사이트 |  |

## 아직 못 올린 것
- docs.x.ai가 이 환경에서 열리지 않았다. 공식 모델 목록과 요금표를 읽지 못했다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [xai-org/grok-build model.rs](https://raw.githubusercontent.com/xai-org/grok-build/main/crates/codegen/xai-grok-pager/src/slash/commands/model.rs)
- [letsdatascience](https://letsdatascience.com/news/xai-releases-grok-47-with-500k-context-43aa2021)
- [vpsranking](https://vpsranking.com/news/ai/ai-2026-09-21-xai-grok-47/)
- [llmgateway](https://llmgateway.io/models/grok-4-7)
- [anotherwrapper](https://anotherwrapper.com/llm-pricing/grok-4.7)
- [pricepertoken](https://pricepertoken.com/pricing-page/model/xai-grok-4.7)
- [usagepricing](https://www.usagepricing.com/ai-token-pricing/xai/grok-4-7)
- [Oracle OCI (열리지 않음)](https://docs.oracle.com/iaas/Content/generative-ai/x-ai-grok-4-7.htm)
- [aiweekly (Bedrock)](https://aiweekly.co/alerts/xais-grok-47-goes-live-on-amazon-bedrock-with-500k-context)
- [CometAPI (사양)](https://www.cometapi.com/en/models/xai/grok-4-7)
