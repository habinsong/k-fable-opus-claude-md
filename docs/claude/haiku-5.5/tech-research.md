# Claude Haiku 5.5 · 기술 연구 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/haiku-5.5/tech-research.md`](../../../md/claude/haiku-5.5/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 가장 싼 티어, 정답 비율 36%, `max`는 비쌈, 프롬프트 약 10만 토큰 이상에서 가격 상승 보고, 서버 쪽 대체 없음.

**이 모델에게 기술 조사를 시킬 때**
- **분류·정리 단계에만 쓴다.** 후보 수십~수백 개를 정해진 기준(라이선스 유형, 지원 언어, 최근 릴리스 날짜)으로 분류해 표로 만드는 일은 용도에 맞는다. 값은 사람이 이미 확보한 1차 자료 텍스트에서 추출하게 하고, 원문에 없으면 null로 둔다. 모델의 기억으로 채우지 않는다.
- **판단은 맡기지 않는다.** 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2). 사람이나 상위 모델이 근거를 보고 판단한다.
- 추출 결과는 무작위 5~10%를 원문과 대조하고, 오류율이 기준을 넘으면 Sonnet 5.5로 올린다.

**Haiku 5.5를 도입 후보로 평가할 때**
- **비용은 effort가 좌우한다.** 입력 $0.10부터 / 출력 $0.50부터(100만 토큰당)이고 입력이 Sonnet 5.5의 약 20분의 1이다. 그러나 `max`에서는 토큰을 많이 써서 벤치마크 작업당 비용이 GPT-6 Luna의 약 3배였다. 프롬프트가 약 10만 토큰을 넘으면 가격이 오른다는 지적이 있다. 토크나이저는 Haiku 4.5보다 같은 글에서 약 30% 더 많은 토큰을 낸다. [확인: 가격 표기·토크나이저 / 부분: 비교·임계값] "정답으로 확인된 결과 한 건당 비용"으로 비교한다.
- **지수와 지식.** Artificial Analysis 지능 지수는 `max` 43, `medium` 34(Haiku 4.5는 17)이고 AA-Omniscience 정답 비율은 36%다. Gemini 3.8 Flash 55%, GPT-6 Luna 44%보다 낮다. [부분] 같은 가격대 후보와 같은 과제로 비교한다.
- **Sonnet 5.5와의 격차.** Terminal-Bench 4.0 39.2% 대 70.6%(Anthropic 수치), OSWorld 2.1 72.4% 대 83.9%. 하위 에이전트로 쓸 때는 Sonnet 5.5가 오케스트레이터인 구조에서 비용을 비교한다. [부분]
- **이행 비용.** Haiku 4.5에서 올 때 깨지는 변경이 5가지다: `budget_tokens`, 샘플링 파라미터, 프리필, `computer_20250124`, 이력 편집으로 인한 추론 블록 무효화. 이전 턴의 추론 블록이 컨텍스트에 남아 다중 턴 입력 토큰이 늘어난다. [확인]
- **서버 쪽 대체가 없다.** 안전장치 거부는 클라이언트에서 처리해야 한다. [확인]
- **데이터 요건.** Haiku 5.5의 데이터 보관·ZDR 조건은 이 조사에서 확인하지 못했다. 도입 전에 Anthropic의 모델별 데이터 보관 문서로 확인한다. [미확인]

## 4. 근거와 한계
- 가격 표기·이행 변경·거부: [What's new in Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5), [Models overview](https://platform.claude.com/docs/en/models/overview) [확인]
- 비용·지수·정답 비율·격차: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Beam](https://beam.ai/agentic-insights/claude-haiku-5-5-subagents), [DataCamp](https://www.datacamp.com/blog/claude-haiku-5-5), [Miraflow](https://miraflow.ai/blog/claude-haiku-5-5-benchmarks-pricing-explained-2026) [부분]
- 한계: 공식 장문 요금 페이지와 데이터 보관 조건은 열어 보지 않았다. 도입 결정 전에 다시 확인한다.
