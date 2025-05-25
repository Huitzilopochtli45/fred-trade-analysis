# 📊 Trade Policy Impact Analysis: Tariffs & Macroeconomic Response

### 🔍 Purpose

This project aims to analyze the economic impact of U.S. tariff policy over time — particularly during key historical inflection points of protectionism or isolationism. Our goal is to explore how increases in effective tariff rates influenced GDP subcomponents, trade balance, inflation, interest rates, and broader macroeconomic behavior.

We'll also examine the **lag time** between tariff changes and their downstream effects — capturing both short- and long-term economic responses.

---

## 🧭 Project Roadmap

### ✅ Step 1: Gather Historical Tariff Data
- Add time series data for **effective tariff rates**, ideally quarterly or annual.
- Identify and annotate **major policy shifts**, such as:
  - Smoot-Hawley Tariff Act (1930s)
  - 1980s Japan-related restrictions
  - Trump-era Trade War (2018–2019)
- Possible series to consider:
  - World Bank effective tariff rate
  - BEA customs duties as a share of imports
  - Manually created event markers

---

### ✅ Step 2: Align Macro Series for Comparison

Already collected:
- Real GDP (`GDP`)
- Net Exports (`NETEXP`)
- Exports (`EXPGS`)
- Imports (`IMPGS`)
- Government Spending (`GCEC96`)
- Personal Savings (`W875RX1`)
- Personal Consumption (`PCE`)

To add next:
- **Inflation**: `CPIAUCSL`, `PCEPI`
- **Bond Market**: `GS10` (10-Year Treasury Yield)
- **Labor Market**: `UNRATE` (Unemployment), `PAYEMS` (Nonfarm Payrolls)
- **Industrial Output**: `INDPRO`

---

### ✅ Step 3: Detect Deviations from Trend
- Calculate **rolling averages** and **moving standard deviations**
- Apply **detrending methods** (e.g., HP filter, linear residuals)
- Analyze behavior **pre- and post-tariff events**
- Plot macro series in ±12 quarter windows around each event

---

### ✅ Step 4: Quantify Economic Response
- Cross-correlation analysis (lags between tariff changes and GDP/trade/inflation)
- Rolling correlations to examine time-varying relationships
- First-difference and percentage-change transformations
- Build regression models:
  - `GDP ~ Tariff_Event_Dummy + Consumption + Net_Exports + Gov_Spending`
  - `Net_Exports ~ Tariff_Rate (lagged)`

---

## 🔬 In Progress

- [x] Combined and saved core macroeconomic series to `data/combined_macro.csv`
- [x] Notebook exploration of GDP structure complete
- [x] Reusable plot script with auto-export to `outputs/`
- [ ] Add tariff rate data and annotate major policy events
- [ ] Begin visual alignment of macro response to trade policy shocks
- [ ] Begin correlation and lag structure analysis

---

## 🧠 Guiding Questions

- Do protectionist tariffs reliably precede GDP slowdowns or trade contraction?
- How long is the lag between tariff increases and observable inflation or bond market stress?
- Are certain subcomponents of GDP (e.g. Net Exports or Consumption) more sensitive to tariffs?
- Can we statistically detect a structural break during trade war periods?

---

## 🧰 Tools Used

- Python (Pandas, Matplotlib, Statsmodels)
- Jupyter for interactive exploration
- FRED API for real-time economic data
- Conda-managed environment (`fred-trade`)

---

## 🗂 Directory Snapshot

