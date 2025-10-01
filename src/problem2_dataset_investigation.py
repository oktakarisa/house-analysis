"""
Problem 2 - Investigating the dataset
--------------------------------------
Task: Explain what kind of dataset this is by referring to Kaggle's overview and data fields.
Why: Before analyzing, we need to understand what the data represents.
Deliverable: Markdown/text explanation + basic inspection.
"""

import pandas as pd
import os

# Load dataset (from Problem 1 output)
data_path = os.path.join("data", "train_loaded.csv")

try:
    df = pd.read_csv(data_path)
    print("Dataset successfully loaded for investigation!\n")
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please run problem1_load_dataset.py first.")
    exit(1)

# --- Investigation content ---
report_lines = []

report_lines.append("## Problem 2 - Investigating the Dataset\n")
report_lines.append("### 1. What this dataset is about:\n")
report_lines.append("- Housing prices in Ames, Iowa.\n")
report_lines.append("- Each row represents a single house sale transaction.\n")
report_lines.append("- There are 79 explanatory variables (features) describing each house.\n")
report_lines.append("- The target variable is 'SalePrice' (the house’s selling price in USD).\n")

report_lines.append("\n### 2. Number of rows and columns:\n")
report_lines.append(f"- Rows (houses): {df.shape[0]}\n")
report_lines.append(f"- Columns (features including target): {df.shape[1]}\n")

report_lines.append("\n### 3. Example columns:\n")
report_lines.append("- Id: unique identifier (not useful for modeling).\n")
report_lines.append("- OverallQual: overall material & finish quality (1–10).\n")
report_lines.append("- GrLivArea: above ground living area (square feet).\n")
report_lines.append("- Neighborhood: physical location of the house within Ames.\n")
report_lines.append("- YearBuilt: year house was built.\n")
report_lines.append("- SalePrice: house sale price (target variable).\n")

report_lines.append("\n### 4. Quick sample row (house description):\n")
report_lines.append(df.head(1).T.to_string())
report_content = "\n".join(report_lines)

# --- Save report to text and markdown ---
output_txt = os.path.join("data", "problem2_investigation.txt")
output_md = os.path.join("data", "problem2_investigation.md")

with open(output_txt, "w", encoding="utf-8") as f:
    f.write(report_content)

with open(output_md, "w", encoding="utf-8") as f:
    f.write(report_content)

print("Report saved as:")
print(f"- {output_txt}")
print(f"- {output_md}")

# Also print summary to console
print("\n--- Console Preview ---")
print(report_content[:600] + "\n... (truncated) ...")
