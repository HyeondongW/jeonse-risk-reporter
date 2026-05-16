# 인프라 점수 규칙

`infrastructure.csv`만 사용합니다. 지도 API나 교통 API를 외부에서 호출하지 않습니다.

필수 컬럼:

```csv
legal_dong,nearest_subway_line,nearest_subway_station,subway_walk_min,workplace_transit_min,workplace_transfer_count,mart_walk_min,convenience_walk_min,hospital_walk_min,park_walk_min
```

## 카테고리

| 항목 | 가중치 | 입력 |
|---|---:|---|
| 🚇 대중교통 | 0.3 | `subway_walk_min` |
| 💼 직장·학교 접근성 | 0.3 | `workplace_transit_min`, `workplace_transfer_count` |
| 🛒 생활 인프라 | 0.2 | `mart_walk_min`, `convenience_walk_min` |
| 🏥 의료·여가 | 0.2 | `hospital_walk_min`, `park_walk_min` |

## 거리 점수

지하철:

- `7분 이하`: 5점
- `10분 이하`: 4점
- `15분 이하`: 3점
- `20분 이하`: 2점
- `20분 초과`: 1점

마트, 편의점, 병원, 공원:

- `5분 이하`: 5점
- `10분 이하`: 4점
- `15분 이하`: 3점
- `20분 이하`: 2점
- `20분 초과`: 1점

직장·학교 접근성:

- `30분 이하`: 5점
- `45분 이하`: 4점
- `60분 이하`: 3점
- `75분 이하`: 2점
- `75분 초과`: 1점

환승이 1회를 초과하면 초과 환승 1회당 `0.5점`을 뺍니다. 최저 점수는 1점입니다.

## 누락 데이터

카테고리 계산에 필요한 필드가 없으면 해당 카테고리를 `⚫ 확인 필요`로 표시합니다. 사용 가능한 카테고리만으로 참고용 종합 점수를 계산하고 `참고용`이라고 명시합니다.

별점 표기:

- `4.5` 이상 `5.0` 이하: `★★★★★`
- `3.5` 이상 `4.5` 미만: `★★★★☆`
- `2.5` 이상 `3.5` 미만: `★★★☆☆`
- `1.5` 이상 `2.5` 미만: `★★☆☆☆`
- `1.5` 미만: `★☆☆☆☆`
