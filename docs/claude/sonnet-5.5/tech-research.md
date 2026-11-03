# Claude Sonnet 5.5 · 기술 연구 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/sonnet-5.5/tech-research.md`](../../../md/claude/sonnet-5.5/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: Opus 5.5의 절반 가격이지만 `max`는 더 비쌈, 지식 평가 54%, Sonnet 5에서 올 때 깨지는 변경 5가지.

**이 모델에게 기술 조사를 시킬 때**
- 비교표의 모든 칸에 출처와 확인 수준을 붙이게 하고, 직접 열지 않은 출처의 칸은 비워 두게 한다. 이 모델은 바뀐 세부를 학습 지식으로 답할 수 있으므로 "최신 출처를 검색해 모으라"를 명시한다. [확인]
- 라이선스·특허 판단은 단정하지 않는다. SPDX 식별자, 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다(§3.2).
- 설계 판단이 어려우면 어드바이저 도구(베타)로 더 강한 모델의 조언을 받을 수 있다. Sonnet 5.5 실행기는 Opus 5.5, Opus 5, Fable·Mythos 계열이나 Sonnet 5.5 자신만 어드바이저로 받는다. 조언은 암호화되어 돌아와 클라이언트가 읽지 못한다. [확인]

**Sonnet 5.5를 도입 후보로 평가할 때**
- **Anthropic의 위치 설정.** "속도와 지능의 가장 좋은 조합"이고 가장 어려운 장시간 작업에는 Opus를 권한다. [확인]
- **비용.** 입력 $2 / 출력 $10, 캐시 읽기 $0.10(Sonnet 5의 절반). 그러나 Artificial Analysis에서 `max` 작업당 비용이 Sonnet 5.5 $7.60, Opus 5.5 $5.98로 보고돼 싼 모델이 항상 싼 것은 아니다. 점수도 `xhigh` 52.1%에서 `max` 46.2%로 낮아졌다. [확인: 가격 / 부분: 비교] 레벨별 작업당 총비용으로 비교한다.
- **품질 격차.** Artificial Analysis 지능 지수 56(Opus 5.5는 58), 지식 평가 54%(Opus 5.5는 66%). Terminal-Bench 우위는 한 벤치마크에 의존하고 출처마다 수치가 다르다(70.6% 대 66.4%, 64% 대 60%). [부분]
- **이행 비용.** Sonnet 5에서 올 때 깨지는 변경이 5가지다: `between_tools`로의 전환(`disabled`는 400), 강제 도구 호출 불가, 추론 블록이 모델·대화에 묶임, 일부 컴퓨터 사용 도구 버전 미지원, 어드바이저 짝 제한. 도구 사이 설명이 `thinking` 블록으로 와 기본값에서는 비어 온다. [확인]
- **안전 범주.** 5개 범주(`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`)로 거부될 수 있고, 서버 쪽 대체는 `cyber`·`frontier_llm`만 Sonnet 5로 재시도한다. [확인]
- **데이터 요건.** Sonnet 5.5의 데이터 보관·ZDR 조건은 이 조사에서 확인하지 못했다. 도입 전에 Anthropic의 모델별 데이터 보관 문서로 확인한다. [미확인]
- **라인업.** 미출시 모델 정보(Fable 5.5)는 공식 발표가 없다. [미확인]

## 4. 근거와 한계
- 위치·가격·이행 변경·안전 범주: [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5), [Models overview](https://platform.claude.com/docs/en/models/overview) [확인]
- 비용·지수·지식 평가: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-sonnet-5-5-review), [Kingy.ai](https://kingy.ai/blog/claude-sonnet-5-5-specs-benchmarks-pricing/), [Claude 5.5 is brilliant, confusing, and very hungry](https://dreasays.substack.com/p/claude-55-is-brilliant-confusing) [부분]
- 한계: 시스템 카드 원문과 데이터 보관 조건은 열어 보지 않았다. 도입 결정 전에 다시 확인한다.
