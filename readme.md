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

# Findings
## Changes in daily revenue
> 1. **Delivery sales amounts over time generally trends flat with some days higher and some days lower**
> 2. **Delivery sales totals are generally higher on weekends than on weekdays**
> 3. **The high-delivery period from Mid-February to Mid-March coincides with South Korean pandemic response measures**
> 4. **In the month following the high-delivery period, delivery sales slowly return to pre-pandemic numbers**

## Neighborhood translations and locations
Standard Delivery Charge: 2000 won

**Chuncheon Center:**
- '조운동' 'Joundong' - Center of Chuncheon Neighborhoods - Standard Delivery Charge

**Inner Ring Around Joundong:**
- '약사명동' 'Yaksamyeongdong' - West of Joundong - Standard Delivery Charge
- '효자 1동' 'Hyoja 1' - Southwest of Joundong - Standard Delivery Charge
- '효자 2동' 'Hyoja 2' - South of Joundong - Standard Delivery Charge
- '효자 3동' 'Hyoja 3' - Southeast of Joundong - Standard Delivery Charge
- '교동' and '교동 ' 'Gyodong' - Northeast of Joundong - Standard Delivery Charge
- '소양동' 'Soyangdong' - Northwest of Joundong - Standard Delivery Charge

**Outer North and South of Joundong:**
- '근화동' 'Geunhwadong' - Northwest of Joundong Ring - *Higher* Delivery Charge
- '퇴계동' 'Toegyedong' - South of Joundong Ring - *Higher* Delivery Charge
- '석사동' 'Seoksadong' - Southeast of Joundong Ring - *Higher* Delivery Charge
- '후평 2동' 'Hupyeong 2' - East of Joundong Ring - Standard Delivery Charge
- '후평 3동' 'Hupyeong 3' - East edge of Hupyeong 2 - Standard Delivery Charge
- '후평 1동' 'Hupyeong 1' - Northeast of Joundong Ring - Standard Delivery Charge

**Far Reaches of Chuncheon:**
- '신사우동' 'Sinsaudong' - North - **Highest** Delivery Charge
- '강남동' 'Gangnamdong' - West - *Higher* Delivery Charge
- '신동면' 'Sindongmyeon' - South - No Delivery Charge (the single observation has item charge equal to total charge)
- '동내면' 'Dongnaemyeon' - Southeast - *Higher* Delivery Charge
- '동면' 'Dongmyeong' - Northeast - Standard Delivery Charge

## Delivery locations and their trends
### Do certain areas order during a certain time of day?
> - **All delivery locations have highest delivery orders between 11am (opening time) and 2pm**
> - **Two-thirds** of delivery locations order mostly in the opening hour of business (11am)
>     * 12 locations of 18
>     * Potentially ordering delivery to make it to workplace or home by noon lunch (standard lunchtime in South Korea)
> - Four locations of 18 order mostly in the second hour (12pm)
> - Remaining two locations order mostly in the third hour (1pm)

### Do certain areas purchase more items on average?
> - **All locations average about 4 items bought per transaction**

### Do certain areas purchase more in terms of revenue?
> - **Most locations have a similar average transaction revenue, around 20,000 won**

### Did certain areas have increased/decreased activity weeks or months?
> - **Yes.** Specific details could be gathered in future analysis

### Do certain areas purchase more of an item than others?
> - **Yes.** Specific details could be gathered in future analysis

## Products and their trends
> - **Items that sold the most: Angbutter, plain bread, and croissants**
> - **Items that sold the least: tiramisu, lemonade, and merinque cookies**
> - **Items that brought in the most revenue: Angbutter, plain bread, and croissants**

### Are there significant increases or decreases in certain items sold during holidays or otherwise?
> - In my opinion, the observation period of 10 months is too short to say for sure

### Are any items being disproportionately bought by certain areas?
> - Yes. Specific details could be gathered in future analysis

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
