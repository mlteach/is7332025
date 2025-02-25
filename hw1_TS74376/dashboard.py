# updated filters

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the dataset
# df = pd.read_csv('ai_job_market_insights_with_years.csv')

# # Streamlit App
# st.title('AI Job Market Insights Dashboard')

# # Sidebar Filters (for Local Insights)
# st.sidebar.header('Filters for Local Insights')
# selected_industry = st.sidebar.selectbox('Select Industry', df['Industry'].unique())
# selected_job_title = st.sidebar.selectbox('Select Job Title', df['Job_Title'].unique())

# # Filtered Data (Local Insights)
# filtered_data = df[(df['Industry'] == selected_industry) & (df['Job_Title'] == selected_job_title)]

# # Display Filtered Data
# st.header('Local Insights (Filtered Data)')
# st.write('Filtered Data:', filtered_data)

# # Plots for Filtered Data
# st.subheader('Salary Distribution')
# fig, ax = plt.subplots()
# sns.histplot(filtered_data['Salary_USD'], kde=True, bins=30, color='blue', ax=ax)
# st.pyplot(fig)

# st.subheader('AI Adoption Level (Filtered)')
# fig, ax = plt.subplots()
# sns.countplot(x='AI_Adoption_Level', data=filtered_data, palette='viridis', ax=ax)
# st.pyplot(fig)

# # Global Insights (Story Points)
# st.header('Global Insights')

# # 1. AI Adoption Across Industries
# st.subheader('1. AI Adoption Across Industries')
# fig, ax = plt.subplots(figsize=(10, 6))
# ai_adoption_pivot = df.pivot_table(index='Industry', columns='AI_Adoption_Level', aggfunc='size', fill_value=0)
# sns.heatmap(ai_adoption_pivot, annot=True, fmt='d', cmap='Blues', ax=ax)
# plt.title('AI Adoption Levels Across Industries')
# plt.xlabel('AI Adoption Level')
# plt.ylabel('Industry')
# st.pyplot(fig)

# # 2. Automation Risk by Industry
# st.subheader('2. Automation Risk by Industry')
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.boxplot(x='Industry', y='Automation_Risk', data=df, ax=ax)
# plt.title('Automation Risk Distribution by Industry')
# plt.xlabel('Industry')
# plt.ylabel('Automation Risk Level')
# plt.xticks(rotation=45)
# st.pyplot(fig)

# # 3. Job Growth Projection vs Salary
# st.subheader('3. Job Growth Projection vs Salary')
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.scatterplot(x='Job_Growth_Projection', y='Salary_USD', hue='Job_Title', data=df, palette='tab20', s=100, ax=ax)
# plt.title('Job Growth Projection vs Salary')
# plt.xlabel('Job Growth Projection')
# plt.ylabel('Salary (USD)')
# plt.xticks(rotation=45)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
# plt.tight_layout()
# st.pyplot(fig)

# # 4. Salary Trends Over Time by Job Title
# st.subheader('4. Salary Trends Over Time by Job Title')
# fig, ax = plt.subplots(figsize=(10, 5))
# sns.lineplot(x='Year', y='Salary_USD', hue='Job_Title', data=df, ci=None, ax=ax)
# plt.title('Salary Trends Over Time by Job Title')
# plt.xlabel('Year')
# plt.ylabel('Salary (USD)')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
# plt.tight_layout()
# st.pyplot(fig)

# # 5. Automation Risk vs. AI Adoption by Industry
# st.subheader('5. Automation Risk vs. AI Adoption by Industry')
# fig, ax = plt.subplots(figsize=(8, 5))
# sns.scatterplot(x='AI_Adoption_Level', y='Automation_Risk', hue='Industry', data=df, palette='viridis', s=100, ax=ax)
# plt.title('Automation Risk vs. AI Adoption by Industry')
# plt.xlabel('AI Adoption Level')
# plt.ylabel('Automation Risk')
# plt.xticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
# plt.yticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
# plt.tight_layout()
# st.pyplot(fig)




# to run this dashoard use this command - streamlit run dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('ai_job_market_insights_with_years.csv')

