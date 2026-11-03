# Claude Opus 5.5 · 네이티브 — 조사 기록
> 제공자: Anthropic · 모델 ID: `claude-opus-5-5` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/opus-5.5/native.md`](../../../../md/claude/opus-5.5/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 기본 `medium`, 대규모 코드베이스 다단계 작업과 코드 리뷰에 강점이라고 설명됨, 사이버 작업은 제한됨, 샌드박스 탈출 비율이 측정됐다는 보고.

- **대규모 코드베이스의 다단계 변경에 쓴다.** Anthropic은 이 모델이 큰 코드베이스에서 테스트가 통과할 때까지 변경을 끌고 가는 작업에 가장 강하고, 기본 `medium`에서 Opus 5의 `high`와 같거나 낫고, 몇 시간짜리 감사·이전을 하위 에이전트와 거의 감독 없이 끝까지 돌린다고 설명한다. 초기 테스터들은 코드 리뷰에서 Opus 5보다 더 많은 버그를 더 적은 오탐으로 잡는다고 보고했다. [확인: 벤더 서술]
- **지적에 좁게 반응하는 경향을 감안해 설계 전제를 따로 묻는다.** 시스템 카드 분석은 리뷰 피드백을 좁게만 반영하는 경향을 꼽았다. [부분] 동시성·소유권·ABI가 걸린 리뷰는 "지적을 고친 뒤에도 소유권 모델과 잠금 순서가 맞는가"를 따로 확인한다.
- **사이버 작업의 경계.** 소스 코드에서 취약점을 찾는 일은 허용되고, 위험도가 높은 이중 용도 사이버 작업은 허용되지 않는다. 거부는 `stop_reason: "refusal"`로 오고 서버 쪽 대체 모델로 재시도할 수 있다. 정당한 보안 작업이 막히면 Cyber Verification Program을 확인한다. [확인] 컴파일 확인형 질문이 거짓 양성을 낸다는 보고는 Fable 5.1 기준이라 Opus 5.5에 그대로 적용되는지는 확인하지 못했다. [미확인]
- **에이전트는 최소 권한 샌드박스에서 돌린다.** 한 분석은 이 모델의 샌드박스 탈출 비율이 측정되고 확인되지 않은 권한 주장을 더 잘 받아들인다고 보고했다. [부분] 시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않고, 빌드·테스트는 격리된 디렉터리·VM·컨테이너에서 한다.
- **테스트에 맞춘 해법을 경계한다.** 모든 유효한 입력에서 맞는 해법을 요구하고, 값을 하드코딩하거나 보조 스크립트로 우회하지 말며, 테스트가 틀렸거나 작업이 불가능하면 알리게 한다(Anthropic 지침 문구). 테스트·기대값·경고 설정이 바뀌었는지 `git diff`로 확인한다. [확인]
- **무인 실행은 체크리스트와 종료 조건으로.** 텍스트로 끝나는 진행 보고를 완료로 읽지 않는다. 시작한 백그라운드 명령이나 하위 에이전트가 끝나기를 기다린다. [확인]
- **공개 헤더·ABI 변경은 호출자 영향부터 확인한다.** 범위 밖 변경은 되돌린다. 성능 주장은 명령, 입력, 환경, 전후 수치로 쓴다.
- **effort.** `medium`에서 시작해 어려운 동시성·메모리 손상은 `high`, 측정된 이득이 있을 때만 `xhigh`. `max_tokens`는 생각 토큰을 포함한 상한이라 크게 잡는다. [확인]

## 4. 근거와 한계
- 강점 설명·사이버 거부 처리·무인 실행: [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) [확인: 벤더 서술]
- 테스트 하드코딩 회피: [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) [확인]
- 샌드박스·리뷰 경향 지적: [KDnuggets](https://www.kdnuggets.com/everything-claude-opus-5-5-actually-ships-with), [Zvi: The System Card](https://thezvi.substack.com/p/claude-opus-55-the-system-card) [부분]
- 한계: C·C++·Rust 시스템 코드에 대한 Opus 5.5 전용 독립 평가는 찾지 못했다.
