import pandas as pd
import matplotlib.pyplot as plt
import os

# === Setup ===

# Absolute path to the directory containing the CSV files
csv_path = "C:/Users/troyr/OneDrive - Self Taught LLC/PythonDev/03-projects/fred-trade-analysis/data/combined_macro.csv"

# Load data
df = pd.read_csv(csv_path, index_col=0, parse_dates=True)

# Rename for display clarity
df = df.rename(columns={"GDP": "Real GDP"})

# === Output folder setup ===
output_dir = "C:/Users/troyr/OneDrive - Self Taught LLC/PythonDev/03-projects/fred-trade-analysis/outputs"
os.makedirs(output_dir, exist_ok=True)

# === Plot settings ===
plot_vars = ["Real GDP", "Net_Exports", "Exports", "Imports"]
colors = ["purple", "blue", "green", "orange"]

for var, color in zip(plot_vars, colors):
    print(f"📈 Plotting {var}...")

    df[var].plot(title=f"{var} Over Time", figsize=(12, 6), color=color)
    plt.xlabel("Date")
    plt.ylabel("Billions of Dollars")
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    filename = f"{var.replace(' ', '_').lower()}_trend.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.clf()  # Clear figure for next plot

    print(f"✅ Saved to {filepath}")

print("🎉 All plots completed.")