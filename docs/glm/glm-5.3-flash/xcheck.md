# GLM-5.3 Flash — 교차 확인
> 제공자: Z.ai (Zhipu) · 모델 ID: `glm-5.3-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/glm/glm-5.3-flash/general.md`](../../../md/glm/glm-5.3-flash/general.md)

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
| 파라미터 | 320B 총 / 18B 활성 | [확인] 1차 | zai-org/GLM-5 README | 한 2차 글의 수치와 일치 |
| 출시일 | 2026-08-26 (오픈 웨이트) | [부분] 2차 4곳 일치 | datanorth, datacamp, llmgateway, getdeploying |  |
| 가격 (입력/출력) | $0.15 / $0.50 (50% 프로모션이 09-09까지) | [부분] 2차 3곳 일치 | datanorth, llmgateway, pricepertoken | 프로모션 종료 후 값을 확인한다 |
| 컨텍스트 / 최대 출력 | 1M / 약 128~131K | [부분] 2차 3곳 일치 | datacamp, getdeploying, llmgateway | 일부 호스팅 제공자는 더 짧은 컨텍스트를 서비스한다 |
| 라이선스 | MIT (가중치) / 저장소 Apache-2.0(1차, 코드) | [부분] 2차 3곳 일치 | letsdatascience('GLM-5.3 Flash Available Under the MIT License'), developersdigest, datacamp | 저장소 라이선스는 코드 기준이라 가중치와 다를 수 있다. 모델 카드 원문은 읽지 못함 |

## 아직 못 올린 것
- docs.z.ai, huggingface.co가 이 환경에서 열리지 않았다.
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
