# src/problem7_correlation_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Prevent GUI crash
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/train_cleaned.csv")
print("Dataset successfully loaded for correlation analysis!")

# --- Keep only numeric columns for correlation ---
numeric_df = df.select_dtypes(include='number')

# --- 1. Full correlation matrix ---
corr_matrix = numeric_df.corr()
corr_matrix.to_csv("data/correlation_matrix.csv")
plt.figure(figsize=(12,10))
sns.heatmap(corr_matrix, cmap='coolwarm', center=0)
plt.title("Full Correlation Matrix of Numeric Features")
plt.tight_layout()
plt.savefig("plots/correlation_matrix_full.png")
plt.close()
print("Full correlation matrix heatmap saved as plots/correlation_matrix_full.png")

# --- 2. Top 10 features most correlated with SalePrice ---
top_corr = corr_matrix['SalePrice'].abs().sort_values(ascending=False)
top_10_features = top_corr[1:11].index.tolist()  # skip SalePrice itself
print("Top 10 features most correlated with SalePrice:", top_10_features)

# --- 3. Heatmap of top 10 features + SalePrice ---
top_features = top_10_features + ['SalePrice']
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df[top_features].corr(), annot=True, fmt=".2f", cmap='coolwarm', center=0)
plt.title("Correlation of Top 10 Features with SalePrice")
plt.tight_layout()
plt.savefig("plots/correlation_top10.png")
plt.close()
print("Top 10 correlation heatmap saved as plots/correlation_top10.png")

# --- 4. Feature descriptions ---
feature_descriptions = {
    'OverallQual': 'Rates the overall material and finish of the house (1-10)',
    'GrLivArea': 'Above ground living area (in square feet)',
    'GarageCars': 'Size of garage in car capacity',
    'GarageArea': 'Size of garage in square feet',
    'TotalBsmtSF': 'Total square feet of basement area',
    '1stFlrSF': 'First Floor square feet',
    'FullBath': 'Number of full bathrooms',
    'TotRmsAbvGrd': 'Total rooms above grade (does not include bathrooms)',
    'YearBuilt': 'Original construction year',
    'YearRemodAdd': 'Remodel year (same as construction if no remodeling)'
}

# --- 5. Highly correlated pairs among top 10 features ---
high_corr_pairs = []
for i in range(len(top_10_features)):
    for j in range(i+1, len(top_10_features)):
        f1, f2 = top_10_features[i], top_10_features[j]
        if abs(numeric_df[f1].corr(numeric_df[f2])) > 0.8:
            high_corr_pairs.append((f1,f2))

# --- 6. Markdown report ---
md_content = f"""
## Problem 7 - Correlation Analysis

### Top 10 features most correlated with SalePrice:
{top_10_features}

### Feature explanations (from Kaggle DataDescription):
"""
for f in top_10_features:
    md_content += f"- **{f}**: {feature_descriptions.get(f, 'Description not found')}\n"

md_content += "\n### Highly correlated feature pairs among top 10:\n"
if high_corr_pairs:
    for f1,f2 in high_corr_pairs:
        md_content += f"- {f1} and {f2}\n"
else:
    md_content += "- None found above correlation 0.8\n"

md_content += """
### Why high correlation between features is a problem:
When two features are highly correlated, it can cause multicollinearity in regression models.
This makes coefficient estimates unstable and reduces model interpretability.
"""

# Save reports
with open("data/problem7_correlation_report.md", "w") as f:
    f.write(md_content)
with open("data/problem7_correlation_report.txt", "w") as f:
    f.write(md_content)

print("Markdown and text reports saved as data/problem7_correlation_report.md / .txt")
