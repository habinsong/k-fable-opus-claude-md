# Muse Spark · 앱 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: 최신 버전 1.3의 API ID는 확인 필요(`muse-spark-1.3` 형태로 보이나 미확인), 오픈 가중치 변형은 "Muse Spark Open" · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-spark/app.md`](../../../md/muse/muse-spark/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 폐쇄형 API 모델(오픈 변형은 별도 라이선스), 버전 갱신 잦음, 데이터 약관 불분명, 모바일 개발 독립 평가 없음, 이미지 입력.

**앱에 내장할 때**
- **기기 안에서 돌릴 모델이 아니다.** 폐쇄형 Spark는 API로만 쓴다. 오픈 가중치 변형(Spark Open)도 M5 Ultra 맥 스튜디오 두 대로 로컬 실행이 가능하다는 수준이라 휴대 기기용이 아니다. 모바일 온디바이스는 `gemma-4-e2b`, `gemma-4-e4b` 문서를 본다. [부분]
- **API 키를 앱 바이너리나 리소스에 넣지 않는다.** 앱에서 직접 호출하지 말고 자체 백엔드에서 키 보관, 사용량 제한, 요청 검증, 로깅을 한다(§3.1 비밀 규칙). 모델 출력은 신뢰하지 않는 입력으로 취급해 서버에서 검증한 뒤 앱에 전달한다.
- **개인정보 선언과 실제 동작을 맞춘다.** 사용자 입력을 Meta Model API로 보내면 수집·전송 항목을 앱 스토어의 개인정보 선언(Apple 개인정보 영양 표시, Google Play 데이터 보안 양식)과 처리방침에 반영한다. 데이터 처리 서술이 충돌한다(Meta는 프롬프트·응답을 학습에 쓰지 않는다고 했다는 전언 대 약관상 사용 데이터로 API를 개선할 수 있고 무료 서비스 콘텐츠는 분리 후 학습에 쓸 수 있다는 서술). 프롬프트 보관 기간과 영 보관 등급도 공개돼 있지 않다. [미확인, 충돌] 출시 전에 약관을 원문으로 읽고, 아동·민감정보는 확인 전에 보내지 않는다. 값싼 "Contributor" 등급($0.10/$0.20)은 트래픽이 학습에 쓰일 수 있다는 서술이 있어 쓰지 않는다.
- **이미지 입력을 쓰면 사진에 담긴 개인정보를 고려한다.** 이 모델은 이미지를 입력으로 받는다. 얼굴, 위치, 문서가 담긴 사진은 서버와 제3자로 전송된다. 약관 확인과 사용자 동의 없이 보내지 않는다.
- **버전 교체에 대비한다.** 1.1(7월), 1.2(8월), 1.3(9월)로 한두 달마다 갱신됐고 상위 모델 Muse Wonder도 있다. 서버 쪽 모델 설정, 폴백 모델, 회귀 시험, 기능 플래그를 두어 앱 업데이트 없이 교체할 수 있게 한다. [부분]
- **비용은 과제당으로 서버에서 제한한다.** 단가는 입력 $1.25 / 출력 $4.25(1.3까지 같다는 서술)지만 1.3은 에이전트 평가에서 입력 토큰을 약 57% 더 썼다는 독립 보고가 있다. 사용자당 한도와 `max_tokens`를 서버에 두고 실제 청구서로 확인한다. [부분]
- **오픈 가중치를 번들·배포하려면 라이선스를 먼저 읽는다.** 자체 "Muse Model License"는 상업 이용 조건이 제한적이고 재판매에 Meta 승인이 필요하며 제품에 "Built with Muse Spark Open" 표시 의무가 있다는 서술이 있다. 원문을 확인하고 고지 의무를 지킨다(§1.5). [부분/미확인]

**개발 보조로 쓸 때**
- **모바일(Kotlin·Swift) 코드에 대한 독립 평가는 찾지 못했다.** [미확인] 컴파일·린트·단위 테스트·UI 테스트로 검증하고, 수명주기·권한·비동기 처리가 걸린 구현은 상위 모델 문서를 따른다(`claude/sonnet-5.5`, `gpt-6.1-sol`, `gemini-4-argon`, 또는 `muse-wonder`).
- 스토어 규정은 기억으로 답하지 않고 공식 문서로 확인한다(§3.2). 서명 키, 프로파일, 스토어 제출·배포는 승인 후에만 한다.

## 4. 근거와 한계
- 오픈 변형 크기·라이선스·배포: [The New Stack: Muse Spark Open](https://thenewstack.io/meta-muse-spark-open/), [Trending Topics: 라이선스](https://www.trendingtopics.eu/muse-spark-open-meta-open-weight-license/) (스니펫만) [부분]
- 데이터 약관(충돌): [ConductAtlas: Llama API 약관](https://conductatlas.com/platform/meta/llama-api-terms-of-service/provision/CA-P-060472/meta-may-use-usage-data-to-improve-api/), [Standard Compute: Meta](https://standardcompute.com/providers/meta) (스니펫만) [미확인, 충돌]
- 가격·Contributor 등급·버전: [DataLearner: Muse Spark 1.3](https://www.datalearner.com/en/ai-models/pretrained-models/muse-spark-1-3), [DataNorth: 1.3 출시](https://datanorth.ai/news/meta-launches-muse-spark-1-3) (스니펫만) [부분, 충돌]
- 한계: 모바일 개발에 대한 평가가 없다. Meta 공식 약관·라이선스 본문을 읽지 못했다.
