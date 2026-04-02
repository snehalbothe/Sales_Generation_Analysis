import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Vibe Settings: 150,000 orders for a 'Vast' Sales Project
np.random.seed(42)
n_orders = 150000
n_products = 1000
n_customers = 5000

print(f"Baking a VAST Sales Generation dataset ({n_orders} orders) with Marketing ROI...")

# 1. Product Portfolio (The 'What')
categories = ["Electronics", "Fashion", "Home & Kitchen", "Fitness", "Beauty"]
prod_ids = [f"SKU-{2000 + i}" for i in range(n_products)]
base_costs = np.round(np.random.uniform(5.0, 500.0, n_products), 2)
margins = np.random.uniform(1.2, 2.5, n_products) 
prices = np.round(base_costs * margins, 2)

products_df = pd.DataFrame({
    "Product_ID": prod_ids,
    "Category": np.random.choice(categories, n_products),
    "Base_Cost": base_costs,
    "Unit_Price": prices
})

# 2. Marketing Channels (The 'How')
channels = ["Instagram_Ad", "Google_Search", "Affiliate", "Direct_Referral", "Email_Campaign"]
cpc_rates = [0.85, 1.20, 0.40, 0.20, 0.05] # Cost Per Click/Engagement
conversion_lift = [0.05, 0.08, 0.03, 0.15, 0.02]

# 3. Customer Segments (The 'Who')
segments = ["VIP", "Regular", "Discount_Seeker", "One_Time_Buyer"]
segment_probs = [0.1, 0.4, 0.3, 0.2]
cust_ids = [f"CUST-{30000 + i}" for i in range(n_customers)]
cust_df = pd.DataFrame({
    "Customer_ID": cust_ids,
    "Segment": np.random.choice(segments, n_customers, p=segment_probs)
})

# 4. Sales Transactions (The 'Money')
order_indices = np.arange(n_orders)
order_ids = [f"ORD-{900000 + i}" for i in order_indices]
cust_samples = np.random.randint(0, n_customers, n_orders)
prod_samples = np.random.randint(0, n_products, n_orders)

# Quantities & Pricing
quantities = np.random.choice([1, 2, 3, 4, 5], n_orders, p=[0.7, 0.15, 0.08, 0.04, 0.03])
order_channels = np.random.choice(channels, n_orders, p=[0.3, 0.3, 0.15, 0.15, 0.1])

# Discount Logic (Discount Seekers get more coupons)
base_discounts = np.random.choice([0.0, 0.1, 0.2, 0.4], n_orders, p=[0.7, 0.15, 0.1, 0.05])
cust_segments = cust_df.loc[cust_samples, "Segment"].values
is_discount_seeker = cust_segments == "Discount_Seeker"
final_discounts = np.where(is_discount_seeker & (base_discounts == 0), 0.1, base_discounts)

# Timestamps (Spreading across 2025-2026)
start_dt = datetime(2025, 1, 1)
offsets = np.random.randint(0, 450, n_orders)
order_dates = [start_dt + timedelta(days=int(o), hours=np.random.randint(0,23)) for o in offsets]

sales_df = pd.DataFrame({
    "Order_ID": order_ids,
    "Order_Date": order_dates,
    "Customer_ID": cust_df.loc[cust_samples, "Customer_ID"].values,
    "Product_ID": products_df.loc[prod_samples, "Product_ID"].values,
    "Quantity": quantities,
    "Ad_Source": order_channels,
    "Discount_Pct": final_discounts
})

# Merge to get Price and Cost for ROI
sales_df = sales_df.merge(products_df, on="Product_ID", how="left")
sales_df["Gross_Sales"] = np.round(sales_df["Quantity"] * sales_df["Unit_Price"] * (1 - sales_df["Discount_Pct"]), 2)
sales_df["Net_Profit"] = np.round(sales_df["Gross_Sales"] - (sales_df["Quantity"] * sales_df["Base_Cost"]), 2)

# Save Everything to 'data/'
products_df.to_csv("../data/product_catalog.csv", index=False)
cust_df.to_csv("../data/customer_segments.csv", index=False)
sales_df.to_csv("../data/raw_sales_logs_vast.csv", index=False)

print("Vast Sales Generation Data Export Complete:")
print(f"- 150,000 Sales Logs saved to 'raw_sales_logs_vast.csv'")
print(f"- Includes Category, Ad_Source, and Profit Margin analytics.")
