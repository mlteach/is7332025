import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plots for data visualisation storypoints
# Load the dataset
df = pd.read_csv('ai_job_market_insights_with_years.csv')
data = pd.read_csv('ai_job_market_insights_with_years.csv')


# Heatmap for AI Adoption Across Industries
plt.figure(figsize=(10, 6))
ai_adoption_pivot = data.pivot_table(index='Industry', columns='AI_Adoption_Level', aggfunc='size', fill_value=0)
sns.heatmap(ai_adoption_pivot, annot=True, fmt='d', cmap='Blues')
plt.title('AI Adoption Levels Across Industries')
plt.xlabel('AI Adoption Level')
plt.ylabel('Industry')
plt.show()

# 2. Boxplot for Automation Risk by Industry
plt.figure(figsize=(10, 6))
sns.boxplot(x='Industry', y='Automation_Risk', data=data)
plt.title('Automation Risk Distribution by Industry')
plt.xlabel('Industry')
plt.ylabel('Automation Risk Level')
plt.xticks(rotation=45)
plt.show()

# 3. Growth Projections and Salaries
plt.figure(figsize=(10, 6))  # Reduced figure size
sns.scatterplot(x='Job_Growth_Projection', y='Salary_USD', hue='Job_Title', data=df, palette='tab20', s=100)
plt.title('Job Growth Projection vs Salary')
plt.xlabel('Job Growth Projection')
plt.ylabel('Salary (USD)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)  # Legend outside the plot
plt.tight_layout()  # Automatically adjust layout to prevent cutting
plt.show()

# 3. Line Plot for Salary Trends Over Time by Job Title
plt.figure(figsize=(10, 5))  # Smaller figure size
sns.lineplot(x='Year', y='Salary_USD', hue='Job_Title', data=data, ci=None)
plt.title('Salary Trends Over Time by Job Title')
plt.xlabel('Year')
plt.ylabel('Salary (USD)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)  # Legend outside the plot
plt.tight_layout()  # Adjust layout to prevent cutting
plt.show()


# 5.  Automation Risk vs. AI Adoption

plt.figure(figsize=(8, 5))  # Smaller figure size
sns.scatterplot(x='AI_Adoption_Level', y='Automation_Risk', hue='Industry', data=data, palette='viridis', s=100)
plt.title('Automation Risk vs. AI Adoption by Industry')
plt.xlabel('AI Adoption Level')
plt.ylabel('Automation Risk')
plt.xticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])  # Map numerical values to labels
plt.yticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])  # Map numerical values to labels
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)  # Legend outside the plot
plt.tight_layout()  # Adjust layout to prevent cutting
plt.show()







