# Yuva Intern Task 01 — Data Exploration & Problem Definition

## 📌 Project Overview

This project is completed as part of **Yuva Internship Task 01**.

The objective of this task is to perform **Data Exploration and Problem Definition** using Python and identify meaningful business insights from a real-world sales dataset.

The **Sample Superstore Dataset** is used for this analysis.

---

## 🎯 Objectives

The main objectives of this project are:

* Explore and understand the dataset.
* Identify the structure, data types, and important variables.
* Check missing values and duplicate records.
* Calculate descriptive statistics.
* Analyze sales, profit, quantity, discount, categories, regions, and customer segments.
* Create meaningful visualizations.
* Identify initial business insights.
* Define a clear analytics problem.
* Develop business questions and hypotheses.
* Propose an analysis plan for further investigation.

---

## 📊 Dataset

**Dataset:** Sample Superstore

The dataset contains sales transactions for a retail business.

### Dataset Size

* **Rows:** 9,994
* **Columns:** 21
* **Total Sales:** 2,297,200.86
* **Total Profit:** 286,397.02
* **Total Quantity:** 37,873
* **Missing Values:** 0
* **Duplicate Rows:** 0

### Important Variables

| Variable       | Description             |
| -------------- | ----------------------- |
| Order ID       | Unique order identifier |
| Order Date     | Date of order           |
| Ship Date      | Shipping date           |
| Ship Mode      | Shipping method         |
| Customer ID    | Customer identifier     |
| Customer Name  | Customer name           |
| Segment        | Customer segment        |
| Country/Region | Country or region       |
| State          | State                   |
| City           | City                    |
| Product ID     | Product identifier      |
| Product Name   | Product name            |
| Category       | Product category        |
| Sub-Category   | Product sub-category    |
| Sales          | Sales amount            |
| Quantity       | Quantity sold           |
| Discount       | Discount applied        |
| Profit         | Profit generated        |

---

## 🛠️ Tools & Technologies

The following tools and technologies were used:

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**
* **GitHub**

---

## 🔍 Exploratory Data Analysis

The following steps were performed during the exploration:

### 1. Data Loading

The dataset was loaded using Pandas.

### 2. Data Understanding

The dataset structure was examined using:

* `head()`
* `shape`
* `columns`
* `info()`
* `dtypes`

### 3. Data Quality Check

The dataset was checked for:

* Missing values
* Duplicate records
* Invalid values
* Negative profit records
* Data type consistency

### 4. Descriptive Statistics

Statistical summaries were generated for numerical variables such as:

* Sales
* Quantity
* Discount
* Profit

### 5. Business Analysis

The following areas were explored:

* Category performance
* Sub-category profitability
* Regional sales
* Customer segments
* Monthly sales trends
* Product-level performance

---

## 📈 Visualizations

The project includes visualizations for understanding the data.

### Category-wise Sales

Shows sales contribution from different product categories.

### Monthly Sales Trend

Shows how sales change over time.

### Regional Sales

Compares sales performance across different regions.

### Sub-category Profit

Highlights profit differences between product sub-categories.

---

## 💡 Initial Findings

The initial exploration indicates that:

* Sales performance varies across product categories.
* Profitability differs significantly between sub-categories.
* Some products can generate high sales but comparatively low profit.
* Regional performance is not uniform.
* Discounts require further investigation because they may be associated with lower profitability.
* Sales performance changes over time and should be examined for trends and seasonal patterns.

These findings are preliminary and require further statistical and business analysis.

---

## ❓ Problem Definition

### Business Problem

The business needs to understand the factors associated with **sales and profitability** across products, categories, regions, customer segments, and time.

The analysis should identify:

* Areas generating strong revenue.
* Areas generating weak or negative profit.
* Products with high sales but low profitability.
* The relationship between discounting and profitability.
* Regional and customer-segment differences.

### Main Analytics Question

> Which products, categories, regions, customer segments, and discount levels contribute most to revenue and profit, and where are there opportunities to improve profitability without unnecessarily reducing sales?

---

## 📋 Key Business Questions

1. How do sales and profit change over time?
2. Which categories and sub-categories generate the highest sales?
3. Which categories and sub-categories generate the highest profit?
4. Which products have high sales but low or negative profit?
5. Is there a relationship between discount and profit?
6. Which regions generate the highest sales and profit?
7. Which customer segments contribute most to revenue and profit?
8. Are there geographic areas with weak profitability?
9. Does shipping mode have any relationship with sales or profit?

---

## 🧪 Hypotheses

The following hypotheses were proposed for further analysis:

### H1 — Discount and Profit

Higher discounts may be associated with lower profit margins.

### H2 — Category Performance

Sales and profitability may differ significantly between product categories and sub-categories.

### H3 — High Sales vs High Profit

Products with high sales may not always generate high profit.

### H4 — Regional Differences

Sales and profitability may differ across geographic regions.

### H5 — Time-based Patterns

Sales may show trends or seasonal patterns over time.

---

## 🔬 Proposed Analysis Plan

Further analysis can include:

### Statistical Analysis

* Correlation analysis
* Group comparisons
* ANOVA where appropriate
* Non-parametric statistical tests where assumptions are not satisfied

### Visualization

* Bar charts
* Line charts
* Scatter plots
* Box plots
* Heatmaps
* Time-series visualizations

### Business Analysis

* Profit margin analysis
* Discount-profit relationship
* Product profitability analysis
* Regional performance analysis
* Customer segment analysis
* Time-series analysis

---

## 📁 Project Structure

```text
YuvaIntern_Task_01/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── Sample - Superstore.csv
│
├── notebooks/
│   └── Week_1_Data_Exploration.ipynb
│
├── src/
│   └── data_exploration.py
│
├── visualizations/
│   ├── category_sales.png
│   ├── monthly_sales.png
│   ├── profit_subcategory.png
│   └── region_sales.png
│
└── reports/
    └── Week_1_Data_Exploration_and_Problem_Definition.docx
```

---

## ▶️ How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone https://github.com/aryan87-ui/YuvaIntern_Task_01.git
```

### Step 2 — Open the Project

```bash
cd YuvaIntern_Task_01
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/Week_1_Data_Exploration.ipynb
```

and run the notebook cells.

---

## 📄 Deliverable

The final deliverable is a comprehensive report containing:

* Dataset overview
* Data quality analysis
* Descriptive statistics
* Exploratory data analysis
* Visualizations
* Initial insights
* Problem definition
* Business questions
* Hypotheses
* Proposed analysis plan
* Limitations
* Future improvements

---

## ⚠️ Limitations

This analysis has some limitations:

* The dataset is primarily used for educational and analytical practice.
* The data is observational, so relationships identified do not automatically imply causation.
* Discount may be affected by other business factors.
* Important business variables such as advertising expenditure, inventory costs, returns, and customer acquisition costs are not included.
* Aggregated results may hide individual product or customer-level patterns.

---

## 🚀 Future Improvements

Future analysis can include:

* Statistical hypothesis testing
* Predictive sales analysis
* Profit forecasting
* Customer segmentation
* Product recommendation analysis
* Advanced Power BI dashboards
* Machine learning models
* Time-series forecasting
* Detailed regional profitability analysis

---

## 👨‍💻 Author

**Aryan Verma**

B.Tech — Computer Science & Engineering

---

## ⭐ Conclusion

This project establishes the foundation for a deeper **Sales and Profitability Analytics** study.

The exploratory analysis helps identify important patterns and business questions that can be investigated further using statistical analysis, visualization, dashboards, and predictive techniques.
