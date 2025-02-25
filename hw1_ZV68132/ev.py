import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the Dataset
file_path = 'Electric_Vehicle_Population_Dataset.csv'
ev_data = pd.read_csv(r"C:\Users\shara\OneDrive\Desktop\Spring 2025\IS 733\Electric_Vehicle_Population_Dataset.csv")

# 1. Basic Dataset Overview
print("Total Rows:", ev_data.shape[0])
print("Total Columns:", ev_data.shape[1])
print("\nData Types:\n", ev_data.dtypes)

# 2. Missing Values Percentage
missing_values = (ev_data.isnull().mean() * 100).sort_values(ascending=False)
print("\nMissing Values (%):\n", missing_values)

# 3. Summary Statistics for Numeric Columns
numeric_summary = ev_data.describe().T
print("\nSummary Statistics for Numeric Columns:\n", numeric_summary)

# 4. Categorical Data Analysis
categorical_summary = {}
for col in ev_data.select_dtypes(include='object').columns:
    unique_values = ev_data[col].nunique()
    top_values = ev_data[col].value_counts().head(3).to_dict()
    categorical_summary[col] = {
        "Unique Values": unique_values,
        "Top 3 Values": top_values
    }
# Display Categorical Summary
print("\nCategorical Data Summary:\n")
for col, summary in categorical_summary.items():
    print(f"{col} - Unique Values: {summary['Unique Values']}")
    print(f"Top 3 Values: {summary['Top 3 Values']}\n")

# 5. Check for anything surprising or unique in the dataset
outside_wa = ev_data[ev_data['State'] != 'WA']
print("\nEntries from outside Washington:\n", outside_wa)

# 6. Temporal Pattern Analysis - Yearly EV Registrations
ev_data['Model Year'] = ev_data['Model Year'].astype(str)
sorted_years = sorted(ev_data['Model Year'].unique(), key=lambda x: int(x))
plt.figure(figsize=(12,6))
sns.countplot(data=ev_data, x='Model Year', hue='Model Year', palette="coolwarm", order=sorted_years, legend=False)  
plt.title('Yearly EV Registrations', fontsize=14)
plt.xlabel('Model Year', fontsize=12)
plt.ylabel('Number of Vehicles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#7. Distribution of Electric Range
ev_data['Electric Range'] = ev_data['Electric Range'].fillna(ev_data['Electric Range'].median())
plt.figure(figsize=(10,6))
sns.histplot(ev_data['Electric Range'], bins=30, kde=True, color='#4C72B0', edgecolor='black', kde_kws={'bw_adjust': 0.8})
plt.title('Distribution of Electric Range', fontsize=14)
plt.xlabel('Electric Range (miles)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#8. Distribution of Base MSRP
filtered_data = ev_data['Base MSRP'].dropna()
filtered_data = filtered_data[filtered_data > 0]
plt.figure(figsize=(12, 7))
sns.histplot(filtered_data, 
             kde=False, 
             color='salmon', 
             bins=50,  
             edgecolor='black', 
             alpha=0.6, 
             label='Histogram')
sns.kdeplot(filtered_data, 
             color='blue', 
             linewidth=2, 
             label='KDE', 
             bw_adjust=0.3) 
plt.title('Distribution of Base MSRP', fontsize=16)
plt.xlabel('Base MSRP ($)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

#9. Top EV Makes
plt.figure(figsize=(12, 6))
top_makes = ev_data['Make'].value_counts().head(10)
top_makes_df = pd.DataFrame({'Make': top_makes.index, 'Number of Vehicles': top_makes.values})
bar_plot = sns.barplot(data=top_makes_df, 
                       x='Make', 
                       y='Number of Vehicles', 
                       palette='coolwarm', 
                       hue='Make', 
                       legend=False) 
plt.title('Top 10 EV Makes', fontsize=16)
plt.xlabel('Make', fontsize=14)
plt.ylabel('Number of Vehicles', fontsize=14)
for p in bar_plot.patches:
    bar_plot.annotate(f'{int(p.get_height())}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='bottom', 
                      fontsize=12)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

#10. Top EV Models
plt.figure(figsize=(12, 6))
top_models = ev_data['Model'].value_counts().head(10)
top_models_df = pd.DataFrame({'Model': top_models.index, 'Number of Vehicles': top_models.values})
bar_plot = sns.barplot(data=top_models_df, 
                       x='Model', 
                       y='Number of Vehicles', 
                       palette='magma', 
                       hue='Model',  
                       legend=False) 
plt.title('Top 10 EV Models', fontsize=16)
plt.xlabel('Model', fontsize=14)
plt.ylabel('Number of Vehicles', fontsize=14)
for p in bar_plot.patches:
    bar_plot.annotate(f'{int(p.get_height())}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='bottom', 
                      fontsize=12)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

#11. Geographic Distribution by City 
plt.figure(figsize=(12, 6))
top_cities = ev_data['City'].value_counts().head(10)
top_cities_df = pd.DataFrame({'City': top_cities.index, 'Number of Vehicles': top_cities.values})
bar_plot = sns.barplot(data=top_cities_df, 
                       x='City', 
                       y='Number of Vehicles', 
                       palette='Set2',  
                       hue='City',  
                       legend=False) 
plt.title('Top 10 Cities with EV Registrations', fontsize=16)
plt.xlabel('City', fontsize=14)
plt.ylabel('Number of Vehicles', fontsize=14)
for p in bar_plot.patches:
    bar_plot.annotate(f'{int(p.get_height())}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='bottom', 
                      fontsize=12)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

#12. Electric Range vs Base MSRP
import numpy as np
plt.figure(figsize=(10, 6))
jitter_strength = 5 
ev_data['Electric Range Jittered'] = ev_data['Electric Range'] + np.random.normal(0, jitter_strength, size=len(ev_data))
sns.scatterplot(data=ev_data, 
                x='Electric Range Jittered', 
                y='Base MSRP', 
                hue='Make', 
                alpha=0.5,
                palette='Set1', 
                s=80) 
plt.title('Electric Range vs. Base MSRP by Make', fontsize=16)
plt.xlabel('Electric Range (miles)', fontsize=14)
plt.ylabel('Base MSRP ($)', fontsize=14)
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()