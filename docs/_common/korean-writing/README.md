# 한국어 윤문 — 공통 조사 기록

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다. 컨텍스트용 지침은 [`universal/ko-*.md`](../../../universal/)와 `md/<계열>/<모델>/ko-*.md`다.
> 기준일 2026-11-03. 근거 표기는 [`docs/README.md`](../../README.md)를 따른다.

## 문서 구성

| 문서 | 내용 |
|---|---|
| [`ai-tell-projects.md`](ai-tell-projects.md) | 한국어 AI 말투를 다루는 공개 프로젝트: 분류 체계, 라이선스, 내가 직접 읽은 범위 |
| [`empirical-validation.md`](empirical-validation.md) | 사람 글과 AI 글의 실측 비교(저자 자체 보고)와 그 한계, 지침에 채택한 것과 버린 것 |
| [`language-principles.md`](language-principles.md) | 한국어 문장 원리, 번역투 문헌, 문장 부호, 사전·규범, 명저·서지, 문체 평가 |
| [`vendor-writing-guides.md`](vendor-writing-guides.md) | 모델 제공자의 프롬프트 가이드 중 글쓰기와 관련된 내용 |
| [`sources-and-gaps.md`](sources-and-gaps.md) | 열람하지 못한 출처, 확인하지 못한 것, 사용자 요구 항목별 근거 지도 |
| [`trial-log.md`](trial-log.md) | 규칙을 실제 글에 적용해 전후를 잰 시험, 발견한 도구 누락과 규칙 모순, 사람 평가 절차 |

모델별 조사는 `docs/<계열>/<모델>/korean-writing.md`에 있다(gpt, claude, gemini, gemma 17개 모델).

## 읽는 법

- 지침에 들어간 규칙은 이 폴더의 근거 위에서 정했다. 근거가 약한 규칙은 지침에서 강도를 낮추거나 "되풀이될 때만"처럼 조건을 붙였다.
- 수치는 대부분 한 프로젝트 저자의 **자체 보고**다. 동료 심사를 거치지 않았고, 비교한 AI 모델의 버전이 이 저장소의 현재 모델과 다르다. 모델 간 우열을 말하는 근거로 쓰지 않는다.
- 공식 규범(국립국어원)과 일부 연구 원문은 조사 환경에서 열리지 않아 검색 요약으로만 확인했다.
