# Kimi K3.1 · 앱 — 조사 기록
> 제공자: Moonshot AI · 모델 ID: API `kimi-k3.1-pro`, 고속 변형 `kimi-k3.1-pro-highspeed`(Moonshot 발표를 전한 보도의 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/kimi/kimi-k3.1/app.md`](../../../../md/kimi/kimi-k3.1/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 총 약 2.8조급 MoE라 기기 내 실행 불가(가중치는 11-04 공개 예정, 라이선스 미확인), 이미지·영상 입력, 출시 직후 가용성 문제, 데이터 정책 서술 불일치, 모바일 개발 독립 평가 없음.

**앱에 내장할 때**
- **기기 안에서 돌릴 모델이 아니다.** 가중치가 공개돼도 규모가 크다(총 약 2.8조, 활성 약 1,040억 서술). 앱은 서버를 거쳐 호출하는 구조만 가능하다. 모바일 온디바이스는 `gemma-4-e2b`, `gemma-4-e4b` 문서를 본다. [부분]
- **API 키를 앱 바이너리나 리소스에 넣지 않는다.** 앱에서 직접 호출하지 말고 자체 백엔드에서 키 보관, 사용량 제한, 요청 검증, 로깅을 한다(§3.1 비밀 규칙). 모델 출력은 신뢰하지 않는 입력으로 취급해 서버에서 검증한 뒤 앱에 전달한다.
- **개인정보 선언과 실제 동작을 맞춘다.** 데이터 정책 서술이 어긋난다. Moonshot 문서가 API 데이터의 학습 사용에 대해 다르게 적는다는 지적이 있고, 소비자 서비스는 사용자 콘텐츠로 모델을 학습·최적화한다고 정책에 있으며, 보관은 계정이 활성인 동안 또는 API 요청 30일로 갈리고, ZDR은 기업 계약이라는 서술이 있다. 국제 플랫폼 서버는 싱가포르이고 본사는 중국이며 지역별 엔드포인트가 따로 있고 추론 위치는 공개돼 있지 않다. [부분, 충돌] 출시 전에 약관과 개인정보 처리방침을 원문으로 읽고 앱의 개인정보 선언(Apple 개인정보 영양 표시, Google Play 데이터 보안 양식)과 처리방침에 전송 항목과 국외 이전을 반영한다. 소비자용 Kimi 서비스와 API를 혼동하지 않는다. 아동·민감정보는 확인 전에 보내지 않는다.
- **이미지·영상을 보내는 기능은 조심한다.** 텍스트·이미지·영상 입력이라는 서술이 있다. 사진·영상에 담긴 얼굴·위치·문서 정보가 서버와 제3자로 전송되므로 약관 확인과 사용자 동의 없이 보내지 않는다. [부분]
- **비용을 과제당으로 서버에서 제한한다.** 단가는 표준 입력 $2 / 출력 $10이고 기본 추론 단계가 `max`라는 서술이 있어 호출마다 단계를 명시한다. 이전 K3는 지수 실행에서 출력 토큰이 1.61억 개였다. 사용자당 한도, `max_tokens`, 요청 빈도 제한을 서버에 두고 실제 청구서로 확인한다. [부분]
- **가용성에 대비한다.** 출시 직후 사용량 제한으로 유료 사용자 접근이 끊긴 사례가 보도됐다. 429·타임아웃에 대한 재시도, 폴백 모델, 오류 UX를 설계한다. [부분]
- **모델 교체를 앱 업데이트 없이 할 수 있게 설계한다.** 출시 후 열흘 사이에 가중치 공개, 라이선스, 가격이 바뀔 수 있다. 서버 쪽 모델 설정, 폴백 모델, 회귀 시험, 기능 플래그를 둔다.
- **가중치를 직접 호스팅하려면 공개 후 LICENSE를 먼저 읽는다.** 직전 K3는 MIT가 아닌 자체 라이선스(MaaS 사업자 매출 기준 별도 계약, 대규모 제품의 "Kimi K3" 표시 의무)였다. K3.1에 같은 조건이 적용되는지 미확인이다. 앱이 최종 사용자에게 모델 접근을 제공하는 형태면 MaaS 정의에 해당하는지 법무가 판단한다. [부분/미확인]

**개발 보조로 쓸 때**
- **모바일(Kotlin·Swift) 코드에 대한 독립 평가는 찾지 못했다.** [미확인] 컴파일·린트·단위 테스트·UI 테스트로 검증하고, 수명주기·권한·비동기 처리가 걸린 구현은 상위 모델 문서(`claude/sonnet-5.5` 이상, `gpt-6.1-sol`, `gemini-4-argon`)와 같은 과제로 비교한다.
- 스토어 규정은 기억으로 답하지 않고 공식 문서로 확인한다(§3.2). 서명 키, 프로파일, 스토어 제출·배포는 승인 후에만 한다.

## 4. 근거와 한계
- 데이터 정책(2차): [DevelopersDigest: Moonshot 보관](https://www.developersdigest.tech/models/data-retention/moonshot), [Standard Compute: Moonshot](https://standardcompute.com/providers/moonshotai), [Security Scientist: Kimi 데이터 프라이버시](https://www.securityscientist.net/blog/12-questions-and-answers-about-kimi-data-privacy-as-a-chinese-model/) (스니펫만) [부분, 충돌]
- K3 라이선스(2차): [Unite.AI: Kimi K3 라이선스](https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/), [OpenRouter: Kimi K3는 오픈소스인가](https://openrouter.ai/blog/insights/kimi-k3-open-source/) (스니펫만) [부분: 2차, 원문 미확인]
- 가용성·가격: [Cryptopolitan: 쿼터 초기화](https://www.cryptopolitan.com/moonshot-resets-kimi-k3-1-pro-quotas-after-rate-limit-apology/), [Price Per Token: K3.1 Pro](https://pricepertoken.com/pricing-page/model/moonshotai-kimi-k3.1-pro) (스니펫만) [부분]
- 한계: 모바일 개발과 데이터 정책에 대한 1차 자료를 읽지 못했다.
