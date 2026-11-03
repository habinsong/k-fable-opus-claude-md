# GPT-6 Astra — 교차 확인
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/general.md`](../../../md/gpt/gpt-6-astra/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- openai-python 3.8.0 (2026-09-03): "add gpt-6-astra and related features" — 식별자가 SDK에 들어온 날짜다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-09-03 | [확인] 1차 + [부분] 2차 4곳 일치 | SDK 변경 기록; llmgateway, gradually.ai, guptadeepak, vorplabs | pricepertoken만 09-04. SDK 추가일은 식별자 공개일이고 제공 시작 시각은 아니다 |
| 컨텍스트 / 최대 출력 | 1,050,000 / 128,000 | [부분] 2차 3곳 일치 | guptadeepak, vorplabs, pricepertoken | pricepertoken은 1.1M으로 반올림. Codex 기본값 약 26만 토큰은 최대치와 다른 기본값으로 보인다 [추정] |
| 가격 (입력/출력, 100만 토큰당) | $10 / $50, 캐시 입력 $1, 배치 50% 할인 | [부분] 2차 3곳 일치 | llmgateway, guptadeepak, 기존 문서의 CloudZero·eesel.ai | pricepertoken은 $5/$25로 상충. 낮은 쪽이 낡았거나 틀린 것으로 보인다 [추정] |
| 장문 요금 (입력 272K 초과) | $20 / $75 (입력·캐시 2배, 출력 1.5배) | [부분] 2차 4곳 일치 | llmgateway 등급표, yottalabs, creolestudios, gradually.ai | 높은 요금이 272K 초과분이 아니라 요청 전체에 붙는다는 서술이 두 곳(piapi 블로그 포함). PiAPI의 $2/$10은 재판매 가격이라 제외 |
| 캐시 쓰기 / 배치·Flex | $12.50 / 표준의 50% | [부분] 2차 2곳 일치 | llmgateway, yottalabs |  |
| 지식 컷오프 | 2026-04-30 | [부분] 단일 출처 | vorplabs |  |
| 출시 전 소문 (컨텍스트 2M·10M, $2.50/$12) | 제외 | 해당 없음 | 여러 블로그 | 출시 전 추측 글이다. 출시된 Astra와 무관하게 본다 |

## 아직 못 올린 것
- openai.com, developers.openai.com 본문이 이 환경에서 열리지 않아 공식 모델 페이지와 요금표는 읽지 못했다. 열리면 컨텍스트, 요금, 기본 effort를 [확인]으로 올릴 수 있다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [openai/openai-python CHANGELOG](https://raw.githubusercontent.com/openai/openai-python/main/CHANGELOG.md)
- [llmgateway](https://llmgateway.io/models/gpt-6-astra)
- [gradually.ai](https://www.gradually.ai/en/ai-models/gpt-6-astra/)
- [guptadeepak](https://guptadeepak.com/ai-models/openai/gpt-6-astra/)
- [vorplabs](https://vorplabs.com/models/releases/gpt-6-astra)
- [pricepertoken](https://pricepertoken.com/pricing-page/model/openai-gpt-6-astra)
