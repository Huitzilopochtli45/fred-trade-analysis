# 📘 Housing & Capacity Series — Definitions & Methodology

This document explains the quarterly macroeconomic indicators stored in `/data/raw/housing-capacity`. These indicators measure activity in the residential construction sector and the broader capacity utilization of U.S. industry. Together, they reflect physical expansion, cyclical demand, and production constraints across the economy.

---

## 🏠 HOUST — Housing Starts (Total)

- **Definition**: The number of new privately-owned housing units on which construction has started during the reported period.
- **Units**: Thousands of units (seasonally adjusted annual rate)
- **Source**: U.S. Census Bureau
- **Methodology**:
  - Includes single-family homes and multi-family structures (5+ units).
  - Seasonally adjusted and annualized.
- **Importance**:
  - Leading indicator of economic activity
  - Sensitive to interest rates, credit markets, and consumer confidence
  - Strongly cyclical — tends to fall before recessions

---

## 🧱 PERMIT — Building Permits

- **Definition**: The number of new privately-owned housing units authorized by building permits.
- **Units**: Thousands of units (seasonally adjusted annual rate)
- **Economic Role**:
  - Forward-looking indicator for housing construction
  - Correlates with future starts and completions
  - Reacts to mortgage rates and regulatory policy

---

## 🏭 TCU — Capacity Utilization (Total Industry)

- **Definition**: The percentage of industrial capacity that is currently being used.
- **Scope**: Manufacturing, mining, utilities
- **Units**: Percent (%)
- **Source**: Federal Reserve Board
- **Interpretation**:
  - High TCU (80–85%) may signal inflation pressure due to demand > supply
  - Low TCU indicates slack in the industrial sector
  - Used in productivity and inflation modeling

---

## 📁 File Naming Convention

- `HOUST.csv` — Housing Starts
- `PERMIT.csv` — Building Permits
- `TCU.csv` — Capacity Utilization

Each file includes:
- `Date`: End-of-quarter period
- `Value`: Measurement in thousands of units or percent

---

## ✅ Use Cases

These series are used for:
- Monitoring business cycle turning points
- Forecasting investment in residential structures
- Identifying overheating or underutilization in industrial production