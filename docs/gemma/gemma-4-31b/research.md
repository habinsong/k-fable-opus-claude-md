# Gemma 4 31B · 연구 (로컬) — 조사 기록
> 제공자: Google · 모델 ID: `google/gemma-4-31B-it` (Hugging Face 토론 URL에서 확인한 표기, 본문은 열지 못함) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemma/gemma-4-31b/research.md`](../../../md/gemma/gemma-4-31b/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 밀집 약 31B, AIME 2026 89.2%·GPQA Diamond 84.3%·MMLU-Pro 85.2%(추론 모드, 도구 없음, 모델 카드를 인용한 2차 출처), 독립 지수 39(2026-04 버전, 이후 척도 충돌), 연구 보조 독립 평가 없음.

- **연구의 추론과 인용은 이 모델에 맡기지 않는다.** 수학·과학 문제 점수는 높게 보도됐으나 모델 카드를 인용한 2차 출처 수치이고 추론 모드·도구 없음 조건이다. [부분] 같은 점수대의 경쟁 모델(Qwen 3.5 27B: GPQA Diamond 85.5%, MMLU-Pro 86.1%)이 있어 변별력도 크지 않다. 시험 문제 풀이 점수는 가설 설계, 통계 해석, 문헌 종합의 정확도를 대신하지 않는다. 새 가설·증명·통계 해석은 `gemini-4-argon`, `claude/opus-5.5`, `gpt-6-astra` 문서를 따르고 전문가 검토를 거친다. 연구 보조 정확도에 대한 독립 평가는 찾지 못했다. [미확인]
- **참고문헌을 만들거나 보충하게 하지 않는다.** 26개 LLM 연구에서 검증 가능한 참고문헌 중 모든 필드가 맞은 비율은 48.3%였고 저자 목록이 가장 약했다(51.7%). 이 모델의 별도 측정은 찾지 못했다. [부분/미확인] 모든 인용은 Crossref·DataCite·원문에서 제목·저자·연도·권호와 주장의 실제 존재를 확인한다(§3.2).
- **써도 되는 작업.** 서지 정보 서식 변환, 실험 로그·메타데이터 정리, 표 형식 변환, 논문 초록에서 정해진 필드 추출, 분석 스크립트(파이썬)의 초안, 개인정보가 섞인 자료의 형식 점검. "원문에 없으면 null"을 명시하고 추출값은 원문과 한 건씩 대조한다. 분석 스크립트는 알려진 입력과 결과로 먼저 시험한다.
- **수학·정량 풀이는 코드로 재검산한다.** 추론 모드로 푼 풀이도 결과가 틀릴 수 있다. 식은 스크립트·기호 계산 도구로 다시 계산하고, 단계를 사람이 읽는다.
- **로컬 실행의 이점은 데이터 보호다.** 미공개 데이터나 개인 식별 정보를 외부 API로 보내지 않고 정리에 쓸 수 있다. 정확도를 보증하지는 않는다. 사람 대상 자료는 연구 윤리 심의와 개인정보 동의 범위를 먼저 확인한다(§3.3).
- **분석 결과를 모델 설명으로 대체하지 않는다.** 통계는 코드를 다시 실행해서 확인한다. 시드, 데이터 버전, 라이브러리 버전을 기록하고, 이상치 제거·필터·검정 기준이 결과에 맞춰 바뀌지 않았는지 `git diff`로 확인한다.
- **긴 논문 묶음은 발췌한다.** 컨텍스트가 256K지만 전체 컨텍스트의 KV 캐시가 약 20 GiB(bf16 추정)까지 가고 속도도 느리다(약 3.4 토큰/초, 한 기기 측정). 논문 한 편씩, 필요한 구간만 넣는다. 종합과 반증 탐색은 상위 모델이나 사람이 한다. [부분]
- **전문 영역(의료, 법률, 안전) 결론에는 "전문가 검토 필요"를 붙인다.**

## 4. 근거와 한계
- 벤치마크(모델 카드 인용, 추론 모드·도구 없음)와 Qwen 3.5 비교: [DataLearner: Gemma 4 31B](https://www.datalearner.com/en/ai-models/pretrained-models/gemma-4-31b), [Gemma 4 benchmarks (gemma4all)](https://gemma4all.com/blog/gemma-4-benchmarks-performance), [AI Brew: Gemma 4 31B](https://aibrew-io.pages.dev/en/models/gemma-4-31b) [부분: 2차]
- 독립 지수(버전 충돌): [Artificial Analysis: Gemma 4](https://artificialanalysis.ai/articles/gemma-4-everything-you-need-to-know), [26B A4B vs 31B 비교](https://artificialanalysis.ai/models/comparisons/gemma-4-26b-a4b-vs-gemma-4-31b) (스니펫만) [부분, 충돌]
- 참고문헌 정확도(타 모델 포함): [Biomedical Reference Generation Remains Unreliable across 26 LLMs](https://arxiv.org/pdf/2609.14988) [부분]
- 한계: 이 모델의 연구 보조 정확도를 측정한 독립 자료가 없다. 모델 카드 원문을 열지 못해 벤치마크 조건은 2차 출처를 따랐다.
