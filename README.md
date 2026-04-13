# MoMo Top-up User Behavior Analysis

## Project Overview

This project analyzes **MoMo top-up transactions** to understand **user behavior, transaction patterns, and revenue distribution**.

Instead of focusing only on high-level KPIs, the analysis is driven by **business questions**, aiming to explain:
- What drives transaction growth?
- How users distribute spending across top-up amounts?
- Where revenue concentration comes from?

The project transforms raw data into **analytics-ready data marts** using **Python (Pandas)**, designed for **Power BI visualization and business storytelling**.

---

## Business Objectives

The analysis is structured around key business problems:

- Understand how users behave when topping up  
- Identify drivers of growth (frequency vs. transaction value)  
- Analyze revenue concentration across users and amount tiers  
- Evaluate distribution of top-up amounts  
- Support data-driven storytelling via dashboards  

---

## Key Business Insights

- **Revenue Concentration:** A small group of users contributes a disproportionately large share of revenue → strong dependency on high-value users  
- **Stable Ticket Size:** Average top-up amount remains relatively stable → growth is mainly driven by **transaction frequency**, not basket size  
- **Amount Distribution:** Transactions are heavily concentrated in fixed denominations (10K, 20K, 50K, 100K) → reflects strong user habits and product design influence  
- **Seasonality:** Transaction volume increases toward year-end → likely driven by campaigns and seasonal demand  

Detailed explanation is provided in the Insights Report.

---

## Key Analytical Questions

### 1. Growth Drivers
- Is revenue growth driven by more users, higher frequency, or higher spending per transaction?
- Are users becoming more active over time?

### 2. User Behavior
- How frequently do users top up?
- Are there distinct behavioral segments?

### 3. Amount Distribution
- Which top-up amounts dominate transaction volume?
- Do users prefer fixed denominations?
- How does each amount contribute to:
  - % of transactions
  - % of revenue

### 4. Revenue Concentration
- How concentrated is revenue across users?
- Do a small number of users drive most of the revenue?

### 5. Monthly Trends
- How do transactions and revenue evolve over time?
- Are there seasonal or campaign-driven spikes?

---

## Analytics Approach

The project follows a **data mart-driven approach**, where each mart answers a specific business question:

- **User Mart** → user behavior & frequency  
- **Monthly Mart** → growth trends  
- **Amount Distribution Mart** → transaction & revenue distribution by top-up value  
- **Revenue Distribution Mart** → concentration analysis  

All marts are optimized for **Power BI dashboards**.

---

## Analytics Pipeline

| Stage | Description | Notebook |
|------|------------|----------|
| Data Understanding | Explore structure, detect anomalies | `01_data_understanding.ipynb` |
| Data Cleaning | Fix missing values, standardize data | `02_data_cleaning.ipynb` |
| Feature Engineering | Create behavioral & revenue features | `03_feature_engineering.ipynb` |
| Analytics Mart | Build datasets for BI & analysis | `04_building_analytics_mart.ipynb` |

---

## Project Structure
```
momo_topup_analysis/
│
├── Dashboard/
│ ├── visualization.pbix
│ └── visualization.pdf
│
├── Data/
│ ├── raw/
│ ├── processed/
│ └── mart/
│
├── Notebooks/
│ ├── 01_data_understanding.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_feature_engineering.ipynb
│ └── 04_building_analytics_mart.ipynb
│
├── Reports/
│ └── Insights.md
│
└── README.md
```

---

## Data Architecture

| Layer | Description |
|------|------------|
| Raw Data | Original transaction data |
| Clean Data | Preprocessed & validated data |
| Feature Layer | Behavioral & revenue features |
| Analytics Mart | Aggregated datasets for BI |

---

## Core Metrics

- Total Transactions  
- Total Revenue  
- Average Order Value (AOV)  
- Transactions per User  
- Active Users  

> Metrics are used to support analysis, not as the final output.

---

## Tech Stack

- Python (Pandas)  
- Jupyter Notebook  
- Power BI  
