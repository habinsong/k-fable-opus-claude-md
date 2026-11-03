# Claude Fable 5.5 · 기술 연구 (미출시 대비) — 조사 기록
> 제공자: Anthropic · 모델 ID: 미정(공식 확인 전 [미확인]) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.5/tech-research.md`](../../../../md/claude/fable-5.5/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때 (잠정)
2026-11-03 기준 Fable 5.5는 공식 목록에 없다. 모델 상태와 출시일 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 출시 전에는 `claude/fable-5.1/tech-research.md`를 적용한다.

**도입 후보로 평가할 때 (출시 후)**
- **Anthropic의 선택 기준이 바뀌었는지.** 지금은 "대부분 Opus 5.5로 시작하고, 어려운 추론·장시간 작업이거나 Opus 5.5의 높은 effort로도 기준에 못 미칠 때 Fable"이다. 5.5가 나온 뒤 이 문구와 모델 간 위치가 어떻게 바뀌는지 모델 목록에서 확인한다.
- **비용.** Fable 5.1은 입력 $10 / 출력 $50, 캐시 읽기 $0.25였다. 5.5의 가격, 캐시 요금, 배치 요금, 토크나이저 변경으로 인한 토큰 수 변화를 확인한다. 작업당 토큰 사용이 Astra 대비 3배 가까이 크다는 Fable 5.1에 대한 보고가 있었으므로, 5.5도 같은 과제로 작업당 총비용을 직접 비교한다.
- **이행 비용.** Fable 5에서 5.1로 올 때도 4가지가 깨졌다(강제 도구 호출, 추론 블록의 모델 결합, 이력 편집 시 무효화, 어드바이저 조합 제한). 5.5의 이행 가이드에서 깨지는 변경 목록을 먼저 읽는다. 모델을 바꾸면 이전 모델의 추론이 사라지는 구조도 확인한다.
- **데이터 요건.** Fable 5.1은 30일 보관, ZDR 비대상이었다. 5.5의 보관·ZDR·Covered Model 지정을 확인한다.
- **가용성.** 가장 높은 사이버 능력이 검증된 조직 전용 연계 모델(Mythos 계열)에만 있는지, 5.5에도 연계 모델이 있는지.
- **독립 측정.** 출시 직후 벤더 수치와 첫 주 리뷰는 같은 수치를 반복한다. Artificial Analysis 같은 독립 측정이 나온 뒤, 지표와 하네스를 확인해서 읽는다. Fable 5.1에서도 같은 기관 안에서 지표에 따라 순위가 갈렸다.
- **루머로 결정하지 않는다.** 공식 발표 전에는 Fable 5.1과 Opus 5.5로 평가한다.

**라이선스·규정**
- 모델 출력 사용권, 데이터 사용 정책, 텍스트 워터마크 같은 조건이 5.5에서 바뀌었는지 약관과 모델 문서로 확인한다. 규제 인증 여부는 계약·인증 문서로 직접 확인한다.

## 4. 근거와 한계
- 미출시 확인: [Models overview](https://platform.claude.com/docs/en/models/overview), [anthropic.com/news/models](https://www.anthropic.com/news/models) [확인: 2026-11-03에 직접 읽음]
- 직전 모델의 비용·이행·보관 조건: [What's new in Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1), [Artificial Analysis: Benchmarking GPT-6 Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) [확인/부분: Fable 5.1 기준]
- 한계: 이 문서의 모든 5.5 관련 서술은 확인 항목 목록이며 모델 특성이 아니다.
