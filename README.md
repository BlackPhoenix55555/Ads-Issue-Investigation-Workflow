# Ads Issue Investigation & Support Workflow (gTech Ads–Style)

## Overview
This project simulates real-world advertiser issue investigations similar to Google gTech Ads workflows.

## Problem Statements
- Spend drops
- Conversion mismatches
- Funnel breaks
- Configuration-related performance regressions

## Datasets
- Campaigns, ad groups, daily performance metrics
- Conversion logs
- Configuration change history

## Key Analyses
- Spend anomaly detection
- Funnel break identificationads-issue-investigation/
│
├── data/                        # Raw and processed CSV datasets
│   ├── ad_groups.csv
│   ├── campaigns.csv
│   ├── config_changes.csv
│   ├── conversions.csv
│   └── daily_metrics.csv
│
├── generate_additional_data.py  # Script to generate or augment data
│
├── investigations/               # Documentation of investigations
│   ├── issue_intake.md
│   ├── rca_template.md
│   └── resolved_cases.md
│
├── notebooks/                    # Analysis and experimentation notebooks/scripts
│   └── exploratory_analysis.py
│
├── sql/                          # SQL scripts (currently empty folder)
│
└── README.md                     # Project overview

- Before/after performance comparison
- Root cause analysis tied to config changes

## Tools & Skills
- SQL (joins, CTEs, window functions)
- Python (pandas, automation)
- Data validation & diagnostics
- Stakeholder-ready documentation

## Outcome
Enabled structured, end-to-end issue ownership:
intake → investigation → RCA → resolution → prevention



