# Workforce Analysis

from pathlib import Path
import pandas as pd


# Load and preview data
repo_root = Path(__file__).resolve().parents[1]
input_path = repo_root / "4_Dataset" / "employee_dataset_raw.csv"
output_path = repo_root / "4_Dataset" / "employee_dataset_cleaned.csv"

df_raw = pd.read_csv(input_path)
df_raw.info()
df_raw.head(5)

# Create a copy of dataset to protect raw
df_cleaned = df_raw.copy()

# Fix irregular column header formatting
df_cleaned.columns = (df_cleaned.columns
                      .str.replace(r'([a-z0-9])([A-Z])', r'\1_\2', regex=True)
                      .str.replace(r'([a-zA-Z])([0-9])', r'\1_\2', regex=True)
                      .str.replace(r'([0-9])([a-zA-Z])', r'\1_\2', regex=True)
                      .str.lower())

df_cleaned.head(10)


# Standardise data within string columns
text_cols = df_cleaned.select_dtypes(include=['object', 'string']).columns

for col in text_cols:
    df_cleaned[col] = (
        df_cleaned[col]
        .fillna('unknown')
        .str.strip()
        .str.replace(r'\s+', ' ', regex=True)
        .str.lower())

for col in text_cols:
    df_cleaned[col] = df_cleaned[col].fillna('unknown')

initial_rows = len(df_cleaned)
df_cleaned = df_cleaned.drop_duplicates()
final_rows = len(df_cleaned)
if initial_rows != final_rows:
    print(f"⚠️ Removed {initial_rows - final_rows} absolute duplicate rows.")

duplicates = df_cleaned['employee_id'].duplicated().sum()
print(f"Duplicate employee IDs: {duplicates}")

df_cleaned.head(5)

# Values check
print("1. Number of NA values per column")
print(df_cleaned.isna().sum())
print('')

print("2. Number of Duplicate employee_ID (should be 0)")
df_cleaned['employee_id'].duplicated().sum()


# Export the cleaned dataset
df_cleaned.to_csv(output_path, index=False)
print("Data successfully exported to CSV ready for SQL")
