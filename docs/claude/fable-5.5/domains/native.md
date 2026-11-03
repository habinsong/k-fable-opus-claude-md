# Claude Fable 5.5 · 네이티브 (미출시 대비) — 조사 기록
> 제공자: Anthropic · 모델 ID: 미정(공식 확인 전 [미확인]) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.5/native.md`](../../../../md/claude/fable-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용 (잠정)
2026-11-03 기준 Fable 5.5는 공식 목록에 없다. 모델 상태와 출시일 체크리스트는 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 출시 전에는 `claude/fable-5.1/native.md`를 적용한다.

**출시 후 네이티브 작업에서 따로 확인할 것**
- 안전장치의 거짓 양성. Fable 5.1에서는 컴파일 확인형 질문, 덜 알려진 언어, 도구 출력의 base64가 원인이었다. 5.5의 원인 목록과 거부 범주를 공식 문서에서 확인하고, 같은 질문 표현으로 재현해 본다.
- 사이버 인접 작업의 경계. 소스 코드에서 취약점을 찾는 일이 계속 허용되는지, 검증 프로그램이 필요한 범위가 바뀌었는지 확인한다.
- 작은 수정에서 파일 전체를 다시 쓰는 경향과 범위 밖 변경, 필요 이상의 테스트 추가. `git diff --stat`으로 변경 크기를 비교한다.
- 테스트에 맞춘 하드코딩이나 보조 스크립트 우회 경향. 테스트·기대값·경고 설정이 바뀌는지 `git diff`로 확인한다.
- Terminal-Bench 같은 벤더 수치가 나와도 Artificial Analysis 등 독립 측정이 나오기 전에는 주장으로만 취급한다. Fable 5.1에서도 지표에 따라 순위가 갈렸다.
- 시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 모델이 바뀌어도 승인 없이 건드리지 않는다.

**잠정 운용**
- 출시 전 시스템 코드 작업은 Fable 5.1과 Opus 5.5로 진행한다. sanitizer 빌드와 성능 측정은 사람이 직접 확인한다.

## 4. 근거와 한계
- 미출시 확인: [Models overview](https://platform.claude.com/docs/en/models/overview) [확인: 2026-11-03에 직접 읽음]
- 잠정 규칙과 거짓 양성 사례: 같은 저장소의 `claude/fable-5.1/native.md`, [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) [확인: Fable 5.1 기준]
- 한계: 이 문서의 모든 5.5 관련 서술은 확인 항목 목록이며 모델 특성이 아니다.
