# data.py
import pandas as pd

# Load the Excel once and reuse everywhere
df = pd.read_excel("startups_funded.xlsx")

# Shared values for sliders / dropdowns
year_min = int(df["founding_year"].dropna().min())
year_max = int(df["founding_year"].dropna().max())

industry_options = (
    [{"label": "All industries", "value": "ALL"}] +
    [{"label": ind, "value": ind}
     for ind in sorted(df["major_industry"].dropna().unique())]
)
