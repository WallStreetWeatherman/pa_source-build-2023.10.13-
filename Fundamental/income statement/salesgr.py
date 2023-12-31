# Sales Growth Rate Calculator
# ----------------------------
# Overview:
# The Sales Growth Rate evaluates the percentage increase in sales over a specific period.
# It provides insights into a company's ability to grow its revenues and is an essential metric 
# for analyzing the financial health and potential of a company.
#
# Formula:
# Sales Growth Rate = [(Sales in Current Period - Sales in Previous Period) / Sales in Previous Period] x 100
#
# Desired Value:
# Positive growth rates indicate that a company's sales are increasing, which is generally favorable. 
# However, extremely high growth rates may not be sustainable in the long run.
# Negative growth rates suggest declining sales, which might be a concern.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Sales in Previous Period (in million dollars format)
sales_previous_period_in_millions = 15.00  # Example value representing sales of $15,000,000 in the previous period
sales_previous_period = convert_to_actual_value(sales_previous_period_in_millions)

# Sales in Current Period (in million dollars format)
sales_current_period_in_millions = 18.00  # Example value representing sales of $18,000,000 in the current period
sales_current_period = convert_to_actual_value(sales_current_period_in_millions)

# Calculate Sales Growth Rate
if sales_previous_period == 0:
    sales_growth_rate = 0
else:
    sales_growth_rate = ((sales_current_period - sales_previous_period) / sales_previous_period) * 100

# Output the results
print(f"Sales Growth Rate: {sales_growth_rate:.2f}%")

if sales_growth_rate > 0:  
    print("The company's sales are growing, indicating a positive trend.")
elif sales_growth_rate == 0:
    print("The company's sales remain constant.")
else:
    print("The company's sales are declining, which could be a concern.")
