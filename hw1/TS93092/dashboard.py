import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Load the dataset
file_path = "C:/Users/dunes/OneDrive/Documents/Code/global_air_quality_dataset.csv"
df = pd.read_csv(file_path)

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract temporal features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day_of_Week'] = df['Date'].dt.day_name()

# Streamlit Dashboard
st.title("Global Air Quality Data Explorer")

# Sidebar filters
st.sidebar.header("Filter Data")
selected_cities = st.sidebar.multiselect("Select Cities:", options=df['City'].unique(), default=df['City'].unique())
selected_countries = st.sidebar.multiselect("Select Countries:", options=df['Country'].unique(), default=df['Country'].unique())
selected_year = st.sidebar.selectbox("Select Year:", options=df['Year'].dropna().unique())

# Filtered Data
df_filtered = df[(df['City'].isin(selected_cities)) & (df['Country'].isin(selected_countries)) & (df['Year'] == selected_year)]

# Show filtered data
st.subheader("Filtered Data")
st.dataframe(df_filtered)

# Plot: Monthly Average AQI Trend
st.subheader("Monthly Average AQI Trend")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df_filtered, x='Month', y='AQI', estimator='mean', ci=None, marker='o', ax=ax)
ax.set_title('Monthly Average AQI Trend')
ax.set_xlabel('Month')
ax.set_ylabel('Average AQI')
ax.grid(True)
st.pyplot(fig)

# Plot: AQI Distribution by Day of the Week
st.subheader("AQI Distribution by Day of the Week")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_filtered, x='Day_of_Week', y='AQI', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ax=ax)
ax.set_title('AQI Distribution by Day of the Week')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('AQI')
ax.grid(True)
st.pyplot(fig)

# Plot: AQI Over Time for Top 3 Most Polluted Cities
top_cities = df_filtered.groupby('City')['AQI'].mean().sort_values(ascending=False).head(3).index.tolist()
if top_cities:
    st.subheader("AQI Over Time for Top 3 Most Polluted Cities")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df_filtered[df_filtered['City'].isin(top_cities)], x='Date', y='AQI', hue='City', ax=ax)
    ax.set_title('AQI Over Time for Top 3 Most Polluted Cities')
    ax.set_xlabel('Date')
    ax.set_ylabel('AQI')
    ax.grid(True)
    st.pyplot(fig)

# Plot: Correlation Heatmap
st.subheader("Correlation Heatmap of Numerical Features")
fig, ax = plt.subplots(figsize=(10, 8))
corr = df_filtered.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)

# Plot: Average AQI by Country
if 'Country' in df_filtered.columns:
    st.subheader("Average AQI by Country")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_filtered, x='Country', y='AQI', estimator=np.mean, ci=None, ax=ax)
    ax.set_title('Average AQI by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average AQI')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)
    st.pyplot(fig)

# Instructions to run the dashboard
st.sidebar.markdown("---")
st.sidebar.markdown("Made By")
st.sidebar.markdown("Tushara Sai Maddikara")
