# Qwen3.8-Max · 범용 — 조사 기록
> 제공자: Alibaba(Qwen) · 모델 ID: API `qwen3.8-max`(8월 3일 빌드 `0803`과 9월 2일 빌드 `0902`가 별도 표기됨, 정확한 ID는 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/qwen/qwen3.8-max/general.md`](../../../md/qwen/qwen3.8-max/general.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/general.md`](../../_common/domain-rules/general.md)

## 2. 모델 특성 — Qwen3.8-Max (API 전용 플래그십)
이 환경에서는 Alibaba Cloud·Qwen 공식 문서가 열리지 않아 검색 스니펫과 2차 출처로 썼다. 별도 표기가 없으면 [부분]이다. 같은 세대의 공개 가중치는 `qwen3.8-2.4t-a95b`, `qwen3.8-27b` 문서에 둔다.

### 2.1 위치와 연혁 — 같은 이름 아래 빌드가 둘이다
- 2026-07-19 상하이 WAIC에서 미리보기, **2026-08-03 정식 출시**(QwenCloud, Alibaba Cloud Model Studio). 이후 **9월 2일 빌드(`0902`)**가 따로 평가 사이트에 올라 있다. 두 빌드의 차이는 확인하지 못했다. 점수를 인용할 때 빌드를 명시한다. [부분]
- 총 약 2.4조 파라미터의 MoE이고 쿼리당 활성 약 950억이다(공개 가중치 체크포인트의 이름 `2.4T-A95B`와 일치). 컨텍스트 100만 토큰(입력 최대 약 991,000, 추론 켜면 983,000), 최대 출력은 131,000 또는 65,536으로 출처가 갈린다. [부분, 충돌]
- **가격**(100만 토큰당): 입력 $2 / 출력 $6, 컨텍스트 전 구간에서 같고 장문 추가 요금이 없다는 서술이 있다. 공식 가격표는 확인하지 못했다. [부분]
- **오픈 가중치와 혼동하지 않는다.** API의 Max는 호스팅 전용이다. 같은 세대에서 공개된 2.4T-A95B 체크포인트는 텍스트 전용이고 Max API의 비전과 네이티브 100만 컨텍스트가 빠진 것으로 서술된다(`qwen3.8-2.4t-a95b` 문서). Baseten은 이 모델을 가중치가 공개된 첫 Qwen-Max급이라 부르고 AA는 0902를 비공개로 분류한다. [부분, 충돌]

### 2.2 성능 근거를 읽는 법 — 독립 지수가 스냅샷마다 다르다
- **독립 지수(Artificial Analysis)**: 출시 직후 56으로 보도됐고 이후 58로 상향됐으며, 페이지에 따라 53, 45, 58이 보인다. 0902 빌드의 지수 실행에서 출력 토큰 약 1.9억 개(가격대에서 높은 편), 작업당 비용은 AA 페이지 $5.41, 출시 보도 $1.14로 갈린다. 지수 버전(v4.1.1 등)과 빌드를 함께 확인한다. 한 보도는 56점이 미국 기업 가운데 Anthropic과 OpenAI 외에는 앞선다고 썼고 다른 보도는 Kimi K3가 25% 싸면서 점수가 더 높다고 비교했다. [부분, 충돌]
- **벤더 보고**: Terminal-Bench 2.1 86.6(Claude Opus 4.8·Fable 5 84.6, GPT-5.6 Sol 88.8). 모두 Alibaba 내부 실행이고 독립 검증이 대기 중이다. Alibaba가 코딩 벤치마크를 Anthropic의 에이전트 하네스에서 돌렸다는 서술이 있다(같은 도구에서 모든 모델을 돌리므로 공정하다는 평과 하네스 의존이라는 평이 갈림). 다른 하네스에서 같은 점수를 기대하지 않는다. [부분: 벤더 주장]
- **환각 값은 찾지 못했다.** AA-Omniscience 점수가 보도에 나오지 않았다. [미확인]

