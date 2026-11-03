# Muse Wonder · 앱 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/app.md`](../../../../md/muse/muse-wonder/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델이라 기기 내 실행 불가, 입력 $4 / 출력 $20, 토큰 소비 많음, Active Memory의 저장 정보 부족, 데이터 약관 충돌, 모바일 개발 독립 평가 없음.

**앱에 내장할 때**
- **기기 안에서 돌릴 모델이 아니다.** 폐쇄형이며 가중치를 받을 수 없다. 앱은 서버를 거쳐 호출하는 구조만 가능하다. 모바일 온디바이스는 `gemma-4-e2b`, `gemma-4-e4b` 문서를 본다.
- **API 키를 앱 바이너리나 리소스에 넣지 않는다.** 앱에서 직접 호출하지 말고 자체 백엔드에서 키 보관, 사용량 제한, 요청 검증, 로깅을 한다(§3.1 비밀 규칙). 모델 출력은 신뢰하지 않는 입력으로 취급해 서버에서 검증한 뒤 앱에 전달한다.
- **Active Memory를 앱 기능으로 쓰기 전에 보관 조건을 확인한다.** 대화를 넘어 맥락을 유지하는 기능이라 사용자 정보가 모델 측 서비스에 장기 보관될 수 있다. API에서의 노출 방식, 저장 위치·기간, 사용자별 삭제 방법을 찾지 못했다. [미확인] 앱의 개인정보 선언(Apple 개인정보 영양 표시, Google Play 데이터 보안 양식)과 처리방침, 삭제 요청(정보주체 권리) 처리에 반영할 수 있는지 확인되기 전에는 기억 기능을 켜지 않는다. 제3자(연락처 등)에 대한 개인정보를 기억에 넣지 않는다. 별개 제품인 개인용 Muse 에이전트가 기억으로 연락처 프로필을 만든다는 프라이버시 우려 보도가 있다. [부분: 별개 제품]
- **개인정보 선언과 실제 동작을 맞춘다.** 사용자 입력을 Meta Model API로 보내면 수집·전송 항목을 선언에 반영한다. 데이터 처리 서술이 충돌하고(학습 불사용 전언 대 약관상 사용 데이터로 API 개선 가능), 보관 기간·영 보관 등급이 공개돼 있지 않다. [미확인, 충돌] 출시 전에 약관을 원문으로 읽고, 아동·민감정보는 확인 전에 보내지 않는다.
- **비용을 과제당으로 서버에서 제한한다.** 단가는 입력 $4 / 출력 $20이고 AA 지수 실행에서 출력 토큰이 비교군 중앙값의 약 1.5배였다. 사용자당 한도, `max_tokens`, 요청 빈도 제한을 서버에 두고 실제 청구서로 확인한다. 높은 노력 단계는 비용이 크므로 단순 질의는 `muse-spark`나 더 싼 모델로 라우팅한다. [부분]
- **Wonder Full을 앱 백엔드로 가정하지 않는다.** 공개 API는 Wonder만 제공하고 Full은 Muse Code 구독자 전용이다. [부분]
- **모델 교체를 앱 업데이트 없이 할 수 있게 설계한다.** Muse 계열은 석 달 사이에 여러 번 갱신됐다. 서버 쪽 모델 설정, 폴백 모델, 회귀 시험, 기능 플래그를 둔다.
- **안전 분류기의 거부를 UX에 반영한다.** 모델 카드가 시스템 수준 분류기를 적용한다고 밝혔다. 정당한 요청이 거부될 수 있으므로 거부 응답 처리와 폴백을 설계하고 거부율을 우리 시나리오로 시험한다. [부분/추정]

**개발 보조로 쓸 때**
- **모바일(Kotlin·Swift) 코드에 대한 독립 평가는 찾지 못했다.** [미확인] 컴파일·린트·단위 테스트·UI 테스트로 검증하고, 수명주기·권한·비동기 처리가 걸린 구현은 상위 모델 문서(`claude/sonnet-5.5` 이상, `gpt-6.1-sol`, `gemini-4-argon`)와 같은 과제로 비교한다.
- 스토어 규정은 기억으로 답하지 않고 공식 문서로 확인한다(§3.2). 서명 키, 프로파일, 스토어 제출·배포는 승인 후에만 한다.

## 4. 근거와 한계
- Active Memory·Active Focus 설명: [Digit: Active Memory와 Active Focus](https://www.digit.in/features/general/meta-muse-wonder-explained-what-active-memory-and-active-focus-do.html), [Android Headlines: 장기 기억](https://androidheadlines.com/2026/10/meta-muse-wonder-ai-model-long-term-memory-upgrade.html) (스니펫만) [부분: 벤더 설명]
- 프라이버시 우려(별개 제품): [Let's Data Science: 연락처 프로필](https://letsdatascience.com/news/meta-muse-creates-profiles-of-users-contacts-15585c25), [Atlanta News First](https://www.atlantanewsfirst.com/2026/10/09/metas-new-muse-ai-agent-raises-privacy-concerns/) (스니펫만) [부분]
- 토큰 소비: [Artificial Analysis: Muse Wonder (Max)](https://artificialanalysis.ai/de/models/muse-wonder) (스니펫만) [부분]
- 데이터 약관: [ConductAtlas: Llama API 약관](https://conductatlas.com/platform/meta/llama-api-terms-of-service/provision/CA-P-060472/meta-may-use-usage-data-to-improve-api/) (스니펫만) [미확인, 충돌]
- 한계: 모바일 개발과 Active Memory의 저장 정책에 대한 1차 자료를 읽지 못했다.
