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