### 2.3 데이터·정책
- Alibaba Cloud Model Studio FAQ는 사용자 데이터를 모델 학습에 쓰지 않는다고 밝힌다는 서술이 있다. 리전이 접근 지점과 데이터 저장 위치를 정하고 정적 데이터는 선택 리전에 머문다(추론은 별도 배포 범위 설정). ZDR은 국제 사이트 기업 고객 전용이며 일부 기능은 제외된다. 보관은 최대 30일이라는 제3자 서술이 있으나 공식 문구로 확인하지 못했다. 대화 저장·파일 같은 상태 유지 기능은 사용자가 지울 때까지 남는다. [부분, 충돌]
- 싱가포르 리전을 쓰면 저장 위치가 달라지지만 모기업은 중국에 본사를 두고 있고 중국 법령이 그룹사에 미칠 수 있다는 위험 분석이 있다. 데이터 경계가 중요한 업무는 법무·보안 검토를 거친다. [부분]

### 2.4 운용
- **빌드를 고정한다.** `0803`/`0902`처럼 날짜 빌드가 따로 있으면 재현성이 필요한 작업에서 빌드 ID를 지정하고 갱신 전후 회귀 시험을 돌린다. 별칭이 최신 빌드로 움직이는지는 공식 문서로 확인한다. [추정]
- **추론 모드와 출력 한도.** 추론을 켜면 입력 한도가 줄고(991K→983K) 추론 토큰이 출력 한도를 쓸 수 있다. 출력 한도 서술이 갈리므로(131,000/65,536) 긴 출력은 실제 값으로 시험한다. [부분, 충돌]
- **지침은 짧게.** 이 문서의 §0과 §1.2·§1.3·§1.6을 시스템 프롬프트에 두고 분야 규칙은 필요한 작업에 붙인다. 한국어 존댓말 준수는 직접 측정한다. [미확인]

### 2.5 비판적 평가
- 강점 후보: 낮은 단가, 100만 토큰, 높은 독립 지수(56~58), 장시간 에이전트를 내세운 계열. 약점 후보: 빌드가 둘이고 점수가 스냅샷마다 다름, 토큰 소비가 큼, 벤더 수치가 하네스 의존적, 데이터 정책 일부가 2차 출처, 환각 값 미확인.
- 막히면 `claude/opus-5.5`, `gpt-6.1-sol`, `gemini-4-argon` 문서의 모델로 올린다.

## 4. 근거와 한계
| 내용 | 출처 | 수준 |
|---|---|---|
| 출시일·사양·가격·벤더 수치 | [DataNorth: Qwen3.8-Max 출시](https://datanorth.ai/news/alibaba-releases-qwen3-8-max), [Yotta Labs: Qwen 3.8 Max](https://www.yottalabs.ai/post/qwen-3-8-max-release-date-specs-how-to-access-2026), [Noze: Qwen3.8-Max 2.4T MoE](https://www.noze.it/en/insights/qwen-3-8-max/), [Cloudprice: Qwen3.8-Max](https://cloudprice.net/models/alibaba-qwen3-8-max) (스니펫만) | [부분, 충돌] |
| 독립 지수·토큰·비용 | [Artificial Analysis: Qwen3.8 Max (0902)](https://artificialanalysis.ai/models/qwen3-8-max), [Artificial Analysis: Qwen3.8 Max (0803)](https://artificialanalysis.ai/models/qwen3-8-max-0803), [The Decoder: Kimi K3와의 비교](https://the-decoder.com/qwen3-8-max-catches-claude-opus-4-8-but-kimi-k3-still-scores-higher-for-25-percent-less/), [OfficeChai: AA 56점](https://officechai.com/ai/qwen-3-8-max-scores-56-on-artificial-analysis-intelligence-index-ahead-of-all-us-companies-except-anthropic-and-openai/) (스니펫만) | [부분, 충돌] |
| 데이터 정책 | [Alibaba Cloud Model Studio: 데이터 보관 정책](https://www.alibabacloud.com/help/en/model-studio/data-retention-policy), [DevelopersDigest: Qwen 보관](https://www.developersdigest.tech/models/data-retention/qwen), [Security Scientist: Qwen 위험 평가](https://www.securityscientist.net/blog/qwen-risk-assessment-template/) (스니펫만) | [부분, 충돌] |
- Alibaba 공식 모델 카드·약관 본문을 열지 못했다. 이 표의 어떤 값도 [확인]이 아니다.
