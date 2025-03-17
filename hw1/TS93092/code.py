import pandas as pd
import numpy as np

file_path = "C:/Users/dunes/OneDrive/Documents/Code/global_air_quality_dataset.csv" 
df = pd.read_csv(file_path)

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

profile_details = []

for column in df.columns:
    column_info = {
        "Column Name": column,
        "Data Type": None,
        "Category": None,
        "Min": None,
        "Max": None,
        "Mean": None,
        "Median": None,
        "Std Dev": None,
        "Unique Values": None,
        "Top 3 Frequent Values": None,
        "Missing Values (%)": df[column].isnull().mean() * 100
    }

    if pd.api.types.is_numeric_dtype(df[column]):
        column_info["Data Type"] = "Numeric"
        column_info["Category"] = "Continuous"
        column_info.update({
            "Min": df[column].min(),
            "Max": df[column].max(),
            "Mean": df[column].mean(),
            "Median": df[column].median(),
            "Std Dev": df[column].std()
        })

    elif pd.api.types.is_datetime64_any_dtype(df[column]):
        column_info["Data Type"] = "Datetime"
        column_info["Category"] = "Temporal"

    elif pd.api.types.is_object_dtype(df[column]):
        column_info["Data Type"] = "Object"
        column_info["Category"] = "Discrete"
        column_info["Unique Values"] = df[column].nunique()
        value_counts = df[column].value_counts()
        column_info["Top 3 Frequent Values"] = value_counts.head(3).to_dict()

    profile_details.append(column_info)

profile_df = pd.DataFrame(profile_details)

print(profile_df)

profile_df.to_csv("C:/Users/dunes/OneDrive/Documents/Code/dataset_profile.csv", index=False)

surprising_notes = []

high_missing = profile_df[profile_df["Missing Values (%)"] > 50]
if not high_missing.empty:
    surprising_notes.append(f"Columns with more than 50% missing values: {', '.join(high_missing['Column Name'].tolist())}")

no_variance = profile_df[(profile_df["Data Type"] == "Numeric") & (profile_df["Std Dev"] == 0)]
if not no_variance.empty:
    surprising_notes.append(f"Columns with no variance: {', '.join(no_variance['Column Name'].tolist())}")

high_unique = profile_df[(profile_df["Unique Values"].notnull()) & (profile_df["Unique Values"] > 100)]
if not high_unique.empty:
    surprising_notes.append(f"Columns with high cardinality (more than 100 unique values): {', '.join(high_unique['Column Name'].tolist())}")

for note in surprising_notes:
    print(note)
