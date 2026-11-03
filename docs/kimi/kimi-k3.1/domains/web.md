# Kimi K3.1 · 웹 — 조사 기록
> 제공자: Moonshot AI · 모델 ID: API `kimi-k3.1-pro`, 고속 변형 `kimi-k3.1-pro-highspeed`(Moonshot 발표를 전한 보도의 표기, 확인 필요) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/kimi/kimi-k3.1/web.md`](../../../../md/kimi/kimi-k3.1/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 상위 폴더의 [`README.md`](../README.md)가 안내하는 개요·운용·비판 문서를 따른다. 요약: 가중치는 11-04 공개 예정(라이선스 미확인), 입력 $2 / 출력 $10, 독립 지수 55, 기본 추론 단계 `max`, 이미지·영상 입력, 출시 직후 가용성 문제, 데이터 정책 서술 불일치.

- **웹 UI 생성의 독립 평가는 찾지 못했다.** [미확인] Moonshot이 내세운 강점은 코드, 3D 제작, 금융 리서치, 장기 에이전트이고 프런트엔드는 거론되지 않았다. 앱과 코딩 도구에 편집 가능한 3D 모델 기능이 추가됐다는 보도는 있으나 웹 UI 품질과 다른 능력이다. 컴포넌트 단위 수정, 새 화면, 스크린샷 재현을 우리 코드베이스에서 상위 모델과 같은 조건으로 돌려 비교하고, 스크린샷 대조와 린터·타입체크·테스트 출력으로 판정한다. 기존 UI 체계가 우선한다(§3.1). [부분]
- **스크린샷을 입력으로 줄 수 있다.** 텍스트·이미지·영상 입력이라는 서술이 여럿이다. 스크린샷의 레이아웃·간격·색 재현 정확도를 잰 자료는 찾지 못했으므로 우리 화면으로 직접 시험한다. [부분/미확인]
- **기본 추론 단계가 최고(`max`)라는 서술이 있다.** 컴포넌트 수정 같은 작은 일에 최고 단계를 쓰면 토큰과 비용이 크다. 단계를 요청마다 명시하고 `low`·`high`로 시작해 품질 차이를 측정한다. 이전 K3는 지수 실행에서 출력 토큰 1.61억 개였다. 지정 방법은 공식 문서로 확인한다. [부분/미확인]
- **Moonshot의 대표 수치를 웹 개발 능력으로 옮기지 않는다.** Terminal-Bench 4.0 65.7%는 벤더 제공값이고 일부 평가에서 모델마다 다른 에이전트 프레임워크를 썼다는 지적이 있다. 출시 시점에 일부 점수 칸이 자리표시 문자열로 남아 있었고 DeepSWE v1.1, SWE-Marathon v1.1은 각주에만 있고 점수가 공개되지 않았다는 서술도 있다. [부분: 벤더 주장]
- **Kimi Code를 쓰려면 Moonshot 안내와 §1.6을 따른다.** 승인 기능을 켜 두고, diff를 검토하고, 비밀을 보호하고, 되돌릴 수 있는 Git 브랜치를 쓴다. 완료 보고는 린터·타입체크·테스트 출력과 `git diff`로 확인한다. [부분]
- **가용성을 설계에 반영한다.** 출시 직후 사용량 제한으로 유료 사용자 접근이 끊겨 Moonshot이 사과하고 쿼터를 복원했다는 보도가 있다. CI와 코드 생성 파이프라인에는 폴백 모델과 재시도·타임아웃을 둔다. [부분]
- **고속 변형은 비용과 맞바꾼다.** Highspeed는 2~3배 빠르지만 단가가 두 배($4/$20)다. 대화형 UI 작업의 지연이 병목일 때만 쓴다. [부분]
- **보안·접근성 판단을 맡기지 않는다.** 인가, 입력 검증, 비밀 노출, 접근성 "충족" 여부는 도구 출력과 §3.1 기준으로 사람이 점검한다. API·CSS·브라우저 지원은 공식 문서와 린터·컴파일러 출력으로 확인한다.
- **미공개 소스를 보내기 전에 약관을 확인한다.** API 데이터의 학습 사용·보관·처리 위치 서술이 서로 어긋난다(README.md가 안내하는 개요·운용 문서.5). [부분, 충돌] 확인 전에는 비밀·고객 데이터가 담긴 코드를 보내지 않는다(§1.6).

## 4. 근거와 한계
- 강점 영역·입력 방식·고속 변형: [Mixed News: Kimi 3D 모델과 K3.1 Pro](https://mixed-news.com/en/?p=38061), [CometAPI: Kimi K3.1 Pro](https://www.cometapi.com/zh-TW/models/moonshotai/kimi-k3-1-pro/), [Braindetox: Kimi K3.1 Pro 출시](https://braindetox.kr/en/posts/kimi_k3_1_pro_release_2026.html) (스니펫만) [부분]
- 대표 수치의 조건·자리표시 문자열: [OrcaRouter: K3.1 Pro 벤치마크](https://www.orcarouter.ai/blog/kimi-k3-1-pro-benchmark), [BenchmarkList: Kimi K3.1 Pro](https://benchmarklist.com/models/moonshotai-kimi-k3.1-pro/) (스니펫만) [부분: 벤더 주장]
- 가용성 문제: [Cryptopolitan: 쿼터 초기화](https://www.cryptopolitan.com/moonshot-resets-kimi-k3-1-pro-quotas-after-rate-limit-apology/), [SCMP: Moonshot 사과](https://scmp.com/tech/big-tech/article/3372247/moonshot-apologises-after-kimi-k31-pro-roll-out-stumbles-promotional-scrutiny-widens) (스니펫만) [부분]
- 한계: 웹 UI·프런트엔드 독립 평가가 없다. Moonshot 공식 문서를 읽지 못했다.
