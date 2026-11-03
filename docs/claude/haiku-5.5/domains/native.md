# Claude Haiku 5.5 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-haiku-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/haiku-5.5/native.md`](../../../../md/claude/haiku-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 어려운 자율 코딩에는 부적합, 지식 회상 36%, `low`에서 검사를 건너뜀, 안전장치 거부에 서버 쪽 대체 없음.

- **시스템 코드의 구현·수정에는 쓰지 않는다.** 메모리 관리, 동시성, ABI는 문법이 맞아도 틀리기 쉽고 틀린 결과가 보안 문제로 이어진다. Terminal-Bench 4.0에서 Sonnet 5.5(70.6%)에 크게 뒤지는 39.2%(Artificial Analysis 자체 하네스에서는 33%)다. [부분] 이 영역은 `sonnet-5.5` 이상 문서를 따른다.
- **써도 되는 좁은 일.** 컴파일러 오류 메시지 분류, 크래시 로그·스택 트레이스 그룹화, 빌드 로그 요약, 헤더 주석 초안, 이름 바꾸기 같은 기계적 변환. 도구 출력과 대조할 수 있는 일로 한정한다. 하위 에이전트로 여러 파일의 로그를 읽어 요약하는 용도에 맞다.
- **API·플래그·시스템 호출을 기억에서 가져오지 않는다.** 정답 비율 36%(AA-Omniscience)다. [부분] 시스템 API, 링커·컴파일러 옵션은 매뉴얼과 도구 출력으로 확인한다.
- **변경 후 실제 검사를 강제한다.** `low`·`medium`에서는 코드를 바꾸고 검사 없이 완료로 보고할 수 있다. 프로젝트 테스트·타입 체커·빌드를 돌리게 하고, sanitizer 빌드를 못 돌렸으면 "미실행"으로 보고한다. [확인]
- **분석 결과로 설정을 바꾸지 않는다.** "이 sanitizer 경고는 무시해도 된다"는 말로 억제 지시문을 넣지 않는다. 테스트·경고·sanitizer 설정이 바뀌었는지 `git diff`로 확인한다.
- **긴 에이전트 프롬프트에서 일찍 멈출 수 있다.** 계속 진행 지시를 넣거나 `medium` 이상을 쓴다. [확인]
- **거부는 클라이언트에서 처리한다.** 보안 인접 요청이 `cyber` 범주로 거부될 수 있고 서버 쪽 대체가 없다. 같은 요청을 다시 보내도 대개 같은 거부가 온다. 정당한 보안 작업은 Cyber Verification Program을 확인한다. [확인]
- **시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다.**

## 4. 근거와 한계
- 검증 강제·조기 중단·거부 처리: [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) [확인]
- Terminal-Bench·정답 비율: [eesel.ai 리뷰](https://www.eesel.ai/blog/claude-haiku-5-5-review), [Miraflow](https://miraflow.ai/blog/claude-haiku-5-5-benchmarks-pricing-explained-2026) [부분]
- 한계: C·C++·Rust 시스템 코드에 대한 Haiku 5.5 전용 독립 평가는 없다. 사용 범위 제한은 일반 지표에서 도출한 보수적 권고다.
