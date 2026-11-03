# Gemini 4 Carbon · 네이티브 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/native.md`](../../../../md/gemini/gemini-4-carbon/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용 (잠정)
2026-11-03 기준 Carbon은 사이버 방어 조직 일부에게만 제한 공개돼 있고 일반 개발자는 쓸 수 없다. 모델 상태와 일반 공개 시 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 일반 접근에서는 `gemini/gemini-4-argon/native.md`를 적용한다.

**접근 권한이 있는 조직이 네이티브 작업에 쓸 때**
- Google이 공개한 벤치마크가 이 분야와 가장 가깝다. 취약점 찾기(SEC-bench Pro 88.2%), 악용(ExploitGym 54.8%), 패치(CWE-bench 71.0%)인데, Google은 이 값이 안전장치 없이 평가한 것이라고 밝혔다. [부분: 벤더 수치] 실제 배포 모델이 같은 정확도를 낸다는 뜻이 아니다.
- 방어 목적의 사용만 한다. 자사 코드의 취약점 점검, 패치 후보 제안, 크래시 분석에 한정하고 악용 코드를 만들거나 외부 시스템에 시험하지 않는다. Fairwind 파트너의 허용 범위는 승인된 위협 시뮬레이션, 리버스 엔지니어링, 방어·학술 연구 목적의 악성코드 분석이다. [부분]
- 모델이 제안한 패치는 sanitizer 빌드와 회귀 테스트로 확인하고, 모델의 "고쳤다"는 설명을 근거로 삼지 않는다. 테스트·경고·sanitizer 설정이 바뀌었는지 `git diff`로 확인한다.
- 시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다.

**일반 공개 시 네이티브 작업에서 따로 확인할 것**
- 일반 접근에서 사이버 작업이 어디까지 거부되는지(거부 범주와 조건). 보호 장치 없이 잰 벤치마크와 배포 모델의 차이를 직접 잰다.
- Argon이 약하다고 평가된 자기 검증(변경 후 검사 후 되돌아가 고치기)이 나아졌는지, Terminal-Bench 같은 지표를 독립 측정으로 확인한다.
- 장시간 작업 중 단계별 테스트 통과 비율과 범위 이탈(`git diff --stat`).

## 4. 근거와 한계
- 사이버 벤치마크·Fairwind 범위: [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Fairwind Program](https://deepmind.google/fairwind-program/) (검색 스니펫만) [부분: 벤더 수치]
- 잠정 규칙: 같은 저장소의 `gemini/gemini-4-argon/native.md`.
- 한계: Carbon의 일반 시스템 코드 작업 성능에 대한 정보는 없다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
