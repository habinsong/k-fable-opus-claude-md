# MiniMax-M3.1-Flash · 범용 — 조사 기록
> 제공자: MiniMax · 모델 ID: API `MiniMax-M3.1-Flash`(프리뷰는 `MiniMax-M3.1-Flash-Preview`, 정확한 ID는 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/minimax/minimax-m3.1-flash/general.md`](../../../md/minimax/minimax-m3.1-flash/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — MiniMax-M3.1-Flash (경량 변형, 공개 가중치 여부 충돌)
이 환경에서는 MiniMax 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 상위 모델은 `minimax-m3` 문서에 둔다.

### 2.1 위치와 연혁
- **2단계로 출시됐다.** 프리뷰 `MiniMax-M3.1-Flash-Preview`가 2026-09-27에 MiniMax Code 안에서 먼저 공개됐고(종량제 가격 없이 Token Plan과 MiniMax Code로만 사용 가능), 정식 API는 2026-10-19(또는 10월 20일, 출처별)에 나왔다. 이후 토큰 가격을 내렸다는 보도가 있으나 세부는 확인하지 못했다. [부분, 충돌]
- **가중치 공개 여부가 출처마다 어긋난다.** 한 곳(MiniMax가 "초효율 공개 가중치 모델"로 10월 19일 출시했다는 서술, Vals AI의 "공개 가중치" 표기)은 공개라고 하고, 다른 곳(벤더 기준 다운로드 가능한 가중치 없음, Hugging Face 카드 없음)은 아니라고 한다. 공식 릴리스 노트를 확인하기 전에는 둘 중 하나로 단정하지 않는다. [부분, 충돌/미확인]

### 2.2 사양 (출처마다 다름)
- 컨텍스트 100만 토큰, 최대 출력 524,288(또는 512K). **파라미터 수는 확인되지 않았다.** 428B·활성 23B라는 서술은 모회사 모델 M3에서 빌려 온 수치일 수 있다는 경고가 있다. 이 문서는 M3.1 Flash의 크기를 쓰지 않는다. [부분, 충돌/미확인]
- **가격**(100만 토큰당): 정식 출시 시 입력 $0.15 / 출력 $0.60, 캐시 읽기 $0.015. 프리뷰를 $0.30 / $1.20이라고 적은 곳도 있으나 다른 수치와 맞지 않는다. 출시 후 인하 보도가 있어 현재 가격은 공식 가격표로 확인한다. [부분, 충돌]
- **속도**: 한 출처가 초당 약 100 토큰(프리뷰 기준, 미검증), MiniMax는 M3보다 거의 3배 빠르다고 주장한다. 독립 측정은 찾지 못했다. [부분: 벤더 주장]

### 2.3 성능 근거를 읽는 법
- **독립 지수(Artificial Analysis)**: M3.1 Flash 42(비교 중앙값 13). 더 오래된 서술에서 M3는 29로 적혀 있어 후속이 낫다는 비교가 나오지만, 다른 페이지는 M3를 44로 적어(지수 버전 차이) 순위가 뒤바뀐다. 같은 지수 버전의 값끼리만 비교한다. [부분, 충돌]
- **작업당 비용**: AA는 M3.1 Flash를 약 $0.22 / 지수 작업, M3를 약 $0.51로 보고했다(57% 감소). MiniMax가 말한 70% 사용 비용 절감보다 독립 측정의 감소 폭이 작다. 출력 토큰 약 1.8억 개라는 화면 설명이 있으나 비교 중앙값을 확인하지 못했다. [부분]
- **벤더 수치**: DeepSWE v1.1 73.7%는 MiniMax 제공값이고 독립 재현이 없다. [부분: 벤더 주장]
- **환각 위험이 크다.** AA가 이 모델에서 환각률 93%를 보고했다는 서술이 있다. 모르는 질문에 거절하지 않고 답을 시도하는 경향을 재는 시험이라는 설명이다. 2차 출처의 서술이며 AA 원문 수치를 확인하지 못했다. 그래도 사실 질문과 인용에 이 모델을 쓰지 않는다는 보수적 근거로 충분하다. [부분: 2차, 원문 미확인]
- **독립 코딩 에이전트 후기는 찾지 못했다.** 비교 글 다수가 같은 AA 수치를 반복하고 한 리뷰는 직접 시험을 하지 않았다고 밝힌다. [미확인]

### 2.4 데이터·정책
- 싱가포르 법인(Nanonoble Pte. Ltd.)이 정책을 발행하고 데이터가 미국에 저장된다는 독립 안내와, 중국을 가리키는 오래된 정책이 충돌한다. 보관 기간은 고정값이 없고 포괄적 학습 제외 약속이나 ZDR은 공개 문서로 확인되지 않는다. 소비자 제품은 정책이 따로다. 모두 2차 출처다. [부분, 충돌]

### 2.5 운용
- **프리뷰 ID와 정식 ID를 혼동하지 않는다.** 프리뷰는 종량제가 없었고 정식과 가격·한도가 다르다. 사용할 경로(API, Token Plan, MiniMax Code)의 약관과 한도를 확인한다. [부분]
- **사실 질문·인용·정확성이 중요한 작업에는 쓰지 않고, 추출·분류·초안처럼 결과를 코드나 사람이 검증하는 작업에 쓴다.** [추정]
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.6 비판적 평가
- 강점 후보: 매우 낮은 단가, 100만 토큰, 작업당 비용 감소(독립 측정 57%), 빠르다는 주장. 약점 후보: 환각률 93% 보도, 파라미터·가중치 공개 여부 미확인, 벤더 수치 조건 불명, 독립 지수 버전 혼재, 프리뷰와 정식 단계 혼선, 가격 변동.
- 막히면 `minimax-m3`나 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 프리뷰·정식 출시·가격·컨텍스트·파라미터 경고·가중치 충돌 | [eesel: MiniMax M3.1 Flash](https://www.eesel.ai/blog/minimax-m3-1-flash), [DataNorth: M3.1 Flash 프리뷰](https://datanorth.ai/news/minimax-releases-m3-1-flash-preview), [UsagePricing: M3.1 Flash API 출시](https://www.usagepricing.com/blueprint/activity/minimax-2026-10-19-m3-1-flash-api-launch), [Vals AI: MiniMax M3.1 Flash](https://www.vals.ai/models/minimax_MiniMax-M3.1-flash) (스니펫만) | [부분, 충돌] |
| 가격 인하·비용 비교 | [Let's Data Science: M3.1 Flash 가격 인하](https://letsdatascience.com/news/minimax-cuts-m31-flash-token-prices-dbc14153), [Braindetox: M3.1 Flash 비용](https://braindetox.kr/en/posts/minimax_m3_1_flash_agent_cost_2026.html) (스니펫만) | [부분] |
| 독립 지수·작업당 비용·환각 보도 | [Artificial Analysis: MiniMax-M3.1-Flash](https://artificialanalysis.ai/models/minimax-m3-1-flash), [OrcaRouter: M3.1 Flash 지능 지수](https://www.orcarouter.ai/fr/blog/minimax-m3-1-flash-ga-intelligence-index), [MyClaw: M3.1 Flash 대 M3](https://myclaw.ai/blog/minimax-m3-1-flash-vs-m3) (스니펫만) | [부분, 충돌] |
| 데이터 정책(2차) | [Flowith: MiniMax 데이터 안전 FAQ](https://flowith.io/blog/minimax-faq-data-safety), [Opper: MiniMax](https://opper.ai/provider/minimax) (스니펫만) | [부분, 충돌] |
- MiniMax 공식 모델 카드·약관 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
