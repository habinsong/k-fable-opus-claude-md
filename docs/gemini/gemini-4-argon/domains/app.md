# Gemini 4 Argon · 앱 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-4-argon` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-4-argon/app.md`](../../../../md/gemini/gemini-4-argon/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: Android Studio에서도 진입할 수 있는 Google 생태계 모델, 자기 검증이 약하다는 평가, 컴퓨터 사용은 프리뷰, 2026-11-30 이후 가격 2배.

- **Android 개발 도구 연동이 공식 진입점으로 소개된다.** Google은 Gemini API의 유료 티어를 Google AI Studio와 Android Studio에서 쓰는 것을 개발자 진입점으로 안내한다. [부분] 다만 모바일 앱 개발 품질에 대한 독립 평가는 찾지 못했다. [미확인] 실기기 검증을 생략하지 않는다.
- **변경 후 실제 검사를 지시문으로 박는다.** 이 모델은 자기 검증이 약하다는 후기가 있다. [부분] "컴파일·린트·단위 테스트를 돌리고 출력을 읽고, 실패하면 원인을 고쳐 다시 돌려라. 못 돌렸으면 무엇을 왜 못 했는지 말하라"를 시작에 적는다. 빌드·테스트 출력은 파일로 한 번 저장한 뒤 실패한 구간만 읽는다.
- **스토어 정책·플랫폼 요건은 grounding으로 확인하고 출처를 연다.** 이 모델은 Google 검색 grounding과 URL 컨텍스트를 지원한다. [부분] §3.2 표의 날짜는 모델의 말이 아니라 공식 정책 페이지에서 직접 확인한다.
- **컴퓨터 사용은 프리뷰다.** 시뮬레이터 조작에 쓰려면 프리뷰 제약과 성공률을 자체 과제로 측정하고, 결과는 스크린샷·로그로 확인한다. 독립 수치는 찾지 못했다. [부분/미확인]
- **Live API와 명시적 캐싱이 없다.** 실시간 음성 앱이나 긴 정적 프롬프트 재사용에 의존하는 설계는 암묵적 캐싱만 가능함을 감안한다. [부분]
- **`thinking_level`을 명시한다.** 짧은 UI 문자열 작업은 `LOW`, 일반 구현은 `MEDIUM`(기본), 어려운 수명주기 문제만 `HIGH`. `MINIMAL`은 400이다. [부분]
- **함수 호출 하네스는 thought signature를 돌려준다.** [부분]
- **비용.** 2026-11-30 이후 입력 $4 / 출력 $20이다. 번역 초안·로그 분류 같은 대량 작업은 Gemini 3.8 Flash나 더 작은 모델을 쓴다. [부분]
- **서명 키, 프로파일, 스토어 제출·배포는 승인 후에만.**

## 4. 근거와 한계
- Android Studio 진입점·가격·컴퓨터 사용 프리뷰: [Gemini 4 Argon is now available for developers](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/), [OpenRouter 목록](https://openrouter.ai/google/gemini-4-argon) (스니펫만) [부분]
- 자기 검증 약점·누락 기능: [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-4-argon-review), [Layer3 Labs 리뷰](https://www.layer3labs.io/guides/gemini-4-argon-review) [부분]
- 한계: 모바일 개발에 대한 Argon 전용 독립 벤치마크는 없다.
