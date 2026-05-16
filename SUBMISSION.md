# Skillathon 제출 설명서: jeonse-risk-reporter

## 제출 주제

`jeonse-risk-reporter`는 한국 전월세 매물 1건을 분석해 1장짜리 Markdown 위험 리포트를 생성하는 Codex Skill입니다.

대상 사용자는 처음 전월세를 구하는 20-30대 한국 청년이며, 서울·수도권 매물을 우선 가정합니다.

## 해결하려는 문제

전월세 매물을 볼 때 사용자는 매물 사이트, 등기부등본, 실거래가, 생활 인프라 정보를 따로 확인해야 합니다. 이 과정은 반복적이고, 초보자는 어떤 항목이 위험 신호인지 판단하기 어렵습니다.

이 Skill은 구조화된 mock 입력을 사용해 다음 내용을 한 리포트에 묶습니다.

- 시세 비교
- 권리관계 요약
- 위험 신호 체크리스트
- 인프라 점수
- 종합 판단과 다음 행동

## 입력

- `examples/listings/*.yaml`: 매물 정보와 선택 입력인 `registry` 등기부 요약
- `examples/user-profile.yaml`: 사용자 예산과 선호 조건
- `examples/market-comps.csv`: mock 실거래가 비교 데이터
- `examples/infrastructure.csv`: mock 인프라 데이터

`source_url`은 출처 추적용 메타데이터입니다. Skill은 네이버부동산, 직방, 인터넷등기소, HUG, 국토교통부 사이트를 직접 크롤링하지 않습니다.

## 출력

매물 1건당 Markdown 리포트 1개를 생성합니다.

- 종합 판단
- 고정 10개 위험 신호 체크리스트
- 세 가지 기준의 시세 비교 표
- 등기부 기반 권리관계 요약
- 5점 만점 인프라 점수
- 확인 필요 항목
- 면책 문구

출력 파일명 규칙:

```text
outputs/{listing_file_stem}-report.md
```

## Skill 구조

```text
.agents/skills/jeonse-risk-reporter/
├── SKILL.md
├── references/
│   ├── risk-rules.md
│   ├── market-comparison-rules.md
│   ├── registry-rules.md
│   ├── infra-scoring.md
│   └── report-template.md
├── scripts/
│   └── validate_report.py
└── examples/
    ├── listings/
    ├── user-profile.yaml
    ├── market-comps.csv
    ├── infrastructure.csv
    └── expected-outputs/
```

## 시나리오

| 시나리오 | 입력 파일 | 기대 종합 등급 | 검증 목적 |
|---|---|---|---|
| 안전에 가까운 매물 | `listing-safe.yaml` | 🟢 낮음 | 시세 근처, 등기부 깨끗, 예산 내 매물을 낮은 위험으로 판단 |
| 위험한 전세 매물 | `listing-risky.yaml` | 🔴 높음 | 시세 초과, 큰 근저당, 최근 소유자 변경, 임차권등기 이력을 감지 |
| 정보 부족 매물 | `listing-incomplete.yaml` | ⚫ 판단 불가 | 등기부 미제공 시 추측하지 않고 확인 불가 항목을 명시 |

## 검증 방법

구조 검증, 소프트 패턴 검증, 시나리오별 등급 검증을 실행합니다.

```bash
python3 .agents/skills/jeonse-risk-reporter/scripts/validate_report.py \
  .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-safe-report.md \
  --scenario safe

python3 .agents/skills/jeonse-risk-reporter/scripts/validate_report.py \
  .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-risky-report.md \
  --scenario risky

python3 .agents/skills/jeonse-risk-reporter/scripts/validate_report.py \
  .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-incomplete-report.md \
  --scenario incomplete
```

## 검증 결과

현재 예상 출력 3개가 모두 통과합니다.

```text
PASS .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-safe-report.md [safe]
PASS .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-risky-report.md [risky]
PASS .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-incomplete-report.md [incomplete]
```

## 제출 전 체크리스트

- [x] `README.md`에 문제, 실행 방법, 결과물, 검증 결과, 한계를 정리했습니다.
- [x] `SKILL.md`에 반복 실행 절차, 입력/출력, guardrails를 정리했습니다.
- [x] `references/*.md`에 긴 규칙과 평가 기준을 분리했습니다.
- [x] 실제 민감 데이터 대신 mock data만 포함했습니다.
- [x] 예상 출력 3개와 검증 스크립트를 포함했습니다.
- [x] 외부 웹 검색 금지와 등기부 추측 금지 정책을 명시했습니다.
- [x] 면책 문구를 리포트 템플릿과 expected output에 포함했습니다.
- [x] API key, token, webhook URL, 비밀번호 등 비밀값을 포함하지 않았습니다.

## 한계

- 이 저장소의 데이터는 모두 mock data입니다.
- 실제 공공데이터, 실시간 지도, 실제 등기부 조회 결과를 사용하지 않습니다.
- 리포트는 법률 자문이나 감정평가가 아닙니다.
- 실제 계약 전에는 인터넷등기소, HUG 안심전세앱, 정부24 건축물대장, 국토교통부 실거래가 공개시스템, 공인중개사를 통해 직접 확인해야 합니다.
