from fredapi import Fred
import matplotlib.pyplot as plt

# Use your working API key
fred = Fred(api_key="306a3b46d80923127981cdabb3c9691f")

# Fetch real GDP data (seasonally adjusted annual rate)
gdp = fred.get_series("GDPC1")

# Plot GDP
plt.figure(figsize=(10, 5))
gdp.plot(title="Real US GDP (Chained 2012 Dollars)")
plt.grid(True)
plt.tight_layout()
plt.show()