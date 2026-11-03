# Claude Fable 5.1 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-fable-5-1` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.1/native.md`](../../../../md/claude/fable-5.1/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 장시간 코딩에 강점, 안전장치 거짓 양성이 남아 있음, 작은 수정에도 파일을 통째로 쓰는 경향.

- **시스템 코드의 장시간 작업에 쓴다.** 여러 파일에 걸친 변경, 대규모 리팩터링·마이그레이션, 디버깅, 몇 시간 단위 코드 리뷰가 Anthropic이 꼽는 개선 영역이다. [확인: 벤더 서술] Artificial Analysis의 Terminal-Bench v4.0에서는 Astra 59%, Fable 5.1 52%였고 같은 기관의 코딩 에이전트 지수에서는 Claude Code 기준 Fable 5.1이 가장 높았다. 지표마다 순위가 바뀐다. [부분]
- **안전장치 거짓 양성을 피하는 표현을 쓴다.** 거짓 양성이 줄었지만 남아 있다. 원인으로 알려진 것은 컴파일 확인형 질문("이게 컴파일되는가?"), 덜 알려진 언어, 도구 출력의 base64다. "이 프로그램에 버그가 있는가?"로 묻고, 낯선 언어는 문서를 주고, base64가 컨텍스트에 들어가지 않게 한다. 취약점 찾기는 허용된다. 고위험 이중 용도 사이버 작업은 허용되지 않고 검증 프로그램(Mythos 5.1)에 한한다. [확인]
- **작은 수정은 부분 편집으로.** 헤더·소스 몇 줄을 고치려고 파일 전체를 다시 쓰면 diff가 커지고 검토가 어렵다. "필요한 부분만 고쳐라"를 명시하고 `git diff --stat`으로 변경 크기를 확인한다. [확인]
- **범위 밖 변경을 막는다.** 인접 코드 수정이나 필요 이상의 테스트 추가를 하지 않는다. 발견한 문제는 후속으로 보고한다. 공개 헤더·ABI를 건드렸다면 호출자 영향을 먼저 확인한다. [확인]
- **테스트를 통과시키는 것이 목표가 아니다.** Anthropic 지침은 테스트에 맞춘 하드코딩과 보조 스크립트 우회를 피하라고 한다. 테스트가 틀렸거나 불가능한 작업이면 우회하지 말고 알린다. [확인] 테스트·기대값·경고 설정이 바뀌었는지 `git diff`로 확인한다.
- **sanitizer 빌드와 성능 측정은 직접 한다.** 모델의 "이 경고는 무시해도 된다"를 근거로 억제 지시문을 넣지 않는다. 성능 주장은 명령, 입력, 환경, 전후 수치로 쓴다.
- **effort.** `high`에서 시작하고, 어려운 동시성·메모리 손상은 `xhigh`를 비교한다. `max_tokens`를 크게 잡는다. 컴파일 오류 분류 같은 단순 작업은 `medium`이나 `low`로 충분한지 측정한다. [확인]
- **시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다.**

## 4. 근거와 한계
- 거짓 양성·부분 편집·범위 억제: [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) [확인]
- 테스트 하드코딩 회피: [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) [확인]
- 순위 비교: [Artificial Analysis](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) [부분]
- 한계: C·C++·Rust 시스템 코드에 대한 Fable 5.1 전용 독립 평가는 찾지 못했다.
