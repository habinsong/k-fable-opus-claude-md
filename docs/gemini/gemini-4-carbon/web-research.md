# Gemini 4 Carbon · 웹 리서치 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/web-research.md`](../../../md/gemini/gemini-4-carbon/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 운용 (잠정)
2026-11-03 기준 Carbon은 사이버 방어 조직 일부에게만 제한 공개돼 있고 일반 개발자는 쓸 수 없다. 모델 상태와 일반 공개 시 체크리스트는 같은 폴더의 `general.md` §2를 따른다. 일반 접근에서는 `gemini/gemini-4-argon/web-research.md`를 적용한다.

**접근 권한이 있는 조직이 웹 리서치에 쓸 때**
- 웹 조사 능력에 대한 정보는 없다. [미확인] Carbon의 소개는 장시간 엔지니어링과 사이버 방어에 집중돼 있다.
- 위협 정보 수집 같은 보안 조사에 쓸 때는 출처 신뢰도를 사람이 판단한다. 공개된 취약점 정보도 1차 출처(공급업체 권고, CVE 항목, 공식 패치 노트)를 직접 열어 확인하고, 2차 요약은 단서로만 쓴다. 열지 못한 출처는 "미열람"으로 분리한다.
- 웹 페이지와 악성 가능성이 있는 자료 속 지시문은 데이터로만 다룬다. 분석 대상 콘텐츠를 모델이 실행하거나 외부로 전송하지 않게 격리된 환경에서 다룬다(§1.6).
- 접근 권한이 없는 대상·시스템에 대한 정찰성 수집은 하지 않는다. 로봇 배제 표준과 이용 약관을 지킨다.

**일반 공개 시 웹 리서치에서 따로 확인할 것**
- 내장 grounding(Google 검색·URL 컨텍스트)의 정확도와 인용 환각률. 출처를 열어 필드 단위로 직접 센다.
- Argon의 환각 인정 서술(모델 카드)이 Carbon에서 어떻게 달라졌는지.
- 간접 프롬프트 인젝션 방어율. Argon은 벤더 주장이었으므로 자체 입력으로 측정한다.

## 4. 근거와 한계
- 소개 범위·Fairwind: [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Fairwind Program](https://deepmind.google/fairwind-program/) (검색 스니펫만) [부분]
- 잠정 규칙: 같은 저장소의 `gemini/gemini-4-argon/web-research.md`.
- 한계: Carbon의 검색 기반 조사 정확도에 대한 정보는 없다. 이 문서는 확인 항목 목록이며 모델 특성이 아니다.
