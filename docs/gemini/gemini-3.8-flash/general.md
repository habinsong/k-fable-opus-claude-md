# Gemini 3.8 Flash · 범용 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-3.8-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-3.8-flash/general.md`](../../../md/gemini/gemini-3.8-flash/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Gemini 3.8 Flash
이 환경에서는 Google 공식 문서 본문이 열리지 않아 Google Cloud 문서의 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다.

### 2.1 위치와 사양
- 비용 중심 Flash 티어다. 2026-09-02 정식 출시(GA), 모델 ID `gemini-3.8-flash`, 컨텍스트 1,048,576 토큰, 최대 출력 65,536 토큰, 추론 지원이다. Gemini 3.7 Flash를 바탕으로 만들어졌다고 모델 카드가 서술했다는 리뷰가 있다. 지식 컷오프는 2026-03로 보도됐다(2차). [부분]
- **가격이 곧 오른다.** 도입가는 입력 $0.75 / 출력 $3.75(100만 토큰당)이고 2026-12-31까지다. 2027-01-01부터 $1.50 / $7.50이라는 2차 정리가 있다(Google 가격 페이지로 확인하지 못했다). 생각 토큰은 출력 요금으로 청구된다. 비용 계획은 인상된 가격으로 세운다.
- 추론은 `thinking_level` `LOW` / `MEDIUM`(기본) / `HIGH`. `MINIMAL`을 지정하면 검증 오류다. Flash 계열은 추론을 완전히 끌 수 없다.
- 사이버 변종 `Gemini 3.8 Flash Cyber`는 Fairwind 프로그램의 신뢰 방어 담당자에게만 제공되고 일반 공개가 아니다. 가격과 일반 공개 일정은 공개되지 않았다.

### 2.2 도구·하네스
- Gemini 4와 3 모델은 함수 호출 시 thought signature를 돌려주지 않으면 검증 오류라는 Google 안내가 있다. 3.8 Flash가 이 규칙에 포함되는지는 확인하지 못했다. [미확인] 하네스를 직접 만들면 응답의 모든 파트를 그대로 다음 턴에 넣는다.
- **Gemini CLI는 이 모델에 맞는 도구다.** Gemini CLI는 Gemini 4 이후에 최적화돼 있지 않다고 README가 적는데, 3.8 Flash는 3.x 세대다. Gemini CLI는 `GEMINI.md`를 지속 컨텍스트 파일로 읽는다. [확인] 이 문서를 프로젝트 루트에 `GEMINI.md`로 복사하면 된다. Antigravity CLI에서 쓰려면 `AGENTS.md`로 복사하고 `GEMINI.md`와 둘 다 두지 않는다. [확인/부분]

### 2.3 행동 특성과 이 문서를 쓰는 법
- **`thinking_level`을 명시한다.** 단순 변환은 `LOW`, 일반 구현은 `MEDIUM`(기본), 어려운 디버깅은 `HIGH`. 생각 토큰도 출력 요금이므로 `HIGH`는 비용이 크다.
- **첫 토큰이 느리다.** 한 제3자 측정에서 첫 토큰까지 13.30초(중앙값 2.99초)였고, 출력 속도는 196개 중 3위다. 추론하는 동안 응답이 시작되지 않는 구조다. → 대화형 UI에서는 `LOW`를 쓰고 스트리밍과 로딩 표시를 둔다. 총 지연은 출력 속도로 상쇄될 수 있다. [부분]
- **말이 많다.** 장황함 순위가 74위로 보고됐다. → 최종 보고는 5항목, 항목당 1~2줄로 제한한다.
- **자기 검증을 지시한다.** 같은 계열 상위 모델 Argon에서 자기 검증이 약하다는 후기가 있었다. 3.8 Flash에 대한 같은 평가는 찾지 못했지만 [미확인], "변경 후 실제 검사를 돌리고 출력을 읽고 고치라"를 지시한다(§1.2).

### 2.4 비판적 평가 (독립 측정은 2차 출처)
- **싸지만 작업당 비용은 이전 Flash보다 높다.** Artificial Analysis에서 3.7 Flash 대비 같은 평가에 출력 토큰을 약 1.77배 내고 작업당 비용이 $0.74로 3.7 Flash의 $0.55보다 높았다. 지수는 지능 40.9, 코딩 76.3, 에이전트 40.2로 보고됐다. [부분]
- **최상위 모델과의 격차.** Google 자신의 비교표에서 Terminal-Bench 4.0이 Claude Opus 5보다 32.7점 낮다. DeepSWE v1.1 73.7%는 벤더 수치다. [부분]
- **지식 평가는 소형 모델 중 나은 편이다.** AA-Omniscience 정답 비율 55%로 GPT-6 Luna(44%), Claude Haiku 5.5(36%)보다 높게 인용됐다. 그래도 절반 가까이는 맞히지 못한다. → 사실 질의는 검색으로 확인한다. [부분]
- **가격 인상 위험.** 2027-01-01 이후 가격이 두 배가 된다는 정리가 있어 장기 계약·예산에 반영한다. [부분]
- **초기 평가가 얕다.** 대부분 출시 직후 블로그와 집계 사이트다.

### 2.5 쓸 때와 쓰지 않을 때
- 쓴다: 비용에 민감한 구현·수정 반복, 대량 코드 변환, 빠른 출력이 필요한 작업, Gemini CLI 사용 환경.
- 올린다: 막히면 Gemini 4 Argon이나 Sonnet 5.5·GPT-6.1 Sol.
- 쓰지 않는다: 첫 토큰 지연에 민감한 실시간 UI(`LOW` 없이), 최고 난도의 자율 코딩, 2027-01-01 이후 가격에서 예산이 빠듯한 대량 작업.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 모델 ID·출시일·컨텍스트·변종 | [Gemini 3.8 Flash (Google Cloud 문서)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash), [9to5Google](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/) (스니펫만) | [부분] |
| thinking 레벨·MINIMAL | [Thinking (Google Cloud)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking), [What's new in Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8) (스니펫만) | [부분] |
| 비용·지수·지연·격차 | [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-3-8-flash), [Gemini 3.8 Flash Review: The Token Bill](https://truestandard.ai/blog/gemini-3-8-flash-review), [DataNorth](https://datanorth.ai/news/google-launches-gemini-3-8-flash-gemini-3-8-flash-cyber) | [부분] |
| Gemini CLI와 GEMINI.md | [google-gemini/gemini-cli README](https://github.com/google-gemini/gemini-cli) (직접 읽음) | [확인] |
- Google 공식 가격 페이지를 열지 못해 2027-01-01 이후 가격은 2차 정리다. 도입 전에 공식 페이지로 확인한다.
- 지식 평가 수치는 다른 모델 리뷰가 인용한 것이다. Artificial Analysis 원본으로 확인한다.
