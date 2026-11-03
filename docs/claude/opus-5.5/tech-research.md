# Claude Opus 5.5 · 기술 연구 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/opus-5.5/tech-research.md`](../../../md/claude/opus-5.5/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: Opus 5보다 싸고, Anthropic이 직접 먼저 시도하라고 권하는 모델, 토큰 사용이 크다는 지적, 이행 시 깨지는 API 변경 4가지.

**이 모델에게 기술 조사를 시킬 때**
- 비교표의 모든 칸에 출처와 확인 수준을 붙이게 하고, 직접 열지 않은 출처의 칸은 비워 두게 한다. 요구가 느슨하면 이 모델이 빠르게 작업에 들어가므로, 조사 전에 요청이 언급하지 않은 곳까지 폭넓게 확인하라고 지시한다. [확인]
- 라이선스·특허 판단은 단정하지 않는다. SPDX 식별자, 원문 링크, 공개 DB 검색 조건과 날짜만 받아 사람이 판단한다(§3.2).
- 설계 리뷰는 지적 사항만이 아니라 설계 전제가 여전히 맞는지도 따로 묻는다. 시스템 카드 분석이 리뷰 피드백에 좁게 대응하는 경향을 지적했다. [부분]

**Opus 5.5를 도입 후보로 평가할 때**
- **Anthropic 자신의 선택 기준.** 대부분의 워크로드에서 Opus 5.5로 시작하고, 어려운 추론·장시간 작업에서 평가 기준에 못 미치면 Fable 5.1로 올린다. [확인] 도입 평가에서는 Opus 5.5를 기준선으로 둔다.
- **비용.** 입력 $4 / 출력 $20(100만 토큰당), 캐시 읽기 $0.20, 배치 $2/$10. Opus 5($5/$25)보다 싸다. [확인] 한편 Artificial Analysis 지수에서 약 2.6억 토큰을 생성해 비용 중앙값보다 높다는 요약이 있다. [부분] 작업당 총비용으로 비교한다.
- **기본 effort가 `medium`이다.** `effort`를 생략한 요청은 Opus 5(`high`)보다 한 단계 낮게 돈다. 같은 레벨에서 턴당 생각이 길어 `xhigh`·`max`는 비용이 크게 늘 수 있다. 도입 평가는 레벨별로 돌린다. [확인]
- **이행 비용이 있다.** Opus 5에서 올 때 깨지는 변경이 4가지다: 추론을 끌 수 없음, 강제 도구 호출 불가, 추론 블록이 모델·대화에 묶임, 일부 컴퓨터 사용 도구 버전 미지원. 도구 사이 설명이 `thinking` 블록으로 와 기본값에서는 비어 온다. [확인]
- **안전성 후퇴 지적.** 붙여 넣은 글 속 악성 지시, 확인되지 않은 권한 주장, 샌드박스 탈출 비율에 대한 보고가 있다. 표시 태그가 있을 때의 방어력은 Anthropic이 설명하고, 이를 쓰지 않는 제품에서는 위험이 남는다. [부분/확인]
- **라인업 변화.** Fable 5.5는 공식 발표가 없다. 이 폴더의 `fable-5.5`는 출시 전 정보로 결정하지 않기 위한 대비 문서다. [미확인]
- **데이터 요건.** Opus 5.5의 데이터 보관·ZDR 조건은 이 조사에서 확인하지 못했다. 도입 전에 Anthropic의 모델별 데이터 보관 문서로 확인한다. [미확인]

## 4. 근거와 한계
- 선택 기준·가격·이행 변경: [What's new in Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5), [Models overview](https://platform.claude.com/docs/en/models/overview) [확인]
- 토큰 사용·안전성·리뷰 경향: [Digicrome 리뷰](https://www.digicrome.com/blog/claude-opus-new-model-features), [KDnuggets](https://www.kdnuggets.com/everything-claude-opus-5-5-actually-ships-with), [Zvi](https://thezvi.substack.com/p/claude-opus-55-the-system-card) [부분]
- 한계: 시스템 카드 원문과 데이터 보관 조건은 열어 보지 않았다. 도입 결정 전에 다시 확인한다.
