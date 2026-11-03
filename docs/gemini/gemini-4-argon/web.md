# Gemini 4 Argon · 웹 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-4-argon` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-argon/web.md`](../../../md/gemini/gemini-4-argon/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: `thinking_level` 명시, 자기 검증이 약하다는 평가, 2026-11-30 이후 가격 2배, 함수 호출 시 thought signature 필수.

- **웹 UI 생성 품질에 대한 독립 평가는 찾지 못했다.** [미확인] Google은 Argon으로 만든 창작 프로젝트 사례를 소개하지만 이는 벤더 시연이다. [부분] 시각 마감은 스크린샷을 직접 대조하고, 확인하지 못했으면 "화면 미확인"이라고 보고한다.
- **변경 후 실제 검증을 지시문으로 박는다.** 이 모델은 자기 검증과 코드 재검토로 돌아가는 데 약하다는 후기가 있다. [부분] "화면을 브라우저에서 열고, 콘솔 오류와 실패한 네트워크 요청을 확인하고, 관련 테스트를 돌린 뒤 결과를 읽고 실패하면 고쳐서 다시 돌려라. 못 했으면 못 했다고 말하라"를 작업 시작에 적는다. 완료 기준에 통과해야 할 검증을 포함한다.
- **낡은 명세·충돌하는 규칙을 컨텍스트에 두지 않는다.** 한 후기는 이 모델이 정확성보다 규칙을 우선하고 레거시 명세·코드에 주의가 흐트러진다고 적었다. [부분] 오래된 디자인 문서나 폐기된 컴포넌트 설명을 입력에서 빼고, 기존 UI 체계가 우선한다는 §3.1 규칙을 한 번 명시한다.
- **문서·구조 편집에는 맞을 수 있다.** 구조 편집기로 좋았다는 단일 후기가 있다. 마크업·컴포넌트 구조 정리는 시도해 볼 만하지만 결과를 린터·타입체크·테스트로 확인한다. [부분]
- **웹 사실은 Google 검색 grounding과 URL 컨텍스트로 확인한다.** 브라우저 지원, 표준, 라이브러리 버전은 grounding된 출처 URL을 직접 열어 대조한다. [부분]
- **함수 호출 하네스를 직접 만들면 thought signature를 돌려준다.** 응답의 모든 파트를 그대로 다음 턴에 넣지 않으면 검증 오류가 난다. [부분]
- **비용.** 2026-11-30 이후 입력 $4 / 출력 $20이다. 화면 단위 반복 작업은 Gemini 3.8 Flash나 다른 제공자의 균형형 모델과 작업당 비용을 비교한다. 이 모델은 지수 평가에서 출력 토큰도 많이 썼다. [부분]

## 4. 근거와 한계
- 자기 검증·낡은 명세 지적: [Google AI 개발자 포럼](https://discuss.ai.google.dev/t/how-bad-is-gemini-4-argon/190009), [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-4-argon-review), [Layer3 Labs 리뷰](https://www.layer3labs.io/guides/gemini-4-argon-review) [부분]
- thought signature·가격: [Thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures), [Now available for developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/) (스니펫만) [부분]
- 한계: 웹 프런트엔드 품질의 독립 비교는 찾지 못했다.
