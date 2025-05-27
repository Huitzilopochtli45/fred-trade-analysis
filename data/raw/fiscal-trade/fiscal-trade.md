# 📘 Fiscal & Trade Series — Definitions & Methodology

This document describes the quarterly macroeconomic indicators stored in `/data/raw/fiscal-trade`. These series represent core components of government fiscal activity and international trade flows, helping explain the public sector’s influence on the economy and the nation's global trade balance.

---

## 🏛️ FGEXPND — Federal Government Expenditures

- **Definition**: Total outlays by the U.S. federal government, including discretionary, mandatory, and interest payments.
- **Units**: Billions of current dollars
- **Source**: Bureau of Economic Analysis (BEA)
- **Methodology**:
  - Includes defense, healthcare, Social Security, infrastructure, and debt service.
  - Seasonally adjusted and reported quarterly.
- **Importance**:
  - Proxy for fiscal stimulus or austerity
  - Commonly analyzed relative to GDP

---

## 🧾 FGRECPT — Federal Government Receipts

- **Definition**: Total revenue collected by the federal government, primarily through taxes.
- **Units**: Billions of current dollars
- **Components**:
  - Individual and corporate income taxes
  - Social insurance contributions
  - Excise and customs duties
- **Economic Use**:
  - Together with expenditures, defines the federal **budget balance** or deficit.

---

## 🌐 EXPGSC1 — Real Exports of Goods and Services

- **Definition**: Inflation-adjusted value of goods and services sold to foreign residents.
- **Units**: Billions of chained 2017 dollars
- **Use**:
  - Measures external demand for U.S. output
  - Sensitive to exchange rates, global growth, and trade policy
- **Real Term Adjustment**: Removes price-level changes to focus on physical volume

---

## 🚢 IMPGSC1 — Real Imports of Goods and Services

- **Definition**: Inflation-adjusted value of goods and services purchased from abroad.
- **Units**: Billions of chained 2017 dollars
- **Use**:
  - Reflects U.S. domestic demand for foreign goods
  - Key input in calculating **net exports**:
    \[
    \\text{Net Exports} = \\text{Exports} - \\text{Imports}
    \]
- **Macro Relevance**:
  - Directly affects GDP via subtraction from output
  - Indicates trade deficits/surpluses over time

---

## 📁 File Naming Convention

- `FGEXPND.csv` – Government spending
- `FGRECPT.csv` – Government revenue
- `EXPGSC1.csv` – Real exports
- `IMPGSC1.csv` – Real imports

Each file contains:
- `Date`: Quarter-end timestamp
- `Value`: Series value in billions of dollars (nominal or chained)

---

## ✅ Use Cases

These series support analysis of:
- Fiscal stance (deficit/surplus)
- Government stimulus timing
- Trade-driven GDP fluctuations
- Global exposure of U.S. demand and output
