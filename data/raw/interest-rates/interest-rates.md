# 📘 Interest Rate Series — Definitions & Methodology

This document describes the macroeconomic interest rate indicators located in `/data/raw/interest-rates`. These series represent foundational benchmarks in U.S. monetary and capital markets, influencing everything from consumer lending to government borrowing and corporate investment.

---

## 💰 FEDFUNDS — Effective Federal Funds Rate

- **Definition**: The interest rate at which depository institutions trade federal funds (balances held at the Federal Reserve) with each other overnight.
- **Source**: Federal Reserve Board
- **Units**: Percent (annualized)
- **Type**: Market rate — not set directly by the Fed, but guided by target ranges.
- **Role in Policy**:
  - Main tool for Federal Reserve open market operations
  - Impacts inflation control, unemployment, and short-term economic activity
  - Often used to compare with inflation to assess real rates

---

## 🏦 GS10 — 10-Year Treasury Constant Maturity Rate

- **Definition**: Yield on U.S. Treasury securities with a 10-year term, adjusted to constant maturity.
- **Units**: Percent (annualized)
- **Use**:
  - Benchmark for mortgage rates, student loans, corporate bonds
  - Reflects long-run inflation expectations and risk appetite
- **Calculation**:
  - Derived by averaging yields of actively traded Treasury securities to approximate a 10-year term structure.
- **Importance**:
  - Acts as a proxy for long-term interest rate environment
  - Used in yield curve analysis and monetary policy effectiveness

---

## 📁 File Naming Convention

- `FEDFUNDS.csv` — Fed Funds Rate (quarterly average)
- `GS10.csv` — 10-Year Treasury Rate (quarterly average)

Each file contains:
- `Date`: End of quarter
- `Value`: Interest rate as a percentage

---

## ✅ Use Cases

These interest rate indicators support:
- Yield curve slope analysis
- Real interest rate construction (e.g., Fed Funds – Inflation)
- Monetary stance classification (tight, neutral, accommodative)
- Bond pricing and investment return expectations