# Gemini 4 Argon — 교차 확인
> 제공자: Google · 모델 ID: `gemini-4-argon` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-argon/general.md`](../../../md/gemini/gemini-4-argon/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- python-genai 2.31.0 (2026-10-14): "interactions: Add gemini-4-argon to Model enum" — 식별자가 SDK에 들어온 날짜다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 발표 / GA | 발표 2026-09-30(사이버 방어자 한정), GA 2026-10-13 | [확인] 1차(식별자 10-14) + [부분] 2차 4곳 일치 | toolhalla(Gemini API changelog 인용), tech-insider(Google Cloud 발표 인용), letsdatascience, braindetox | Apidog·OrcaRouter 일부 글은 09-30 한정 공개 시점의 서술이라 낡았다 |
| 모델 ID | `gemini-4-argon` | [확인] 1차 + [부분] 2차 2곳 일치 | SDK 변경 기록; toolhalla, tech-insider |  |
| 컨텍스트 / 출력 | 1,048,576(입출력 공유) / 동기 요청 기본 65,536 | [부분] 2차 3곳 일치 | codersera, toolhalla, pricepertoken | 한 목록은 출력을 32,768로 적는다 |
| 가격 (입력/출력) | $2 / $10 (2026-11-30까지) → $4 / $20 (12-01부터), 캐시 입력 $0.10 → $0.20 | [부분] 2차 7곳 일치 | letsdatascience, fourweekmba(2건), eesel.ai, daniel vaughan, smartscope, buildmvpfast | Google 각주를 인용했다는 글이 여럿이다. Vertex AI는 소개가를 '순지출의 50% 크레딧 환급'으로 적용하고 'Gemini 4 Argon Cyber Permissive'에는 적용되지 않는다는 서술. 한 글은 각주가 기간을 정의하지 않았다고 적어 상충 |
| Gemini 앱 구독자 개방 | 2026-10-13 | [부분] 단일 출처 | letsdatascience | API와 앱은 다른 표면이다 |
| 제공 표면 | Gemini API, Google AI Studio, Antigravity | [부분] 단일 출처, 일부 상충 | tech-insider, braindetox | Pro 구독의 Gemini 앱 포함 여부는 서술이 갈린다 (API와 앱은 다른 표면) |

## 아직 못 올린 것
- blog.google, ai.google.dev가 이 환경에서 열리지 않아 공식 모델 페이지, 요금표, changelog 본문은 읽지 못했다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.
- 소개가가 12-01에 두 배가 되는 점은 이 문서 기준일(11-03)에서 한 달도 남지 않았으므로 쓰기 전에 요금 페이지로 다시 확인한다.

## 출처
- [googleapis/python-genai CHANGELOG](https://raw.githubusercontent.com/googleapis/python-genai/main/CHANGELOG.md)
- [toolhalla](https://toolhalla.ai/blog/gemini-4-argon-api-price-context-2026)
- [tech-insider](https://tech-insider.org/?p=36556)
- [letsdatascience](https://letsdatascience.com/news/gemini-4-argon-undercuts-claude-on-price-73027210)
- [codersera](https://codersera.com/blog/gemini-4-argon-complete-guide-2026/)
- [braindetox](https://braindetox.kr/en/posts/gemini_4_argon_general_availability_2026.html)
- [buildmvpfast](https://www.buildmvpfast.com/blog/gemini-4-argon-pricing-intro-rates-2026)
- [fourweekmba (Argon 가격 각주)](https://fourweekmba.com/ai-gemini-4-argon-introductory-price-footnote-4-20/)
- [eesel.ai (Argon 가격)](https://www.eesel.ai/blog/gemini-4-argon-pricing)
- [Google 블로그 Argon (열리지 않음)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
