import pandas as pd
import numpy as np

# Load the dataset using a raw string to avoid escape issues in the file path
df = pd.read_csv(r"C:\Users\saita\OneDrive - UMBC\Desktop\air+quality\AirQualityUCI.csv", 
                 sep=';', 
                 decimal=',')

# Convert the Time column to use colons instead of periods
df['Time'] = df['Time'].str.replace('.', ':', regex=False)

# Combine Date and Time columns into a DateTime column
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)

# Drop columns that contain only NaN values (sometimes extra columns are present)
df = df.dropna(axis=1, how='all')

# Print total number of rows and columns
total_rows, total_cols = df.shape
print(f"Total rows: {total_rows}")
print(f"Total columns: {total_cols}\n")

# Initialize a dictionary to store the profile for each column
profile = {}

for col in df.columns:
    profile[col] = {}
    
    # Determine attribute type and compute relevant statistics
    if pd.api.types.is_numeric_dtype(df[col]):
        profile[col]['Attribute Type'] = 'Numeric'
        profile[col]['Min'] = df[col].min()
        profile[col]['Max'] = df[col].max()
        profile[col]['Mean'] = df[col].mean()
        profile[col]['Median'] = df[col].median()
        profile[col]['Std'] = df[col].std()
    elif pd.api.types.is_datetime64_any_dtype(df[col]):
        profile[col]['Attribute Type'] = 'Temporal'
    else:
        profile[col]['Attribute Type'] = 'Symbolic/Discrete'
        profile[col]['Unique Count'] = df[col].nunique()
        # Get top three most frequent values
        top_freq = df[col].value_counts().head(3)
        profile[col]['Top 3 Frequent'] = top_freq.to_dict()
    
    # Calculate missingness: percentage of missing values in the column
    missing_pct = df[col].isnull().mean() * 100
    profile[col]['Missingness (%)'] = missing_pct

# Display the profile information for each column
for col, stats in profile.items():
    print(f"Column: {col}")
    for stat, value in stats.items():
        print(f"  {stat}: {value}")
    print("\n")
