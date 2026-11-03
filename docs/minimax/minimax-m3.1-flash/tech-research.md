# MiniMax-M3.1-Flash · 기술 연구 — 조사 기록
> 제공자: MiniMax · 모델 ID: API `MiniMax-M3.1-Flash`(프리뷰는 `MiniMax-M3.1-Flash-Preview`, 정확한 ID는 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/minimax/minimax-m3.1-flash/tech-research.md`](../../../md/minimax/minimax-m3.1-flash/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 경량 변형(파라미터·가중치 공개 여부 미확인), 입력 $0.15 / 출력 $0.60(인하 보도), 독립 지수 42, 작업당 비용 $0.22(M3 $0.51), 환각률 93% 보도, 벤더 수치 조건 불명, 프리뷰→정식 한 달.

**이 모델에게 기술 조사를 시킬 때**
- 사실 회상이 필요한 조사에는 쓰지 않는다. 환각률 93% 보도(2차)가 있어 버전·날짜·가격·라이선스를 모델이 말하게 하지 않는다. 쓴다면 사람이 확보한 1차 자료 텍스트에서 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류·추출만 하게 하고 원문에 없으면 null로 두며 근거 구절을 코드로 대조한다. [부분: 2차/추정]
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.

**MiniMax-M3.1-Flash를 도입 후보로 평가할 때**
- **먼저 모델의 정체를 확인한다.** 파라미터 수가 공개되지 않았고(428B·23B는 M3의 수치를 빌려 온 것일 수 있다는 경고), 가중치 공개 여부가 출처마다 충돌한다(공개라는 서술 대 다운로드 가능한 가중치 없음). 프리뷰(`-Preview`)와 정식 ID도 다르다. 이 확인 없이 라이선스·하드웨어 계획을 세우지 않는다. [부분, 충돌/미확인]
- **라이선스는 공개 여부가 확인된 뒤 원문으로 본다.** 공개된다면 상위 M3와 같은 MiniMax Community License(용도 금지 조항)일 수 있으나 이는 추정이다. API만 쓰는 경우에는 API 이용 약관이 적용된다. 어느 경우든 SPDX 식별자가 없으면 "사용자 정의 라이선스"로 기록한다(§3.2). [추정/미확인]
- **환각 위험을 도입 판단의 핵심 항목으로 둔다.** 모르는 질문에도 답을 시도해 환각률이 93%라는 보도가 있다(2차, AA 원문 수치 미확인). 사실 정확성이 필요한 기능(질의응답, 요약, 인용)에는 부적합하고, 결과를 코드나 사람이 검증하는 추출·분류·초안에 적합하다. AA-Omniscience 원문 값을 확인하고 우리 데이터로 거절률과 오류율을 직접 잰다. [부분: 2차]
- **총비용은 과제당 비용이다.** 단가가 낮고 출시 후 인하 보도가 있으며, 독립 측정에서 작업당 비용이 M3의 약 43%($0.22 대 $0.51)였다. MiniMax가 말한 70% 절감보다 독립 측정의 감소 폭이 작다. 재시도와 검증 실패 비용(상위 모델로 올리는 비율)까지 포함해 우리 과제로 계산한다. [부분, 충돌]
- **벤더 수치로 결정하지 않는다.** DeepSWE v1.1 73.7%, "M3보다 약 3배 빠르다"는 벤더 주장이고 독립 재현이 없다. 독립 지수는 42(비교 중앙값 13)이지만 지수 버전에 따라 M3와 순위가 뒤바뀐다(M3 29 또는 44). 후보 비교는 같은 과제, 같은 조건의 자체 실측으로 한다. [부분: 벤더 주장, 충돌]
- **데이터 거버넌스.** 싱가포르 법인 Nanonoble Pte. Ltd.가 정책을 발행하고 데이터가 미국에 저장된다는 독립 안내와 중국을 가리키는 오래된 정책이 충돌하며, 포괄적 학습 제외 약속과 ZDR은 공개 문서로 확인되지 않는다. 약관·개인정보 정책을 원문으로 읽고 법무·보안 검토를 거친다. [부분, 충돌]
- **공급 연속성.** 프리뷰(9월 27일)에서 정식(10월 19~20일)까지 한 달, 그 뒤 가격 인하가 있었다. 가격·한도·ID가 짧은 기간에 바뀌었으므로 모델 교체 절차, 폴백 모델, 회귀 시험을 도입 조건으로 둔다. 사용할 경로(API, Token Plan, MiniMax Code)의 한도와 약관을 확인한다. [부분]
- **제공자 안전장치와 규정.** 규제 적합성은 모델이 아니라 시스템 전체에 대해 판단하고 모델 카드를 규정 준수의 근거로 쓰지 않는다.

## 4. 근거와 한계
- 출시 단계·파라미터 경고·가중치 충돌: [eesel: MiniMax M3.1 Flash](https://www.eesel.ai/blog/minimax-m3-1-flash), [DataNorth: M3.1 Flash 프리뷰](https://datanorth.ai/news/minimax-releases-m3-1-flash-preview), [UsagePricing: M3.1 Flash API 출시](https://www.usagepricing.com/blueprint/activity/minimax-2026-10-19-m3-1-flash-api-launch), [Vals AI: MiniMax M3.1 Flash](https://www.vals.ai/models/minimax_MiniMax-M3.1-flash) (스니펫만) [부분, 충돌]
- 가격·비용: [Let's Data Science: M3.1 Flash 가격 인하](https://letsdatascience.com/news/minimax-cuts-m31-flash-token-prices-dbc14153), [Braindetox: M3.1 Flash 비용](https://braindetox.kr/en/posts/minimax_m3_1_flash_agent_cost_2026.html) (스니펫만) [부분]
- 독립 지수·환각 보도: [Artificial Analysis: MiniMax-M3.1-Flash](https://artificialanalysis.ai/models/minimax-m3-1-flash), [MyClaw: M3.1 Flash 대 M3](https://myclaw.ai/blog/minimax-m3-1-flash-vs-m3) (스니펫만) [부분, 충돌]
- 데이터 정책(2차): [Flowith: MiniMax 데이터 안전 FAQ](https://flowith.io/blog/minimax-faq-data-safety), [Opper: MiniMax](https://opper.ai/provider/minimax) (스니펫만) [부분, 충돌]
- 한계: MiniMax 공식 모델 카드·약관 본문을 읽지 못했다. 도입 전에 공식 문서에서 확인한다.
