# Kimi K3.1 · 기술 연구 — 조사 기록
> 제공자: Moonshot AI · 모델 ID: API `kimi-k3.1-pro`, 고속 변형 `kimi-k3.1-pro-highspeed`(Moonshot 발표를 전한 보도의 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/kimi/kimi-k3.1/tech-research.md`](../../../../md/kimi/kimi-k3.1/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: API는 2026-10-23 출시, 가중치와 라이선스는 11-04 공개 예정(현재 미확인), 입력 $2 / 출력 $10, 독립 지수 55, 벤더 표의 조건 문제, 공격적 사이버 능력 의도적 축소, 출시 직후 가용성 문제와 홍보 논란, 데이터 정책 서술 불일치.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.
- 환각 값이 확인되지 않았으므로 모델이 말하는 버전·날짜·가격·라이선스는 모두 1차 출처로 다시 확인한다.

**Kimi K3.1을 도입 후보로 평가할 때**
- **라이선스는 공개 후에 원문으로 확인한다 — 지금은 결정할 수 없다.** 가중치는 11-04까지 공개한다고 예고됐고 이 문서 기준일에는 공개가 확인되지 않는다. 직전 K3는 MIT가 아닌 자체 "Kimi K3 License"(OSI 승인 목록에 없음)였고, 2차 요약에 따르면 MaaS 사업자는 12개월 매출 2,000만 달러 초과 시 별도 계약이 필요하고, MAU 1억 명 초과 또는 월 매출 2,000만 달러 초과 제품은 "Kimi K3"를 표시해야 하며, 내부 사용·Moonshot 자체 제품·인증 추론 파트너는 면제다. 이 조건이 K3.1에 그대로 적용되는지, 임계값이 바뀌는지는 LICENSE 원문(공식 저장소)으로 확인한다. "오픈 웨이트"를 "오픈소스"로 읽지 않는다(§3.2). [부분: 2차 요약/미확인]
- **벤더 표를 그대로 믿지 않는다.** Terminal-Bench 4.0 65.7%(Claude Opus 5.5 66.4%), BrowseComp 92.1, HLE(도구 포함) 70.0은 Moonshot이 `max` 노력 단계로 잰 값이고, 일부 평가에서 모델마다 다른 에이전트 프레임워크를 썼다는 지적, 출시 시점에 점수 칸이 자리표시 문자열로 남은 점, DeepSWE v1.1·SWE-Marathon v1.1이 점수 없이 각주에만 있던 점이 있다. 독립 지수는 55다. 후보 비교는 같은 과제, 같은 노력 단계, 같은 예산의 자체 실측으로 한다. [부분: 벤더 주장]
- **총비용은 과제당 비용이다.** 표준 입력 $2 / 출력 $10, 캐시 입력 약 $0.2, Highspeed 입력 $4 / 출력 $20(2~3배 빠름)이며 컨텍스트 길이별 요금 단계는 없다는 서술이 있다. 그러나 기본 추론 단계가 `max`라는 서술이 있고 이전 K3는 지수 실행에서 출력 토큰 1.61억 개, 지수 실행 비용이 약 $3,658이었다. 단계를 명시한 상태에서 우리 과제의 토큰·도구 호출 수로 비교한다. [부분]
- **신뢰·가용성.** 출시 직후 사용량 제한으로 유료 사용자 접근이 끊겨 Moonshot이 사과하고 쿼터를 복원했으며 6개월 사이 세 번째 사과라는 보도가 있다. 크리에이터에게 유료 제휴 표기를 하지 말라는 지침이 있었다는 폭로도 있다(공식 대응 미확인). 모두 2차 출처다. SLA, 한도, 장애 이력을 도입 조건으로 확인하고 폴백 모델과 재시도를 둔다. 벤더 홍보 수치는 더 보수적으로 읽는다. [부분]
- **공격적 사이버 능력 축소의 양면.** 데이터 제거로 오용 위험을 낮췄다는 점은 안전 심사에 유리할 수 있으나, 정당한 보안 업무(취약점 분석, 펌웨어 보안 검토)에는 성능이 낮을 수 있다. 직전 K3 가중치는 더 강한 사이버 능력을 가진 채 이미 공개됐다는 보도가 있어 "K 시리즈 전체가 안전하다"고 일반화하지 않는다. 사용 용도별로 시험한다. [부분: 벤더 주장 포함]
- **데이터 거버넌스.** 학습 사용(Moonshot 문서 간 불일치 지적, 소비자 서비스는 학습에 쓰임), 보관(계정 활성 동안 또는 API 30일), ZDR(기업 계약), 서버 위치(국제 플랫폼은 싱가포르, 본사는 중국, 지역별 엔드포인트, 추론 위치 비공개)를 2차 출처로만 확인했다. 약관·개인정보 처리방침·DPA를 원문으로 읽고 법무·보안 검토를 거친다. 수출 통제·고객 계약상 국외 이전 제한이 있는 데이터는 확인 전에 보내지 않는다. [부분, 충돌]
- **자체 호스팅.** 총 약 2.8조급(활성 약 1,040억) 규모라 다중 GPU 노드가 필요하다. 가중치 공개 후 필요한 하드웨어와 운영비를 계산한다. 공식 조직의 저장소에서만 받고 제3자 재업로드는 쓰지 않는다. [추정]
- **공급 연속성.** K3(7월), K3.1 Pro(10월 말)가 석 달 간격으로 나왔고 K3.1 시리즈의 다른 모델이 뒤따를 수 있다. 구버전 폐기 일정, 모델 교체 절차, 폴백 모델, 회귀 시험을 도입 조건으로 둔다. [부분]
- **제공자 안전장치와 규정.** 규제 적합성은 모델이 아니라 시스템 전체에 대해 판단하고, 모델 카드나 가중치 라이선스를 규정 준수의 근거로 쓰지 않는다.

## 4. 근거와 한계
- 출시·가격·가중치 예고: [Let's Data Science: K3.1 Pro API, 가중치 11-04 예정](https://letsdatascience.com/news/moonshot-releases-kimi-k31-pro-api-open-weights-due-nov-4-786e160c), [Hora de Codar: Kimi K3.1 Pro](https://horadecodar.com.br/kimi-k31-pro/), [AICybr: K3.1 Pro API·가중치](https://aicybr.com/blog/kimi-k3-1-pro-api-open-weights-benchmarks-cyber-training) (스니펫만) [부분, 충돌]
- K3 라이선스(2차): [Unite.AI: Kimi K3 라이선스](https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/), [OpenRouter: Kimi K3는 오픈소스인가](https://openrouter.ai/blog/insights/kimi-k3-open-source/), [Let's Data Science: Kimi K3 가중치 공개](https://letsdatascience.com/news/moonshot-ai-releases-kimi-k3-open-weights-29a9edd6) (스니펫만) [부분: 2차, 원문 미확인]
- 벤더 표·조건: [OrcaRouter: K3.1 Pro 벤치마크](https://www.orcarouter.ai/blog/kimi-k3-1-pro-benchmark), [BenchmarkList: Kimi K3.1 Pro](https://benchmarklist.com/models/moonshotai-kimi-k3.1-pro/) (스니펫만) [부분: 벤더 주장]
- 신뢰 이슈: [SCMP: Moonshot 사과](https://scmp.com/tech/big-tech/article/3372247/moonshot-apologises-after-kimi-k31-pro-roll-out-stumbles-promotional-scrutiny-widens), [AI Weekly: 은밀한 홍보 의혹](https://aiweekly.co/fr/alerts/kimi-k31-pro-moonshot-accus-dune-campagne-dinfluence-cache) (스니펫만) [부분: 2차]
- 데이터 정책(2차): [DevelopersDigest: Moonshot 보관](https://www.developersdigest.tech/models/data-retention/moonshot), [Standard Compute: Moonshot](https://standardcompute.com/providers/moonshotai) (스니펫만) [부분, 충돌]
- 한계: Moonshot 공식 문서·모델 카드·LICENSE·약관 본문을 읽지 못했다. 가중치 공개 후 저장소 원문에서 확인한다.
