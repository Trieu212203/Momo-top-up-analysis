# MoMo Top-up User Behavior Analysis

## Project Overview

This project analyzes **top-up transactions on the MoMo e-wallet platform** to identify **user behavior patterns and transaction trends**.

The analysis transforms raw transaction data into structured **analytics-ready datasets (data marts)** to support behavioral insights and dashboard visualization.

The project follows a typical **data analytics workflow** including data exploration, data cleaning, feature engineering, and analytics mart construction.

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
│
├── Notebooks/
│   ├── data_understanding.ipynb
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   └── building_analytics_mart.ipynb
│
├── Reports/
│   └── Reports.md
│
├── Dashboard/
│   ├── Merchant_analysis.png
│   ├── Monthly_performance.png
│   ├── User_behavior.png
│   ├── visualization.pbix
│   └── visualization.pdf
│
├── .gitignore
└── .venv/
```

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
