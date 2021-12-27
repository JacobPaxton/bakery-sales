# Korean Bakery Sales

![This is an image](https://i.imgur.com/5yaaaQU.jpg)

# Overview
This project analyzes a Korean bakery's sales data for a 10-month stretch. The work here is a new iteration on my old work, contained in the folder old-work. 

# The Data
https://www.kaggle.com/hosubjeong/bakery-sales

Includes:
- Date and time of transaction
- Total amount charged (includes delivery fee) 
- Each item sold and how many were sold
- Delivery location
- Separate file: Price of each item and price range for delivery fees

# Objectives
1. Understand changes in daily revenue for the timespan covered
    * Explain any anomalies using context (holidays, lockdowns, etc)
2. Calculate exact delivery fee for each transaction
    * Calculate item charges using counts and prices
    * Subtract item charge from total charges to determine delivery fee
3. Analyze delivery fee in the context of delivery location
    * Increased fees with longer delivery is probable
    * Are delivery fees associated with the 'place' or are they more specific?
    * Can we figure out 'close' and 'far' within a place just based on delivery fee differences?
4. Understand delivery locations and their trends
    * Do certain areas order during a certain time of day?
    * Do certain areas purchase more items on average?
    * Do certain areas purchase more in terms of revenue?
    * Did certain areas have increased/decreased activity weeks or months?
    * Do certain areas purchase more of an item than others?
5. Analyze how products sold
    * Which items sold the most?
    * Which items sold the least?
    * Which item had the highest revenue?
    * Are there significant increases or decreases in certain items sold during holidays or otherwise?
    * Are any items being disproportionately bought by certain areas?
6. Create a Tableau heatmap for locations and sales
7. Model future sales

# Work Done So Far
## Wrangle
- Acquire data, drop nulls in datetime column
- Aggregate transactions into daily_sales
    * Identify down days, EX: Tuesdays are usually closed business, but not Christmas Eve
    * Identify the reasons for other down days
    * With above justification, drop *all* days where business was closed
## Explore
- Plot univariate distributions
    * Histogram of sales totals
    * Histogram of delivery locations
    * Bar chart of individual item sale counts
- Plot daily and weekly trends in total sales
    * Plot daily revenue totals, seven-day rolling average in revenue totals, and average day's revenue
    * Plot weekly revenue totals, four-week rolling average, and average week's revenue
    * Document takeaways from visualizations
    * Explain visualization takeaways using context from world events
- Calculate delivery amounts for each transaction
    * Note: Some discrepancies seem to indicate unknown discounts
- Prepare delivery locations for exploration
    * Change Korean location names to romanized versions
    * 'Place' delivery locations relative to one another based on Google Maps boundary definitions
- Analyze delivery charges by location
    * Calculate average delivery charges by location
    * Calculate ratios for delivery charge in total charges
    * Create boxplots and bar charts showing locational delivery charge information
    * Create histogram of delivery charge amounts for each location
    * Determine central location for potential feature creation
    * Document takeaways
- Map out neighborhoods using sketch on Google Maps overview
    * Add additional layer for delivery charges
- Create crosstab and heatmap for delivery location sales by hour of the day
- Check averages for total items sold by delivery location
- Check averages for total revenue by delivery location and week of operation
- Check averages for total revenue by delivery location and month of operation
- Check overall sales numbers by product