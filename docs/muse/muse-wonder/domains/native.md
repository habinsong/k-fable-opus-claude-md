# Muse Wonder · 네이티브 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/native.md`](../../../../md/muse/muse-wonder/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델, 컨텍스트 100만 토큰, 터미널 지표 Terminal-Bench 4.0에서 Wonder 52%·Full 57%(독일어 글 서술), Meta 표와 독립 값 불일치, 토큰 소비 많음, C/C++·Rust 평가 없음.

**개발 보조로 쓸 때**
- **터미널·코딩 지표는 조건을 확인해 읽는다.** Terminal-Bench 4.0에서 Wonder Full 57%, Wonder 52%이고 Gemini 4 Argon이 Full과 같은 57%라는 서술이 있다. Meta 자체 표에서도 이 지표는 Opus 5.5가 앞선다고 한다. AutomationBench는 Meta 표와 AA 값이 달라 시험 버전이 다르다는 서술이 있다. 벤치마크 이름·버전·노력 단계·보고 주체(Meta 또는 독립)를 확인하지 않은 숫자를 비교하지 않는다. [부분, 충돌]
- **Wonder Full의 수치를 Wonder의 능력으로 옮기지 않는다.** 두 모델은 지수 값이 다르고(56 대 52) 공개 API는 Wonder만 제공한다. 직접 시험할 수 있는 것은 Wonder다. [부분]
- **C++·Rust·시스템 코드의 언어별 평가는 찾지 못했다.** [미확인] 메모리 관리, 동시성, 수명, ABI는 문법이 맞아도 틀리기 쉬우므로 핵심 변경에는 쓰지 않고, 쓴다면 sanitizer(ASan·UBSan·TSan)와 테스트를 지시문으로 강제한다. 핵심 변경은 `claude/sonnet-5.5` 이상, `gpt-6.1-sol`, `gemini-4-argon` 문서를 따르거나 우리 코드로 같은 과제를 비교한다.
- **Muse Code의 이전 평가를 Wonder에 옮기지 않는다.** 8월 비교(AA 코딩 에이전트 지수: Claude Code(Opus 5) 67, Muse Code(Muse Spark 1.2) 61)에서 Muse 쪽 리팩터링이 구조를 거의 바꾸지 못하고 죽은 코드를 남겼다는 후기가 있다. 이는 Spark 1.2 기반이며 Wonder 기반 평가가 아니다. 한편 한 시험은 PR 222건 검토를 5분 안에 10센트로 끝냈다고 하며 여러 테스터가 주 에이전트 대신 보조 도구로 썼다. 비용 구조가 다르므로 대량 코드 리뷰에는 싼 모델, 어려운 설계에는 상위 모델을 쓰는 분업을 시험해 본다. [부분: 개인 후기, 다른 모델]
- **Muse Code의 플랫폼 제약을 확인한다.** 터미널 전용이며 macOS와 Linux를 지원하고 Windows는 WSL을 통해서만 가능하다는 서술이 있다. 개발 환경이 맞는지 먼저 본다. [부분]
- **에이전트 루프에 안전장치를 먼저 둔다.** Active Focus가 중대한 행동 전에 확인한다는 것은 Meta의 설명이다. 파괴적 명령 차단(권한·훅), 작업 디렉터리 격리, 시간·토큰 한도를 설정하고, 완료 보고는 빌드·테스트·sanitizer 출력과 `git diff`로 확인한다. 테스트·경고·sanitizer 설정이 바뀌었는지도 확인한다. 억제 지시문을 넣거나 검사를 끄는 제안은 따르지 않는다. [부분: 벤더 주장]
- **토큰 소비를 한도로 제어한다.** AA 지수 실행에서 출력 토큰이 비교군 중앙값의 약 1.5배였다. 긴 반복 루프에는 호출 횟수·토큰·시간 한도를 둔다. [부분]
- **미공개 소스를 보내기 전에 약관을 확인한다.** 데이터 처리 서술이 충돌하고 Active Memory의 저장 정책을 찾지 못했다(README.md가 안내하는 개요·운용 문서.4). [미확인, 충돌] 확인 전에는 비밀·고객 코드를 보내지 않는다(§1.6).

**애플리케이션에 내장할 때**
- **모델은 서버 API로 호출한다.** 폐쇄형이라 번들할 수 없다. 클라이언트에 API 키를 두지 않고 자체 백엔드를 거친다. 모델 출력으로 만든 경로·명령·코드를 그대로 실행하지 않으며 파서·역직렬화 코드는 퍼징 대상으로 본다(§3.1).
- **오프라인·자체 호스팅이 필요하면 Wonder가 아니라 다른 모델을 본다.** 같은 계열의 오픈 변형은 Spark Open뿐이고(`muse-spark` 문서) 라이선스가 제한적이다. 소형 로컬 모델은 `gemma-4-e4b`, `qwen3.6-27b` 문서를 본다.

## 4. 근거와 한계
- 터미널 지표·Meta 표와 독립 값 불일치: [Braindetox: 평가 조건](https://braindetox.kr/en/posts/meta_muse_wonder_agent_models_release_2026.html), [MindStudio: Wonder 벤치마크](https://www.mindstudio.ai/blog/muse-wonder-benchmarks-vs-opus-gpt6), [Dev.to: Muse Wonder 벤치마크](https://dev.to/hassann/muse-wonder-benchmarks-1h1n) (스니펫만) [부분, 충돌]
- Muse Code 평가(Spark 1.2 기반): [Artificial Analysis: Claude Code 대 Muse Code](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-muse-code), [The New Stack: Muse와 Claude Code](https://thenewstack.io/meta-muse-claude-code/), [Composio: Muse Code 대 Claude Code](https://composio.dev/blog/muse-code-vs-claude-code) (스니펫만) [부분: 개인 후기, 다른 모델]
- 토큰 소비: [Artificial Analysis: Muse Wonder (Max)](https://artificialanalysis.ai/de/models/muse-wonder) (스니펫만) [부분]
- 한계: 언어별 시스템 코드 평가와 Wonder 기반 Muse Code의 현장 평가가 없다.
