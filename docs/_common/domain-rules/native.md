# 분야 규칙 "시점에 민감한 사실"의 근거 수준 — 네이티브

> 사람이 읽는 조사 기록이다. LLM 컨텍스트에 넣지 않는다.
> `universal/native.md`의 "시점에 민감한 사실" 표 각 행이 어디까지 확인됐는지다. 항목과 내용이 `universal`과 같아야 하며 `scripts/docs_tool.py check`가 대조한다.
> 수준 정의는 [`docs/README.md`](../../README.md)에 있다. 원래 수준 표기가 붙은 전체 원문은 git 이력의 `docs/_common/domain-rules/`에 있다.

| 항목 | 근거 수준 | 내용 |
|---|---|---|
| 메모리 안전 권고 | 부분 | CISA 지침(Product Security Bad Practices v2, 2025-01)은 메모리 안전 로드맵 공개를 2025년 말까지 요구하고 신규 제품군은 메모리 안전 언어를 권장. 2030 이전 지원 종료 제품은 제외 |
| Secure Boot 인증서 | 부분 | Microsoft의 2011년 발급 KEK·UEFI CA는 2026-06 말, Windows Production PCA 2011은 2026-10-19 만료(날짜는 출처마다 하루 안팎 차이). 2023 인증서로 교체 필요, PK는 OEM 소유라 영향 없음 |
| 양자내성 암호 | 부분 | NIST IR 8547 최종판 기준 RSA·ECC 등은 2030 이후 deprecated, 2035 전 폐지 취지. FIPS 203(ML-KEM)·204(ML-DSA)·205(SLH-DSA)는 2024-08 발행, FIPS 206(FN-DSA)은 초안 단계로 보도됨 |
