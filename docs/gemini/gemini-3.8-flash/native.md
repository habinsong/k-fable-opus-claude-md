# Gemini 3.8 Flash · 네이티브 — 조사 기록
> 제공자: Google · 모델 ID: `gemini-3.8-flash` · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/gemini/gemini-3.8-flash/native.md`](../../../md/gemini/gemini-3.8-flash/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: Terminal-Bench 4.0에서 Opus 5보다 32.7점 낮음, 코딩 지수 76.3(2차), 말이 많음, 사이버 변종은 제한 제공.

- **시스템 코드의 핵심 변경은 상위 모델에 맡긴다.** Google 자신의 비교표에서 Terminal-Bench 4.0이 Claude Opus 5보다 32.7점 낮다. [부분] 메모리 관리, 동시성, ABI가 걸린 변경은 `gemini-4-argon`, `claude/sonnet-5.5` 이상, `gpt-6.1-sol` 문서와 같은 과제로 비교한 뒤 정한다.
- **써도 되는 작업.** 컴파일러 오류 분류와 설명, 빌드 로그 요약, 헤더 주석 초안, 이름 바꾸기 같은 기계적 변환, 단위 테스트 수정. 코딩 지수 76.3은 이런 반복 작업에서 비용 대비 쓸 만함을 시사한다. 결과는 컴파일러·테스트 출력과 대조한다. [부분]
- **`thinking_level`.** 오류 메시지 분류는 `LOW`, 일반 수정은 `MEDIUM`, 미정의 동작이 얽힌 디버깅은 `HIGH`. `MINIMAL`은 검증 오류다. 생각 토큰도 출력 요금이다. [부분]
- **변경 후 sanitizer 빌드와 테스트를 지시문으로 강제한다.** 돌리지 못한 검사는 "미실행"으로 보고하게 한다. 테스트·경고·sanitizer 설정이 바뀌었는지 `git diff`로 확인한다.
- **API·플래그·시스템 호출을 기억에서 가져오지 않는다.** 지식 평가 정답 비율 55%라도 절반 가까이는 틀리거나 모른다. [부분] 시스템 API, 링커·컴파일러 옵션은 매뉴얼과 도구 출력으로 확인한다.
- **사이버 변종 `Gemini 3.8 Flash Cyber`는 Fairwind 승인 파트너에게만 제공된다.** 일반 접근에서는 취약점 분석·리버스 엔지니어링 같은 이중 용도 작업이 제한될 수 있다. [부분] 거부되면 같은 요청을 반복하지 않는다.
- **Gemini CLI에서 쓴다면** 이 문서를 `GEMINI.md`로 복사한다. 시스템 경로, 레지스트리, 드라이버, 부트 설정, 서명 키는 승인 없이 건드리지 않는다. [확인]

## 4. 근거와 한계
- Terminal-Bench 격차·코딩 지수: [eesel.ai 리뷰](https://www.eesel.ai/blog/gemini-3-8-flash), [DataNorth](https://datanorth.ai/news/google-launches-gemini-3-8-flash-gemini-3-8-flash-cyber) [부분]
- Cyber 변종 제한: [DataCamp: Gemini 3.8 Flash](https://www.datacamp.com/blog/gemini-3-8-flash-cyber) [부분]
- 한계: C·C++·Rust 시스템 코드에 대한 3.8 Flash 전용 독립 평가는 찾지 못했다.
