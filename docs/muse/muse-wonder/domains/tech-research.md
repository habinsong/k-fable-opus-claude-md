# Muse Wonder · 기술 연구 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/tech-research.md`](../../../../md/muse/muse-wonder/tech-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/tech-research.md`](../../../_common/domain-rules/tech-research.md)

## 2. 이 모델의 기술 조사 운용, 그리고 이 모델을 평가할 때
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델, 입력 $4 / 출력 $20(Opus 5.5와 비슷한 가격대라는 보도), 독립 평가 점수에서 Opus 5.5에 못 미침, Meta 표와 독립 값 불일치, 토큰 소비 많음, Wonder Full은 구독 전용, 안전 보고서·데이터 약관·Active Memory 정보 부족.

**이 모델에게 기술 조사를 시킬 때**
- 분류·정리 단계에만 쓴다. 후보를 정해진 기준(라이선스 유형, 지원 언어, 릴리스 날짜)으로 분류해 표로 만들 때, 값은 사람이 확보한 1차 자료 텍스트에서 추출하게 하고 원문에 없으면 null로 둔다.
- 라이선스 호환성, 특허, 규정 적용 여부, 도입 권고는 단정시키지 않는다(§3.2, §3.5). 후보를 지나치게 높게 평가하는 경향(아첨)은 측정된 바 없으므로 사람이나 상위 모델이 근거를 보고 판단한다.
- 환각·사실성 평가가 없으므로 모델이 말하는 버전·날짜·가격·라이선스는 모두 1차 출처로 다시 확인한다.

**Muse Wonder를 도입 후보로 평가할 때**
- **Wonder와 Wonder Full과 Spark를 구분한다.** 공개 API로 호출 가능한 것은 Wonder(Full은 Muse Code Power/Maximum 구독자 전용)이다. Full의 헤드라인 수치(독립 평가 점수 56, Terminal-Bench 4.0 57%)를 Wonder(52, 52%)의 능력으로 읽지 않는다. 더 싼 하위 모델은 `muse-spark`(1.3), 오픈 가중치는 Spark Open뿐이다. 후보 문서에 정확한 모델명을 쓴다. [부분]
- **Meta의 수치로 결정하지 않는다.** Meta 모델 카드의 AA 벤치마크 점수 항목(Full 59.0)은 AA 게시값(56)과 다르고, AutomationBench 값도 다르며, 대부분 `max` 단계의 값이고, 일부는 Meta 내부 LLM 심사 평가(MemoryBench)다. 독립 평가 점수는 Opus 5.5(58)에 못 미친다. 후보 비교는 같은 과제, 같은 노력 단계, 같은 예산의 자체 실측으로 한다. [부분, 충돌]
- **총비용은 과제당 비용이다.** 단가가 Opus 5.5와 비슷한 가격대라는 보도가 있고($4/$20), AA 벤치마크 점수 실행에서 출력 토큰이 비교군 중앙값의 약 1.5배(1.3억 대 8,500만)였으며 평균 과제당 $4.52였다는 서술이 있다. 가격표만 보지 말고 우리 과제의 토큰 사용량으로 비교한다. 독립 평가 점수에서 앞서는 모델이 같은 가격대에 있다면 선택 근거가 약해진다. [부분]
- **접근 경로와 구독 의존.** Meta Model API(공개 API), Muse Code 구독(Full 포함), Muse 앱(순차 적용, 일정 없음)의 약관·한도·SLA가 다르다. Full에 의존하는 설계는 구독 정책 변경 위험이 크다. 사용하려는 경로의 서비스 수준과 이용 정책을 확인한다. [부분]
- **데이터 거버넌스 — 가장 큰 미확인 영역.** 처리 서술이 충돌한다(프롬프트·응답을 학습에 쓰지 않는다는 전언 대 약관상 사용 데이터로 API를 개선할 수 있고 무료 서비스 콘텐츠는 분리 후 학습에 쓸 수 있다는 서술). 보관 기간과 영 보관 등급이 공개돼 있지 않다. Active Memory의 저장 위치·기간·삭제 방법은 찾지 못했다. Meta 소비자 제품은 AI 상호작용을 광고 개인화에 쓸 수 있다고 알려졌고 API에 적용되는지는 미확인이다. [미확인, 충돌] 약관과 개인정보 처리방침을 원문으로 읽고 법무·보안 검토를 거친다.
- **안전 문서가 불완전하다.** 모델 카드는 완화 조치가 없다면 Wonder Full이 화학·생물 위협의 고위험 기준에 도달할 가능성을 배제하지 못한다고 하고, 전체 안전 보고서를 약속했으나 출시 시점에 공개되지 않았다. 사이버 위험 평가의 세부도 찾지 못했다. 규제·내부 리스크 심사(AI 위험 등급, 공급자 실사)에 필요한 문서가 갖춰졌는지 확인하고, 없으면 "자료 미비"로 기록한다. [부분]
- **폐쇄형이라는 점.** 가중치와 구조·학습 데이터 정보가 공개되지 않아 저작권·라이선스 출처 검증, 자체 호스팅, 오프라인 사용이 불가능하다. 학습 데이터의 저작권 문제는 확인할 수 없다(§1.5). [부분/미확인]
- **공급 연속성과 버전 관리.** Spark 1.1(7월)·1.2(8월)·1.3(9월)·Spark Open(10월)·Wonder(10월)가 석 달 사이에 나왔다. 구버전 폐기 일정, 모델 교체 절차, 폴백 모델, 회귀 시험을 도입 조건으로 둔다. [부분]
- **제공자 안전장치와 규정.** 시스템 수준 분류기가 정당한 요청을 거부할 수 있다. 규제 적합성은 모델이 아니라 시스템 전체에 대해 판단하고, 모델 카드를 규정 준수의 근거로 쓰지 않는다.

