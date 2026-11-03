# GPT-6 Astra · 연구 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/research.md`](../../../../md/gpt/gpt-6-astra/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 추론 과정 설명을 근거로 쓸 수 없고, 자기 평가가 틀릴 수 있으며, 인용 환각이 남아 있다.

- **참고문헌은 필드 단위로 검증한다.** 26개 LLM을 비교한 2026년 연구에서 검증 가능한 참고문헌 중 모든 필드가 맞은 비율은 48.3%였고, 저자 목록이 가장 약했다(51.7%). Astra에 대한 한 측정은 지어낸 DOI 비율이 3.0%(이전 모델 8.8%)라고 하나, 검색 없이 측정했고 신뢰구간이 넓으며 독립 재현이 없다. [부분]
  → DOI가 존재하는지만 보지 않고, Crossref·DataCite 또는 원문에서 제목·저자 목록·연도·권호가 맞는지, 인용한 주장이 해당 논문에 실제로 있는지 확인한다. 이 확인을 마치지 못한 항목은 목록에서 분리한다.
- **분석 결과는 코드를 다시 실행해서 확인한다.** 시스템 카드는 이전 모델 대비 추론 과정의 모니터링 가능성이 크게 줄었다고 인정했다. [부분] 그래서 모델이 쓴 추론 설명이나 "검토했다"는 문장을 분석의 근거로 삼지 않는다. 데이터, 코드 버전, 시드, 명령 출력으로 재현 가능해야 채택한다.
- **마케팅 주장을 연구 근거로 인용하지 않는다.** "AGI 시대" 같은 OpenAI의 주장은 외부 비평가들이 의문을 제기했고, ARC-AGI-3 99.9% 등은 벤더 수치다. [부분] 보고서에서는 "OpenAI 주장"으로 표기하거나 쓰지 않는다.
- **전문 영역은 전문가 검토 필요를 명시한다.** 법률·생의학 연구 용도의 가이드들은 Astra가 여전히 참고문헌을 만들어내거나 주장을 잘못 귀속할 수 있다고 경고한다. [부분] 생의학·법률 결론에는 "전문가 검토 필요"를 붙인다.
- **한계를 먼저 적는다.** 이 모델은 상세하고 서식이 많은 답을 내는 경향이 있다. 한계 항목(표본, 측정, 일반화, 사용한 모델·도구의 한계)을 결과 앞에 두고, 항목당 1~2문장으로 쓴다.

## 4. 근거와 한계
- 참고문헌 정확도: [Biomedical Reference Generation Remains Unreliable across 26 LLMs](https://arxiv.org/pdf/2609.14988), [GPT-6 Astra Hallucination Rate, Measured](https://truestandard.ai/releases/gpt-6-astra) [부분]
- 연구 용도 주의: [GPT-6 Astra for Research](https://www.layer3labs.io/guides/gpt-6-astra-for-research), [LiveScience](https://www.livescience.com/technology/artificial-intelligence/openai-claims-weve-entered-the-agi-era-has-gpt-6-astra-really-demonstrated-general-intelligence) [부분]
- 한계: Astra의 연구 보조 정확도를 통제된 조건에서 측정한 독립 자료는 찾지 못했다. 논문 사본과 원자료로 직접 검증하기 전에는 이 모델의 문헌 요약을 1차 근거로 쓰지 않는다.
