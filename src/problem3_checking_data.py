# problem3_checking_data.py
#
# Problem 3 – Checking the data
#
# What we do:
# 1. Check data types of each column
# 2. Identify the target variable
# 3. Summarize numerical columns with .describe()
# 4. Save a small markdown/text report for documentation

import pandas as pd

# Load the dataset from Problem 1
df = pd.read_csv("data/train_loaded.csv")

print("Dataset successfully loaded for checking!")

# --- 1. Check data types ---
print("\n--- Column Data Types ---")
print(df.dtypes)

# --- 2. Identify the target variable ---
target_variable = "SalePrice"
print(f"\nTarget variable: {target_variable}")

# --- 3. Describe numerical features ---
numerical_summary = df.describe()
print("\n--- Numerical Summary ---")
print(numerical_summary)

# --- 4. Save report to file ---
report_md = f"""
## Problem 3 - Checking the Data

### 1. Column Data Types:
{df.dtypes.to_markdown()}

### 2. Target Variable:
- {target_variable}

### 3. Summary of Numerical Features:
{numerical_summary.to_markdown()}
"""

report_txt = f"""
Problem 3 - Checking the Data

1. Column Data Types:
{df.dtypes}

2. Target Variable:
{target_variable}

3. Summary of Numerical Features:
{numerical_summary}
"""

# Save markdown and txt report
with open("data/problem3_checking_data.md", "w") as f_md:
    f_md.write(report_md)

with open("data/problem3_checking_data.txt", "w") as f_txt:
    f_txt.write(report_txt)

print("\nReports saved as:")
print("- data/problem3_checking_data.md")
print("- data/problem3_checking_data.txt")
