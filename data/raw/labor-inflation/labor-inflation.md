# 📘 Labor & Inflation Series — Definitions & Methodology

This document describes the macroeconomic indicators under `/data/raw/labor-inflation`. These series reflect labor market strength, participation trends, and inflation pressures — key to understanding the dual mandate of the Federal Reserve and the behavior of consumers and wages over time.

---

## 👷 UNRATE — Unemployment Rate

- **Definition**: Percentage of the labor force that is jobless, actively seeking employment, and available to work.
- **Source**: Bureau of Labor Statistics (BLS)
- **Frequency**: Monthly (averaged to quarterly)
- **Methodology**:
  - Calculated as:
    \[
    \\text{Unemployment Rate} = \\frac{\\text{Unemployed Persons}}{\\text{Labor Force}} \\times 100
    \]
  - Based on the **Current Population Survey (CPS)** of households.

---

## 👥 CIVPART — Labor Force Participation Rate

- **Definition**: Percentage of the working-age population that is either employed or actively seeking work.
- **Interpretation**: Indicates potential labor supply and structural shifts in employment dynamics (e.g., aging, education, care roles).
- **Formula**:
  \[
  \\text{Participation Rate} = \\frac{\\text{Labor Force}}{\\text{Civilian Population}} \\times 100
  \]

---

## 💵 CPIAUCSL — Consumer Price Index (All Urban Consumers)

- **Definition**: A price index that measures the average change over time in the prices paid by urban consumers for a basket of goods and services.
- **Scope**: All items, not seasonally adjusted
- **Use**: Core measure of inflation
- **Base Year**: Index, normalized to 100 for a given base period
- **Note**: Influences cost-of-living adjustments, real wage calculations, and inflation expectations.

---

## 📈 PCEPI — Personal Consumption Expenditures Price Index

- **Definition**: A broader inflation measure than CPI, reflecting changes in prices paid by consumers for goods and services.
- **Source**: Bureau of Economic Analysis (BEA)
- **Methodology**:
  - Chain-type index
  - More dynamically updated than CPI
  - Includes healthcare spending via third parties
- **Use by Fed**: Preferred inflation gauge for monetary policy targets (e.g., 2% inflation)

---

## 📁 File Naming Convention

Each dataset is saved in `/data/raw/labor-inflation/` as:
- `UNRATE.csv`
- `CIVPART.csv`
- `CPIAUCSL.csv`
- `PCEPI.csv`

Each CSV includes:
- `Date`: Quarterly end date
- `Value`: Series measurement (percent or index)

---

## ✅ Use Cases

These indicators are key inputs for:
- NAIRU estimation
- Real wage analysis
- Inflation-adjusted metrics
- Phillips Curve modeling
- Monetary policy simulations

