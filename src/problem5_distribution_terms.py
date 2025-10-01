# src/problem5_research_terminology.py
"""
Problem 5 – Researching terminology: Kurtosis & Skewness

This script summarizes the definitions of skewness and kurtosis and saves the report.
"""

# Explanation
kurtosis_def = """
Kurtosis:
- Kurtosis measures the "tailedness" of a distribution.
- High kurtosis: more data in the tails (heavy tails, outliers more likely)
- Low kurtosis: flatter distribution (light tails)
- Types:
  - Leptokurtic: sharp peak, heavy tails
  - Platykurtic: flat peak, light tails
  - Mesokurtic: similar to normal distribution
"""

skewness_def = """
Skewness:
- Skewness measures the asymmetry of a distribution.
- Positive skew: tail extends to the right (more small values)
- Negative skew: tail extends to the left (more large values)
- Zero skew: symmetric distribution
"""

# Combine into report
report_md = f"""
## Problem 5 – Researching Terminology

### 1. Kurtosis
{kurtosis_def}

### 2. Skewness
{skewness_def}
"""

# Save report as markdown
with open("data/problem5_terminology.md", "w") as f:
    f.write(report_md)

# Also save as plain text
with open("data/problem5_terminology.txt", "w") as f:
    f.write(report_md)

print("Reports saved as:")
print("- data/problem5_terminology.md")
print("- data/problem5_terminology.txt")