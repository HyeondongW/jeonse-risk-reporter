# jeonse-risk-reporter

Korean jeonse/monthly rental listing risk reporter for Skillathon.

This Skill turns one structured listing YAML plus mock market and infrastructure data into a one-page Markdown report for first-time Korean renters. It does not crawl real estate sites or fetch external data. Links are stored only as source metadata.

## What It Produces

- Overall risk grade: 🟢 낮음 / 🟡 주의 / 🔴 높음 / ⚫ 판단 불가
- Fixed 10-item rental risk checklist
- Market comparison table using mock `market-comps.csv`
- Registry summary from optional YAML/text/PDF-derived data
- 5-point infrastructure score
- Missing-data list and disclaimer

## Quick Run

```bash
python3 .agents/skills/jeonse-risk-reporter/scripts/validate_report.py \
  .agents/skills/jeonse-risk-reporter/examples/expected-outputs/listing-risky-report.md \
  --scenario risky
```

## Main Files

- `.agents/skills/jeonse-risk-reporter/SKILL.md`
- `.agents/skills/jeonse-risk-reporter/references/`
- `.agents/skills/jeonse-risk-reporter/examples/`
- `.agents/skills/jeonse-risk-reporter/scripts/validate_report.py`
- `SUBMISSION.md`

All example listings are mock data. They use real Seoul legal-dong names with fictional addresses and building names.
