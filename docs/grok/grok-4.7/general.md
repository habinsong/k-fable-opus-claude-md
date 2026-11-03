# Grok 4.7 · 범용 — 조사 기록
> 제공자: xAI(일부 자료는 회사명을 SpaceXAI로 표기하나 확인하지 못함) · 모델 ID: API `grok-4.7`(집계 사이트의 `grok-4-7` 표기, 확인 필요), 경량 변형 "Grok 4.7 Fast"는 Cursor·Grok Build 전용이라는 서술 · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/grok/grok-4.7/general.md`](../../../md/grok/grok-4.7/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Grok 4.7 (폐쇄형 API 모델)
이 환경에서는 xAI 공식 문서(docs.x.ai)와 공지 페이지가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 미출시 후속은 `grok-4.8`, `grok-5` 문서에 둔다.

### 2.1 위치와 연혁
- **2026-09-21 출시**(xAI 공지를 인용한 여러 집계). 직전 모델은 Grok 4.5(2026-07-08), Grok 4.6(2026-08-12, 머스크가 말한 8월 7일경보다 늦었다는 서술)이다. 한 출처는 4.7이 약 2.1조 파라미터 규모로 지연에 걸려 있다고 서술해 출시 상태와 어긋난다. 출시 이후 정보로 보이는 쪽을 따르되 파라미터 수는 공개되지 않았다고 본다. [부분, 충돌]
- xAI의 코딩 에이전트 **Grok Build**가 4.7을 기본으로 시작하며(Grok Build 1.0.40이 9월 20일 지원 추가), Cursor와 VS Code 확장에서도 쓸 수 있다. [부분]

### 2.2 사양 (출처마다 다름)
- 컨텍스트 50만 토큰. 입력은 텍스트·이미지(비전), 기능은 함수 호출과 구조화 출력. xAI는 이 모델의 별도 최대 출력 한도를 공개하지 않는다는 서술이 있다. [부분]
- **가격**(100만 토큰당): 입력 $2 / 출력 $6, 캐시 입력 $0.5. 프롬프트가 20만 토큰에 이르면 모든 요청 토큰에 장문 요금(입력 $4 / 출력 $12)이 적용된다는 서술이 있다. 라우터·게이트웨이는 $2.6/$7.8, $1.6/$4.8처럼 달라 xAI 정가로 읽지 않는다. 공식 가격표는 확인하지 못했다. [부분, 충돌]
- 추론 노력 변형이 따로 평가된다(`low`, `high`, `xhigh`). 어떤 파라미터로 지정하는지는 확인하지 못했다. [미확인]
- 모델 카드를 찾지 못했다. 한 글은 xAI 공지 페이지가 올라온 9월 21일에 4.7 모델 카드는 확인되지 않았다고 쓴다. [미확인]

### 2.3 성능 근거를 읽는 법
- **독립 지수(Artificial Analysis v4.3.2)**: `xhigh` 46, `high` 46, `low` 42. 노력 단계를 올려도 `high`와 `xhigh`가 같은 점수라 `xhigh`의 추가 비용이 이득이 없을 수 있다. 비교 중앙값은 페이지마다 달라(11, 27) 같은 기준으로 읽으려면 지수 버전과 비교군을 확인한다. 이 지수는 10개 평가(AA-Briefcase, GDPval-AA, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-Omniscience, AA-LCR)로 구성된다. [부분]
- **토큰을 많이 쓴다.** 지수 실행에서 `xhigh`는 출력 토큰 2.4억 개, `high`는 2.0억 개로 비교군 중앙값 9,200만의 두 배 이상이었다. 단가가 낮아도 과제당 비용은 올라간다. [부분]
- **코딩 에이전트 지수**: Grok 4.7(`xhigh`) + Grok Build가 56점으로 4.6보다 9점 높고 네이티브 하네스 가운데 4위라는 독일어 글의 서술이 있다. 같은 글이 높은 노력 단계가 가격 대비 성능에서 나을 수 있다고 한다. 원문을 확인하지 못했다. [부분/미확인]
- **환각·사실성 값은 확인하지 못했다.** AA 모델 페이지에 "1 − 환각률"과 AA-Omniscience 항목이 있으나 값을 보지 못했다. [미확인] 벤더 벤치마크는 공개된 것이 없다("점수 집계 중" 표기). [부분]

### 2.4 안전·정책·데이터
- **안전 문서가 약하다.** 4.7의 모델 카드·시스템 카드는 확인되지 않았고, 4.6 카드에는 거부·탈옥 강건성 절이 있다는 서술이 있다. xAI는 시스템 프롬프트에 탈옥 시도가 온다고 경고하는 방식(접종)을 쓰며 시스템 프롬프트가 `xai-org/grok-prompts` 저장소에 공개돼 있다고 한다. Grok 4.5 출시 직후 연구자가 몇 시간 안에 안전 통제를 우회했다고 주장한 사례가 있고 스크린샷만으로 안정적 공격 성공률을 알 수 없다는 지적이 붙는다. 2025년 Grok 4는 시스템 카드 미공개와 위험 능력 평가 결과 미공개로 비판받았다. [부분: 단일 블로그·개인 주장]
- **API 데이터**: 여러 집계가 xAI가 명시적 허락 없이 API 입력·출력으로 학습하지 않으며 기본 30일 암호화 보관(남용 감사용)이라고 정리한다. 영 보관(ZDR)은 기업 계정 전용이라는 서술과 팀 관리자가 콘솔에서 켜는 토글이라는 서술이 갈린다. 소비자용 Grok은 정책이 다르다. SOC 2 Type 2와 요청 시 BAA 제공 서술이 있다. 모두 2차 출처이며 xAI 약관·DPA 본문을 읽지 못했다. [부분, 충돌]

### 2.5 이 모델을 운용하는 법
- **노력 단계는 과제로 정한다.** `high`와 `xhigh`의 지수가 같으므로 기본은 `high`에서 시작하고 `xhigh`가 우리 과제에서 이득인지 측정한다. [추정]
- **장문 요금 문턱(20만 토큰)을 넘기지 않게 입력을 줄인다.** 요금이 전체 요청 토큰에 적용된다는 서술이 맞다면 20만 토큰 직전과 직후의 비용 차이가 크다. 공식 문서로 확인한다. [부분]
- **노출된 프롬프트와 정책에 의존하지 않는다.** 시스템 프롬프트가 공개돼 있어도 모델의 실제 거부·정렬 동작은 시험으로 확인한다.
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.6 비판적 평가
- 강점 후보: 낮은 단가, 50만 토큰 컨텍스트, 독립 지수 46, Grok Build와의 통합. 약점 후보: 토큰 소비가 많음, 모델 카드·안전 문서 부재, 벤더 벤치마크 미공개, 데이터 정책이 2차 출처뿐, 출시·갱신 속도가 빨라 버전 관리 부담.
- 막히면 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시일·컨텍스트·가격·기능 | [Let's Data Science: Grok 4.7 출시](https://letsdatascience.com/news/xai-releases-grok-47-with-500k-context-43aa2021), [Price Per Token: Grok 4.7](https://pricepertoken.com/pricing-page/model/xai-grok-4.7), [Another Wrapper: Grok 4.7 가격](https://anotherwrapper.com/llm-pricing/grok-4.7) (스니펫만) | [부분, 충돌] |
| 독립 지수·토큰 사용량 | [Artificial Analysis: Grok 4.7 (xhigh)](https://artificialanalysis.ai/models/grok-4-7), [Grok 4.7 (high)](https://artificialanalysis.ai/models/grok-4-7-high), [Grok 4.7 (low) 독일어](https://artificialanalysis.ai/de/models/grok-4-7-low) (스니펫만) | [부분] |
| 코딩 에이전트 지수·Grok Build | [ToolNavs: Grok 4.7 벤치마크](https://toolnavs.com/de/article/2040-grok-47-benchmark-coding-agent-breaks-into-top-four-at-81k-tokens-per-task), [Gradually: Grok Build 변경 이력](https://www.gradually.ai/changelogs/grok-build/), [Grok Build](https://x.ai/build) (스니펫만) | [부분] |
| 안전·탈옥 서술 | [Hora de Codar: Grok 4.7 거부·탈옥](https://horadecodar.com.br/grok-4-7-jailbreak/), [Penligent 분석](https://www.penligent.ai/hackinglabs/de/?p=6348) (스니펫만) | [부분: 단일 블로그] |
| 데이터 정책(2차) | [guptadeepak: 데이터 취급·보관](https://guptadeepak.com/ai-models/data-handling/), [DevelopersDigest: xAI 보관](https://www.developersdigest.tech/models/data-retention/xai), [BAA Atlas: Grok](https://baa-atlas.vercel.app/ai/grok) (스니펫만) | [부분, 충돌] |
- xAI 공식 문서·모델 카드·약관·DPA 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
