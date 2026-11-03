# Gemma 4 31B — 출처와 한계
> 제공자: Google · 모델 ID: `google/gemma-4-31B-it` (저장소 이름은 검색 결과의 표기 기준, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemma/gemma-4-31b/general.md`](../../../md/gemma/gemma-4-31b/general.md)
> 소제목의 번호(2.x)는 주제별로 나누기 전 일반 조사 기록의 번호다. 문장 속 `§2.x`는 그 번호를 가리킨다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 크기·메모리·컨텍스트·라이선스·샘플링 | [Gemma 4 model overview](https://ai.google.dev/gemma/docs/core), [Gemma 4 locally, which size fits your GPU](https://jacar.es/en/gemma-4-locally-with-ollama/), [Gemma 4 hardware requirements (Yotta Labs)](https://www.yottalabs.ai/post/gemma-4-hardware-requirements-gpu-memory-2026) (스니펫만) | [부분] |
| KV 캐시·구조 분석 | [Kaitchup: Gemma 4 31B and 26B A4B 구조와 메모리](https://kaitchup.substack.com/p/gemma-4-31b-and-26b-a4b-architecture) (이 환경에서 본문이 열리지 않아 스니펫만) | [부분] |
| 독립 지수(2026-04 및 이후 버전) | [Artificial Analysis: Gemma 4](https://artificialanalysis.ai/articles/gemma-4-everything-you-need-to-know), [26B A4B vs 31B 비교](https://artificialanalysis.ai/models/comparisons/gemma-4-26b-a4b-vs-gemma-4-31b) (스니펫만) | [부분, 충돌] |
| 벤치마크 집계(LiveCodeBench·τ²·Terminal-Bench·SWE-bench 불일치) | [DataLearner 분석](https://www.datalearner.com/en/ai-models/pretrained-models/google-gemma-4-31b/analysis), [BenchLM 비교](https://benchlm.ai/compare/gemma-4-31b-vs-glm-4-5) | [부분: 집계 사이트] |
| Qwen3.6 27B와의 후기 비교·메모리 보고 | [HN 스레드](https://hn.nuxt.dev/item/48385906), [Brian Lovin HN](https://brianlovin.com/hn/47960507) | [부분: 개인 후기] |
- 공식 모델 카드 본문을 열지 못했다. 모델 ID 표기는 검색 결과에서 가져온 것이다.
- 비교 후기는 개인 경험이며 런타임·양자화·프롬프트에 따라 달라진다.
