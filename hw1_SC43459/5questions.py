import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Define the file path to your cleaned dataset
file_path = r"C:\Users\saita\OneDrive\Documents\Desktop\733project\AirQuality_Cleaned.csv"

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
