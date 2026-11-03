# Muse Wonder · 펌웨어 — 조사 기록
> 제공자: Meta(Meta Superintelligence Labs) · 모델 ID: `muse-wonder-1.0`(한 출처의 표기, 확인 필요), 상위 변형 Wonder Full은 `muse-wonder-full-1.0`(카탈로그 전용, 한 출처의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/muse/muse-wonder/firmware.md`](../../../../md/muse/muse-wonder/firmware.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/firmware.md`](../../../_common/domain-rules/firmware.md)

## 2. 이 모델의 펌웨어 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 폐쇄형 API 모델이라 기기 내 실행 불가, 장시간 에이전트(Active Focus)를 내세움, 임베디드 평가 없음, 안전 분류기 적용, 데이터 약관 충돌.

- **기기 안에서 돌릴 모델이 아니다.** 폐쇄형이며 가중치를 받을 수 없다. 개발 워크스테이션에서 API로 쓰는 보조 도구로만 쓴다. 기기 내 추론이 필요하면 소형 모델 문서(`gemma-4-e2b`, `gemma-4-e4b`)를 본다.
- **펌웨어 코드를 직접 쓰거나 고치게 하지 않는다.** 레지스터 값, 인터럽트, 부트·업데이트 경로, 서명 검증은 환각이 장치 고장이나 보안 구멍이 된다. 임베디드·펌웨어 평가는 찾지 못했다. [미확인] 터미널 작업 점수(Terminal-Bench 4.0에서 Wonder 52%, Full 57%라는 서술)는 장치 쓰기나 실시간 제약과 무관하다. 이 영역은 `gemini-4-argon`, `claude/sonnet-5.5` 이상, `gpt-6.1-sol` 문서를 따른다. [부분]
- **레지스터·타이밍을 모델의 기억에서 가져오지 않는다.** 환각·사실성 평가를 찾지 못했다. 데이터시트·레퍼런스 매뉴얼의 개정판과 페이지를 사람이 확보한 텍스트로 주고, 확인하지 못했으면 값을 쓰지 않는다(§3.1). [미확인]
- **써도 되는 작업.** UART·RTT 로그 분류, 맵 파일 요약, 컴파일러 경고 그룹화, 변경 이력 요약, 호스트에서 돌리는 테스트 코드(하드웨어 추상화 뒤쪽 로직)의 초안. 입력은 관련 구간만 준다. 출력은 원본 로그·맵 파일과 한 건씩 대조한다. 단가가 높으므로($4/$20) 대량 로그 분류는 `muse-spark`나 더 싼 모델로 처리한다.
- **장시간 에이전트에 장치 접근을 열어 주지 않는다.** Meta는 Active Focus가 막히면 대안을 시도하고 중대한 행동 전에 확인한다고 설명한다. 벤더 설명이며, 대안을 시도하는 성향은 되돌릴 수 없는 장치 쓰기에서는 위험 요인이 될 수 있다. 플래시 소거, 퓨즈·OTP, 보호 비트, 부트로더 덮어쓰기, 디버그 포트 잠금은 사람이 대상 장치와 이미지를 확인한 뒤 실행한다. 프로그래머·시리얼 제어 도구는 읽기 전용부터 연결하고 권한·훅으로 쓰기 명령을 차단한다. [부분: 벤더 주장/추정]
- **변경 후 검증을 강제한다.** 호스트 단위 테스트와 정적 분석을 직접 돌려 출력을 읽고, 경고를 억제하라는 제안은 따르지 않는다. 실제 보드에서 확인하지 못했으면 "하드웨어 미검증"이라고 쓴다.
- **안전 분류기를 고려한다.** 임베디드 보안·취약점 분석(퍼징, 익스플로잇 재현 등)은 분류기의 거부 대상이 될 수 있다. 정당한 보안 연구라면 우회하지 말고 사람의 검토 경로를 둔다. [부분/추정]
- **펌웨어 소스·로그·서명 키·양산 이미지를 API로 보내지 않는다(약관 확인 전).** 데이터 처리 서술이 충돌하고 Active Memory의 저장 정책을 찾지 못했다. [미확인, 충돌] 서명 키와 디버그 인증 정보는 약관과 무관하게 보내지 않는다(§3.4).

## 4. 근거와 한계
- 터미널 지표: [Braindetox: 평가 조건](https://braindetox.kr/en/posts/meta_muse_wonder_agent_models_release_2026.html), [MindStudio: Wonder 벤치마크](https://www.mindstudio.ai/blog/muse-wonder-benchmarks-vs-opus-gpt6) (스니펫만) [부분, 충돌]
- Active Focus 설명: [Digit: Active Memory와 Active Focus](https://www.digit.in/features/general/meta-muse-wonder-explained-what-active-memory-and-active-focus-do.html) (스니펫만) [부분: 벤더 설명]
- 안전 분류기 서술: [BetaNews: Muse Wonder](https://betanews.com/article/muse-wonder-frontier-model-developers/) (스니펫만) [부분]
- 한계: 임베디드·펌웨어에 대한 평가가 없다. 사용 범위 제한은 모델 규모와 비가역 작업의 위험에서 도출한 안전 권고다.
