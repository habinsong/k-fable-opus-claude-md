# Claude Fable 5.5 · 범용 (미출시 대비) — 조사 기록
> 제공자: Anthropic · 모델 ID: 미정(`claude-fable-5-5`는 명명 규칙에서 한 추정, 공식 확인 전 [미확인]) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/claude/fable-5.5/general.md`](../../../md/claude/fable-5.5/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 상태 — Claude Fable 5.5 (2026-11-03 기준 미출시)

### 2.1 확인된 것과 확인되지 않은 것
- **공식 목록에 없다.** 2026-11-03에 직접 읽은 Anthropic 모델 목록([Models overview](https://platform.claude.com/docs/en/models/overview), [anthropic.com/news/models](https://www.anthropic.com/news/models))의 Fable 계열 최신은 Fable 5.1이고 Fable 5.5는 없다. [확인]
- **임박설은 있으나 출처가 약하다.** 2026-10-25자 한 보도(TestingCatalog를 인용한 블로그)는 Anthropic이 곧 출시할 준비 중이라고 했고, 같은 보도가 Anthropic의 공식 확인이 없다고 적었다. 다른 정리 글은 Anthropic이 Fable 5.5의 존재 여부조차 확인하지 않았다고 쓴다. 특정 날짜가 소셜 미디어에 돌지만 Anthropic 문서에 근거가 없다. [부분/미확인]
- **그래서 스펙을 쓰지 않는다.** 가격, 컨텍스트, 기본 effort, API 변경, 안전 범주, 데이터 보관은 모두 [미확인]이다. 이 폴더의 어떤 문장도 Fable 5.5의 성능이나 동작을 단정하지 않는다.
- 출시 전에 모델 ID 문자열을 코드에 박지 않는다. 명명 규칙으로 추정한 ID가 틀릴 수 있다. 공식 Models API나 모델 목록에서 확인한 ID만 쓴다.

### 2.2 잠정 규칙: 출시 전까지는 Fable 5.1 문서를 따른다
- 같은 계열의 직전 모델이므로 `claude/fable-5.1/` 문서의 규칙을 그대로 쓴다. 그 규칙은 Fable 5.1에 대해 확인된 것이며, Fable 5.5에서 같다는 보장은 없다.
- 상속 가능성이 높아 보이는 항목(추정): 적응형 추론 상시 켜짐, 강제 도구 호출 불가, 샘플링 파라미터 지정 불가, 이력 append-only, 추론 블록의 모델·대화 결합. 이 항목은 Fable 5와 Fable 5.1에서 연속으로 유지됐다. [확인: 두 세대 / 추정: 5.5]
- 바뀔 가능성이 큰 항목(추정): 가격과 캐시 요금, 기본 effort, effort별 생각량, 진행 알림·병렬 도구 호출·파일 통째 재작성 같은 행동 경향. Fable 5와 5.1 사이에서도 이런 항목이 바뀌었다. [확인: 5→5.1의 변화 / 추정: 5.5]

### 2.3 출시 당일 확인 체크리스트 (공식 문서에서 직접, 하나씩)
1. 모델 ID, 별칭, 지원 플랫폼(Claude API, Bedrock, Google Cloud, Foundry), 폐기 예정일.
2. 가격: 입력·출력·캐시 쓰기·캐시 읽기·배치. Fable 5.1은 $10/$50, 캐시 읽기 $0.25.
3. 컨텍스트 크기, 최대 출력, 지식 컷오프, 토크나이저 변경 여부(토큰 수가 달라지면 예산이 바뀐다).
4. 기본 effort와 지원 레벨(Fable 5.1은 기본 `high`, 5단계). 레벨 이름이 같아도 생각량은 달라진다.
5. 추론: 끌 수 있는지, `display` 옵션, 진행 알림이 어디로 오는지.
6. 강제 도구 호출, 샘플링 파라미터, 프리필, 컴퓨터 사용 도구 버전의 지원 여부.
7. 추론 블록의 상호 호환(Fable 5.1의 블록을 읽는지, Fable 5.5의 블록을 누가 읽는지), 이력 편집 시 오류 정책.
8. 안전장치: 거부 범주, 서버 쪽 대체 대상, 거부 과금 규칙, 검증 프로그램(Mythos 5.5 같은 짝 모델 여부).
9. 데이터 보관·ZDR·Covered Model 지정.
10. 모델 전용 프롬프팅 페이지(`prompting-claude-fable-5-5`일 가능성, 추정)와 이행 가이드의 "깨지는 변경" 목록.
11. Anthropic의 선택 기준(지금은 "대부분 Opus 5.5로 시작, 어려우면 Fable") 변화.
12. 독립 평가: Artificial Analysis 등의 측정이 나올 때까지 벤더 수치는 주장으로만 취급한다.

### 2.4 비판적 점검
- **루머로 도입을 결정하지 않는다.** 출시일과 성능에 대한 글은 대부분 추측이다. 공식 발표 전에는 Fable 5.1과 Opus 5.5로 평가를 진행한다.
- **출시 직후 측정은 얕다.** 첫 주의 리뷰는 같은 벤더 수치를 반복하고 하네스·effort 조건이 제각각이다. Fable 5.1에서도 순위가 지표마다 갈렸다. 같은 과제·같은 예산으로 Opus 5.5와 직접 비교한다.
- **이행 비용을 먼저 본다.** Fable 5에서 5.1로 올 때도 깨지는 변경이 4가지였다. 5.5로 올릴 때 하네스를 고쳐야 할 수 있다.
- **이 폴더를 출시 후 갱신한다.** 위 체크리스트를 채운 뒤 이 `general.md`의 §2를 실제 사양으로 바꾸고, 8개 분야 문서의 §2에 모델별 운용을 쓴다. 갱신 전의 이 문서는 추정을 단정으로 읽지 않기 위한 장치다.

## 4. 근거와 한계
- 미출시 확인: [Models overview](https://platform.claude.com/docs/en/models/overview), [anthropic.com/news/models](https://www.anthropic.com/news/models) [확인: 2026-11-03에 직접 읽음, Fable 5.5 항목 없음]
- 임박설·루머: [ClaudeAINews](https://www.claudeainews.com/news/anthropic-claude-fable-5-5-release-next-week), [Geotoolbox: Fable 5.5 Release Date, Leaks & What's Confirmed](https://geotoolbox.ai/blog/claude-fable-5-5) [미확인: 모두 2차, 출처가 약함]
- 직전 모델 규칙: 같은 저장소의 `claude/fable-5.1/` 문서.
- 한계: 2026-10-25 이후 출시 여부는 이 조사에서 직접 확인했으며(공식 목록에 없음), 그 뒤 며칠 사이 출시됐을 가능성은 배제할 수 없다. 이 문서를 쓰기 전에 공식 목록을 다시 확인한다.
