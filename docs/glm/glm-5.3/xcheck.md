# GLM-5.3 — 교차 확인
> 제공자: Z.ai (Zhipu) · 모델 ID: `glm-5.3` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/glm/glm-5.3/general.md`](../../../md/glm/glm-5.3/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- zai-org/GLM-5 README: 다운로드 표에 GLM-5.3(744B-A40B)과 GLM-5.3-Flash(320B-A18B)가 있고 Hugging Face·ModelScope의 BF16·FP8 가중치를 링크한다. GLM-5.2에는 '1M 토큰 컨텍스트' 서술이 있다. 저장소 라이선스는 Apache-2.0이다(코드 기준일 수 있음). GLM-5.5는 언급되지 않는다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 파라미터 | 744B 총 / 40B 활성 | [확인] 1차 | zai-org/GLM-5 README | GLM-5.2·5.1·5도 같은 표기 |
| 발표 / 가중치 | 발표 2026-08-14(또는 08-18), 가중치 08-28~29 | [부분] 상충 | 여러 2차, gigazine(2026-08-29) | 발표일이 14일과 18일로 갈린다 |
| 가격 (입력/출력) | $1.40 / $4.40 | [부분] 단일 출처 | 2차 비교 글 | GLM-5.2와 같은 가격이라는 서술 |
| 컨텍스트 | 1M | [부분] 2차 3곳 일치 | 여러 2차 | GLM-5.2의 1M 서술은 1차에도 있다 |
| 라이선스 | 저장소 Apache-2.0(1차, 코드) / 가중치는 커스텀 'GLM-5.3 License'(Copyright (c) 2026 Z.AI) | [부분] 2차 3곳 일치 | letsdatascience, issoh.co.jp, developersdigest (+ 검색에 잡힌 Hugging Face LICENSE 링크) | GLM-5.2·5.3-Flash는 MIT, 5.3은 아니라는 대비. 상업 이용은 조건부 허용. 연매출 100억 달러 기준은 한 곳 서술뿐이고 LICENSE 원문을 읽지 못해 단정하지 않는다 |

## 아직 못 올린 것
- docs.z.ai, huggingface.co가 이 환경에서 열리지 않았다. 가중치 라이선스는 원문 확인 전까지 상충으로 둔다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [zai-org/GLM-5 README](https://github.com/zai-org/GLM-5)
- [datanorth (Flash)](https://datanorth.ai/news/z-ai-releases-glm-5-3-flash)
- [datacamp (Flash)](https://www.datacamp.com/blog/glm-5-3-flash)
- [llmgateway (Flash)](https://llmgateway.io/models/glm-5.3-flash)
- [gigazine (5.3 가중치)](https://gigazine.net/gsc_news/en/20260829-glm-5-3-open/)
- [letsdatascience (Flash MIT)](https://letsdatascience.com/news/zai-releases-glm-53-under-conditional-license-fa46b61b)
- [Hugging Face GLM-5.3 LICENSE (검색에만 잡힘)](https://huggingface.co/zai-org/GLM-5.3/blob/935644c05e76fc198714f4cca449fd8b970ff6d7/LICENSE)
- [cloudprice (5.3)](https://cloudprice.net/models/zai-org/GLM-5.3)
