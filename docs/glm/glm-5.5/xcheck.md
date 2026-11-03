# GLM-5.5 (미출시) — 교차 확인
> 제공자: Z.ai (Zhipu) · 모델 ID: `glm-5.5(미확인)` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/glm/glm-5.5/general.md`](../../../md/glm/glm-5.5/general.md)

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
| 공식 저장소에 있는가 | 없음 | [확인] 1차 (부재 확인) | zai-org/GLM-5 README | 다운로드 표의 최신은 GLM-5.3-Flash |
| 릴리스 노트 | 최신 항목은 GLM-5.3-Flash(08-26), glm-5.5 문서·블로그 URL은 404 | [부분] 2차 2곳 일치 (부재) | evolink.ai, dev.to 추적 글 | 2026-10 중순까지의 서술 |
| 8월 출시 전망 | JPMorgan 분석 인용 보도(Reuters·CGTN 경유) | [부분] 단일 출처 | 2차 | 예측이지 Z.ai 확약이 아니다. 8월은 이미 지났고 출시 근거는 없다 |

## 아직 못 올린 것
- 사양을 쓰지 않는다. 출시 전에 모델 ID를 코드에 박지 않는다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [zai-org/GLM-5 README](https://github.com/zai-org/GLM-5)
- [evolink.ai](https://evolink.ai/blog/glm-5-5-release-date)
- [dev.to 추적](https://dev.to/tokenmixai/i-traced-9-glm-55-claims-august-looks-real-the-1t-spec-sheet-doesnt-p65)
