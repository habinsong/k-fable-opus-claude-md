# 열람하지 못한 출처, 확인하지 못한 것, 요구 항목별 근거 지도

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.

## 1. 이 환경에서 열리지 않은 호스트 (원문 미열람)

digitalmarketer.co.kr, discuss.pytorch.kr, koreancenter.or.kr, blog.pebblous.ai, korean.go.kr(PDF), skillselion.com, friendli.ai, aiweekly.co, developers.openai.com, docs.cloud.google.com. 모두 호스트 이름이 풀리지 않는 오류였고 우회하지 않았다. 해당 출처의 내용은 검색 요약으로만 확인했다.

## 2. 확인하지 못한 것

- 도치: AI의 도치 남용을 다룬 공개 자료 [미확인]. 2026-11-03에 확장 검색으로 한 번 더 찾았으나 도치나 어순을 다룬 자료는 나오지 않았다.
- 모델별 한국어 문체: GPT-6·Claude 5.5·Gemini 4·Gemma 4의 한국어 문체를 사람이 평가한 독립 자료. 검색 결과는 영어 창작 리더보드와 개인 블로그 체감뿐이었다 [미확인].
- 학술 한국어: 한다체, 일인칭, 용어 병기의 공식 규범. 한국연구재단 생성형 AI 연구윤리 가이드 본문.
- 실측 연구의 원천: `baseline.json` 쉼표 기준값의 원천 데이터. KatFishNet 논문 본문(사람·AI 방향).
- 서지: 김정선 책의 출판사, 강원국·은유 등의 책.
- 최신성: 검색 범위는 대체로 2026년 9월 말~10월이다.

## 3. 사용자 요구 항목별 근거 지도

| 요구 | 지침 위치 | 근거 문서 | 근거 수준 |
|---|---|---|---|
| 자연스러운 기술적 표현(논문) | `universal/ko-academic.md` §3.10 | [`language-principles.md`](language-principles.md) §1·§6 | 한다체 규범은 관행(추정) |
| 일상 대화·글 | `universal/ko-everyday.md` §3.10 | `language-principles.md` §1(구어 종결), `empirical-validation.md` | [부분] |
| 문학 | `universal/ko-literary.md` §3.10 | `language-principles.md` §4·§5 | 문체 평가는 개인 평 |
| 문장 사이의 흐름과 호흡 | `ko-core.md` §3.3 | `empirical-validation.md` §2·§4 | [부분], 편집 효과 가능 |
| 과서술 | §3.4 | `ai-tell-projects.md` §2 | [부분], 반대 방향(과소 서술)도 반영 |
| 사람이 쓰지 않는 용어·문장 | §3.5 | `empirical-validation.md` §3(기각된 통념 포함) | [부분] |
| 인위적인 감정 표현 | §3.7 | `vendor-writing-guides.md` §4(따뜻함 연구 보도) | 감정 과장 전용 공개 분류는 없음 |
| 대구 | §3.6 | `empirical-validation.md` §2 | [부분], 가장 강한 신호 |
| 도치 | §3.6 | `language-principles.md` §7 | **사용자 관찰, 공개 근거 없음 [미확인]** |
| 웹 검색 적극 활용 | `universal/contract.md` §1.7 | 사용자 지시 | 해당 없음 |

## 4. 지침의 이해 한계

- 형식 검사(`scripts/docs_tool.py`)는 통과해도 문체의 자연스러움은 검사하지 못한다. `scripts/ko_style_probe.py`도 정규식 휴리스틱이라 탐지기가 아니다.
- 문서 안의 예시 문장은 새로 쓴 것이며 규칙이 맞는지 입증하지 않는다.
- 이 규칙들을 적용한 실제 출력을 사람이 읽고 평가한 적은 없다. 규칙을 믿기 전에 같은 원문 몇 개로 전후를 비교한다.
