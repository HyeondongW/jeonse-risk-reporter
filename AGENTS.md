# Agent Notes

사용자가 `$jeonse-risk-reporter` 또는 `jeonse-risk-reporter`를 언급하거나, 한국 전세/월세 매물 분석, 전세사기 위험 평가, 1장짜리 매물 리포트를 요청하면 이 Skill을 사용합니다.

사용 가능한 입력은 구조화된 listing YAML, mock `market-comps.csv`, mock `infrastructure.csv`, 선택 입력인 등기부 요약입니다.

외부 사이트에서 매물, 등기부, 실거래가, 지도 데이터를 가져오지 않습니다. 제공된 파일에 없는 정보는 추측하지 말고 `⚫ 확인 불가`로 표시합니다.
