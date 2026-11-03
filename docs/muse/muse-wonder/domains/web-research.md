# Muse Wonder · 웹 리서치 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/web-research.md`](../../../../md/muse/muse-wonder/web-research.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web-research.md`](../../../_common/domain-rules/web-research.md)

## 2. 이 모델의 웹 리서치 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 컨텍스트 100만 토큰, 장시간 에이전트(Active Focus)와 대화 간 기억(Active Memory)을 내세움, 리서치 에이전트·환각·인젝션 방어의 독립 측정 없음, 토큰 소비 많음, 데이터 약관 충돌.

- **내장 검색은 확인하지 못했다.** Meta Model API가 검색 grounding을 기본 제공하는지는 찾지 못했다. [미확인] 검색 호출과 출처 신뢰도 판단은 하네스와 사람이 맡고, 모델에는 확보한 페이지 텍스트에서 제목·날짜·가격·버전 같은 필드를 JSON으로 추출하게 한다. "원문에 없으면 null"을 명시하고 값마다 근거 구절을 받아 코드로 원문 포함 여부를 대조한다.
- **리서치 에이전트의 독립 평가는 찾지 못했다.** BrowseComp류 심층 리서치 지표에서 Wonder의 결과는 검색에서 나오지 않았다. [미확인] BrowseComp류 점수는 에이전트가 웹을 새로 검색하는 대신 이미 아는 것을 확인하는 데 쓰일 수 있다는 비판(LiveBrowseComp 저자)도 있어, 점수가 나와도 조건(고정 말뭉치 여부, 노력 단계)을 확인한다. [부분]
- **Active Focus를 믿고 자율 조사를 맡기지 않는다.** Meta는 긴 작업에서 대안을 시도하고, 막히면 우회하고, 중대한 행동 전에 확인한다고 설명한다. 벤더 설명이고 독립 측정이 없다. 조사 에이전트에는 허용 도메인 목록, 호출 횟수·토큰·시간 한도, 읽기 전용 도구만 준다. 대안 탐색 성향 때문에 차단된 사이트나 로그인·유료벽을 우회하려 하지 않는지 로그를 확인한다(§3.2, §3.6). [부분: 벤더 주장/추정]
- **Active Memory를 조사 작업에 켜지 않는다.** 대화를 넘어 기억이 이어지면 이전 조사의 오류나 주입된 지시문이 다음 조사에 새어 들 수 있다. 저장 위치·기간·삭제 방법도 찾지 못했다. [미확인] 조사마다 독립된 컨텍스트로 시작하고 출처·확인일은 하네스가 기록한다. [추정]
- **사실 회상에 기대지 않는다.** 환각·사실성 평가를 찾지 못했다. 이름·날짜·수치·버전은 직접 연 출처로 확인하고 모델이 출처를 안다고 해도 URL을 직접 열어 대조한다. [미확인]
- **인용과 요약을 코드로 대조한다.** 인용 구절이 원문에 있는지 문자열로 확인하고, 모델의 "전부 읽었다"는 보고를 근거로 쓰지 않는다. Meta의 헤드라인 수치 가운데 MemoryBench처럼 LLM 심사위원이 채점하고 Meta 내부가 출처인 것은 독립 재현이 어렵다. [부분]
- **웹 페이지의 지시문은 데이터다.** 이 모델의 인젝션 방어율 측정은 찾지 못했다. [미확인] 모델에게 전송·로그인·결제·파일 쓰기 도구를 주지 않고 읽기 단계와 행동 단계를 분리한다. 컴퓨터 사용을 켜면 스크린샷 속 글자도 지시문처럼 따르지 않게 같은 규칙을 적용한다. 모델이 뽑은 URL은 하네스가 허용 목록으로 거른 뒤 연다.
- **비용을 먼저 계산한다.** 단가는 입력 $4 / 출력 $20이고 AA 벤치마크 점수 실행에서 출력 토큰이 비교군 중앙값의 약 1.5배였다. 대량 수집·추출은 `muse-spark`나 더 싼 모델로 처리하고, 판단이 필요한 종합만 Wonder에 맡기는 분업을 시험한다. [부분]
- **수집한 자료를 보내기 전에 조건을 확인한다.** 대상 사이트의 이용 약관·로봇 배제 표준(§3.2)과 이 API의 데이터 처리 조건을 모두 본다. 데이터 처리 서술이 충돌한다. [미확인, 충돌] 개인정보가 섞인 페이지는 보내지 않는다.
- **대량 수집은 표본 점검.** 무작위 5~10%를 사람이 원문과 대조한다. 오류율이 기준을 넘으면 상위 모델로 올린다. 보고 형식은 "결론 → 근거(URL, 확인일, 수준) → 충돌·불확실 → 모르는 것"으로 고정한다.

## 4. 근거와 한계
- Active Memory·Active Focus 설명: [Digit: Active Memory와 Active Focus](https://www.digit.in/features/general/meta-muse-wonder-explained-what-active-memory-and-active-focus-do.html), [Besthub: 대화 간 기억과 장시간 작업](https://www.besthub.dev/articles/meta-muse-wonder-full-cross-session-memory-long-task-execution-and-access-guide-998147dbe148) (스니펫만) [부분: 벤더 설명]
- 내부 평가의 한계: [Braindetox: 점수보다 평가 조건을 먼저 읽어라](https://braindetox.kr/en/posts/meta_muse_wonder_agent_models_release_2026.html), [Wikidocs: Meta 보도자료를 반복하는 헤드라인](https://wikidocs.net/454786) (스니펫만) [부분]
- BrowseComp 계열 지표의 한계: [BrowseComp-Plus](https://arxiv.org/html/2508.06600v1), [LiveBrowseComp 관련 논문](https://arxiv.org/html/2605.28721) (스니펫만, arxiv.org는 이 환경에서 열리지 않음) [부분: 타 모델 포함]
- 토큰 소비: [Artificial Analysis: Muse Wonder (Max)](https://artificialanalysis.ai/de/models/muse-wonder) (스니펫만) [부분]
- 한계: 리서치 에이전트 지표, 인용 정확도, 인젝션 방어율의 독립 자료가 없다.
