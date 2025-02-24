import matplotlib.pyplot as plt
import pandas as pd

# machine learning predictions
# Count job listings by year
df = pd.read_csv('ai_job_market_insights_with_years.csv')
year_counts = df['Year'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
year_counts.plot(kind='bar', color='skyblue')
plt.title('Job Listings by Year')
plt.xlabel('Year')
plt.ylabel('Number of Job Listings')
plt.xticks(rotation=0)
plt.show()


# Count job listings by industry
industry_counts = df['Industry'].value_counts()

# Plot
plt.figure(figsize=(12, 6))
industry_counts.plot(kind='bar', color='lightgreen')
plt.title('Job Listings by Industry')
plt.xlabel('Industry')
plt.ylabel('Number of Job Listings')
plt.xticks(rotation=45)
plt.show()

# Calculate average salary by year
avg_salary_by_year = df.groupby('Year')['Salary_USD'].mean()

# Plot
plt.figure(figsize=(10, 6))
avg_salary_by_year.plot(kind='line', marker='o', color='orange')
plt.title('Average Salary by Year')
plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')
plt.grid(True)
plt.show()


# point 3 data distribution and machine learning

import matplotlib.pyplot as plt

# Plot the distribution of salaries
plt.figure(figsize=(10, 6))
plt.hist(df['Salary_USD'], bins=30, color='blue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()