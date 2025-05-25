import pandas as pd
import os

# Load original cleaned file
path = "C:/Users/troyr/OneDrive - Self Taught LLC/PythonDev/03-projects/fred-trade-analysis/data/TARIFF_EVENTS_CLEANED.csv"
df = pd.read_csv(path, parse_dates=["Date"])

# Define short display names manually (in same order as DataFrame)
short_labels = [
    "Smoot-Hawley",
    "Trade Exp. Act",
    "Vol. Export Res.",
    "Section 232",
    "Section 301",
    "Phase 1 Deal"
]

# Append new column
df["Short_Label"] = short_labels

# Save updated CSV
save_path = path.replace("CLEANED.csv", "LABELED.csv")
df.to_csv(save_path, index=False)

# Confirm structure and print first few rows
print(f"✅ Updated file saved to:\n{save_path}")
print("\n🔍 First few rows of labeled tariff events:\n")
print(df[["Date", "Event_Name", "Short_Label"]].head())
