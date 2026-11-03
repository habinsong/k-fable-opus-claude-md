# Gemini 4 Carbon · 연구 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/research.md`](../../../../md/gemini/gemini-4-carbon/research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/research.md`](../../../_common/domain-rules/research.md)

## 2. 이 모델의 연구 작업 운용 (잠정)
2026-11-03 기준 Carbon은 사이버 방어 조직 일부에게만 제한 공개돼 있고 일반 개발자는 쓸 수 없다. 모델 상태와 일반 공개 시 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 일반 접근에서는 `gemini/gemini-4-argon/research.md`를 적용한다.

**접근 권한이 있는 조직이 연구에 쓸 때**
- 연구 보조 능력에 대한 정보는 없다. [미확인] 지수 1위(59)는 Google이 인용한 종합 점수이고 연구 용도 정확도를 뜻하지 않는다.
- **방어·학술 연구의 윤리와 책임.** Fairwind 파트너의 허용 범위는 방어·학술 연구 목적의 이중 용도 작업이다. [부분] 사람 대상 자료, 개인정보, 취약점 정보의 공개·보고(책임 있는 공개) 절차는 연구 윤리 심의와 소속 기관 정책을 따르고, 모델이 판단하거나 실행하지 않는다.
- 취약점 연구의 재현성: 사용한 대상 버전, 환경, 입력, 코드 버전, 난수 시드를 기록하고, 모델이 만든 재현 절차는 격리된 환경에서 사람이 다시 실행해 확인한다. 안전장치 없이 측정된 벤치마크 수치를 연구 결과로 인용할 때는 "벤더 보고, 안전장치 없는 조건"으로 표기한다.
- 인용은 필드 단위로 검증한다. 26개 LLM 연구에서 모든 필드가 맞은 참고문헌 비율은 48.3%였고 저자 목록이 가장 약했다. Carbon의 별도 측정은 없다. [부분/미확인]

**일반 공개 시 연구 작업에서 따로 확인할 것**
- 입출력 통합 한도에서 긴 논문 묶음의 세부 연결 정확도.
- 열린 과학 추론과 통계 해석의 오류율. 알려진 정답이 있는 문제로 자체 측정한다.
- 생성 텍스트의 출처 표기·워터마크 정책과 투고 대상 학술지·arXiv의 AI 사용 정책.

## 4. 근거와 한계
- 접근·허용 범위: [Fairwind Program](https://deepmind.google/fairwind-program/), [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) (검색 스니펫만) [부분]
- 참고문헌 정확도(타 모델 포함): [Biomedical Reference Generation Remains Unreliable across 26 LLMs](https://arxiv.org/pdf/2609.14988) [부분]
- 한계: Carbon의 연구 보조 능력에 대한 정보는 없다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
