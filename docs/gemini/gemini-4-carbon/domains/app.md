# Gemini 4 Carbon · 앱 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/app.md`](../../../../md/gemini/gemini-4-carbon/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용 (잠정)
2026-11-03 기준 Carbon은 사이버 방어 조직 일부에게만 제한 공개돼 있고 일반 개발자는 쓸 수 없다. 모델 상태와 일반 공개 시 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 일반 접근에서는 `gemini/gemini-4-argon/app.md`를 적용한다.

**접근 권한이 있는 조직이 앱 작업에 쓸 때**
- 모바일 앱 개발에 대한 정보는 없다. [미확인] 앱 보안 점검(권한 남용, 토큰 저장, 서드파티 SDK의 수집 데이터)에 쓰는 경우에도 점검 범위를 자사 앱과 승인된 대상으로 한정한다.
- 서명 키, 프로파일, 스토어 제출·배포는 모델이 바뀌어도 사람이 승인한 뒤에만 한다(§1.6).

**일반 공개 시 앱 작업에서 따로 확인할 것**
- 안드로이드 도구(Android Studio)·Antigravity CLI에서 쓸 수 있는지, 접근 등급이 어떤지.
- 컴퓨터 사용(프리뷰)의 지원 범위와 시뮬레이터 조작 성공률. 벤더 수치가 아닌 자체 과제로 측정한다.
- 스토어 정책 같은 최신 사실의 grounding 정확도. 출처를 직접 열어 확인한다.
- 입출력 통합 한도에서 빌드 로그와 생각 토큰이 쓰는 몫.

## 4. 근거와 한계
- 접근 단계: [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) (검색 스니펫만) [부분]
- 잠정 규칙: 같은 저장소의 `gemini/gemini-4-argon/app.md`.
- 한계: Carbon의 앱 개발 성능에 대한 정보는 없다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
