# Gemini 4 Carbon (제한 공개) — 교차 확인
> 제공자: Google · 모델 ID: `gemini-4-carbon(미확인)` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/general.md`](../../../md/gemini/gemini-4-carbon/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- python-genai 변경 기록(2026-10-14 기준 2.31.0)에 carbon 항목이 없다. 공개 SDK 열거형에 없다는 뜻이며 출시 여부의 증거는 아니다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 발표 | 2026-10-28, 사이버 방어자 일부 → Fairwind Program으로 단계적 확대 | [부분] 2차 5곳 일치 | betanews, techrepublic, letsdatascience, nerdschalk, smartscope | Google 블로그 링크는 검색 결과에 있었으나 이 환경에서 열리지 않았다 |
| 일반 출시일 | 없음 ('soon'만 언급) | [부분] 2차 3곳 일치 | betanews, techrepublic, nerdschalk | 2026-10-29 기준 Gemini 앱·API·Enterprise 모두 미제공이라는 서술 |
| 가격 | 소개가 $2 / $10 보도 | [부분] 단일 출처 | aicybr 등 | 공개 API에 없는 모델의 가격이라 근거가 약하다 |

## 아직 못 올린 것
- blog.google, ai.google.dev가 이 환경에서 열리지 않아 공식 모델 페이지, 요금표, changelog 본문은 읽지 못했다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.
- 사양(컨텍스트, 출력, 요금)은 쓰지 않는다. 출시 전에 모델 ID를 코드에 박지 않는다.

## 출처
- [googleapis/python-genai CHANGELOG](https://raw.githubusercontent.com/googleapis/python-genai/main/CHANGELOG.md)
- [betanews](https://betanews.com/article/gemini-4-carbon-cyber-defenders/)
- [techrepublic](https://www.techrepublic.com/article/news-google-gemini-4-carbon-access/)
- [letsdatascience](https://letsdatascience.com/news/google-announces-gemini-4-carbon-limiting-first-access-to-cy-f33fd14e)
- [smartscope](https://smartscope.blog/en/blog/gemini-4-carbon-availability-release-date-differences-argon-2026/)
- [Google 블로그 (열리지 않음)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
