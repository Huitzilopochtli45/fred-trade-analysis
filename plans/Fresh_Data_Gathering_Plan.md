
# 📘 Phase 1: Fresh Macroeconomic Data Gathering Plan

This plan outlines a complete restart of the macroeconomic data pipeline, focused on clean, quarterly-aligned acquisition from reliable FRED sources. The goal is to create a consistent and comprehensive dataset for economic analysis from Q1 1972 to present.

---

## 🎯 Objective

To build a clean, extensible macroeconomic dataset from scratch using quarterly FRED series covering real output, inflation, labor, trade, fiscal policy, consumption, housing, and interest rates.

---

## 📦 Data Domain Categories & Target Series

### 🏭 Real Economy
| Description                  | FRED Code |
|------------------------------|-----------|
| Real GDP (Chained 2017 $)    | `GDPC1`   |
| Nominal GDP                  | `GDP`     |
| Real GNP                     | `GNPCA`   |
| Industrial Production Index  | `INDPRO`  |
| Manufacturing Production     | `IPMAN`   |

### 👷 Labor & Inflation
| Description                     | FRED Code  |
|----------------------------------|------------|
| Unemployment Rate               | `UNRATE`   |
| Labor Force Participation Rate  | `CIVPART`  |
| Consumer Price Index (CPI-U)    | `CPIAUCSL` |
| PCE Price Index                 | `PCEPI`    |

### 🌍 Fiscal & Trade
| Description                          | FRED Code  |
|---------------------------------------|------------|
| Federal Government Expenditures      | `FGEXPND`  |
| Federal Government Receipts          | `FGRECPT`  |
| Real Exports of Goods and Services   | `EXPGSC1`  |
| Real Imports of Goods and Services   | `IMPGSC1`  |

### 🛒 Consumption & Savings
| Description                         | FRED Code  |
|--------------------------------------|------------|
| Real Personal Consumption Expenditures | `PCECC96` |
| Nominal Personal Consumption          | `PCEC`     |
| Personal Savings Rate                 | `PSAVERT`  |
| Real Disposable Personal Income       | `DSPIC96`  |

### 🏠 Housing & Capacity
| Description                  | FRED Code |
|------------------------------|-----------|
| Housing Starts               | `HOUST`   |
| Building Permits             | `PERMIT`  |
| Capacity Utilization         | `TCU`     |

### 💰 Interest Rates
| Description                     | FRED Code  |
|----------------------------------|------------|
| Effective Fed Funds Rate        | `FEDFUNDS` |
| 10-Year Treasury Yield          | `GS10`     |

---

## 🧭 Workflow Plan

1. **Pull Data**: Use `fredapi` to fetch each series
2. **Resample**: Ensure quarterly frequency
3. **Trim**: Cut to `1972-03-31` start for consistent coverage
4. **Save**:
   - Each series to individual CSV
   - Optionally consolidate to multi-tab Excel
5. **Directory Layout**:
   - `/data/raw` — original FRED pulls
   - `/data/quarterly` — trimmed & cleaned quarterly data

---

## ✅ Deliverables

- Raw and resampled data files per series
- Consistent `Date` column (quarter-end)
- Fully aligned datasets for master table merge

---

## 🧱 Next Step

Generate the data collection script to fetch, resample, and organize all listed series.
