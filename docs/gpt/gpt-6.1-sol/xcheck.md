# GPT-6.1 Sol — 교차 확인
> 제공자: OpenAI · 모델 ID: `gpt-6.1-sol` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6.1-sol/general.md`](../../../md/gpt/gpt-6.1-sol/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- openai-python 3.21.0 (2026-09-29): "add GPT-6.1 Sol model identifier".
- 같은 변경 기록 3.18.0 (2026-09-22)에는 "GPT-6 Sol" 식별자가 먼저 추가돼 있다. 6 Sol과 6.1 Sol은 다른 식별자다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 (6.1 Sol) | 2026-09-29 | [확인] 1차 + [부분] 2차 3곳 일치 | SDK 변경 기록; gradually.ai, devtk.ai, anotherwrapper | 한 곳은 GPT-6 Sol이 09-22라고 적는다. 6 Sol과 6.1 Sol을 섞은 서술이다 |
| 가격 (입력/출력) | $2 / $10, 캐시 입력 $0.10 | [부분] 2차 4곳 일치 | gradually.ai, anotherwrapper, devtk.ai, getmaxim | pricepertoken은 $1/$5로 상충 |
| 컨텍스트 / 최대 출력 | 약 1.05M / 128K | [부분] 2차 3곳 일치 | gradually.ai, devtk.ai, llm-stats | 장문 요금은 입력 약 272K 초과 구간. 한 블로그의 $4/$15는 가격 출처가 아니라 해설 글이다 |

## 아직 못 올린 것
- openai.com, developers.openai.com 본문이 이 환경에서 열리지 않아 공식 모델 페이지와 요금표는 읽지 못했다. 열리면 컨텍스트, 요금, 기본 effort를 [확인]으로 올릴 수 있다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.
- 한 비교 사이트는 developers.openai.com과 대조했다고 쓰지만 이 환경에서는 그 페이지를 열 수 없다.

## 출처
- [openai/openai-python CHANGELOG](https://raw.githubusercontent.com/openai/openai-python/main/CHANGELOG.md)
- [gradually.ai](https://www.gradually.ai/en/ai-models/gpt-6.1-sol/)
- [anotherwrapper](https://anotherwrapper.com/llm-pricing/gpt-6.1-sol)
- [devtk.ai](https://devtk.ai/en/models/gpt-6-1-sol/)
- [pricepertoken](https://pricepertoken.com/pricing-page/model/openai-gpt-6.1-sol)
- [developersdigest 비교](https://www.developersdigest.tech/models/compare/gpt-6-1-sol-vs-gpt-6-sol)
