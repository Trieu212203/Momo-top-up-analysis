import json

filepath = r"C:\Users\ASUS\Documents\Project\Momo case study\Notebooks\feature_engineering.ipynb"

with open(filepath, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Helper to create a markdown cell
def create_md_cell(content):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [content]
    }

new_cells = []
# Prepend header
new_cells.append(create_md_cell("# 🛠️ Feature Engineering & Data Integration\n\nThis notebook merges and prepares user, transaction, and product data for analysis."))

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell.get('source', []))
        if "import pandas as pd" in source:
             new_cells.append(create_md_cell("## 1. Import Libraries & Load Data\n\nWe start by loading pandas and defining the paths to our cleaned data sources."))
        elif "df_trans.duplicated('order_id').sum()" in source:
             new_cells.append(create_md_cell("## 2. Data Quality Checks\n\nChecking for duplicate transactions and users to ensure data integrity before merging."))
        elif "df_trans = df_trans.merge(" in source and "df_products" in source:
             new_cells.append(create_md_cell("## 3. Integrating Products & Revenue Calculation\n\nMerging the transactions array with product lookup data to calculate the actual revenue for each transaction, based on the percentage rate."))
        elif "df_trans['Date'] = pd.to_datetime" in source:
             new_cells.append(create_md_cell("## 4. Date Transformations & Temporal Features\n\nConverting `Date` and `First_tran_date` columns to standard datetime formats and calculating aggregates like the most profitable month and day."))
        elif "df_users.rename(columns={'User_id': 'user_id'}" in source:
             new_cells.append(create_md_cell("## 5. Integrating User Data\n\nUnifying the user ID column names to successfully join the transaction data with demographic information."))
        elif "df_trans_tx[\"Age\"] = df_trans_tx[\"Age\"].astype(\"category\")" in source:
             new_cells.append(create_md_cell("## 6. Feature Engineering: Categorization & User Type\n\nOptimizing data types by converting age ranges to categories. We also engineer a new feature, `Type_user`, which flags whether the transaction occurred in the same month as the user's first transaction (New vs Current user)."))
        elif "output_dir =" in source:
             new_cells.append(create_md_cell("## 7. Data Export\n\nSaving the integrated and transformed dataset into the processed data folder for further analysis or modeling."))

    new_cells.append(cell)

nb['cells'] = new_cells

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")

print("Successfully injected Markdown cells into feature_engineering.ipynb")
