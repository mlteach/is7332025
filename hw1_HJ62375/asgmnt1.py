import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import plotly.express as px

#importing the dataset
ds=pd.read_csv('C:\\Users\\Dell\\Desktop\\ml\\is733\\nba_elo_latest.csv');

#Printing total number of rows and columns
print(f"Total Rows are : {ds.shape[0]}");
print(f"\nTotal Columns are: {ds.shape[1]}");

#displays first few rows of the dataset
print(f"\nThe first few rows are:\n {ds.head()}");


# Manually specify known temporal (date) columns
date_columns = ['date']  # Add more if needed

# Convert only known date columns to datetime format
for col in date_columns:
    if col in ds.columns:
        ds[col] = pd.to_datetime(ds[col], errors='coerce')  # Coerce ensures invalid dates become NaT

# Function to analyze each column
def analyze_columns(ds):
    column_analysis = []

    for column in ds.columns:
        col_data = ds[column]
        col_summary = {
            'Column Name': column,
            'Data Type': col_data.dtype,
            'Missing Percentage': col_data.isnull().mean() * 100
        }

        # Identify Temporal Attributes (Only Check Specified Columns)
        if column in date_columns:
            col_summary['Attribute Type'] = 'Temporal (Date/Time)'

        # Identify Spatial Attributes (Using keywords)
        elif any(keyword in column.lower() for keyword in ['lat', 'lon', 'long', 'location']):
            col_summary['Attribute Type'] = 'Spatial (Geographical)'

        # Checking if column is numeric
        elif pd.api.types.is_numeric_dtype(col_data):
            unique_values = col_data.nunique()
            
            # Determine if it's continuous or discrete
            if unique_values > 20:  # Arbitrary threshold, usually > 20 means continuous
                numeric_type = 'Continuous (Real)'
            else:
                numeric_type = 'Discrete (Integer Counts)'

            col_summary.update({
                'Attribute Type': f'Numeric ({numeric_type})',
                'Min': col_data.min(),
                'Max': col_data.max(),
                'Mean': col_data.mean(),
                'Median': col_data.median(),
                'Standard Deviation': col_data.std()
            })

        # Checking if column is categorical (symbolic/discrete)
        else:
            unique_values = col_data.value_counts()
            col_summary.update({
                'Attribute Type': 'Symbolic/Discrete',
                'Unique Values Count': unique_values.shape[0],
                'Top 3 Values': unique_values.head(3).to_dict()
            })

        column_analysis.append(col_summary)

    return column_analysis

# Run analysis
column_details = analyze_columns(ds)

# Display results
for col in column_details:
    print(col)
    print('-' * 50)


#Generating plots based on the matches like year to year, month to month ,day to day
# Extract year, month, and day of the week for analysis

ds['year'] = ds['date'].dt.year
ds['month'] = ds['date'].dt.month
ds['day_of_week'] = ds['date'].dt.dayofweek  # 0 = Monday, 6 = Sunday

#Mapping month numbers to names
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ds['month_name'] = ds['month'].apply(lambda x: month_names[x - 1])

#Set Seaborn style
sns.set_style('whitegrid')

#Create a figure for the first two graphs
plt.figure(figsize=(14, 6))

#Yearly Distribution
plt.subplot(1, 2, 1)
sns.countplot(x='year', data=ds, color='blue')
plt.xlabel('Year');
plt.title('Yearly Distribution of Games')

#Monthly Distribution
plt.subplot(1, 2, 2)
sns.countplot(x='month_name', data=ds, color='grey', order=month_names)
plt.title('Monthly Distribution of Games')
plt.xlabel('Month')

plt.tight_layout()
plt.show()

#Day of the Week Distribution (Separate Figure)
plt.figure(figsize=(8, 6))
sns.countplot(x='day_of_week', data=ds, color='Purple')
plt.title('Day of the Week Distribution')
plt.xlabel('Day of the Week (0=Mon, 6=Sun)')
plt.show()


#Top 10 Teams by Frequency (Separate Figure)
plt.figure(figsize=(10, 6))
sns.countplot(y='team1', data=ds, order=ds['team1'].value_counts().head(10).index, palette='mako')
plt.title('Top 10 Teams by Game Frequency')
plt.ylabel('Team')
plt.show()

#Playoff Game Types Distribution (Separate Figure)
plt.figure(figsize=(8, 6))
sns.countplot(x='playoff', data=ds[ds['playoff'].notnull()], palette='rocket')
plt.title('Playoff Game Types')
plt.xlabel('Playoff Stage')
playoff_labels = {
    'p': 'Preliminary',
    'q': 'Quarterfinals',
    's': 'Semifinals',
    'c': 'Conference Finals',
    'f': 'NBA Finals'
}

# Updating x-axis labels
plt.xticks(ticks=range(len(playoff_labels)), labels=playoff_labels.values())
plt.show()


#Interactive Distribution of Elo Ratings (Plotly) - Best 5 Performing Teams
if 'elo1_pre' in ds.columns and 'team1' in ds.columns:
    # Calculate the total elo1_pre rating for each team
    top_5_teams = ds.groupby('team1')['elo1_pre'].sum().nlargest(5).index  # Get top 5 teams based on total Elo rating
    #print(top_5_teams);
    # Filter dataset for only these teams
    filtered_ds = ds[ds['team1'].isin(top_5_teams)]  
    
    fig = px.line(filtered_ds, x='date', y='elo1_pre', color='team1', 
                  title='Interactive Elo Rating Trend for Top 5 Performing Teams', 
                  labels={'elo1_pre': 'Elo Rating', 'date': 'Date', 'team1': 'Team'})
    
    # Align title to center
    fig.update_layout(title_x=0.5)
    
    # Show interactive plot
    fig.show()
else:
    print("Required columns not found in dataset.")