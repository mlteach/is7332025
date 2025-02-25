import pandas as pd
from skimpy import skim

# Load the dataset
df = pd.read_csv('ai_job_market_insights_with_years.csv')

# Generate the summary report
skim(df)

# just run this file using button on top right