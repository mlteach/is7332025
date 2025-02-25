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

# Print first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Print last 5 rows of the dataset
print("Last 5 rows of the dataset:")
print(df.tail(), "\n")

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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset and parse the DateTime column
df = pd.read_csv("AirQuality_Cleaned.csv", parse_dates=["DateTime"])
df["DateTime"] = pd.to_datetime(df["DateTime"], errors="coerce")

# -----------------------------
# Plot 1: Distribution of Temperature (T)
# -----------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df["T"].dropna(), kde=True, bins=30, color="cornflowerblue")
plt.title("Distribution of Temperature (T)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -----------------------------
# Plot 2: Distribution of CO(GT)
# -----------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df["CO(GT)"].dropna(), kde=True, bins=30, color="salmon")
plt.title("Distribution of CO(GT)")
plt.xlabel("CO(GT) Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the cleaned air quality dataset and ensure DateTime is parsed
df = pd.read_csv("AirQuality_Cleaned.csv", parse_dates=["DateTime"])
df["DateTime"] = pd.to_datetime(df["DateTime"], errors="coerce")

# Create additional columns for temporal analysis
df["YearMonth"] = df["DateTime"].dt.to_period("M").astype(str)
df["DayOfWeek"] = df["DateTime"].dt.day_name()

# -----------------------------
# Plot 1: Temperature Over Time (Line Chart)
# -----------------------------
plt.figure(figsize=(12, 6))
plt.plot(df["DateTime"], df["T"], color="darkblue", alpha=0.6)
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# -----------------------------
# Plot 2: Distribution of CO(GT) (Histogram + KDE)
# -----------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df["CO(GT)"].dropna(), kde=True, bins=30, color="salmon")
plt.title("Distribution of CO(GT)")
plt.xlabel("CO(GT) Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -----------------------------
# Plot 3: Average Temperature by Month (Aggregated by YearMonth)
# -----------------------------
monthly_avg = df.groupby("YearMonth")["T"].mean().reset_index()
plt.figure(figsize=(14, 6))
sns.barplot(x="YearMonth", y="T", data=monthly_avg, palette="viridis")
plt.title("Average Temperature by Month")
plt.xlabel("Year-Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Plot 4: Relative Humidity by Day of the Week (Box Plot)
# -----------------------------
plt.figure(figsize=(10, 6))
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sns.boxplot(x="DayOfWeek", y="RH", data=df, order=order, palette="Set2")
plt.title("Relative Humidity by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Relative Humidity (%)")
plt.tight_layout()
plt.show()

