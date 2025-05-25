from fredapi import Fred
import pandas as pd
import os

# Initialize FRED API
api_key = "306a3b46d80923127981cdabb3c9691f"
fred = Fred(api_key=api_key)

# Define the series to fetch
series = {
    "GDP": "GDPC1",
    "Net_Exports": "NETEXP",
    "Exports": "EXPGS",
    "Imports": "IMPGS",
    "Gov_Spending": "GCEC96",
    "Savings": "W875RX1",
    "Consumption": "PCE"
}

# Fetch each series and build DataFrame
df = pd.DataFrame()
for name, sid in series.items():
    print(f"📡 Fetching {name}...")
    df[name] = fred.get_series(sid)

# Drop rows with any missing values
df.dropna(inplace=True)

# Ensure data/ folder exists
os.makedirs("data", exist_ok=True)

# Save the result
df.to_csv("data/combined_macro.csv")
print("✅ Saved to data/combined_macro.csv")

