# jeonse-risk-reporter

처음 전월세를 구하는 한국 청년을 위한 **전월세 매물 위험 분석 Skill**입니다.

구조화된 매물 YAML, mock 실거래가 CSV, mock 인프라 CSV, 선택 입력인 등기부 요약을 읽고 매물 1건에 대한 1장짜리 Markdown 리포트를 생성합니다. 네이버부동산, 직방, 인터넷등기소, HUG 등 외부 사이트는 크롤링하지 않습니다.

## 문제 정의

전월세 매물을 보러 다닐 때 매물 하나마다 시세 비교, 등기부 권리관계 확인, 위험 신호 체크, 생활 인프라 확인을 손으로 정리해야 합니다. 특히 처음 집을 구하는 20-30대는 어떤 항목을 봐야 하는지 알기 어렵고, 정보가 흩어져 있어 매물별 비교가 번거롭습니다.

이 Skill은 제공된 mock data만 사용해 다음 질문에 답하는 리포트를 만듭니다.

- 이 매물의 보증금/월세가 주변 시세 대비 과한가?
- 등기부상 근저당, 압류, 신탁, 임차권등기 같은 위험 신호가 있는가?
- 정보가 부족해서 판단을 보류해야 하는 부분은 무엇인가?
- 지하철, 직장 접근성, 생활 인프라, 의료·여가 접근성은 어느 정도인가?

## 결과물

리포트에는 다음 항목이 포함됩니다.

- 종합 등급: `🟢 낮음` / `🟡 주의` / `🔴 높음` / `⚫ 판단 불가`
- 고정 10개 위험 신호 체크리스트
- mock `market-comps.csv` 기반 시세 비교 표
- 등기부 요약 기반 권리관계 분석
- 5점 만점 인프라 점수
- 확인 필요 항목
- 법률 자문이 아니라는 면책 문구

## 폴더 구조

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

## 실행 방법

예상 리포트가 제출 기준을 만족하는지 검증합니다.

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

현재 세 시나리오 모두 통과했습니다.

```text
PASS listing-safe-report.md [safe]
PASS listing-risky-report.md [risky]
PASS listing-incomplete-report.md [incomplete]
```

## 예시 시나리오

| 시나리오 | 파일 | 기대 등급 | 목적 |
|---|---|---|---|
| 안전에 가까운 매물 | `listing-safe.yaml` | 🟢 낮음 | 낮은 위험 매물을 낮음으로 판단하는지 확인 |
| 위험한 전세 매물 | `listing-risky.yaml` | 🔴 높음 | 고시세, 큰 근저당, 최근 소유자 변경, 임차권등기 이력을 잡는지 확인 |
| 정보 부족 매물 | `listing-incomplete.yaml` | ⚫ 판단 불가 | 등기부 미제공 시 추측하지 않고 판단 불가 처리하는지 확인 |

## 한계와 가드레일

- 모든 예시는 mock data이며 실제 매물이 아닙니다.
- 법정동은 실제 지명을 사용하지만 상세 주소와 건물명은 가상입니다.
- 외부 웹 검색, 로그인, 유료 리소스 사용을 하지 않습니다.
- 등기부가 없으면 권리관계를 추측하지 않고 `⚫ 확인 불가`로 표시합니다.
- 이 리포트는 의사결정 보조용이며 법률 자문이나 감정평가가 아닙니다.
- 실제 계약 전 등기부등본, 건축물대장, HUG 보증보험 가능 여부, 공인중개사 설명을 직접 확인해야 합니다.

## 주요 파일 위치

- Skill 본문: `.agents/skills/jeonse-risk-reporter/SKILL.md`
- 세부 규칙: `.agents/skills/jeonse-risk-reporter/references/`
- mock data: `.agents/skills/jeonse-risk-reporter/examples/`
- 검증 스크립트: `.agents/skills/jeonse-risk-reporter/scripts/validate_report.py`
- 제출 설명: `SUBMISSION.md`
