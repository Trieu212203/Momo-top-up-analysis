import json

filepath = r"C:\Users\ASUS\Documents\Project\Momo case study\Notebooks\building_analytics_mart.ipynb"

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
new_cells.append(create_md_cell("# 📊 Building Analytics Mart\n\nThis notebook processes the integrated dataset to create various analytics focus areas (Marts)."))

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell.get('source', []))
        if "import pandas as pd" in source:
             new_cells.append(create_md_cell("## 1. Setup & Initialization\n\nImporting libraries and defining paths to the processed transaction data."))
        elif "df['Date'] = pd.to_datetime" in source:
             new_cells.append(create_md_cell("## 2. Data Type Optimization\n\nEnsuring all date columns are in datetime format and optimizing categorical columns to reduce memory footprint."))
        elif "df['month'] = df['Date'].dt.to_period" in source:
             new_cells.append(create_md_cell("## 3. Time Feature Extraction\n\nExtracting month and year for periodic analysis."))
        elif "mart_growth =" in source:
             new_cells.append(create_md_cell("## 4. Growth Analytics Mart\n\nCalculating active users, new users, and current users per month to track platform growth."))
        elif "mart_revenue =" in source:
             new_cells.append(create_md_cell("## 5. Revenue Analytics Mart\n\nAnalyzing financial metrics including Average Order Value (AOV), Revenue per User, and Take Rate."))
        elif "mart_merchant =" in source:
             new_cells.append(create_md_cell("## 6. Merchant Performance Mart\n\nAggregating users and revenue by merchant to identify top-performing partners."))
        elif "mart_behavior =" in source:
             new_cells.append(create_md_cell("## 7. User Behavior Mart\n\nSegmenting data by demographics (Location, Gender, Age) and user type to understand behavior patterns."))
        elif "mart_cohort =" in source:
             new_cells.append(create_md_cell("## 8. Cohort Analysis Mart\n\nTracking user retention by comparing the month of their first transaction with subsequent activity months."))
        elif "output_dir =" in source:
             new_cells.append(create_md_cell("## 9. Data Persistence\n\nCreating the mart directory and exporting all processed analytics marts to CSV files for visualization."))

    new_cells.append(cell)

nb['cells'] = new_cells

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")

print("Successfully injected Markdown cells into building_analytics_mart.ipynb")
