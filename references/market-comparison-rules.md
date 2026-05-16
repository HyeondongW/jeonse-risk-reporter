# 시세 비교 규칙

`market-comps.csv`만 사용합니다. 실제 실거래가 데이터를 외부에서 가져오지 않습니다.

필수 컬럼:

```csv
legal_dong,area_m2,contract_date,listing_type,deposit,monthly_rent,building_type,floor,source_note
```

## 비교군

시세 비교 표에는 항상 아래 세 행을 만듭니다.

1. `같은 동·면적대 (6개월)`: 같은 `legal_dong`, 같은 `listing_type`, 면적 `±5m²`, `analysis_date` 기준 최근 6개월.
2. `같은 동·면적대 (1년)`: 같은 `legal_dong`, 같은 `listing_type`, 면적 `±5m²`, `analysis_date` 기준 최근 1년.
3. `같은 동 전체 (6개월)`: 같은 `legal_dong`, 같은 `listing_type`, 면적 제한 없음, `analysis_date` 기준 최근 6개월.

`analysis_date`가 없으면 현재 날짜를 사용합니다.

## 중위값

전세는 `deposit` 중위값을 사용합니다.

월세 또는 반전세는 보증금 중위값과 월세 중위값을 함께 표시합니다. 월세가 사용자의 주된 월 지출이면 화면에 보이는 차이는 `monthly_rent` 기준으로 계산합니다.

비교군 거래가 3건 미만이면 신뢰도를 `⚠️ 부분`으로 표시하고 거래 건수가 적다는 점을 설명합니다. 비교군이 0건이면 `⚫ 확인 불가`로 표시합니다.

## 차이 판정

전세 보증금 기준:

- `+15.0%` 이상: `🔴`
- `+5.0%` 이상 `+15.0%` 미만: `🟡`
- `-5.0%` 이상 `+5.0%` 미만: `✅`
- `-5.0%` 미만: `✅`

비율은 소수점 1자리로 반올림합니다. 양수에는 `+` 기호를 붙입니다.
