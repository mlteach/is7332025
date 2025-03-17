import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = "C:/Users/dunes/OneDrive/Documents/Code/global_air_quality_dataset.csv"
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day_of_Week'] = df['Date'].dt.day_name()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Month', y='AQI', estimator='mean', ci=None, marker='o')
plt.title('Monthly Average AQI Trend for 2024')
plt.xlabel('Month')
plt.ylabel('Average AQI')
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Day_of_Week', y='AQI', order=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
plt.title('AQI Distribution by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('AQI')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['AQI'], bins=30, kde=True)
plt.title('Distribution of AQI Values')
plt.xlabel('AQI')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

if 'PM2.5 (µg/m³)' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['PM2.5 (µg/m³)'], bins=30, kde=True)
    plt.title('Distribution of PM2.5 Levels')
    plt.xlabel('PM2.5 (µg/m³)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='City', y='AQI', estimator=np.mean, ci=None)
plt.title('Average AQI by City')
plt.xlabel('City')
plt.ylabel('Average AQI')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

if 'Country' in df.columns and 'PM2.5 (µg/m³)' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='Country', y='PM2.5 (µg/m³)', estimator=np.mean, ci=None)
    plt.title('Average PM2.5 Levels by Country')
    plt.xlabel('Country')
    plt.ylabel('Average PM2.5 (µg/m³)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

top_cities = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(3).index.tolist()
plt.figure(figsize=(12, 6))
sns.lineplot(data=df[df['City'].isin(top_cities)], x='Date', y='AQI', hue='City')
plt.title('AQI Over Time for Top 3 Most Polluted Cities')
plt.xlabel('Date')
plt.ylabel('AQI')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 8))
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features')
plt.show()

if 'Country' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Country', y='AQI')
    plt.title('AQI Distribution by Country')
    plt.xlabel('Country')
    plt.ylabel('AQI')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
