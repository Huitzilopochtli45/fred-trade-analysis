from fredapi import Fred
import pandas as pd
import os

# === Setup ===
api_key = "306a3b46d80923127981cdabb3c9691f"
fred = Fred(api_key=api_key)

series_map = {
    "GDPC1": "Real GDP (Chained 2012 Dollars)",
    "GDPCA": "Nominal GDP (Current Dollars)",
    "GNPCA": "Gross National Product (Current Dollars)"
}

output_dir = "C:/Users/troyr/OneDrive - Self Taught LLC/PythonDev/03-projects/fred-trade-analysis/data"
os.makedirs(output_dir, exist_ok=True)

# === Fetch and save ===
for series_id, label in series_map.items():
    print(f"📡 Fetching {label}...")
    data = fred.get_series(series_id)
    df = pd.DataFrame(data)
    df.columns = [label]
    df.index.name = "Date"
    
    csv_path = os.path.join(output_dir, f"{series_id}.csv")
    df.to_csv(csv_path)
    print(f"✅ Saved to: {csv_path}")
