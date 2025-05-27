# 📘 Bond Market Yield Series — Definitions & Methodology

This document describes the interest rate series saved under `/data/raw/bond-market/`. These represent the yields on U.S. Treasury securities at various maturities and serve as benchmarks for credit markets, monetary policy, and yield curve analysis.

---

## 📊 What Are Treasury Yields?

Treasury yields reflect the return investors demand to hold U.S. government debt over different maturities. They are expressed as **annualized interest rates** and vary based on:
- Duration (term)
- Inflation expectations
- Federal Reserve policy
- Market risk appetite

---

## 📈 GS1 — 1-Year Treasury Constant Maturity Rate
- Short-term interest rate, aligned closely with Fed policy actions.

## 📈 GS2 — 2-Year Treasury Constant Maturity Rate
- Tracks expectations of near-term rate changes and inflation.
- Commonly used in yield curve slope comparisons (e.g., 10Y-2Y).

## 📈 GS3 — 3-Year Treasury Constant Maturity Rate
- Transitional mid-short term rate, less volatile than GS1 or GS2.

## 📈 GS5 — 5-Year Treasury Constant Maturity Rate
- Influenced by inflation outlook and Fed guidance over medium horizons.

## 📈 GS10 — 10-Year Treasury Constant Maturity Rate
- Benchmark for long-term rates; influences mortgage and loan rates.

## 📈 GS20 — 20-Year Treasury Constant Maturity Rate
- Long-duration yield with applications in infrastructure financing.

## 📈 GS30 — 30-Year Treasury Constant Maturity Rate
- Longest-term benchmark; critical for pensions and fixed income hedging.

---

## 📁 File Naming Convention

Each CSV is named after its FRED series code:
- `GS1.csv`
- `GS2.csv`
- `GS3.csv`
- `GS5.csv`
- `GS10.csv`
- `GS20.csv`
- `GS30.csv`

Each file contains:
- `Date`: Quarter-end timestamp
- `Value`: Yield (% annualized)

---

## ✅ Use Cases

- Yield curve construction and slope analysis
- Macro-financial modeling of term structure
- Market expectations of inflation and Fed policy
- Duration targeting and interest rate risk assessment