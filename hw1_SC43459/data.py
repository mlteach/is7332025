import pandas as pd
import numpy as np
from tabulate import tabulate

# --------------------------------------------------
# 1. Loading and Cleaning the Dataset
# --------------------------------------------------

# Specify the file path (update if needed)
file_path = file_path = r"C:\Users\saita\OneDrive - UMBC\Desktop\air+quality\AirQualityUCI.csv"



# Load the dataset; note the semicolon as the delimiter and comma as the decimal marker
df = pd.read_csv(file_path, sep=';', decimal=',')

# Display missing values before cleaning
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# Create a cleaned copy with selected columns (adjust columns based on your dataset)
# For example, common columns in the UCI Air Quality dataset might include:
# 'Date', 'Time', 'CO(GT)', 'C6H6(GT)', 'T', 'RH', etc.
# Here we combine Date and Time to create a proper datetime column.
df_cleaned = df.copy()

# Fix the time format: replace periods with colons (e.g., "18.00.00" becomes "18:00:00")
df_cleaned['Time'] = df_cleaned['Time'].str.replace('.', ':', regex=False)

# Combine Date and Time into a new 'DateTime' column; assume dates are in DD/MM/YYYY format
df_cleaned['DateTime'] = pd.to_datetime(df_cleaned['Date'] + ' ' + df_cleaned['Time'], dayfirst=True)

# Remove columns that are completely empty (if any)
df_cleaned = df_cleaned.dropna(axis=1, how='all')

# Display missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# Save the cleaned dataset to a new CSV file
df_cleaned.to_csv("AirQuality_Cleaned.csv", index=False)
print("\nCleaned dataset saved successfully.")

# --------------------------------------------------
# 2. Displaying Sample Data and Dataset Info
# --------------------------------------------------

# Show the first 5 rows
print("\nFirst 5 rows of the cleaned dataset:")
print(df_cleaned.head())

print("\n" + "="*80 + "\n")  # Separator for readability

# Show the last 5 rows
print("Last 5 rows of the cleaned dataset:")
print(df_cleaned.tail())

print("\n" + "="*80 + "\n")
print("Dataset Info:")
print(df_cleaned.info())

# --------------------------------------------------
# 3. Profiling the Dataset
# --------------------------------------------------

profile_data = []

for col in df_cleaned.columns:
    col_info = {}
    col_info['Column Name'] = col
    
    # Check the data type of the column
    if pd.api.types.is_numeric_dtype(df_cleaned[col]):
        col_info['Attribute Type'] = 'Numeric'
        col_info['Min'] = df_cleaned[col].min()
        col_info['Max'] = df_cleaned[col].max()
        col_info['Mean'] = round(df_cleaned[col].mean(), 2)
        col_info['Median'] = df_cleaned[col].median()
        col_info['Std Dev'] = round(df_cleaned[col].std(), 2)
    elif pd.api.types.is_datetime64_any_dtype(df_cleaned[col]):
        col_info['Attribute Type'] = 'Temporal'
    else:
        col_info['Attribute Type'] = 'Symbolic'
        col_info['Unique Values'] = df_cleaned[col].nunique()
        top_values = df_cleaned[col].value_counts().head(3)
        col_info['Top 3 Frequent'] = ', '.join([f"{k}: {v}" for k, v in top_values.items()])
    
    # Calculate percentage of missing values
    col_info['Missing %'] = round(df_cleaned[col].isnull().mean() * 100, 2)
    
    profile_data.append(col_info)

profile_df = pd.DataFrame(profile_data)

print("\nDataset Profile:\n")
print(tabulate(profile_df, headers='keys', tablefmt='grid'))

print("\nDataset Profiling Complete!")

import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Define the file path to your cleaned dataset
file_path = file_path = r"C:\Users\saita\OneDrive - UMBC\Desktop\air+quality\AirQualityUCI.csv"


# Load the dataset and ensure the DateTime column is correctly parsed
df = pd.read_csv(file_path, parse_dates=["DateTime"])
df["DateTime"] = pd.to_datetime(df["DateTime"], errors="coerce")

# Create additional columns for filtering/grouping
df["YearMonth"] = df["DateTime"].dt.to_period("M").astype(str)
df["DayOfWeek"] = df["DateTime"].dt.day_name()

# Define the list of key metrics (pollutants) for selection
pollutants = ["T", "CO(GT)", "C6H6(GT)", "RH", "AH"]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Air Quality Data Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for selecting a pollutant
    html.Div([
        html.Label("Select Pollutant:"),
        dcc.Dropdown(
            id='pollutant-dropdown',
            options=[{'label': p, 'value': p} for p in pollutants],
            value=pollutants[0],
            clearable=False
        )
    ], style={'width': '40%', 'display': 'inline-block', 'padding': '10px'}),
    
    # Date picker to select the date range
    html.Div([
        html.Label("Select Date Range:"),
        dcc.DatePickerRange(
            id='date-picker-range',
            min_date_allowed=df["DateTime"].min().date(),
            max_date_allowed=df["DateTime"].max().date(),
            start_date=df["DateTime"].min().date(),
            end_date=df["DateTime"].max().date()
        )
    ], style={'width': '40%', 'display': 'inline-block', 'padding': '10px'}),
    
    # Graph to display the time series
    dcc.Graph(id='time-series-chart')
])

# Callback to update the graph based on user selections
@app.callback(
    Output('time-series-chart', 'figure'),
    [Input('pollutant-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_chart(selected_pollutant, start_date, end_date):
    # Filter the DataFrame by the selected date range
    mask = (df["DateTime"] >= start_date) & (df["DateTime"] <= end_date)
    filtered_df = df.loc[mask].copy()
    
    # If no data is available, return an empty figure with a message
    if filtered_df.empty:
        return px.line(title="No data available for selected range")
    
    # Aggregate data by day to compute the daily average for the selected pollutant
    filtered_df["Date"] = filtered_df["DateTime"].dt.date
    daily_avg = filtered_df.groupby("Date")[selected_pollutant].mean().reset_index()
    
    # Create an interactive line chart using Plotly Express
    fig = px.line(daily_avg, x="Date", y=selected_pollutant,
                  title=f"Daily Average {selected_pollutant} Over Time",
                  labels={selected_pollutant: f"Average {selected_pollutant}"})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
import pandas as pd

file_path = r"C:\Users\saita\OneDrive - UMBC\Desktop\733project\AirQuality_Cleaned.csv"

# Load the dataset without parsing dates first
df = pd.read_csv(file_path)

# Print column names to check if 'DateTime' exists
print(df.columns)
