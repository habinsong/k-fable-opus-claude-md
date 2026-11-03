# Gemma 4 31B · 앱 (로컬) — 조사 기록
> 제공자: Google · 모델 ID: `google/gemma-4-31B-it` (Hugging Face 토론 URL에서 확인한 표기, 본문은 열지 못함) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemma/gemma-4-31b/app.md`](../../../../md/gemma/gemma-4-31b/app.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/app.md`](../../../_common/domain-rules/app.md)

## 2. 이 모델의 앱 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 밀집 약 31B, 4비트 약 17.5~20 GB + KV 캐시, 느림, 앱 개발 독립 평가 없음.

**앱에 내장할 때**
- **휴대 기기에 올릴 모델이 아니다.** 4비트 가중치만 약 17.5~20 GB이고 BF16은 약 62.5 GB다. 모바일 온디바이스는 E2B·E4B를 검토한다(`gemma-4-e2b`, `gemma-4-e4b` 문서). 이 크기는 앱의 서버 측 로컬 추론이나 개발자 워크스테이션에 맞는다. [부분]
- **서버 측에 올리는 비용을 먼저 계산한다.** 밀집 31B는 한 기기 측정에서 약 3.4 토큰/초였다. 동시 사용자가 늘면 처리량이 급격히 줄므로 대상 하드웨어에서 동시성·지연·메모리를 실측한다. 개인정보가 서버를 거치는 경로는 앱의 개인정보 선언과 일치시킨다.
- **라이선스 고지.** Apache 2.0이라고 모델 카드가 적었다. 가중치를 배포·번들하면 고지·NOTICE를 지키고 받는 경로의 약관도 확인한다. [부분]
- **제공자 쪽 안전장치가 없다.** 입력 필터, 출력 검증, 위험한 기능(결제, 계정 변경, 외부 전송)의 권한 제한을 앱이 직접 한다.
- **모바일 SDK 지원은 작은 모델 기준이다.** Android는 E2B용 Kotlin API가 있다는 개발자 보고가 있고, iOS는 네이티브 Swift API가 없어 C++ API에 의존한다는 보고와 mlx-swift-lm 2.31.x에서 Gemma 4가 기본 지원되지 않는다는 Apple 개발자 포럼 글이 있다. 이 보고들은 31B에 해당하지 않으며 시점이 지났을 수 있다. 현재 SDK 문서에서 확인한다. [부분/미확인]

**개발 보조로 쓸 때**
- **모바일(Kotlin·Swift) 코드에 대한 31B의 독립 평가는 찾지 못했다.** [미확인] 일반 코딩 후기는 있다(한 사용자의 8건 실무 과제 중 7건 통과, 다른 사용자의 "코드 생성에 매우 좋다" 평가). 모바일 과제가 아니고 비공식 보고다. [부분: 개인 후기] 컴파일·린트·단위 테스트·UI 테스트로 검증한다.
- **어려운 단발 요청에 쓰고 대화형 반복 편집에는 쓰지 않는다.** 속도가 느려 수정-확인 루프의 지연이 크다. 반복 편집은 26B A4B나 더 빠른 모델이 낫다. 수명주기·권한·비동기 처리가 걸린 구현은 `claude/sonnet-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 같은 상위 모델 문서를 따른다.
- 스토어 규정은 기억으로 답하지 않고 공식 문서로 확인한다(§3.2). 서명 키, 프로파일, 스토어 제출·배포는 승인 후에만 한다.

## 4. 근거와 한계
- 메모리·크기: [Gemma 4 model overview](https://ai.google.dev/gemma/docs/core), [Gemma 4 hardware requirements (Yotta Labs)](https://www.yottalabs.ai/post/gemma-4-hardware-requirements-gpu-memory-2026) (스니펫만) [부분]
- 모바일 SDK 상태(E2B 기준): [Gemma 4 E2B on mobile (DEV)](https://dev.to/devpicon/gemma-4-e2b-on-mobile-android-vs-ios-reality-1-38lm), [Apple 개발자 포럼](https://origin-devforums.apple.com/forums/profile/jingyangye) [부분: 개인 후기]
- 일반 코딩 후기: [Reddit 스냅샷](https://reddit.sentinel-team.org/posts/1slnhrd/snapshots/2026-04-17T23%3A20%3A42.645991Z) [부분: 개인 후기]
- 한계: 모바일 앱 개발에 대한 31B 전용 평가가 없다. SDK 지원 상태는 시점이 지났을 수 있다.
