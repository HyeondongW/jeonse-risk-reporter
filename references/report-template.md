# 리포트 템플릿

모든 리포트는 아래 구조를 사용합니다.

```markdown
# 🏠 매물 위험 분석 리포트
**{address}** · {listing_type} {price_text} · {area_text} · {floor}/{building_total_floors}층
*분석일: {analysis_date} · 출처: {source_url_or_manual_input}*

## 🚦 종합 판단
**종합 등급: {grade}**

- 장점: {one_line_strength}
- 위험: {one_line_risk}
- 다음 행동: {one_line_next_action}

## ⚠️ 위험 신호 체크리스트
**신뢰도: {confidence}**

| No. | 결과 | 항목 | 근거 |
|---:|---|---|---|
| 1 | {status} | 보증금이 사용자 max_deposit 초과 | {evidence} |
| 2 | {status} | 시세 대비 보증금 +15% 이상 | {evidence} |
| 3 | {status} | 시세 대비 보증금 +5~15% | {evidence} |
| 4 | {status} | 근저당 채권최고액 + 보증금 > 시세 80% | {evidence} |
| 5 | {status} | 압류·가압류 존재 | {evidence} |
| 6 | {status} | 신탁 등기 존재 | {evidence} |
| 7 | {status} | 최근 1년 내 소유자 변경 | {evidence} |
| 8 | {status} | 임차권등기명령 이력 | {evidence} |
| 9 | {status} | 등기부 미제공 | {evidence} |
| 10 | {status} | 다가구주택인데 선순위 보증금 미확인 | {evidence} |

## 💰 시세 비교
**신뢰도: {confidence}**

| 비교 기준 | 거래 건수 | 중위값 | 이 매물 차이 |
|---|---:|---:|---:|
| 같은 동·면적대 (6개월) | {count}건 | {median} | {difference} |
| 같은 동·면적대 (1년) | {count}건 | {median} | {difference} |
| 같은 동 전체 (6개월) | {count}건 | {median} | {difference} |

## 📋 권리관계 요약
**신뢰도: {confidence}**

- 소유자: {owner_summary}
- 근저당: {mortgage_summary}
- 압류·가압류: {seizure_summary}
- 신탁: {trust_summary}
- 임차권등기명령: {lease_registration_summary}
- 말소기준권리 추정: {priority_right_summary}

## 🚇 인프라 점수
**신뢰도: {confidence}**

| 항목 | 점수 | 근거 |
|---|---:|---|
| 🚇 대중교통 | {score} | {evidence} |
| 💼 직장·학교 접근성 | {score} | {evidence} |
| 🛒 생활 인프라 | {score} | {evidence} |
| 🏥 의료·여가 | {score} | {evidence} |

**종합:** {score}/5 {stars}

## ❓ 확인 필요 항목

- {missing_or_next_check}

## 📌 면책 문구

> 📌 **본 리포트는 mock data 기반 의사결정 보조 도구이며, 법률 자문·감정평가가 아닙니다.**
>
> 실제 계약 전 다음을 반드시 직접 확인하세요:
> - 인터넷등기소(iros.go.kr)에서 등기부등본 직접 발급
> - HUG 안심전세앱에서 임대인 정보·보증보험 가입 가능 여부 조회
> - 정부24에서 건축물대장 발급 (위반건축물 여부)
> - 국토교통부 실거래가 공개시스템에서 실제 시세 확인
> - 공인중개사를 통한 계약 진행
>
> 본 Skill은 Skillathon 학습 목적으로 제작되었으며, 본 리포트로 인한
> 의사결정 결과에 대해 제작자는 책임지지 않습니다.
```
