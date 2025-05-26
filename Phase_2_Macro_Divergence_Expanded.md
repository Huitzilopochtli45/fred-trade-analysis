
# 📘 Phase 2: Exploring Broader Macroeconomic Drivers of GDP Divergence and Trade Dynamics

This document outlines the next stage in analyzing U.S. economic divergence, expanding beyond basic trade imbalance into deeper macroeconomic dynamics. The goal is to uncover structural and temporal relationships between:

- GDP divergence (Nominal vs. Real)
- Net export **growth rates** or **change patterns**
- Key macroeconomic indicators like interest rates, fiscal policy, and consumption behavior

---

## ✅ Objective

To explore how **GDP divergence** and **Net Export changes** are influenced by broader macroeconomic forces such as:
- GDP and GNP growth rates
- Government fiscal policy (spending, receipts, and deficits)
- Interest rate trends
- Inflation metrics
- Personal savings and consumption shifts

---

## 📦 Key Data Sources (via FRED API)

| Domain                      | FRED Series ID     | Notes                                |
|-----------------------------|--------------------|--------------------------------------|
| Real GDP                    | GDPC1              | Already processed                    |
| Nominal GDP                 | GDPCA              | Already processed                    |
| Gross National Product      | GNPCA              | Nominal GNP                          |
| Net Exports (Growth Rate)   | Derived            | From EXPGSCA - IMPGSCA               |
| Fed Funds Rate              | FEDFUNDS           | Daily → resample quarterly           |
| 10-Year Treasury Yield      | GS10               | Monthly or daily → resample          |
| CPI-U (Inflation)           | CPIAUCSL           | Consumer inflation index             |
| PCE Price Index             | PCEPI              | Core inflation index                 |
| Federal Outlays             | FYONGDA188S        | Government spending                  |
| Federal Receipts            | FYFRGDA188S        | Government revenue                   |
| Personal Saving Rate        | PSAVERT            | % of disposable income               |
| Real Consumption (PCE)      | PCECC96            | Chained 2012 dollars                 |
| Nominal Consumption (PCE)   | PCEC               | Nominal dollars                      |

---

## 🔧 Step-by-Step Workflow

### Step 1: Data Collection and Preprocessing
- Pull each series from FRED using `fredapi`
- Convert daily/monthly to quarterly where needed
- Calculate:
  - GDP and GNP growth rates
  - Net Export **growth rate** or **absolute change**
  - Government Deficit = Outlays - Receipts
  - Deficit-to-GDP ratio
  - Real vs. Nominal PCE delta

---

### Step 2: Merge With Master Divergence Table
- Align all macro series by date
- Merge with GDP divergence and Net Export Share/Change
- Normalize and clean for correlation testing

---

### Step 3: Exploratory Analysis
- Run **correlation** and **regression** analysis
- Visualize:
  - Time series overlays
  - Lagged scatter plots
  - Correlation heatmaps
- Identify:
  - Structural breaks
  - Regime inflection points
  - High-impact episodes

---

### Step 4: Regime-Specific Analysis
Segment the data by historical periods:
- Bretton Woods (1947–71)
- Inflation/Volcker (1971–85)
- Globalization Boom (1985–2001)
- China-WTO Expansion (2001–2020)
- COVID & Reshoring (2020–present)

Compare how **GDP divergence and Net Export dynamics** co-evolve with macro forces in each regime.

---

## 🎯 Goal

To develop a multi-dimensional understanding of how U.S. economic divergence and trade behavior reflect broader macro conditions. This phase aims to expose:
- The economic levers behind inflation distortions
- The fiscal/monetary backdrop to trade and growth cycles
- Regime-based behavioral shifts in GDP and GNP alignment

