# Create detailed descriptions of each real economy metric in markdown format

# 📘 Real Economy Series — Definitions & Methodology

This document provides descriptions and interpretive guidance for the macroeconomic indicators saved under `/data/raw/real-economy`. These series capture the output and production activity across the U.S. economy, with a focus on both aggregate and sector-specific real indicators.

---

## 🔹 GDPC1 — Real Gross Domestic Product (Chained 2017 Dollars)

- **Definition**: The inflation-adjusted value of all goods and services produced within the U.S. economy. Expressed in chained 2017 dollars to remove the effects of inflation.
- **Frequency**: Quarterly
- **Source**: U.S. Bureau of Economic Analysis (BEA)
- **Methodology**:
  - Uses the **expenditure approach** to measure GDP:
    \[
    GDP = C + I + G + (X - M)
    \]
    where:
    - C = Consumption
    - I = Investment
    - G = Government spending
    - X = Exports
    - M = Imports
  - Adjusted using chain-weighted price indices to reflect real growth over time.

---

## 🔹 GDP — Nominal Gross Domestic Product

- **Definition**: Total monetary value of all final goods and services produced within the U.S. in current prices.
- **Units**: Billions of U.S. Dollars
- **Purpose**: Captures overall economic size without adjusting for inflation.
- **Use**: Used to compute inflation via GDP deflator; essential for calculating fiscal ratios (e.g., debt-to-GDP).

---

## 🔹 GNP — Gross National Product

- **Definition**: The total value of goods and services produced by U.S. residents, regardless of location.
- **Formula**: GNP = GDP + net income from abroad
- **Interpretation**: Focuses on **ownership**, not location — it includes income from U.S.-owned companies operating overseas, and subtracts foreign-owned production within the U.S.
- **Contrast with GDP**:
  - GDP = production **within borders**
  - GNP = production **by nationals**

---

## 🔹 INDPRO — Industrial Production Index

- **Definition**: Measures real output of the manufacturing, mining, and electric and gas utilities industries.
- **Base Year**: Indexed to 100 for a specified year
- **Source**: Federal Reserve Board
- **Methodology**:
  - Uses production data from firms, adjusted for seasonality and estimated output changes.
  - Captures real (inflation-adjusted) changes in **physical output**, not value.

---

## 🔹 IPMAN — Manufacturing Production Index

- **Definition**: Subcomponent of INDPRO; measures real output specifically within the **manufacturing** sector.
- **Scope**: Durable and nondurable goods
- **Importance**:
  - High-frequency indicator of cyclical activity
  - Sensitive to shifts in inventories, supply chains, and export demand

---

## 📁 File Naming Convention

Each dataset is saved in `/data/raw/real-economy/` as:
- `GDPC1.csv`
- `GDP.csv`
- `GNP.csv`
- `INDPRO.csv`
- `IPMAN.csv`

Each file includes:
- `Date`: Quarterly period (end of quarter)
- `Value`: Series measurement in either chained dollars or index format