# Kimi K3.1 · 범용 — 조사 기록
> 제공자: Moonshot AI · 모델 ID: API `kimi-k3.1-pro`, 고속 변형 `kimi-k3.1-pro-highspeed`(Moonshot 발표를 전한 보도의 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/kimi/kimi-k3.1/general.md`](../../../md/kimi/kimi-k3.1/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Kimi K3.1 Pro (API 먼저, 가중치는 공개 예정)
이 환경에서는 Moonshot 공식 문서와 Hugging Face가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다.

### 2.1 위치와 공개 상태 — 가중치는 아직 없다
- **K3.1 Pro가 K3.1 시리즈 첫 모델이고 K3를 후속 학습으로 개선한 모델이라고 소개된다.** API 출시일은 2026-10-23로 가장 많이 인용되고 24일, 25일로 쓴 곳도 있다. Kimi.com, Kimi Work, Kimi Code, Kimi API에서 쓸 수 있고 같은 날 고속 변형 Highspeed가 함께 나왔다(최대 3배 빠르다는 홍보). [부분, 충돌]
- **가중치는 11월 4일까지 공개한다고 예고됐다.** 이 문서 기준일(11-03)에는 공개된 것으로 확인되지 않는다. 공개되면 모델 저장소의 LICENSE 원문을 읽기 전에는 K3.1의 라이선스를 단정하지 않는다. [부분/미확인]
- **참고: 직전 K3의 라이선스는 MIT가 아닌 자체 "Kimi K3 License"다.** 가중치는 2026-07-26 또는 27일 `moonshotai/Kimi-K3`로 공개됐고 SPDX 식별자가 없으며 OSI 승인 목록에도 없다. 대부분 MIT처럼 읽히지만 다음 조건이 있다고 요약된다. (1) 제3자에게 추론이나 미세조정 접근을 제공하는 "서비스형 모델(MaaS)" 사업자는 연매출(12개월 합산)이 2,000만 달러를 넘으면 별도 계약이 필요하다(기준 서술이 출처마다 약간 다름). (2) 월간 활성 사용자 1억 명 초과 또는 월 매출 2,000만 달러 초과 제품은 인터페이스에 "Kimi K3"를 눈에 띄게 표시해야 한다. (3) 내부 사용, Moonshot 자체 제품, 인증된 추론 파트너 경유는 면제된다. K3.1에 같은 조건이 적용되는지는 미확인이다. [부분: 2차 요약, 라이선스 원문 미확인]

### 2.2 사양 (출처마다 다름)
- **MoE, 총 약 2.8조(3조급이라는 서술도 있음), 활성 약 1,040억.** 컨텍스트 1,048,576 토큰(약 100만, 100K로 쓴 글은 오류로 보임). 최대 출력은 컨텍스트와 공유한다는 서술, 약 94.4만 토큰이라는 서술, 공개하지 않았다는 서술이 갈린다. [부분, 충돌]
- **가격**(100만 토큰당): 표준 입력 $2 / 출력 $10, 캐시 입력 약 $0.2, Highspeed 입력 $4 / 출력 $20. 컨텍스트 길이별 요금 단계가 없다는 서술이 있다. 공식 가격표는 확인하지 못했다. [부분]
- **추론은 항상 켜져 있고 `low`·`high`·`max` 단계가 있으며 기본값이 `max`라는 서술이 있다.** 기본이 최고 단계라면 토큰 소비와 비용이 기본으로 크다. 지정 방법은 공식 문서로 확인한다. [부분/미확인]

### 2.3 성능 근거를 읽는 법
- **Moonshot의 대표 수치**: Terminal-Bench 4.0 65.7%(Claude Opus 5.5 66.4%, GPT-6 Astra 58.2%와 비교). 이는 Moonshot이 제공한 값이고 독립 검증이 없으며, 평가 일부에서 모델마다 다른 에이전트 프레임워크를 썼다는 지적이 있다. 한 아랍어 보도는 Artificial Analysis가 약 67%를 측정했다고 하나 원문을 확인하지 못했다. [부분: 벤더 주장]
- **독립 지수(Artificial Analysis)**: K3.1 Pro 55, 지수 실행에 출력 토큰 약 1.5억 개. 같은 페이지가 "공개 API 없음"이라고 적었으나 Moonshot은 API가 열렸다고 발표했으므로 페이지가 오래됐을 수 있다. 이전 K3는 페이지에 따라 57(지수 v4.1)과 44(지수 v4.3)로 갈리고 출력 토큰 1.61억 개, 지수 실행 비용 약 $3,658이었다. 지수 버전이 다르면 직접 비교하지 않는다. [부분, 충돌]
- **환각**: 이전 K3에서 AA가 환각률 51%(K2.6의 39%에서 상승)를 측정했다는 2차 글이 있으나 AA 원문으로 확인하지 못했고 K3.1의 값은 찾지 못했다. [미확인]
- **개발자 현장 평가는 얕다.** Kimi Code 튜토리얼이 긴 저장소 규모 작업에서 예산형 선택이라고 쓴 것은 자체 서술이다. 한 비공식 사이트의 도구 선택 967/1,000, 에이전트 루프 199/200 통과 같은 수치는 방법론을 확인할 수 없어 쓰지 않는다. [미확인]

### 2.4 공격적 사이버 능력을 의도적으로 낮췄다
- Moonshot은 학습 데이터에서 사이버 관련 자료를 빼는 방식(거부 계층이 아니라 중간 학습 단계의 데이터 조작)으로 공격적 능력을 줄였다고 밝혔다. 내부 벤치마크의 익스플로잇 성공률이 제한 없는 실험 버전 90.5%에서 최종 K3.1 Pro 81%로 낮아졌다는 보도가 있다. 같은 보도는 코딩 성능이 Claude Opus 5.5에 한 점 안팎까지 근접했다고 쓰나 벤더 측 수치다. [부분: 벤더 주장]
- 시사점: 정당한 보안 연구(취약점 분석, 퍼징 하네스 작성, 펌웨어 분석)에서 성능이 낮을 수 있고, 데이터를 뺀 것이지 거부 규칙을 얹은 것이 아니므로 모델의 동작으로 안전을 가정하지 않는다. 직전 K3 가중치는 더 강한 사이버 능력을 가진 채 이미 공개됐다는 보도가 있다. [추정]

### 2.5 운영·신뢰 이슈
- **출시 직후 사용량 제한으로 유료 사용자의 접근이 끊겨 Moonshot이 사과하고 쿼터를 초기화·25% 복원했다는 보도가 있다.** 한 독일어 보도는 6개월 사이 세 번째 사과라고 한다. 모두 2차 출처다. 가용성과 한도 정책을 도입 전에 시험하고 폴백 모델을 둔다. [부분]
- **홍보 방식 논란**: 출시 홍보에서 크리에이터에게 유료 제휴 표기를 하지 말라는 지침이 있었다는 폭로가 보도됐고 공식 대응은 확인하지 못했다. 벤더 홍보 수치를 더 보수적으로 읽는다. [부분: 단일 보도]
- **데이터 정책이 서술마다 어긋난다.** Moonshot 문서 자체가 API 데이터 학습 사용에 대해 다르게 적는다는 지적이 있고, 소비자 서비스는 사용자 콘텐츠로 모델을 학습·최적화한다고 정책에 있다. 보관은 계정이 활성인 동안이라는 서술과 API 요청 30일이라는 서술이 갈린다. ZDR은 자체 신청이 아닌 기업 계약이라는 서술이 있다. 국제 플랫폼(Moonshot AI PTE. LTD.)의 서버는 싱가포르이고 본사는 중국이며 지역별 엔드포인트가 따로 있고 추론이 어디서 실행되는지는 공개돼 있지 않다는 서술이 있다. 모두 2차 출처다. [부분, 충돌]
- **코딩 에이전트 사용 지침(Kimi Code)**: Moonshot은 승인 기능을 켜 두고, diff를 검토하고, 비밀을 보호하고, 되돌릴 수 있는 Git 브랜치를 쓰라고 안내한다. 이 저장소의 §1.6과 같은 취지이므로 그대로 따른다. [부분]

### 2.6 비판적 평가
- 강점 후보: 100만 토큰 컨텍스트, 낮은 단가(표준), 공개 가중치 예정, 독립 지수 55. 약점 후보: 가중치·라이선스 미공개, 대표 수치가 벤더 제공이고 프레임워크가 달랐다는 지적, 기본이 최고 추론 단계라 토큰 소비가 큼, 출시 직후 가용성 문제와 홍보 논란, 데이터 정책 불일치.
- 막히면 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시·ID·가격·가중치 예고(11-04) | [Let's Data Science: K3.1 Pro API, 가중치 11-04 예정](https://letsdatascience.com/news/moonshot-releases-kimi-k31-pro-api-open-weights-due-nov-4-786e160c), [Hora de Codar: Kimi K3.1 Pro](https://horadecodar.com.br/kimi-k31-pro/), [Price Per Token: K3.1 Pro](https://pricepertoken.com/pricing-page/model/moonshotai-kimi-k3.1-pro), [AICybr: K3.1 Pro API·가중치](https://aicybr.com/blog/kimi-k3-1-pro-api-open-weights-benchmarks-cyber-training) (스니펫만) | [부분, 충돌] |
| 독립 지수·토큰 사용량 | [Artificial Analysis: Kimi K3.1 Pro](https://artificialanalysis.ai/zh/models/kimi-k3-1-pro), [Artificial Analysis: Kimi K3](https://artificialanalysis.ai/es/models/kimi-k3) (스니펫만) | [부분, 충돌] |
| K3 라이선스(2차 요약) | [Unite.AI: Kimi K3 가중치 공개, 매출 구간 라이선스](https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/), [OpenRouter: Kimi K3는 오픈소스인가](https://openrouter.ai/blog/insights/kimi-k3-open-source/) (스니펫만) | [부분: 2차, 라이선스 원문 미확인] |
| 사이버 능력 축소 | [VKTR: K3.1 Pro와 사이버 능력 제한](https://www.vktr.com/ai-platforms/kimi-k31-pro-nears-top-proprietary-models-as-moonshot-limits-its-cyber-skills/), [Forklog](https://forklog.com/en/?p=105758), [WinZheng](https://www.winzheng.com/en/article/kimi-k31-pro-open-weights-cyber-capability-weakening) (스니펫만) | [부분: 벤더 주장 포함] |
| 출시 직후 문제·홍보 논란 | [SCMP: Moonshot 사과](https://scmp.com/tech/big-tech/article/3372247/moonshot-apologises-after-kimi-k31-pro-roll-out-stumbles-promotional-scrutiny-widens), [Cryptopolitan: 쿼터 초기화](https://www.cryptopolitan.com/moonshot-resets-kimi-k3-1-pro-quotas-after-rate-limit-apology/), [AI Weekly: 은밀한 홍보 의혹](https://aiweekly.co/fr/alerts/kimi-k31-pro-moonshot-accus-dune-campagne-dinfluence-cache) (스니펫만) | [부분: 2차] |
| 데이터 정책(2차) | [DevelopersDigest: Moonshot 보관](https://www.developersdigest.tech/models/data-retention/moonshot), [Standard Compute: Moonshot](https://standardcompute.com/providers/moonshotai), [Security Scientist: Kimi 데이터 프라이버시](https://www.securityscientist.net/blog/12-questions-and-answers-about-kimi-data-privacy-as-a-chinese-model/) (스니펫만) | [부분, 충돌] |
- Moonshot 공식 문서·모델 카드·LICENSE·약관 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
- 가중치 공개 후 K3.1의 라이선스와 사양은 저장소 원문으로 다시 확인한다.
