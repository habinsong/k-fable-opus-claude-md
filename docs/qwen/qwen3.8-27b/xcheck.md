# Qwen3.8-27B — 교차 확인
> 제공자: Alibaba (Qwen) · 모델 ID: `qwen3.8-27b` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.8-27b/general.md`](../../../md/qwen/qwen3.8-27b/general.md)

`overview.md`에서 [부분]이던 사양을 공식 문서 말고 다른 출처로 다시 맞춰 본 기록이다. 2026-11-03에 웹 검색 여러 건과 공식 GitHub 저장소 읽기로 했다. 여기서 [확인]은 제공자의 공식 문서나 공식 저장소를 이 환경에서 직접 읽었다는 뜻이다.

## 읽는 법
- **[확인] 1차**: 공식 문서, SDK 변경 기록, 공식 README, 공식 코드를 직접 읽음.
- **[부분] 2차 N곳 일치**: 서로 다른 2차 출처 N곳이 같은 값을 적음. 1차를 못 읽었으므로 [확인]으로 올리지 않는다.
- **[부분] 상충 / 단일 출처**: 값이 갈리거나 한 곳에만 있음. **[미확인]**: 찾지 못함.

## 1차 출처에서 읽은 것
- QwenLM/Qwen3.6 README의 모델 표(공식): 모델 이름과 출시일 목록. 저장소 라이선스는 Apache-2.0이고 가중치 라이선스는 'Hugging Face·ModelScope의 모델과 함께 놓인 라이선스 파일'을 보라고 적는다.
- 같은 README의 serve 명령이 `--context-length 262144`(SGLang), `--max-model-len 262144`(vLLM)를 쓴다. `reasoning_effort`와 `preserve_thinking` 옵션도 적혀 있다.

## 교차 확인 표
| 항목 | 값 | 상태 | 출처 | 비고 |
|---|---|---|---|---|
| 가중치 공개일 | 2026-08-14 | [확인] 1차 | QwenLM/Qwen3.6 README | 2차는 '08-03 발표, 한 주 안 공개'(약속)와 '약속한 주가 지나도 안 나왔다'로 갈렸으나 1차가 08-14로 정리한다 |
| 컨텍스트 | 262,144 | [확인] 1차 | README serve 명령 | 서빙 설정값이므로 모델 최대치와 같다는 보증은 아니다 |
| 라이선스 | Apache 2.0 | [부분] 2차 3곳 일치 (1차는 저장소 라이선스와 '가중치 파일 참조'만) | morphllm(저장소에 Apache 2.0 전문), eWeek, orcarouter | 이전 orcarouter 글의 '미지정'은 공개 전 서술이라 낡았다. 모델 카드 원문은 읽지 못함 |
| 컨텍스트 (네이티브) | 262,144 (최대 1M 확장 서술) | [부분] 2차 2곳 일치, 일부 상충 | morphllm, README serve 명령 / haimaker.ai는 131,072 | 목록 사이트의 131,072는 모델 카드와 맞지 않는 값으로 보인다 [추정] |

## 아직 못 올린 것
- huggingface.co가 이 환경에서 열리지 않아 라이선스 원문을 읽지 못했다.
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
