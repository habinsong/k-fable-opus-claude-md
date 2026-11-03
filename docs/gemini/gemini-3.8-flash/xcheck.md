# Gemini 3.8 Flash — 교차 확인
> 제공자: Google · 모델 ID: `gemini-3.8-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-3.8-flash/general.md`](../../../md/gemini/gemini-3.8-flash/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- python-genai 2.22.0 (2026-09-02): "Add Gemini 3.8 Flash model to SDKs and update Flash model descriptions".
- 같은 변경 기록: 2.26.0 (2026-09-30) Gemini 3.8 Flash TTS·Flash Lite TTS 추가.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 | 2026-09-02 | [확인] 1차 + [부분] 2차 2곳 일치 | SDK 변경 기록; llmgateway, pricepertoken |  |
| 컨텍스트 / 최대 출력 | 1,048,576 / 65,536 | [부분] 2차 3곳 일치 | cloudprice, llmgateway, getmaxim | 한 곳은 출력을 '약 66K'로 적음 |
| 가격 (입력/출력) | $0.75 / $3.75 (소개가), 캐시 입력 $0.075 | [부분] 2차 4곳 일치 | mindstudio, eesel.ai, apidog, anotherwrapper | 소개가 만료가 2026-12-31(두 곳)이라는 서술과 2027-01-01에 $1.50/$7.50으로 두 배라는 서술(한 곳)이 있다 |
| 가격 (낮은 쪽 값) | $0.375 / $1.88 | [부분] 상충 | pricepertoken(2026-09-05 자 페이지), cloudprice | 나머지 다수와 맞지 않는다. 낡은 값으로 본다 [추정] |

## 아직 못 올린 것
- blog.google, ai.google.dev가 이 환경에서 열리지 않아 공식 모델 페이지, 요금표, changelog 본문은 읽지 못했다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.
- 소개가 만료일은 공식 요금 페이지로 확인하기 전에 단정하지 않는다.

## 출처
- [googleapis/python-genai CHANGELOG](https://raw.githubusercontent.com/googleapis/python-genai/main/CHANGELOG.md)
- [mindstudio](https://www.mindstudio.ai/blog/gemini-3-8-flash-pricing)
- [eesel.ai](https://eesel.ai/blog/gemini-3-8-flash-pricing)
- [apidog](https://apidog.com/blog/gemini-3-8-flash-pricing/)
- [llmgateway](https://llmgateway.io/models/gemini-3.8-flash)
- [pricepertoken](https://pricepertoken.com/pricing-page/model/google-gemini-3.8-flash)
