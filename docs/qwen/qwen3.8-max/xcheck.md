# Qwen3.8-Max — 교차 확인
> 제공자: Alibaba (Qwen) · 모델 ID: `qwen3.8-max` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.8-max/general.md`](../../../md/qwen/qwen3.8-max/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- QwenLM/Qwen3.6 README 모델 표에 Qwen3.8-Max는 없다(호스팅 모델). 같은 표에서 Qwen3.8 오픈 웨이트는 2.4T-A95B와 27B 두 개다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 프리뷰 / 출시 | 2026-07-19 / 2026-08-03 | [부분] 2차 3곳 일치 | yottalabs 3건(같은 사이트) | 한 사이트 안의 글이라 독립 출처로 세기 어렵다 |
| 가격 | 입력 $2 / 출력 $6, 캐시 입력 $0.25 | [부분] 단일 출처 (같은 사이트) | yottalabs | 프리뷰 기간 요금은 정가의 약 10%였다는 서술. 현재 요금은 확인 필요 |
| 오픈 웨이트 관계 | Max 자체는 호스팅, 별도로 2.4T-A95B가 2026-08-12 공개 | [확인] 1차 | QwenLM/Qwen3.6 README | 2.4T 체크포인트는 텍스트 전용, 네이티브 컨텍스트 262,144(runtimewire) |

## 아직 못 올린 것
- Alibaba Cloud 공식 문서가 이 환경에서 열리지 않았다.
- 집계 사이트는 같은 원천(OpenRouter 등)을 베낀 것일 수 있어 '곳 수'가 독립성을 보증하지 않는다.

## 출처
- [QwenLM/Qwen3.6 README](https://github.com/QwenLM/Qwen3.6)
- [yottalabs (3.8 Max)](https://www.yottalabs.ai/post/qwen-3-8-max-release-date-specs-how-to-access-2026)
- [runtimewire (2.4T)](https://runtimewire.com/article/alibaba-qwen38-24t-open-weights-enterprise-license)
- [orcarouter (27B)](https://www.orcarouter.ai/blog/qwen-3-8-27b-release-date)
- [eWeek (27B Apache 2.0)](https://www.eweek.com/news/alibaba-qwen3-8-27b-license-apac-china/)
- [morphllm (27B)](https://www.morphllm.com/qwen-3-8)
- [llm-stats 비교(3.6)](https://llm-stats.com/models/compare/qwen3.6-27b-vs-qwen3.6-35b-a3b)
- [llmreference (3.6)](https://www.llmreference.com/compare/qwen3.6-35b-a3b/qwen3.6-27b)
- [yottalabs (3.7 Max)](https://yottalabs.ai/post/qwen-3-7-max-release-date-features-open-source-status-and-how-to-access-2026)
