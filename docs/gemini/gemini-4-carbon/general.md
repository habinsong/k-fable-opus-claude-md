# Gemini 4 Carbon · 범용 (제한 공개 대비) — 조사 기록
> 제공자: Google · 모델 ID: 미공개 [미확인] · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-carbon/general.md`](../../../md/gemini/gemini-4-carbon/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 상태 — Gemini 4 Carbon (2026-11-03 기준 제한 공개)
Google 공식 도메인(`blog.google`, `deepmind.google`)의 검색 스니펫으로 확인한 내용이다. 본문은 이 환경에서 열리지 않았다. 별도 표기가 없으면 [부분]이다.

### 2.1 확인된 것
- **발표됐다.** Google DeepMind가 "Gemini 4 Carbon: our next frontier model"을 공개했다. Google은 이를 장시간(long-horizon) 엔지니어링과 사이버 방어에서 가장 강한 모델이라고 소개하고, Artificial Analysis Intelligence Index v5.0에서 59로 1위라고 주장한다. 같은 지수에서 Argon은 50, Opus 5.5는 58로 정리한 2차 보도가 있다. 지수 수치는 Google의 주장이다.
- **일반에게 열려 있지 않다.** Google은 미국 정부의 자발적 사전 시험 절차에 참여 중이라고 밝혔고, 접근은 사이버 방어 담당자 일부로 시작해 Fairwind 프로그램을 통해 신뢰할 수 있는 파트너로 단계적으로 넓힌다고 한다. 개발자·기업·소비자 일반 공개는 아직이다.
- **Fairwind 프로그램은 승인된 신뢰 파트너 전용이다.** 파트너는 승인된 위협 시뮬레이션, 리버스 엔지니어링, 방어·학술 연구 목적의 악성코드 분석 같은 이중 용도 작업으로 제한된다. 파트너가 어떤 모델을 받는지는 글마다 다르다(Argon 또는 Gemini 3.8 Flash Cyber). Carbon 발표문은 Carbon이 추가되면 무엇을 받는지 밝히지 않았다.
- **사이버 벤치마크 수치는 보호 장치 없이 측정됐다.** Google 자체 발표에 따르면 취약점 찾기(SEC-bench Pro) 88.2%, 악용(ExploitGym) 54.8%, 패치(CWE-bench) 71.0%이고 이는 안전장치 없이 평가한 값이다. 배포 모델의 행동과 같다는 뜻이 아니다. 벤더 수치다.

### 2.2 확인되지 않은 것
- 모델 ID, 가격, 컨텍스트와 최대 출력, `thinking_level` 지원 범위, 도구 지원, 데이터 보관, 일반 공개 일정은 모두 [미확인]이다. 이 폴더의 어떤 문장도 Carbon의 일반 사용 성능이나 동작을 단정하지 않는다.
- 출시 전에 모델 ID 문자열을 코드에 박지 않는다. 공식 모델 목록에서 확인한 ID만 쓴다.

### 2.3 잠정 규칙
- **접근 권한이 없으면 Argon을 쓴다.** Carbon은 승인된 조직만 쓸 수 있다. 접근 권한을 얻으려는 우회(타인 계정 사용, 약관 회피)를 하지 않는다. 권한이 있는 조직은 Fairwind 프로그램의 조건을 따른다.
- **접근 권한이 있어도 Argon 문서를 기준선으로 둔다.** 같은 세대의 직전 모델이므로 `gemini/gemini-4-argon/` 문서의 규칙(thought signature, `thinking_level`, MINIMAL 400, 가격, 검증 강제)을 잠정 적용한다. Carbon에서 같다는 보장은 없다. [추정]
- **방어 목적 외 사용을 하지 않는다.** 이 저장소의 문서는 이중 용도 능력을 가진 모델을 공격 목적으로 쓰도록 돕지 않는다. 승인된 방어·학술 연구 범위 안에서만 쓰고, 파괴적·외부 영향 동작은 사람의 승인을 거친다(§1.6).

### 2.4 일반 공개 시 확인 체크리스트 (공식 문서에서 직접)
1. 모델 ID, 별칭, 지원 플랫폼, 폐기 예정일. 2. 가격·캐시·배치 요금(Argon은 2026-11-30 이후 $4/$20). 3. 컨텍스트, 최대 출력, 입출력 통합 한도. 4. `thinking_level` 범위와 기본값. 5. 도구 지원(함수 호출, thought signature, 컴퓨터 사용, 명시적 캐싱, Live API). 6. 안전장치와 거부 범주, 이중 용도 작업의 접근 조건. 7. 데이터 보관·학습 사용·규제 인증. 8. 모델 카드의 임계 능력 평가와 완화 조치. 9. 독립 평가(Artificial Analysis 등)의 지표·하네스·날짜. 10. Antigravity CLI와의 지원 상태.

### 2.5 비판적 점검
- **벤더 1위 주장을 독립 평가 전에 확정하지 않는다.** 지수 59는 Google이 인용한 수치이고, 같은 회사의 Argon도 발표 때 여러 벤치마크 1위를 주장했지만 독립 정리에서는 Opus 5.5에 뒤졌다. [부분]
- **보호 장치 없는 벤치마크는 배포 성능이 아니다.** 사이버 수치는 안전장치 없이 평가한 값이다. 일반 공개 후 실제로 거부되는 범위를 따로 측정해야 한다.
- **접근 단계가 바뀐다.** Fairwind에서 추가 파트너로 넓히는 단계가 진행 중이므로 이 문서의 접근 서술은 곧 낡을 수 있다.
- **출시 직후 리뷰는 얕다.** 같은 벤더 수치를 반복하는 글이 많다.

## 4. 근거와 한계
- 발표·접근·사이버 벤치마크: [Gemini 4 Carbon: our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Fairwind Program](https://deepmind.google/fairwind-program/), [Google 블로그: Fairwind](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/) (검색 스니펫만) [부분]
- 지수 비교: [Layer3 Labs: Gemini 4 Argon 리뷰](https://www.layer3labs.io/guides/gemini-4-argon-review) [부분: 2차]
- 직전 모델 규칙: 같은 저장소의 `gemini/gemini-4-argon/` 문서.
- 한계: Google 공식 본문을 열지 못했다. Fairwind 파트너가 받는 모델, 일반 공개 일정은 확인하지 못했다.
