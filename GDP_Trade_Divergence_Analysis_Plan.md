
# 📘 GDP Divergence and Trade Dynamics Analysis Plan

This file outlines the current status and strategic next steps for analyzing the divergence between Real and Nominal GDP, with the goal of exploring trade policy, net exports, and macroeconomic relationships over time.

---

## ✅ Current Progress

We have:
- Imported and cleaned Real GDP (`GDPC1`) and Nominal GDP (`GDPCA`) datasets.
- Merged and aligned quarterly data from 1947 onward.
- Calculated **% divergence** between Nominal and Real GDP to reflect inflationary distortions.
- Identified the top and bottom 10 periods of divergence.
- Reviewed historical events surrounding those divergence spikes.

---

## 🎯 Strategic Next Moves

### 1. 📦 Incorporate Net Exports

- Load FRED-based exports and imports data.
- Compute:
  - `Net_Exports = Exports - Imports`
  - `Net_Export_Change = Net_Exports.diff()`
  - `Net_Export_Share = Net_Exports / Nominal_GDP`
- Examine relationship between net export patterns and GDP divergence.

---

### 2. 🚩 Overlay Tariff Events

- Load `TARIFF_EVENTS_CLEANED.csv`
- Add event markers to plots.
- Investigate effects of:
  - New tariffs
  - Tariff hikes
  - Lags post-tariff changes (e.g., 2–6 quarters)

---

### 3. 📊 Regression and Correlation Analysis

- Calculate correlations, e.g.:
  ```python
  from scipy.stats import pearsonr
  pearsonr(merged_df['Divergence_%'], merged_df['Net_Export_Share'])
  ```
- Use linear regression to explore:
  - Trade policy intensity
  - Net export shifts
  - Lagged relationships

---

### 4. 📈 Visual Storytelling

Create these plots:
- Line chart: **Divergence_% over time** with shaded tariff events
- Bar/Line combo: **Net Export Share vs. GDP Divergence**
- Scatter: **Net Export Change vs. Divergence_%**

---

### 5. 🧭 Historical Period Categorization

Segment into macroeconomic regimes:
| Period        | Context                        |
|---------------|--------------------------------|
| 1947–1971     | Bretton Woods, postwar boom    |
| 1971–1985     | Inflation, oil crises          |
| 1985–2001     | Globalization surge            |
| 2001–2008     | China WTO, trade deficits      |
| 2008–2020     | GFC recovery, QE               |
| 2020–2023     | COVID, trade war, reshoring    |

Evaluate if divergence patterns shift across periods.

---

## 🧰 Next Steps (Choose Path)

You may now:
- 🔍 Ingest and align net export data
- 📌 Merge and analyze tariff policy shifts
- 📊 Visualize relationships
- 🧪 Run statistical/regression tests

