# GLM-5.3-Flash · 웹 — 조사 기록
> 제공자: Z.ai(Zhipu) · 모델 ID: API `glm-5.3-flash`(빠른 서빙 변형 `glm-5.3-flashx`가 별도 존재, 표기 확인 필요), 가중치 저장소 `zai-org/GLM-5.3-Flash`(검색 결과의 표기) · 기준일: 2026-11-03 · 근거 표기: [확인]·[부분]·[미확인] (정의는 §1.3)

> 사람이 읽는 조사·검증 기록이다. LLM 컨텍스트에 넣지 않는다.
> 컨텍스트용 지침: [`md/glm/glm-5.3-flash/web.md`](../../../md/glm/glm-5.3-flash/web.md)
> 절 번호는 지침 문서의 번호를 따른다(§0 응답 계약, §1 작업 원칙, §2 모델 지침, §3 분야 규칙).
> 분야 규칙의 근거 수준 표기 원본: [`docs/_common/domain-rules/web.md`](../../_common/domain-rules/web.md)

## 2. 이 모델의 웹 작업 운용
모델 전체 특성은 같은 폴더의 `general.md` §2를 따른다. 요약: 총 약 320B·활성 약 18B MoE, 이미지·영상 입력(출처 충돌), MIT 가중치, 벤더 수치는 미확인, 독립 코딩 평가 얕음, 무료 등급 한도 불안정.

- **웹 UI 코드 생성의 독립 평가는 찾지 못했다.** [미확인] 개인 시험 후기는 SVG 생성, 코딩 게임 같은 소규모 과제였고, 한 리뷰는 단일 코딩 시험이 작은 함수 하나였으며 저장소 수준 변경이 아니었다는 이유로 "통제된 API 시험 대상이지 무조건적인 운영 권장 대상은 아니다"라고 결론냈다. [부분: 개인 후기] 시각 마감은 스크린샷으로 직접 대조하고, 기존 UI 체계가 우선한다(§3.1).
- **스크린샷에서 코드로 만드는 용도는 직접 시험한다.** 이 모델은 이미지를 입력으로 받는다는 서술이 주류이고 차트·문서 이해 지표(OfficeQA Pro, CharXiv, Chartography with Tools)에서 강점을 내세우지만 이는 Z.ai 보고를 옮긴 집계다. 제3자 비전 평가는 종합 66.3%로 33개 중 22위였다(자체 과제 한 번 실행). UI 스크린샷의 레이아웃·간격·색 재현 정확도를 잰 자료는 찾지 못했다. [부분/미확인] 같은 계열의 다른 모델(GLM-5V-Turbo)의 디자인-코드 설명을 옮기지 않는다.
- **디자인 벤치마크의 한계를 안다.** Design2Code류 점수는 픽셀 유사도를 재지 유지보수성을 재지 않는다는 지적이 있다. 컴포넌트 규약, 접근성, 상태 관리가 우리 코드베이스와 맞는지는 별도로 확인한다. [부분]
- **호출 경로마다 동작이 다르다.** 한 제3자 호스트는 자사 서빙에서 `parallel_tool_calls: false`를 강제하고 Z.ai 경로는 강제하지 않는다고 밝혔다. 병렬 도구 호출을 쓰는 하네스는 사용하는 경로에서 시험한다. 속도 변형 `glm-5.3-flashx`의 차이는 서빙 속도뿐이라는 설명만 있다. [부분]
- **무료 등급은 개발 시험용이다.** 요청 한도가 있고 예고 없이 줄 수 있으며, 개발 도구(OpenCode)에서의 기간 한정 무료는 종료일이 미확인이고 운영 용도로 권하지 않는다는 안내가 있다. CI와 제품 코드 생성 파이프라인의 기본 모델로 쓰지 않는다. [부분]
- **보안·접근성 판단을 맡기지 않는다.** 인가, 입력 검증, 비밀 노출, 접근성 "충족" 여부는 도구 출력과 §3.1 기준으로 사람이 점검한다. API·CSS·브라우저 지원은 공식 문서와 린터·컴파일러 출력으로 확인한다.
- **완료 보고는 도구 출력으로 확인한다.** 환각률·도구 호출 오류율의 독립 측정이 없다. [미확인] 린터·타입체크·테스트 출력과 `git diff`를 직접 읽는다.
- **미공개 소스를 API로 보내기 전에 약관을 확인한다.** 데이터 처리 조건을 찾지 못했다. [미확인] 확인 전에는 비밀·고객 데이터가 담긴 코드를 보내지 않는다(§1.6).
- **가중치는 공식 저장소에서만 받는다.** 제3자 재업로드가 많다(general.md §2.4).

## 4. 근거와 한계
- 단일 시험 후기·운영 비권장 결론: [Kingy AI: GLM-5.3 Flash 리뷰](https://kingy.ai/blog/glm-5-3-flash-review-tests-pricing/), [MindStudio: 다중 GPU 시험](https://www.mindstudio.ai/blog/glm-5-3-flash-hands-on-multi-gpu-test/) (스니펫만) [부분: 개인 후기]
- 비전 지표·제3자 평가: [Eden AI 비교](https://www.edenai.co/post/glm-5-3-flash-benchmark-vs-gemini-deepseek-gpt-5-6), [BenchLM: GLM-5.3-Flash](https://benchlm.ai/md/models/glm-5-3-flash.md), [Roboflow 비전 평가](https://playground.roboflow.com/models/z-ai/glm-5-3-flash) (스니펫만) [부분: 벤더·집계]
- 도구 호출 동작·무료 등급: [Sarvam 문서](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash), [SmartScope: OpenCode 무료](https://smartscope.blog/en/blog/opencode-glm-5-3-flash-free-limited-time-2026/) (스니펫만) [부분]
- 한계: 웹 UI·스크린샷 변환의 독립 평가와 공식 자료를 읽지 못했다.
