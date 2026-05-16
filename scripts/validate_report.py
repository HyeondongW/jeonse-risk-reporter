#!/usr/bin/env python3
"""Validate jeonse-risk-reporter Markdown reports.

The validator intentionally checks structure and core judgment signals rather
than exact prose, so Codex can still write natural reports.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTIONS = [
    "# 🏠 매물 위험 분석 리포트",
    "## 🚦 종합 판단",
    "## ⚠️ 위험 신호 체크리스트",
    "## 💰 시세 비교",
    "## 📋 권리관계 요약",
    "## 🚇 인프라 점수",
    "## ❓ 확인 필요 항목",
    "## 📌 면책 문구",
]

RISK_ITEMS = {
    1: "보증금이 사용자 max_deposit 초과",
    2: "시세 대비 보증금 +15% 이상",
    3: "시세 대비 보증금 +5~15%",
    4: "근저당 채권최고액 + 보증금 > 시세 80%",
    5: "압류·가압류 존재",
    6: "신탁 등기 존재",
    7: "최근 1년 내 소유자 변경",
    8: "임차권등기명령 이력",
    9: "등기부 미제공",
    10: "다가구주택인데 선순위 보증금 미확인",
}

MARKET_ROWS = [
    "같은 동·면적대 (6개월)",
    "같은 동·면적대 (1년)",
    "같은 동 전체 (6개월)",
]

INFRA_CATEGORIES = [
    "🚇 대중교통",
    "💼 직장·학교 접근성",
    "🛒 생활 인프라",
    "🏥 의료·여가",
]

EXPECTED_GRADES = {
    "safe": "🟢 낮음",
    "risky": "🔴 높음",
    "incomplete": "⚫ 판단 불가",
}


def fail_if_missing(text: str, needles: list[str], label: str, errors: list[str]) -> None:
    for needle in needles:
        if needle not in text:
            errors.append(f"missing {label}: {needle}")


def extract_statuses(text: str) -> dict[int, str]:
    statuses: dict[int, str] = {}
    row_pattern = re.compile(r"^\|\s*(\d{1,2})\s*\|\s*([✅🟡🔴⚫])\s*\|", re.MULTILINE)
    for match in row_pattern.finditer(text):
        statuses[int(match.group(1))] = match.group(2)
    return statuses


def check_soft_patterns(text: str, errors: list[str]) -> None:
    if not re.search(r"\d{1,3}(,\d{3})+원", text):
        errors.append("missing comma-formatted KRW amount, e.g. 280,000,000원")
    if not re.search(r"[+-]\d+\.\d%", text):
        errors.append("missing signed one-decimal percentage, e.g. +27.3%")
    for keyword in ["mock data", "법률 자문", "감정평가"]:
        if keyword not in text:
            errors.append(f"missing disclaimer keyword: {keyword}")


def check_scenario(text: str, scenario: str, errors: list[str]) -> None:
    expected_grade = EXPECTED_GRADES[scenario]
    if expected_grade not in text:
        errors.append(f"scenario {scenario}: expected overall grade {expected_grade}")

    statuses = extract_statuses(text)
    missing_statuses = sorted(set(RISK_ITEMS) - set(statuses))
    if missing_statuses:
        errors.append(f"scenario {scenario}: missing checklist statuses {missing_statuses}")
        return

    if scenario == "safe":
        bad = {idx: status for idx, status in statuses.items() if status not in {"✅", "—"}}
        if bad:
            errors.append(f"scenario safe: expected all checklist items to be ✅ or —, got {bad}")
    elif scenario == "risky":
        for idx in [2, 4, 7]:
            if statuses[idx] != "🔴":
                errors.append(f"scenario risky: item {idx} should be 🔴, got {statuses[idx]}")
        red_count = sum(1 for status in statuses.values() if status == "🔴")
        if red_count < 4:
            errors.append(f"scenario risky: expected at least 4 🔴 items, got {red_count}")
    elif scenario == "incomplete":
        for idx in [4, 5, 6, 7, 8, 10]:
            if statuses[idx] != "⚫":
                errors.append(f"scenario incomplete: item {idx} should be ⚫, got {statuses[idx]}")


def validate(path: Path, scenario: str | None) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    fail_if_missing(text, SECTIONS, "section", errors)
    fail_if_missing(text, list(RISK_ITEMS.values()), "risk item", errors)
    fail_if_missing(text, MARKET_ROWS, "market comparison row", errors)
    fail_if_missing(text, INFRA_CATEGORIES, "infrastructure category", errors)
    check_soft_patterns(text, errors)

    if scenario:
        check_scenario(text, scenario, errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate jeonse-risk-reporter output.")
    parser.add_argument("report", type=Path, help="Markdown report path")
    parser.add_argument("--scenario", choices=sorted(EXPECTED_GRADES), help="Enable scenario-specific checks")
    args = parser.parse_args()

    if not args.report.exists():
        print(f"FAIL {args.report}: file does not exist", file=sys.stderr)
        return 2

    errors = validate(args.report, args.scenario)
    if errors:
        print(f"FAIL {args.report}")
        for error in errors:
            print(f"- {error}")
        return 1

    scenario_text = f" [{args.scenario}]" if args.scenario else ""
    print(f"PASS {args.report}{scenario_text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
