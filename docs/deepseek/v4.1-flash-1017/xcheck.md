# DeepSeek V4.1 Flash 1017 — 교차 확인
> 제공자: DeepSeek · 모델 ID: `deepseek-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/deepseek/v4.1-flash-1017/general.md`](../../../md/deepseek/v4.1-flash-1017/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- 공식 GitHub 조직 deepseek-ai에는 모델 저장소가 없고 도구 저장소(DeepEP, FlashMLA, deepseek-harness 등)만 있다. 모델 사양의 1차 출처는 api-docs.deepseek.com과 Hugging Face인데 둘 다 이 환경에서 열리지 않았다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| V4.1 Flash 출시 | 2026-09-10 | [부분] 2차 4곳 일치 | llm-stats, yottalabs, propakistani, The Next Web | 이전 문서의 '09-08~10 제한 베타'와 겹친다 |
| 1017 갱신 | 2026-10-17, 같은 `deepseek-flash` 엔드포인트, 가격 불변 | [부분] 2차 5곳 일치 | technode, producthunt, ifeng, mezha, technews.tw |  |
| 가격 (입력/출력) | $0.30 / $1.20 (피크), 비피크 절반 | [부분] 상충 | technode, usagepricing / OpenRouter $0.15/$0.60 / pricepertoken $0.07/$0.18 | 제3자 경로의 가격은 DeepSeek API와 다를 수 있다. 공식 가격표는 읽지 못함 |
| 컨텍스트 / 최대 출력 | 1M / 384K | [부분] 단일 출처, 일부 상충 | technode(1M, 384K) | 1,050,000이라는 표기는 lmmarketcap 한 곳에만 있고 다른 곳에서 확인되지 않았다 |
| 입력 모달리티 | 텍스트 + 이미지 | [부분] 2차 2곳 일치 | technode, 이전 문서의 보도 |  |
| 라이선스 | MIT (저장소와 가중치 모두) | [부분] 2차 3곳 일치 | pasqualepillitteri, mind-verse.de, neura.market | Hugging Face 카드를 인용한 서술이다. 카드 원문은 읽지 못함 |
| 파라미터 수 | 763B(카드 표기) / 552B(백본) / 약 748.5B(engram 포함) | [부분] 상충 | neura.market, pasqualepillitteri, 한 해설 글 | 백본 551.566B + engram 196.929B라는 분해 서술이 상충을 설명할 수 있다 [추정] |

## 아직 못 올린 것
- api-docs.deepseek.com, huggingface.co가 이 환경에서 열리지 않았다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [technode (1017)](https://technode.com/2026/10/19/deepseek-releases-v4-1-flash-1017-with-stronger-coding-and-agent-capabilities/)
- [The Next Web](https://thenextweb.com/news/deepseek-v4-1-flash-launch-v4-pro-retired-price-cut)
- [llm-stats](https://llm-stats.com/models/deepseek-v4.1-flash)
- [pasqualepillitteri (MIT)](https://pasqualepillitteri.it/en/news/24844/deepseek-releases-41-flash-1017-mit-weights-shorter-outputs)
- [mind-verse.de](https://www.mind-verse.de/news/deepseek-v4-1-flash-1017-offene-gewichte-f13538b2a65a)
- [neura.market](https://www.neura.market/news/deepseek-v4-1-flash-1m-context-mit-license-763b-parameters)
- [usagepricing](https://www.usagepricing.com/ai-token-pricing/deepseek/deepseek-v4-1-flash)
- [pricepertoken](https://pricepertoken.com/pricing-page/model/deepseek-deepseek-v4.1-flash)
- [lmmarketcap](https://lmmarketcap.com/zh/model/deepseek-v4-1-flash-1017)
