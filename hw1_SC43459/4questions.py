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
