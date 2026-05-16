# 등기부 분석 규칙

등기부 입력은 다음 형태를 허용합니다.

1. listing YAML의 `registry` 아래에 있는 구조화된 YAML
2. 등기부 PDF에서 복사한 텍스트
3. Codex가 PDF에서 추출한 텍스트

예시는 구조화된 YAML을 사용합니다. 구조화된 필드가 있으면 그 값을 우선합니다.

## 필드

- `owner_name`
- `owner_changes`
- `mortgages`
- `total_max_bond`
- `seizures`
- `trust`
- `lease_registrations`
- `earliest_priority_right`
- `senior_deposit_total`

## 근저당 부담률 공식

같은 법정동·면적대 6개월 시세 중위값이 있으면 아래 공식을 사용합니다. 단, 이 공식은 `total_max_bond > 0`일 때만 근저당 부담률 체크로 적용합니다. 근저당이 없으면 해당 항목은 `✅ 해당 없음`입니다.

```text
부담률 = (채권최고액 합계 + 보증금) / 시세 중위값
```

비율은 소수점 1자리로 표시합니다.

예:

```text
(260,000,000 + 280,000,000) / 220,000,000 = 245.5%
```

`market_median`, `deposit`, 등기부 정보 중 하나라도 없으면 부담률 체크는 `⚫ 확인 불가`입니다.

## 소유자 변경

각 `owner_changes[].date`를 `analysis_date`와 비교합니다.

- 365일 이내: `🔴 해당함`
- 365일 초과: `✅ 해당 없음`
- 등기부 없음: `⚫ 확인 불가`

## 권리관계 요약 톤

확인된 사실만 요약합니다. 범죄 의도, 신용도, 소유자 신뢰도, 계약 가능 여부를 추정하지 않습니다.
