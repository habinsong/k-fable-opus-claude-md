# GPT-6 Luna — 교차 확인
> 제공자: OpenAI · 모델 ID: `gpt-6-luna` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-luna/general.md`](../../../md/gpt/gpt-6-luna/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- openai-python 3.18.0 (2026-09-22): "add GPT-6 Sol and Luna model identifiers".

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-09-22 | [확인] 1차 + [부분] 2차 3곳 일치 | SDK 변경 기록; llmgateway, apidog, codersera |  |
| 가격 (입력/출력) | $0.10 / $0.50 | [부분] 2차 5곳 일치 | llmgateway, apidog, codersera, usagepricing, tokencost.app | 캐시 입력 $0.01은 단일 출처 |
| 장문 요금 (입력 272K 이상) | $0.20 / $0.75 | [부분] 단일 출처 | 한 가격 비교 글 | 나머지 GPT-6 계열과 같은 임계라는 서술이 있다 |
| 컨텍스트 / 최대 출력 | 1,050,000 (최대 입력 922,000) / 128,000 | [부분] 상충 | apidog·codersera 계열은 1.05M, 다른 곳은 1M·1.1M | 1.05M과 922K 입력 상한 서술이 가장 자세하다. 반올림 차이일 수 있다 [추정] |

## 아직 못 올린 것
- openai.com, developers.openai.com 본문이 이 환경에서 열리지 않아 공식 모델 페이지와 요금표는 읽지 못했다. 열리면 컨텍스트, 요금, 기본 effort를 [확인]으로 올릴 수 있다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.
- 'GPT-5.6 Luna'라는 같은 계층 이름이 이전 세대에 있어 검색 결과가 섞인다. 값을 인용할 때 세대(5.6 대 6)를 확인한다.

## 출처
- [openai/openai-python CHANGELOG](https://raw.githubusercontent.com/openai/openai-python/main/CHANGELOG.md)
- [llmgateway](https://llmgateway.io/models/gpt-6-luna)
- [apidog](https://apidog.com/blog/what-is-gpt-6-luna/)
- [codersera](https://codersera.com/blog/gpt-6-luna-complete-guide-2026/)
- [usagepricing](https://www.usagepricing.com/ai-token-pricing/openai/gpt-6-luna)
- [tokencost.app](https://tokencost.app/models/gpt-6-luna)
