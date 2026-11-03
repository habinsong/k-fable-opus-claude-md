# Claude Sonnet 5.5 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-sonnet-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/sonnet-5.5/native.md`](../../../../md/claude/sonnet-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `high`(에이전트는 `medium`부터), `xhigh`·`max`는 요청하지 않은 점검 라운드를 시작함, 사이버 요청은 Sonnet 5로 넘어갈 수 있음.

- **시스템 코드는 `high`에서 시작하고 `xhigh`는 어려운 문제에만.** Anthropic은 가장 어려운 장시간 작업에는 Opus를 권한다. 경쟁 상태, 메모리 손상, 컴파일러 최적화가 얽힌 버그에서 같은 가설이 두 번 틀리면 Opus 5.5에 같은 재현 절차와 로그를 넘긴다. [확인/권고]
- **`xhigh`·`max`의 자체 점검 라운드를 끊는다.** 이 레벨에서는 요청한 일이 끝난 뒤에도 스스로 리뷰·강화 라운드를 돌리고 하위 에이전트를 띄워 관련 수정을 덧붙인다. 시간과 토큰이 크게 든다. "요청한 일이 끝나고 검사가 통과하면 멈추고 보고하라. 스스로 추가 리뷰를 시작하지 말고 요청이 없으면 리뷰어 하위 에이전트를 띄우지 말라"를 쓰면 `max`에서 세션 비용이 약 3분의 1 줄었다고 한다. 일상 작업은 `high` 이하에서 돌린다. [확인]
- **`low`에서는 검증을 건너뛴다.** 의존성이 설치되지 않았다는 이유로 프로젝트 테스트를 건너뛸 수 있다. 실제 검사(테스트, 타입 체커, 빌드, 바뀐 명령 자체)를 요구하고, 불가하면 어떤 검사를 왜 못 했는지 말하게 한다. sanitizer 빌드를 돌리지 못했으면 "미실행"으로 보고한다. [확인]
- **보안 인접 요청의 경계.** 소스에서 취약점을 찾는 일은 허용되고 위험도가 높은 이중 용도 사이버 작업은 제한된다. 거부(`cyber`)는 서버 쪽 대체로 Sonnet 5에서 재시도될 수 있고, 높은 위험의 사이버 요청이 눈에 띄게 Sonnet 5로 넘어간다는 보고가 있다. 정당한 작업이 막히면 Cyber Verification Program을 확인한다. [확인/부분]
- **도구 호출 이름이 어긋날 수 있다.** `bash`와 `Bash`처럼 대소문자가 다른 호출이나 조금 다른 매개변수 이름을 낼 수 있다. 하네스는 명확하면 받아 주거나 기대한 이름을 담은 `is_error: true` 결과를 돌려준다. [확인]
- **끈기가 약하다는 사용자 보고.** 답을 얻으려고 계속 시도하는 데 소극적이라 점수가 낮아진 사례가 있다. 개별 후기다. [부분] 같은 실패가 3번 반복되면 접근을 바꾸거나 막힌 지점을 보고하게 한다(§1.2).
- **테스트에 맞춘 우회를 막는다.** 테스트·기대값·경고 설정이 바뀌었는지 `git diff`로 확인한다. 공개 헤더·ABI 변경은 호출자 영향부터 확인하고 범위 밖 변경은 되돌린다.
- **시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다.**

## 4. 근거와 한계
- 자체 점검 라운드·검증·도구 호출 허용: [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) [확인]
- 거부·대체: [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5) [확인]
- 끈기·Opus와의 비교: [Thomas Wiegold 비교](https://thomas-wiegold.com/blog/claude-sonnet-5-5-review/), [AIToolsReview](https://aitoolsreview.co.uk/insights/claude-sonnet-5-5) [부분]
- 한계: C·C++·Rust 시스템 코드에 대한 Sonnet 5.5 전용 독립 평가는 찾지 못했다.
