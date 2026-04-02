import pandas as pd

# Load relational files from the simulator
sales = pd.read_csv("../data/raw_sales_logs_vast.csv")
products = pd.read_csv("../data/product_catalog.csv")
customers = pd.read_csv("../data/customer_segments.csv")

print("Merging relational datasets into the SALES GROWTH MASTER...")

# 1. Merge Sales with Customer Segments (Sales already has product info)
master = sales.merge(customers, on='Customer_ID', how='left')

# 3. Enhanced Feature Engineering
master['Order_Date'] = pd.to_datetime(master['Order_Date'])
master['Profit_Margin'] = (master['Net_Profit'] / master['Gross_Sales']).round(4)
master['Is_Weekend'] = master['Order_Date'].dt.dayofweek >= 5

# Export to a clean Flat File
master.to_csv("../data/sales_growth_master.csv", index=False)

print("Sales Growth Master Complete: '../data/sales_growth_master.csv' (150k rows) is ready.")
