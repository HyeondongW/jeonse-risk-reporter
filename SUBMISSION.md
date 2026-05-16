# Skillathon Submission: jeonse-risk-reporter

## Problem

First-time Korean renters often compare market prices, registry risks, and local infrastructure by hand for every jeonse/monthly rental listing. Information is scattered across listing sites, registry documents, transaction data, and personal notes. This Skill creates a reproducible one-page Markdown report from structured mock inputs.

## Target User

Korean renters in their 20s and 30s looking for their first jeonse or monthly rental home, focused first on Seoul and the surrounding metro area.

## Inputs

- `examples/listings/*.yaml`: structured listing data with required listing fields and optional embedded `registry`
- `examples/user-profile.yaml`: renter budget and preferences
- `examples/market-comps.csv`: mock market comparison data
- `examples/infrastructure.csv`: mock infrastructure data

Listing links are metadata only via `source_url`. The Skill does not crawl Naver Real Estate, Zigbang, IROS, HUG, or any external website.

## Output

One Markdown report per listing:

- Overall judgment at the top
- Fixed 10-item risk checklist
- Three market comparison rows
- Registry summary
- Weighted 5-point infrastructure score
- Missing information
- Disclaimer

Output filename rule:

```text
outputs/{listing_file_stem}-report.md
```

## Scenarios

| Scenario | Listing | Expected Grade | Purpose |
|---|---|---|---|
| Safe | `listing-safe.yaml` | 🟢 낮음 | Shows the Skill can identify a low-risk mock case |
| Risky | `listing-risky.yaml` | 🔴 높음 | Shows the Skill catches over-market deposit, mortgage burden, ownership change, and prior lease issue |
| Incomplete | `listing-incomplete.yaml` | ⚫ 판단 불가 | Shows the Skill refuses to guess when registry data is missing |

## Validation

Run structural, soft-pattern, and optional scenario checks:

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

## Final Checklist

- [x] `SKILL.md` frontmatter has `name` and `description`
- [x] Description includes Korean trigger keywords
- [x] External web search is prohibited
- [x] Three mock listing scenarios exist
- [x] Three expected outputs exist
- [x] Five reference files exist
- [x] Validation script exists
- [x] Reports include disclaimer
- [x] Mock data is explicitly labeled
- [x] Missing data policy is represented by the incomplete scenario
