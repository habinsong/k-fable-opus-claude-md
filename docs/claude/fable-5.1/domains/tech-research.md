# Claude Fable 5.1 · 기술 연구 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-fable-5-1` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.1/tech-research.md`](../../../../md/claude/fable-5.1/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Anthropic이 직접 "대부분은 Opus 5.5로 시작"을 권하는 상위 티어, ZDR 불가, 토큰 사용이 큼, 순위는 지표마다 다름.

**이 모델에게 기술 조사를 시킬 때**
- 비교표의 모든 칸에 출처와 확인 수준을 붙이게 하고, 직접 열지 않은 출처의 칸은 비워 두게 한다. 최신 정보가 필요한 칸은 `low` effort로 채우지 않는다. 이 모델은 `low`에서 검색을 덜 하고 기억으로 답한다. [확인]
- 라이선스·특허 판단은 단정하지 않는다. SPDX 식별자, 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다(§3.2).
- 요약된 출처 문장은 따옴표 없이 옮겨질 수 있다. 라이선스·저작권 규칙(§1.5)에 따라 직접 인용을 표시하고 나머지는 재서술한다. [확인]

**Fable 5.1을 도입 후보로 평가할 때**
- **Anthropic 자신의 선택 기준.** 대부분은 Opus 5.5로 시작하고, 어려운 추론·장시간 에이전트 작업이거나 Opus 5.5의 높은 effort로도 요건에 못 미칠 때 Fable 5.1을 쓰라고 한다. [확인] 도입 평가는 Opus 5.5를 기준선으로 두고 같은 과제·같은 예산에서 비교한다.
- **비용.** 입력 $10 / 출력 $50(100만 토큰당), 캐시 읽기 $0.25, 배치 $5/$25. 긴 에이전트 세션에서 캐시 읽기가 싸졌지만, 이력을 편집하면 캐시와 thinking이 함께 무효가 된다. [확인] Artificial Analysis 기사에서 Astra가 같은 점수에 출력 약 27k 토큰인데 Fable 5.1(`max`)은 약 78k 토큰으로 보고됐다. [부분] 작업당 총비용으로 비교한다.
- **순위는 지표에 따라 달라진다.** 같은 기관의 코딩 에이전트 지수에서는 Fable 5.1(Claude Code)이 가장 높고, 기사에서는 Astra가 주요 지수에서 동률이며 Terminal-Bench v4.0에서 앞선다. SWE-Bench Pro 81.2%는 Anthropic 자체 보고다. [부분] 단일 순위로 결론내지 않는다.
- **데이터 요건.** 30일 보관, ZDR(보관 없음) 비대상이며 Covered Model이다. 보관 요건이 엄격한 조직은 도입할 수 없다. [확인] 모든 출력 텍스트에 통계적 워터마크가 들어간다. [확인]
- **가용성 제약.** 가장 높은 사이버 능력은 검증된 조직 전용 Mythos 5.1에만 있다. 안전장치 거짓 양성이 남아 있어 정당한 보안 작업이 막힐 수 있다. [확인]
- **종속성과 이행 비용.** 강제 도구 호출 불가, 샘플링 파라미터 불가, 이력 append-only 요건이 있어 기존 하네스를 고쳐야 할 수 있다. 모델을 바꾸면 이전 thinking이 사라진다. [확인]
- **라인업 변화.** 미출시 Fable 5.5는 공식 발표가 없다(루머만). 이 폴더의 `fable-5.5`를 참고하되 출시 전 정보로 결정하지 않는다. [미확인]

## 4. 근거와 한계
- 선택 기준·가격·보관·제약: [What's new in Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1), [Models overview](https://platform.claude.com/docs/en/models/overview) [확인]
- 순위·토큰 사용: [Artificial Analysis: Benchmarking GPT-6 Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra), [BenchLM 비교](https://benchlm.ai/compare/claude-fable-5-1-vs-gpt-6-astra) [부분]
- 한계: 시스템 카드(2026-09-01)는 열어 보지 않았다. 규제 인증과 데이터 레지던시 세부는 Anthropic 문서로 다시 확인한다.
