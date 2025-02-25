import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1. Data Loading & Cleaning
# =========================

# Load the dataset using a raw string to avoid escape issues in the file path.
df = pd.read_csv(r"C:\Users\saita\OneDrive - UMBC\Desktop\air+quality\AirQualityUCI.csv", 
                 sep=';', 
                 decimal=',')

# Replace periods in the Time column with colons to fix the time format.
df['Time'] = df['Time'].str.replace('.', ':', regex=False)

# Combine Date and Time columns into a DateTime column.
# Note: dayfirst=True because the Date is in DD/MM/YYYY format.
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)

# Drop columns that contain only NaN values (sometimes extra columns appear at the end).
df = df.dropna(axis=1, how='all')

# =========================
# 2. Data Profiling
# =========================

# Print overall dimensions of the dataset.
total_rows, total_cols = df.shape
print(f"Total rows: {total_rows}")
print(f"Total columns: {total_cols}\n")

# Initialize a dictionary to store the profile for each column.
profile = {}

for col in df.columns:
    profile[col] = {}
    
    # For numeric columns, compute summary statistics.
    if pd.api.types.is_numeric_dtype(df[col]):
        profile[col]['Attribute Type'] = 'Numeric'
        profile[col]['Min'] = df[col].min()
        profile[col]['Max'] = df[col].max()
        profile[col]['Mean'] = df[col].mean()
        profile[col]['Median'] = df[col].median()
        profile[col]['Std'] = df[col].std()
    
    # For datetime columns.
    elif pd.api.types.is_datetime64_any_dtype(df[col]):
        profile[col]['Attribute Type'] = 'Temporal'
    
    # For categorical/discrete columns.
    else:
        profile[col]['Attribute Type'] = 'Symbolic/Discrete'
        profile[col]['Unique Count'] = df[col].nunique()
        top_freq = df[col].value_counts().head(3)
        profile[col]['Top 3 Frequent'] = top_freq.to_dict()
    
    # Calculate missingness: percentage of missing values in the column.
    missing_pct = df[col].isnull().mean() * 100
    profile[col]['Missingness (%)'] = missing_pct

# Display the profile information for each column.
for col, stats in profile.items():
    print(f"Column: {col}")
    for stat, value in stats.items():
        print(f"  {stat}: {value}")
    print("\n")

# =========================
# 3. Data Visualization
# =========================

# -- Visualization 1: Bar Graph for Frequency of Records by Date --
plt.figure(figsize=(12, 6))
# Sort dates to display them in order.
date_counts = df['Date'].value_counts().sort_index()
date_counts.plot(kind='bar', color='skyblue')
plt.title("Frequency of Records by Date")
plt.xlabel("Date")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -- Visualization 2: Histogram for CO(GT) --
plt.figure(figsize=(10, 6))
sns.histplot(df['CO(GT)'].dropna(), kde=True, bins=30, color='salmon')
plt.title("Distribution of CO(GT)")
plt.xlabel("CO(GT) Value")
plt.ylabel("Frequency")
plt.show()

# -- Visualization 3: Pairplot for Selected Numeric Features --
numeric_columns = ['CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)', 'T', 'RH']
sns.pairplot(df[numeric_columns].dropna())
plt.suptitle("Pairplot of Selected Numeric Features", y=1.02)
plt.show()

# -- Visualization 4: Line Chart for Daily Average Temperature --
plt.figure(figsize=(14, 6))
# Set DateTime as index for time series operations.
df.set_index('DateTime', inplace=True)
# Resample data by day to calculate the daily average of Temperature (T).
daily_avg_temp = df['T'].resample('D').mean()
daily_avg_temp.plot(color='green')
plt.title("Daily Average Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()

# Reset index for any further analysis.
df.reset_index(inplace=True)
