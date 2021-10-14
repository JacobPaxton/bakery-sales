# Overview
This project analyzed a Korean bakery's sales data, ran statistical tests for locality and product differences, and performed time-series analysis and projection for total sales revenue.

# Link to data
https://www.kaggle.com/hosubjeong/bakery-sales

# Findings
## Stats Tests Findings
1. We cannot say with 95% confidence that revenue is rising over time.
2. We cannot say with 95% confidence that March had higher revenue than other months.
3. We cannot say with 95% confidence that Saturdays generate more revenue than other days.
4. We can say with 95% confidence that Sinsau-Dong generates more revenue than other neighborhoods.
5. We can say with 95% confidence that Northwest Chuncheon generates more revenue than other regions of the city.

## Specific Analytic Findings
1. Items that sold the most: Ang Butter (3223 sold), Croissant (1044 sold), Plain Bread (1023 sold)
2. Items that sold the least: Mad Garlic (0 sold), Croque Monsieur (0 sold), Tiramisu (7 sold)

## Model Performance
The **Simple Average as Prediction model performed best** with an RMSE of 8738 won and 6295 won on two out-of-sample data splits.

# Steps
1. Wrangled data
2. Split data into in-sample and out-of-sample data
2. Plotted distributions and plotted total revenue by time and by locality
4. Answered multiple initial hypotheses generated from exploration
5. Built models for in-sample time series data
6. Compared model prediction performance for out-of-sample (future) data
7. Selected best model
8. Tested model performance against final out-of-sample data

# Recreate my work
1. Run final_notebook.ipynb as a Jupyter Notebook Python 3 notebook