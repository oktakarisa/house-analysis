"""
Problem 1 - Obtaining a dataset
--------------------------------
Task: Load the Ames housing dataset (train.csv) into a pandas DataFrame.
Why: Every analysis starts by importing your dataset into a workable format.
Deliverable: A pandas DataFrame stored in a variable (df).
"""

import pandas as pd
import os

# Path to dataset (must be downloaded from Kaggle and placed in project root 'data/' folder)
data_path = os.path.join("data", "train.csv")

# Load dataset
try:
    df = pd.read_csv(data_path)
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please download train.csv from Kaggle and place it in the 'data/' folder.")
    exit(1)

# Show basic confirmation info
print("\n--- Dataset Info ---")
print(f"Shape of dataset: {df.shape}")   # rows, columns
print("\nFirst 5 rows:")
print(df.head())

# Save a working copy (for interdependency with other problems)
output_path = os.path.join("data", "train_loaded.csv")
df.to_csv(output_path, index=False)
print(f"\nA copy of the dataset has been saved to: {output_path}")
