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
momo-topup-analysis/
│
├── notebooks/
│   ├── data_understanding.ipynb
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   └── building_analytics_mart.ipynb
│
├── data/
│   ├── raw
│   └── processed
│
├── marts/
│   └── analytics_marts
│
└── README.md
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
* NumPy
* Jupyter Notebook
* Power BI

---

## Expected Insights

This analysis aims to uncover:

* How frequently users perform top-ups
* Transaction distribution over time
* Identification of high-value users
* Behavioral patterns among different user segments

---

## Author

Duy Nguyen
