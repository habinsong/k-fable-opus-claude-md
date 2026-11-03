# Kimi K3.1 · 네이티브 — 조사 기록
> 제공자: Moonshot AI · 모델 ID: API `kimi-k3.1-pro`, 고속 변형 `kimi-k3.1-pro-highspeed`(Moonshot 발표를 전한 보도의 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/kimi/kimi-k3.1/native.md`](../../../md/kimi/kimi-k3.1/native.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/native.md`](../../_common/domain-rules/native.md)

## 2. 이 모델의 네이티브 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 폐쇄형 API 먼저(가중치 11-04 공개 예정), 대표 수치(Terminal-Bench 4.0 65.7% 등)는 벤더 제공값, 공격적 사이버 능력을 의도적으로 낮춤, C/C++·Rust 평가 없음, 기본 추론 단계 `max`.

**개발 보조로 쓸 때**
- **대표 수치는 벤더 제공값이고 조건이 섞여 있다.** Terminal-Bench 4.0 65.7%(Claude Opus 5.5 66.4%), 출시 표의 BrowseComp 92.1, HLE(도구 포함) 70.0, SWE-Marathon v1.1 51.7은 `max` 노력 단계의 Moonshot 표이며, 평가 일부에서 모델마다 다른 에이전트 프레임워크를 썼다는 지적이 있다. DeepSWE v1.1과 SWE-Marathon v1.1은 각주에만 있고 점수가 공개되지 않았다는 서술도 있다. 벤치마크 이름·버전·노력 단계·하네스·보고 주체를 확인하지 않은 숫자를 비교하지 않는다. [부분: 벤더 주장, 충돌]
- **C++·Rust·시스템 코드의 언어별 평가는 찾지 못했다.** [미확인] 메모리 관리, 동시성, 수명, ABI는 문법이 맞아도 틀리기 쉬우므로 핵심 변경에는 쓰지 않고, 쓴다면 sanitizer(ASan·UBSan·TSan)와 테스트를 지시문으로 강제한다. 핵심 변경은 `claude/sonnet-5.5` 이상, `gpt-6.1-sol`, `gemini-4-argon` 문서를 따르거나 우리 코드로 같은 과제를 비교한다.
- **보안 성격의 시스템 작업은 성능이 낮을 수 있다.** Moonshot은 학습 데이터에서 사이버 관련 자료를 빼 공격적 능력을 의도적으로 낮췄고 내부 익스플로잇 벤치마크 성공률이 실험 버전 90.5%에서 최종 81%로 내려갔다고 한다. 퍼징 하네스 작성, 취약점 분석, 메모리 손상 재현 같은 정당한 보안 작업은 결과가 약할 수 있다. 이는 거부 규칙이 아니라 능력 축소라서 "거부하지 않았으니 안전하다"고 읽지 않고 결과를 사람이 검증한다. [부분: 벤더 주장]
- **기본 추론 단계가 `max`라는 서술이 있다.** 짧은 수정에도 긴 추론과 큰 토큰 소비가 생길 수 있다. 단계를 요청마다 명시하고 `low`·`high`로 시작해 품질 차이를 측정한다. 긴 디버그 루프는 과제당 토큰·도구 호출 수를 기록한다. 지정 방법은 공식 문서로 확인한다. [부분/미확인]
- **에이전트 루프에 안전장치를 먼저 둔다.** Moonshot의 Kimi Code 안내(승인 기능 유지, diff 검토, 비밀 보호, 되돌릴 수 있는 Git 브랜치)를 따르고 파괴적 명령 차단(권한·훅), 작업 디렉터리 격리, 시간·토큰 한도를 설정한다. 완료 보고는 빌드·테스트·sanitizer 출력과 `git diff`로 확인하고, 테스트·경고·sanitizer 설정이 바뀌었는지도 확인한다. 억제 지시문을 넣거나 검사를 끄는 제안은 따르지 않는다. [부분]
- **긴 컨텍스트에 기대지 않는다.** 100만 토큰이어도 관련 함수·호출부·오류 메시지·빌드 설정만 주는 편이 지연·비용에서 낫다. 컨텍스트 길이별 요금 단계가 없다는 서술이 있어 비용 문턱은 낮으나 지연은 남는다. [부분/추정]
- **도구 호출 신뢰도 수치를 쓰지 않는다.** 한 비공식 사이트의 도구 선택 967/1,000, 에이전트 루프 199/200 통과는 방법론을 확인할 수 없다. 우리 하네스에서 호출 실패율을 측정한다. [미확인]
- **미공개 소스를 API로 보내기 전에 약관을 확인한다.** 학습 사용·보관·처리 위치 서술이 어긋난다(general.md §2.5). [부분, 충돌] 확인 전에는 비밀·고객 코드를 보내지 않는다(§1.6).

**애플리케이션에 내장할 때**
- **모델은 서버 API로 호출한다.** 가중치가 공개돼도 규모가 커서 데스크톱 프로그램에 번들할 수 없다. 클라이언트에 API 키를 두지 않고 자체 백엔드를 거친다. 모델 출력으로 만든 경로·명령·코드를 그대로 실행하지 않으며 파서·역직렬화 코드는 퍼징 대상으로 본다(§3.1).
- **오프라인·자체 호스팅이 필요하면 공개 후 라이선스를 먼저 읽는다.** 직전 K3의 자체 라이선스(MaaS 매출 기준 별도 계약, 대규모 제품의 표시 의무)가 K3.1에 적용되는지 미확인이다. 소형 로컬 모델은 `gemma-4-e4b`, `qwen3.6-27b` 문서를 본다. [부분/미확인]

## 4. 근거와 한계
- 대표 수치·조건·자리표시: [BenchmarkList: Kimi K3.1 Pro](https://benchmarklist.com/models/moonshotai-kimi-k3.1-pro/), [OrcaRouter: K3.1 Pro 벤치마크](https://www.orcarouter.ai/blog/kimi-k3-1-pro-benchmark), [DataLearner: K3.1 대 K3](https://www.datalearner.com/ai-models/compare/kimi-k3-1/vs/kimi-k3) (스니펫만) [부분: 벤더 주장]
- 사이버 능력 축소: [VKTR: K3.1 Pro와 사이버 능력 제한](https://www.vktr.com/ai-platforms/kimi-k31-pro-nears-top-proprietary-models-as-moonshot-limits-its-cyber-skills/), [WinZheng: 사이버 능력 약화](https://www.winzheng.com/en/article/kimi-k31-pro-open-weights-cyber-capability-weakening) (스니펫만) [부분: 벤더 주장 포함]
- Kimi Code 안내·도구 호출 수치(비공식): [DEV: Kimi K3와 Kimi Code](https://dev.to/hassann/how-to-use-kimi-k3-for-coding-with-kimi-code-3d7a), [kimi-ai.chat(비공식)](https://kimi-ai.chat/guide/kimi-code/) (스니펫만) [부분/미확인]
- 한계: 언어별 시스템 코드 평가와 도구 호출 오류율의 독립 자료가 없다.
