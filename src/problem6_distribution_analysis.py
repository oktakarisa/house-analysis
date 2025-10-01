# src/problem6_confirm_distribution.py
"""
Problem 6 - Confirming Distribution of SalePrice

Steps:
1. Plot distribution of SalePrice.
2. Calculate skewness and kurtosis.
3. Apply log transformation.
4. Re-plot and recalc.
5. Save explanations + plots.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Load cleaned dataset from Problem 4
df = pd.read_csv("data/train_cleaned.csv")

# Target variable
target = "SalePrice"

# --- Original Distribution ---
plt.figure(figsize=(8,5))
sns.histplot(df[target], kde=True, bins=30, color="skyblue")
plt.title("Original SalePrice Distribution")
plt.xlabel(target)
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/problem6_saleprice_original.png")
plt.close()

orig_skew = skew(df[target])
orig_kurt = kurtosis(df[target])
print(f"Original SalePrice Skewness: {orig_skew:.3f}")
print(f"Original SalePrice Kurtosis: {orig_kurt:.3f}")

# --- Log-transformed Distribution ---
df[target + "_log"] = np.log1p(df[target])

plt.figure(figsize=(8,5))
sns.histplot(df[target + "_log"], kde=True, bins=30, color="lightgreen")
plt.title("Log-Transformed SalePrice Distribution")
plt.xlabel(target + " (log)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/problem6_saleprice_log.png")
plt.close()

log_skew = skew(df[target + "_log"])
log_kurt = kurtosis(df[target + "_log"])
print(f"Log-Transformed SalePrice Skewness: {log_skew:.3f}")
print(f"Log-Transformed SalePrice Kurtosis: {log_kurt:.3f}")

# --- Save explanation as markdown + text ---
report_md = f"""
## Problem 6 - Confirming Distribution

### 1. Original SalePrice Distribution
- Skewness: {orig_skew:.3f}
- Kurtosis: {orig_kurt:.3f}
- Observation: The original SalePrice is highly skewed and leptokurtic (heavy-tailed).

### 2. Log-Transformed SalePrice Distribution
- Skewness: {log_skew:.3f}
- Kurtosis: {log_kurt:.3f}
- Observation: The log transformation reduces skewness and kurtosis, making the distribution closer to normal.

### 3. Plots
- Original distribution: `plots/problem6_saleprice_original.png`
- Log-transformed distribution: `plots/problem6_saleprice_log.png`
"""

with open("data/problem6_distribution.md", "w") as f:
    f.write(report_md)

with open("data/problem6_distribution.txt", "w") as f:
    f.write(report_md)

print("Reports saved as:")
print("- data/problem6_distribution.md")
print("- data/problem6_distribution.txt")