# Streamlit App
st.title('AI Job Market Insights Dashboard')

# Sidebar Filters (for Local Insights)
st.sidebar.header('Filters for Local Insights')
selected_industry = st.sidebar.selectbox('Select Industry', df['Industry'].unique())
selected_job_title = st.sidebar.selectbox('Select Job Title', df['Job_Title'].unique())
selected_year = st.sidebar.selectbox('Select Year', df['Year'].unique())

# Filtered Data (Local Insights)
filtered_data = df[
    (df['Industry'] == selected_industry) &
    (df['Job_Title'] == selected_job_title) &
    (df['Year'] == selected_year)
]

# Display Filtered Data
st.header('Local Insights (Filtered Data)')
st.write('Filtered Data:', filtered_data)

# Plots for Filtered Data
st.subheader('Salary Distribution (Filtered)')
fig1, ax1 = plt.subplots()
sns.histplot(filtered_data['Salary_USD'], kde=True, bins=30, color='blue', ax=ax1)
plt.title(f'Salary Distribution in {selected_industry} ({selected_year})')
st.pyplot(fig1)

st.subheader('AI Adoption Level (Filtered)')
fig2, ax2 = plt.subplots()
sns.countplot(x='AI_Adoption_Level', data=filtered_data, palette='viridis', ax=ax2)
plt.title(f'AI Adoption Level in {selected_industry} ({selected_year})')
st.pyplot(fig2)

# Global Insights (Story Points)
st.header('Global Insights')

# 1. AI Adoption Across Industries (Filtered)
st.subheader('1. AI Adoption Across Industries (Filtered)')
fig3, ax3 = plt.subplots(figsize=(10, 6))
ai_adoption_pivot = filtered_data.pivot_table(index='Industry', columns='AI_Adoption_Level', aggfunc='size', fill_value=0)
sns.heatmap(ai_adoption_pivot, annot=True, fmt='d', cmap='Blues', ax=ax3)
plt.title(f'AI Adoption Levels in {selected_industry} ({selected_year})')
plt.xlabel('AI Adoption Level')
plt.ylabel('Industry')
st.pyplot(fig3)

# 2. Automation Risk by Industry (Filtered)
st.subheader('2. Automation Risk by Industry (Filtered)')
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Industry', y='Automation_Risk', data=filtered_data, ax=ax4)
plt.title(f'Automation Risk Distribution in {selected_industry} ({selected_year})')
plt.xlabel('Industry')
plt.ylabel('Automation Risk Level')
plt.xticks(rotation=45)
st.pyplot(fig4)

# 3. Job Growth Projection vs Salary (Filtered)
st.subheader('3. Job Growth Projection vs Salary (Filtered)')
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Job_Growth_Projection', y='Salary_USD', hue='Job_Title', data=filtered_data, palette='tab20', s=100, ax=ax5)
plt.title(f'Job Growth Projection vs Salary in {selected_industry} ({selected_year})')
plt.xlabel('Job Growth Projection')
plt.ylabel('Salary (USD)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()
st.pyplot(fig5)

# 4. Salary Trends Over Time by Job Title (Filtered)
st.subheader('4. Salary Trends Over Time by Job Title (Filtered)')
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.lineplot(x='Year', y='Salary_USD', hue='Job_Title', data=filtered_data, ci=None, ax=ax6)
plt.title(f'Salary Trends Over Time in {selected_industry} ({selected_year})')
plt.xlabel('Year')
plt.ylabel('Salary (USD)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()
st.pyplot(fig6)

# 5. Automation Risk vs. AI Adoption by Industry (Filtered)
st.subheader('5. Automation Risk vs. AI Adoption by Industry (Filtered)')
fig7, ax7 = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='AI_Adoption_Level', y='Automation_Risk', hue='Industry', data=filtered_data, palette='viridis', s=100, ax=ax7)
plt.title(f'Automation Risk vs. AI Adoption in {selected_industry} ({selected_year})')
plt.xlabel('AI Adoption Level')
plt.ylabel('Automation Risk')
plt.xticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
plt.yticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()
st.pyplot(fig7)

