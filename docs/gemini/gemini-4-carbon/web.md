# Gemini 4 Carbon · 웹 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/web.md`](../../../md/gemini/gemini-4-carbon/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용 (잠정)
2026-11-03 기준 Carbon은 사이버 방어 조직 일부에게만 제한 공개돼 있고 일반 개발자는 쓸 수 없다. 모델 상태와 일반 공개 시 체크리스트는 같은 폴더의 `general.md` §2를 따른다. 일반 접근에서는 `gemini/gemini-4-argon/web.md`를 적용한다.

**접근 권한이 있는 조직이 웹 작업에 쓸 때**
- Carbon은 장시간 엔지니어링과 사이버 방어에 강하다고 소개된다. [부분: 벤더 서술] 웹 서비스에서는 인가·입력 검증·공급망 같은 취약점 점검과 패치 후보 제안에 맞다. 제안된 패치는 기능 테스트와 회귀 테스트로 확인하고, 모델이 "고쳤다"고 말한 것을 근거로 삼지 않는다.
- 취약점 점검 대상은 자사 서비스와 승인된 범위로 한정한다. 승인되지 않은 대상의 점검, 외부 시스템에 대한 시험은 하지 않는다. 외부 전송·배포는 사람이 승인한 뒤에만 한다(§1.6).
- UI 구현 품질에 대한 정보는 없다. [미확인] 화면 구현은 일반적인 모델(Argon, Opus 5.5)과 같은 과제로 비교한 뒤 정한다.

**일반 공개 시 웹 작업에서 따로 확인할 것**
- 함수 호출 하네스의 thought signature 요건과 `thinking_level` 범위가 Argon과 같은지.
- Argon에서 지적된 자기 검증 약점(변경 후 검사 후 되돌아가 고치기)이 개선됐는지 같은 과제로 비교한다.
- 가격이 Argon의 인상 후 가격($4/$20)과 어떻게 다른지, 웹 반복 작업에 쓸 만한 비용인지.

## 4. 근거와 한계
- 접근 단계·소개: [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Fairwind Program](https://deepmind.google/fairwind-program/) (검색 스니펫만) [부분]
- 잠정 규칙: 같은 저장소의 `gemini/gemini-4-argon/web.md`.
- 한계: Carbon의 웹 작업 성능에 대한 정보는 없다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
