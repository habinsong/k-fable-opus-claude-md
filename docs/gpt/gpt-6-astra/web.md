# GPT-6 Astra · 웹 — 조사 기록
> 제공자: OpenAI · 모델 ID: `gpt-6-astra` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gpt/gpt-6-astra/web.md`](../../../md/gpt/gpt-6-astra/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성(API 규칙, effort, 비판적 평가)은 같은 폴더의 `general.md` §2를 따른다. 요약: Responses API 사용, `none`·`minimal` 불가, effort는 항상 명시.

- **UI 품질에 대한 평가가 갈린다.** 한 구조적 비교는 Astra가 다듬기 없이도 완성도 높은 첫 초안을 낸다고 했고, OpenAI는 스케치·참고 이미지·기존 UI를 동작하는 UI로 바꾸고 스크린샷으로 수정하는 용도를 안내한다. 반면 여러 개발자 후기는 UI 완성도(여백, 타이포그래피, 마감)가 Fable 5.1보다 약하다고 보고한다. 대부분 개별 후기이고 체계적 벤치마크가 아니다. [부분]
  → 라우팅·상태 관리·API 연동·테스트는 Astra에 맡기고, 시각 완성도는 스크린샷을 직접 대조해서 확인한다. 디자인 비중이 큰 화면은 같은 요구사항으로 Fable 5.1과 한 번 비교해 본다. [권고]
- **과잉 설계를 막는다.** 새 컴포넌트·유틸·스크립트를 만들기 전에 프로젝트에 이미 있는 것을 먼저 찾는다. 변경 후 `git diff --stat`으로 새로 생긴 파일이 요청에 필요한 것인지 확인한다.
- **완료 기준을 시작할 때 적는다.** 예: "해당 화면이 브라우저에서 열리고, 콘솔 오류가 없고, 키보드만으로 조작되며, 관련 테스트가 통과한다." 중간 검토를 위해 멈추라는 지시는 넣지 않는다(일찍 멈추는 쪽으로 기운다).
- **접근성·성능·보안을 "충족했다"는 자기 판단을 증거로 쓰지 않는다.** 이 모델의 자기 평가가 틀린 사례가 보고됐다. 접근성 도구, 브라우저 콘솔, 성능 측정 출력으로 확인한다.
- **시각 확인.** 스크린샷은 모델의 해석이 아니라 실제 렌더링과 대조한다. 확인하지 못했으면 "화면 미확인"이라고 보고한다.

## 4. 근거와 한계
- 모델 사양·API 규칙: [openai/codex 마이그레이션 가이드](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-6-astra.md) [확인]
- UI 평가: [Claude Fable 5.1 vs GPT-6 Astra for Product Design](https://eidosdesign.substack.com/p/claude-fable-51-vs-gpt-6-astra-for), [A Short Review of OpenAI's GPT 6 Astra](https://medium.com/jonathans-musings/a-short-review-of-openais-gpt-6-astra-091fa5beccf9) [부분: 개별 후기·단일 시험]
- 한계: 웹 UI에 대한 체계적 독립 벤치마크는 찾지 못했다. "Fable 5.1보다 약하다"는 평가도 "첫 초안이 낫다"는 평가도 재현 확인 전까지 잠정이다.
