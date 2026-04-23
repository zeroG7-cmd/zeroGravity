import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
csv_path = BASE_DIR / "data" / "survey_responses.csv"
output_path = BASE_DIR / "responses_summary.md"

df = pd.read_csv(csv_path)

total_responses = len(df)

summary = f"""# Survey Results Summary

## Total Responses
{total_responses}

## Columns Collected
{chr(10).join(f"- {col}" for col in df.columns)}

## Key Findings
TBC after reviewing the response patterns.

## Notes
This summary was generated from the survey CSV export.
"""

output_path.write_text(summary, encoding="utf-8")

print(f"Generated {output_path}")
