import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned air quality dataset and ensure DateTime is parsed
df = pd.read_csv("AirQuality_Cleaned.csv", parse_dates=["DateTime"])
df["DateTime"] = pd.to_datetime(df["DateTime"], errors="coerce")

# ------------------------------
# 1. Year-to-Year Analysis
# ------------------------------
# Create a new column for the year
df["Year"] = df["DateTime"].dt.year

# Calculate the average temperature (T) for each year
yearly_avg = df.groupby("Year")["T"].mean()

plt.figure(figsize=(10, 6))
yearly_avg.plot(kind="bar", color="skyblue")
plt.title("Average Temperature by Year")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()

# ------------------------------
# 2. Month-to-Month Analysis
# ------------------------------
# Option 1: Year-Month trend (each month in each year)
df["YearMonth"] = df["DateTime"].dt.to_period("M")
year_month_avg = df.groupby("YearMonth")["T"].mean()

plt.figure(figsize=(14, 6))
year_month_avg.plot(kind="line", marker="o", color="green")
plt.title("Average Temperature by Year-Month")
plt.xlabel("Year-Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Option 2: Aggregate by Month (over all years)
df["Month"] = df["DateTime"].dt.month
monthly_avg = df.groupby("Month")["T"].mean()

plt.figure(figsize=(10, 6))
monthly_avg.plot(kind="bar", color="orange")
plt.title("Average Temperature by Month (Aggregated Over Years)")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ------------------------------
# 3. Day-of-Week Analysis
# ------------------------------
# Create a column for the day of the week
df["DayOfWeek"] = df["DateTime"].dt.day_name()
weekday_avg = df.groupby("DayOfWeek")["T"].mean()

# Reorder days to display in natural order
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_avg = weekday_avg.reindex(days_order)

plt.figure(figsize=(10, 6))
weekday_avg.plot(kind="bar", color="purple")
plt.title("Average Temperature by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
