# Muse Wonder · 웹 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/web.md`](../../../../md/muse/muse-wonder/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델(Full은 Muse Code 구독 전용), 컨텍스트 100만 토큰, 입력 $4 / 출력 $20, 독립 지수에서 Opus 5.5에 못 미침, Meta 표와 독립 값 불일치, 토큰 소비 많음, 데이터 약관·Active Memory 정보 부족.

- **웹 UI 생성 품질의 독립 평가는 찾지 못했다.** [미확인] Wonder를 코딩 에이전트로 쓴 현장 후기도 찾지 못했다. 집계 사이트의 코딩 점수(예: Haiku 5.5와 비교해 69.8 대 51.3)는 표 수치이고 개발자 경험이 아니다. 컴포넌트 단위 수정, 새 화면, 스크린샷 재현을 우리 코드베이스에서 상위 모델과 같은 조건으로 돌려 비교하고, 스크린샷 대조와 린터·타입체크·테스트 출력으로 판정한다. 기존 UI 체계가 우선한다(§3.1). [부분]
- **Muse Code의 이전 평가를 Wonder에 옮기지 않는다.** 8월의 비교(AA 코딩 에이전트 지수에서 Claude Code(Opus 5) 67, Muse Code(Muse Spark 1.2) 61)와 한 매체의 실작업 비교(Muse의 리팩터링이 구조를 거의 바꾸지 못하고 죽은 코드를 남겼다)는 Spark 1.2 기반이다. Wonder 기반 Muse Code의 평가는 아니다. [부분: 개인 후기, 다른 모델]
- **`max` 단계 헤드라인과 과제당 비용을 구분한다.** Meta의 대부분 수치는 `max` 단계의 값이고 AA는 지수 실행에서 출력 토큰을 비교군 중앙값의 약 1.5배 썼다고 한다. 컴포넌트 수정 한 건당 입력·출력 토큰과 도구 호출 수를 기록해 과제당 비용을 비교한다. 단가($4/$20)가 높은 편이라 Spark(`muse-spark` 문서)나 더 싼 모델로 충분한 작업은 내려 쓴다. [부분]
- **Active Focus의 "확인 질문"을 안전장치로 믿지 않는다.** Meta는 중대한 행동 전에 확인을 구한다고 설명하나 벤더 설명이다. 파일 쓰기·셸 실행 범위, 작업 디렉터리, 파괴적 명령 차단(권한·훅)을 먼저 설정하고 완료 보고는 린터·타입체크·테스트 출력과 `git diff`로 확인한다. [부분: 벤더 주장]
- **Wonder Full은 호출 경로가 구독에 묶인다.** 공개 API는 Wonder만 제공하므로 CI나 제품 코드 생성 파이프라인에는 Wonder를 기준으로 설계한다. 구독 경로의 약관이 자동화 사용을 허용하는지 확인한다. [부분/미확인]
- **보안·접근성 판단을 맡기지 않는다.** 인가, 입력 검증, 비밀 노출, 접근성 "충족" 여부는 도구 출력과 §3.1 기준으로 사람이 점검한다. API·CSS·브라우저 지원은 공식 문서와 린터·컴파일러 출력으로 확인한다.
- **미공개 소스를 보내기 전에 약관을 확인한다.** 데이터 처리 서술이 충돌하고 Active Memory의 저장 위치·기간을 찾지 못했다(README.md가 안내하는 개요·운용 문서.4). [미확인, 충돌] 메모리 기능이 켜진 경로에서는 대화 간에 코드·비밀이 보관될 수 있다는 점을 고려해 확인 전에는 비밀·고객 데이터가 담긴 코드를 보내지 않는다(§1.6).

## 4. 근거와 한계
- 집계 코딩 점수: [BenchLM: Claude Haiku 5.5 대 Muse Wonder](https://benchlm.ai/compare/claude-haiku-5-5-vs-muse-wonder) [부분: 집계 사이트]
- Muse Code(Spark 1.2 기반) 평가: [Artificial Analysis: Claude Code 대 Muse Code](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-muse-code), [The New Stack: Muse와 Claude Code](https://thenewstack.io/meta-muse-claude-code/), [Composio: Muse Code 대 Claude Code](https://composio.dev/blog/muse-code-vs-claude-code) (스니펫만) [부분: 개인 후기, 다른 모델]
- 토큰 소비·지수: [Artificial Analysis: Muse Wonder (Max)](https://artificialanalysis.ai/de/models/muse-wonder) (스니펫만) [부분]
- 한계: Wonder의 웹 UI·프런트엔드 독립 평가가 없다. Meta 공식 문서를 읽지 못했다.
