# 📘 Consumption & Savings Series — Definitions & Methodology

This document explains the quarterly macroeconomic indicators stored in `/data/raw/consumption-savings`. These series reflect household consumption behavior, savings patterns, and income after taxes — all central to understanding demand-side drivers in the economy.

---

## 🛍️ PCECC96 — Real Personal Consumption Expenditures (Chained 2017 Dollars)

- **Definition**: Inflation-adjusted total spending by individuals on goods and services.
- **Source**: Bureau of Economic Analysis (BEA)
- **Methodology**:
  - Uses chain-weighted price indices to eliminate inflation effects.
  - Includes both durable (e.g., vehicles) and nondurable (e.g., food) goods, and services.
- **Units**: Billions of chained 2017 dollars
- **Importance**: The largest component of real GDP.

---

## 💵 PCEC — Nominal Personal Consumption Expenditures

- **Definition**: Total household spending measured in current dollars (not adjusted for inflation).
- **Use**: Helps assess inflationary trends when compared to real PCE (i.e., PCE deflator).
- **Units**: Billions of dollars
- **Economic Role**:
  - Measures effective consumer demand
  - Responds to shifts in employment, wages, credit access

---

## 🏦 PSAVERT — Personal Savings Rate

- **Definition**: Percent of disposable income not spent on consumption.
- **Formula**:
  \[
  \\text{Savings Rate} = \\frac{\\text{Disposable Personal Income} - \\text{PCE}}{\\text{Disposable Personal Income}} \\times 100
  \]
- **Units**: Percent (%)
- **Signals**:
  - High values → consumer caution, deleveraging
  - Low values → expansionary spending, optimism (or stress)

---

## 🧾 DSPIC96 — Real Disposable Personal Income (Chained 2017 Dollars)

- **Definition**: After-tax income adjusted for inflation.
- **Components**:
  - Total personal income
  - Minus: personal current taxes
- **Importance**:
  - Drives future consumption capacity
  - Used in savings and debt models

---

## 📁 File Naming Convention

- `PCECC96.csv` – Real PCE
- `PCEC.csv` – Nominal PCE
- `PSAVERT.csv` – Savings Rate
- `DSPIC96.csv` – Real Disposable Income

Each file includes:
- `Date`: End-of-quarter timestamp
- `Value`: Series value in either chained 2017 dollars, nominal dollars, or percent

---

## ✅ Use Cases

These variables enable:
- Real vs nominal consumption growth comparisons
- Marginal propensity to consume/saving analysis
- Consumption-led GDP decomposition
- Pre-recession household behavior studies