# Grok 4.7 · 기술 연구 — 조사 기록
> 제공자: xAI(일부 자료는 회사명을 SpaceXAI로 표기하나 확인하지 못함) · 모델 ID: API `grok-4.7`(집계 사이트의 `grok-4-7` 표기, 확인 필요), 경량 변형 "Grok 4.7 Fast"는 Cursor·Grok Build 전용이라는 서술 · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/grok/grok-4.7/tech-research.md`](../../../../md/grok/grok-4.7/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델, 입력 $2 / 출력 $6(20만 토큰부터 장문 요금), 독립 평가 점수 46(`high`=`xhigh`), 출력 토큰 소비 많음, 서버 측 검색 도구 별도 과금, 모델 카드·벤더 벤치마크 부재, 데이터 정책은 2차 출처, 빠른 갱신.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.
- 환각 값이 확인되지 않았으므로 모델이 말하는 버전·날짜·가격·라이선스는 모두 1차 출처로 다시 확인한다.

**Grok 4.7을 도입 후보로 평가할 때**
- **벤더 수치가 없고 문서가 부족하다는 점이 첫 번째 평가 항목이다.** 모델 카드·시스템 카드를 확인하지 못했고 벤더 벤치마크가 공개되지 않았다. 독립 평가 점수(AA v4.3.2) 46만 있다. 위험 평가나 공급자 실사(보안·AI 거버넌스)에 필요한 문서가 갖춰졌는지 확인하고, 없으면 "자료 미비"로 기록한다. 2025년 Grok 4 때 시스템 카드와 위험 능력 평가 결과 미공개로 비판받았다는 선례가 있다. [부분]
- **총비용은 과제당 비용이다.** 단가(입력 $2 / 출력 $6, 캐시 입력 $0.5)는 낮지만 AA 벤치마크 점수 실행에서 `xhigh`는 출력 토큰 2.4억 개, `high`는 2.0억 개로 비교군 중앙값(9,200만)의 두 배 이상이었다. 프롬프트가 20만 토큰에 이르면 요청 전체에 장문 요금(입력 $4 / 출력 $12)이 적용된다는 서술도 있다. 웹 검색·X 검색은 호출 1,000회당 $5가 별도로 청구된다. 우리 과제의 토큰·도구 호출 수로 과제당 비용을 비교한다. [부분, 충돌]
- **노력 단계의 이득을 측정한다.** `high`와 `xhigh`의 독립 평가 점수가 같은 46이고 `low`는 42다. 단계를 올리면 비용만 오를 수 있다. [부분]
- **경쟁 모델과 같은 벤치마크 버전·같은 과제로 비교한다.** 점수는 페이지마다 비교군 중앙값이 달라(11, 27) 순위를 단정하기 어렵다. 다른 모델의 값을 인용할 때 벤치마크 버전과 노력 단계를 명시한다. 코딩 에이전트 지수(56, Grok Build 함께)는 하네스와 묶인 값이다. [부분/미확인]
- **접근 경로.** Grok 4.7 Fast는 Cursor와 Grok Build 전용이고 공개 xAI API에는 없다는 서술이 있다. Grok Build는 4.7을 기본으로 시작한다. 사용하려는 경로(공개 API, Grok Build, Cursor)의 한도·약관을 확인한다. [부분]
- **데이터 거버넌스.** 여러 집계가 API 입력·출력을 명시적 허락 없이 학습에 쓰지 않고 기본 30일 암호화 보관한다고 정리하고, SOC 2 Type 2와 요청 시 BAA 제공을 서술한다. 영 보관(ZDR)은 기업 전용이라는 서술과 콘솔 토글이라는 서술이 갈리며 소비자용 Grok은 정책이 다르다. 모두 2차 출처이므로 xAI의 API 보안 FAQ, 약관, DPA를 원문으로 읽고 법무·보안 검토를 거친다. [부분, 충돌]
- **서버 측 도구의 통제.** 내장 웹 검색·X 검색은 xAI 서버에서 실행되므로 조직의 네트워크 통제·허용 목록 정책이 적용되지 않는다. 데이터 경계가 중요한 환경에서는 도구를 끄고 하네스가 직접 검색한다. [추정]
- **공급 연속성과 버전 관리.** Grok 4.5(7월 8일), 4.6(8월 12일), 4.7(9월 21일)이 두 달 사이에 나왔고 4.8·5가 예고돼 있다(`grok-4.8`, `grok-5` 문서). 일정은 반복해서 어긋났다. 구버전 폐기 일정, 모델 교체 절차, 폴백 모델, 회귀 시험을 도입 조건으로 둔다. 회사명 표기가 자료마다 달라(xAI, SpaceXAI) 계약 상대와 약관 주체를 확인한다. [부분]
- **제공자 안전장치와 규정.** 규제 적합성은 모델이 아니라 시스템 전체에 대해 판단하고, 모델 카드를 규정 준수의 근거로 쓰지 않는다. 출시 직후 탈옥 우회 주장 사례가 있어 입력·출력 필터를 직접 둔다. [부분: 개인 주장]

## 4. 근거와 한계
- 출시·가격·컨텍스트: [Let's Data Science: Grok 4.7 출시](https://letsdatascience.com/news/xai-releases-grok-47-with-500k-context-43aa2021), [Price Per Token: Grok 4.7](https://pricepertoken.com/pricing-page/model/xai-grok-4.7), [Another Wrapper: Grok 4.7 가격](https://anotherwrapper.com/llm-pricing/grok-4.7) (스니펫만) [부분, 충돌]
- 독립 평가 점수·토큰 사용량: [Artificial Analysis: Grok 4.7 (xhigh)](https://artificialanalysis.ai/models/grok-4-7), [Grok 4.7 (high)](https://artificialanalysis.ai/models/grok-4-7-high), [Grok 4.7 (low)](https://artificialanalysis.ai/de/models/grok-4-7-low) (스니펫만) [부분]
- 도구 요금: [xAI 문서: 가격](https://docs.x.ai/developers/pricing.md) (스니펫만, 이 환경에서 본문이 열리지 않음) [부분]
- 데이터 정책(2차): [guptadeepak: 데이터 취급·보관](https://guptadeepak.com/ai-models/data-handling/), [BAA Atlas: Grok](https://baa-atlas.vercel.app/ai/grok), [DevelopersDigest: xAI 보관](https://www.developersdigest.tech/models/data-retention/xai) (스니펫만) [부분, 충돌]
- 안전 서술·선례: [Hora de Codar: Grok 4.7 거부·탈옥](https://horadecodar.com.br/grok-4-7-jailbreak/), [VentureBeat: Grok 탈옥](https://venturebeat.com/ai/with-little-urging-grok-will-detail-how-to-make-bombs-concoct-drugs-and-much-much-worse) (스니펫만) [부분]
- 한계: xAI 공식 문서·모델 카드·약관·DPA를 읽지 못했다. 도입 전에 공식 문서에서 확인한다.
