# MoMo Top-up User Behavior Analysis

## Project Overview

This project analyzes **top-up transactions on the MoMo e-wallet platform** to identify **user behavior patterns and transaction trends**.

The analysis transforms raw transaction data into structured **analytics-ready datasets (data marts)** to support behavioral insights and dashboard visualization.

The project follows a typical **data analytics workflow** including data exploration, data cleaning, feature engineering, and analytics mart construction.

---
Dashboard Preview

[Dashboard](/Dashboard)
---
Insight Preview

[Reports](/Reports/Insights.md)
---
## Project Objectives

* Understand **user top-up behavior**
* Identify **transaction patterns**
* Analyze **monthly transaction performance**
* Build **analytics datasets for dashboard visualization**

---

## Analytics Pipeline

| Stage                   | Description                                                         | Notebook                        |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------- |
| Data Understanding      | Explore dataset structure, inspect missing values, detect anomalies | `data_understanding.ipynb`      |
| Data Cleaning           | Handle missing values, fix inconsistencies, correct data types      | `data_cleaning.ipynb`           |
| Feature Engineering     | Create analytical features such as revenue and behavioral metrics   | `feature_engineering.ipynb`     |
| Analytics Mart Building | Transform processed data into datasets for visualization            | `building_analytics_mart.ipynb` |

---

## Project Structure

```
Momo case study/
│
├── README.md
│
├── Data/
│   ├── raw/
│   │   ├── momo_top_up.xlsx
│   │   └── questions.xlsx
│   │
│   ├── processed/
│   │   ├── df_transactions.csv
│   │   ├── df_users.csv
│   │   ├── df_products.csv
│   │   └── final.csv
│   │
│   └── mart/
│       ├── mart_behavior.csv
│       ├── mart_merchant.csv
│       ├── mart_cohort.csv
│       ├── mart_revenue.csv
│       └── mart_growth.csv
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_analysis_revenue.ipynb
│   └── 05_building_analytics_mart.ipynb
│
│
├── reports/
│   ├── figures/
│   │   ├── revenue_by_month.png
│   │   ├── revenue_by_merchant.png
│   │   └── proxy_purchase_ratio.png
│   │
│   └── momo_topup_insights.pdf
│
├── dashboards/
│   └── momo_topup_dashboard.pbix
│
├── .gitignore
└── .venv/
```

---

## Data Architecture

The project follows a layered analytics structure:

| Layer          | Description                                |
| -------------- | ------------------------------------------ |
| Raw Data       | Original transaction dataset               |
| Clean Data     | Data after preprocessing and validation    |
| Feature Layer  | Engineered features for analysis           |
| Analytics Mart | Aggregated datasets used for BI dashboards |

---

## Key Analytical Focus

The analysis focuses on identifying:

* **User transaction frequency**
* **Top-up behavior patterns**
* **Monthly transaction trends**
* **Revenue distribution**
* **User segmentation**

---

## Key Metrics
| Metric                    | Description                             |
| ------------------------- | --------------------------------------- |
| Total Transactions        | Total number of top-up transactions     |
| Total Revenue             | Revenue generated from transactions     |
| Average Order Value (AOV) | Average value per transaction           |
| Transaction Frequency     | Average number of transactions per user |
| Active Users              | Number of users performing transactions |

---

## Tools & Technologies

* Python
* Pandas
* Jupyter Notebook
* Power BI

---



---
