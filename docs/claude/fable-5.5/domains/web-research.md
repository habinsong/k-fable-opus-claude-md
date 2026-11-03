# Claude Fable 5.5 · 웹 리서치 (미출시 대비) — 조사 기록
> 제공자: Anthropic · 모델 ID: 미정(공식 확인 전 [미확인]) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.5/web-research.md`](../../../../md/claude/fable-5.5/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 운용 (잠정)
2026-11-03 기준 Fable 5.5는 공식 목록에 없다. 모델 상태와 출시일 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 출시 전에는 `claude/fable-5.1/web-research.md`를 적용한다.

**출시 후 웹 리서치에서 따로 확인할 것**
- `low` effort의 검색 트리거. Fable 5.1은 낮은 effort에서 검색을 덜 하고 기억으로 답했다. 낯선 이름과 빠르게 바뀌는 분야(AI 모델, 개발 도구)에 대한 질문으로 5.5의 검색 빈도를 센다.
- 요약에서 출처 문장을 따옴표 없이 옮기는 경향. 원문과 겹치는 긴 구절을 검사해 저작권·출처 규칙(§1.5)을 지키는지 확인한다.
- 인용 환각률. DOI·URL·저자·연도·권호를 필드 단위로 검증해 센다. Fable 5.1에 대해서도 독립 측정은 찾지 못했으므로, 5.5의 측정값은 벤더가 아닌 자체 측정으로 만든다.
- 간접 프롬프트 인젝션과 붙여 넣은 글 속 지시에 대한 반응. 표시 태그 유무에 따른 차이를 같은 입력으로 비교한다.
- 진행 알림과 최종 요약. 조사 중간 발견과 독립적으로 읽히는 마지막 요약이 나오는지 확인한다.
- 생성 텍스트의 워터마크·출처 표기 정책이 유지되는지. 투고·제출용 글은 대상 기관의 AI 사용 정책을 따른다.

**잠정 운용**
- 출시 전 조사는 Fable 5.1(`high`)과 Opus 5.5로 진행한다. 핵심 주장은 직접 연 출처 두 곳이나 1차 출처 한 곳으로 확인한다.

## 4. 근거와 한계
- 미출시 확인: [Models overview](https://platform.claude.com/docs/en/models/overview) [확인: 2026-11-03에 직접 읽음]
- 잠정 규칙의 출처: 같은 저장소의 `claude/fable-5.1/web-research.md`, [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) [확인: Fable 5.1 기준]
- 한계: 이 문서의 모든 5.5 관련 서술은 확인 항목 목록이며 모델 특성이 아니다.
