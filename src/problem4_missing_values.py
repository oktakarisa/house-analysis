# src/problem4_missing_values.py
"""
Problem 4 – Dealing with Missing Values (Windows-safe)

This version avoids crashing on GitBash by saving the missingno plot to a file instead of opening an interactive window.
"""

import pandas as pd
import missingno as msno
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for Windows/GitBash
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/train_loaded.csv")
print("Dataset successfully loaded for missing value analysis!\n")

# Count missing values per column
missing_counts = df.isnull().sum()
print("--- Missing Values per Column ---")
print(missing_counts[missing_counts > 0])

# Visualize missing values and save to file
msno.matrix(df)
plt.savefig("data/missing_values_matrix.png")
plt.close()
print("Missing values plot saved as data/missing_values_matrix.png")

# Calculate percentage of missing values
missing_percent = (df.isnull().sum() / len(df)) * 100
print("\n--- Percentage of Missing Values ---")
print(missing_percent[missing_percent > 0])

# Drop columns with 5 or more missing values
cols_to_drop = missing_counts[missing_counts >= 5].index
df = df.drop(columns=cols_to_drop)
print(f"\nDropped columns with >=5 missing values: {list(cols_to_drop)}")

# Drop remaining rows with missing values
initial_rows = len(df)
df = df.dropna()
print(f"Dropped {initial_rows - len(df)} rows containing remaining missing values")

# Save cleaned dataset
df.to_csv("data/train_cleaned.csv", index=False)
print("\nCleaned dataset saved as data/train_cleaned.csv")

# Save markdown report
report = f"""
## Problem 4 - Dealing with Missing Values

### 1. Initial missing values
{missing_counts[missing_counts > 0]}

### 2. Percentage missing
{missing_percent[missing_percent > 0]}

### 3. Columns dropped (>=5 missing)
{list(cols_to_drop)}

### 4. Rows dropped
{initial_rows - len(df)}

### 5. Final dataset shape
{df.shape}

### 6. Missing values plot
Saved as: data/missing_values_matrix.png
"""

with open("data/problem4_missing_report.md", "w") as f:
    f.write(report)

print("\nMarkdown report saved as data/problem4_missing_report.md")