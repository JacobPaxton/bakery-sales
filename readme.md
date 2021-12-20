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
- Wrangle: Acquire data, drop nulls in datetime column
- Wrangle: Drop all Tuesdays except Christmas Eve (closed)
- Wrangle: Identify additional down days and the reasons for closure
- Wrangle: Drop *all* days where business was closed
- Explore: Plot univariate distributions
- Explore: Create structure and plan for achieving objectives