## 4. 근거와 한계
- 출시·접근 경로·가격·기능: [Free Press Journal: Muse Wonder 출시](https://www.freepressjournal.in/tech/meta-launches-muse-wonder-muse-wonder-full-advanced-ai-models-key-features-pricing), [Let's Data Science](https://letsdatascience.com/news/meta-launches-muse-wonder-and-muse-wonder-full-for-agentic-t-41113cca), [MindStudio: 출시](https://www.mindstudio.ai/blog/meta-muse-wonder-launch) (스니펫만) [부분]
- 독립 평가 점수·Meta 표와의 불일치·가격 비교: [Braindetox: 평가 조건](https://braindetox.kr/en/posts/meta_muse_wonder_agent_models_release_2026.html), [Implicator: Opus 아래 순위](https://implicator.ai/meta-muse-wonder-ranks-below-claude-opus), [Pasquale Pillitteri: Opus 5.5 가격·벤치마크](https://pasqualepillitteri.it/en/news/23176/muse-wonder-launches-opus-5-5-prices-trails-benchmarks) (스니펫만) [부분, 충돌]
- 토큰 소비·과제당 비용: [Artificial Analysis: Muse Wonder (Max)](https://artificialanalysis.ai/de/models/muse-wonder) (스니펫만) [부분]
- 안전 서술: [BetaNews: Muse Wonder](https://betanews.com/article/muse-wonder-frontier-model-developers/) (스니펫만) [부분]
- 데이터 약관: [ConductAtlas: Llama API 약관](https://conductatlas.com/platform/meta/llama-api-terms-of-service/provision/CA-P-060472/meta-may-use-usage-data-to-improve-api/), [Standard Compute: Meta](https://standardcompute.com/providers/meta) (스니펫만) [미확인, 충돌]
- 한계: Meta 공식 문서·모델 카드·약관·전체 안전 보고서를 읽지 못했다. 도입 전에 공식 문서에서 확인한다.
