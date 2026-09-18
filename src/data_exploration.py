import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# 1. Load Dataset
# -----------------------------

file_path = "../data/Sample - Superstore.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# -----------------------------
# 2. Basic Dataset Information
# -----------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()


# -----------------------------
# 3. Data Quality Check
# -----------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------
# 4. Descriptive Statistics
# -----------------------------

print("\nDescriptive Statistics:")
print(df.describe())


# -----------------------------
# 5. Business Metrics
# -----------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

profit_margin = (total_profit / total_sales) * 100

print("\nBusiness Metrics")
print("----------------")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity:", total_quantity)
print("Profit Margin:", round(profit_margin, 2), "%")


# -----------------------------
# 6. Category Analysis
# -----------------------------

category_analysis = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nCategory Analysis:")
print(category_analysis)


# -----------------------------
# 7. Sub-Category Profit Analysis
# -----------------------------

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSub-Category Profit:")
print(subcategory_profit)


# -----------------------------
# 8. Regional Analysis
# -----------------------------

region_analysis = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nRegional Analysis:")
print(region_analysis)


# -----------------------------
# 9. Customer Segment Analysis
# -----------------------------

segment_analysis = (
    df.groupby("Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nCustomer Segment Analysis:")
print(segment_analysis)


# -----------------------------
# 10. Monthly Sales Analysis
# -----------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)


# -----------------------------
# 11. Discount and Profit
# -----------------------------

discount_profit = (
    df.groupby("Discount")["Profit"]
    .mean()
    .sort_index()
)

print("\nAverage Profit by Discount:")
print(discount_profit)


# -----------------------------
# 12. Visualizations
# -----------------------------

# Category Sales
category_analysis["Sales"].plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# Regional Sales
region_analysis["Sales"].plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# Sub-category Profit
subcategory_profit.plot(kind="bar")

plt.title("Profit by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Monthly Sales
monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# -----------------------------
# 13. Initial Findings
# -----------------------------

print("\nInitial Findings")
print("----------------")

print("1. Sales and profit vary across categories.")
print("2. Profitability differs across sub-categories.")
print("3. Regional performance is not uniform.")
print("4. Discount levels should be investigated for their relationship with profit.")
print("5. Sales show time-based variation and should be analyzed further.")


# -----------------------------
# 14. Problem Definition
# -----------------------------

print("\nProblem Definition")
print("------------------")

print(
    "The business needs to understand the factors associated with "
    "sales and profitability across products, categories, regions, "
    "customer segments and time."
)


# -----------------------------
# 15. Hypotheses
# -----------------------------

print("\nHypotheses")
print("----------")

print("H1: Higher discounts may be associated with lower profitability.")
print("H2: Sales and profit may differ across categories.")
print("H3: High-sales products may not always be highly profitable.")
print("H4: Regional sales and profitability may differ.")
print("H5: Sales may show time-based trends or seasonal patterns.")
