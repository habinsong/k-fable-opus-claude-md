# Qwen3.8-2.4T-A95B — 교차 확인
> 제공자: Alibaba (Qwen) · 모델 ID: `qwen3.8-2.4t-a95b` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.8-2.4t-a95b/general.md`](../../../md/qwen/qwen3.8-2.4t-a95b/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- QwenLM/Qwen3.6 README의 모델 표(공식): 모델 이름과 출시일 목록. 저장소 라이선스는 Apache-2.0이고 가중치 라이선스는 'Hugging Face·ModelScope의 모델과 함께 놓인 라이선스 파일'을 보라고 적는다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 출시일 (가중치) | 2026-08-12 | [확인] 1차 + [부분] 2차 1곳 일치 | QwenLM/Qwen3.6 README; runtimewire | 2차의 08-12~13 서술과 일치 |
| 규모 | 총 2.4T / 활성 95B | [확인] 1차 (이름에서 읽음) | README 모델 이름 | README는 수치를 이름으로만 나타낸다 |
| 컨텍스트 / 모달리티 | 네이티브 262,144, 텍스트 전용, thinking 필수 | [부분] 단일 출처 | runtimewire | Max API의 비전과 1M 컨텍스트는 이 체크포인트에 없다는 서술 |
| 라이선스 | Alibaba 맞춤 'Qwen3.8-Max' 라이선스 (Apache 2.0 아님). 해당 서비스를 제공하는 기업이 12개월 합산 매출 5천만 달러를 넘으면 별도 라이선스가 필요하다는 서술 | [부분] 2차 2곳 일치 | eWeek, runtimewire | 매출 기준은 eWeek 한 곳의 서술이다. 라이선스 원문을 읽지 못해 조건을 단정하지 않는다 |

## 아직 못 올린 것
- huggingface.co가 이 환경에서 열리지 않아 라이선스 원문을 읽지 못했다. 상업 이용 조건을 단정하지 않는다.
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
