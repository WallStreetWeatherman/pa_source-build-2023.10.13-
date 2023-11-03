# Operating Performance Ratio Calculator
# --------------------------------------
# Overview:
# The Operating Performance Ratio (OPR) gauges a company's ability to convert 
# its sales into cash. A higher ratio indicates that the company is efficient 
# at translating its sales into actual cash flow, which can be used for 
# reinvestment, debt servicing, or returned to shareholders.
#
# Formula:
# Operating Performance Ratio = Operating Cash Flow / Sales Revenue
#
# Desired Value:
# A higher ratio is preferable as it means the firm is more efficient in 
# turning its sales into cash. Conversely, a lower ratio may indicate inefficiencies 
# in the company's operations or its collection practices.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Operating Cash Flow (in million dollars format for simplicity)
operating_cash_flow_in_millions = 1583.00 # Cash from Operations in Tikr
operating_cash_flow = convert_to_actual_value(operating_cash_flow_in_millions)

# Sales Revenue (in million dollars format for simplicity)
sales_revenue_in_millions = 23606.00  # Revenues in Tikr
sales_revenue = convert_to_actual_value(sales_revenue_in_millions)

# Calculate Operating Performance Ratio for the company
opr_company = operating_cash_flow / sales_revenue

# Hard-coded values for the industry average
industry_average_operating_cash_flow_in_millions = 1600.00  
industry_average_operating_cash_flow = convert_to_actual_value(industry_average_operating_cash_flow_in_millions)

industry_average_sales_revenue_in_millions = 24000.00  
industry_average_sales_revenue = convert_to_actual_value(industry_average_sales_revenue_in_millions)

# Calculate OPR for the industry
opr_industry = industry_average_operating_cash_flow / industry_average_sales_revenue

# Output the results
print(f"Company's Operating Performance Ratio: {opr_company:.2f}")
print(f"Industry Average Operating Performance Ratio: {opr_industry:.2f}\n")

if opr_company > 0.5:
    print("For the company, a significant portion of sales is being converted into cash, indicating efficient operations.")
elif opr_company > 0.2:
    print("For the company, a moderate portion of sales is being converted into cash.")
else:
    print("For the company, there may be inefficiencies in turning its sales into cash.")

if opr_company > opr_industry:
    print("The company's OPR is above the industry average, suggesting superior operational efficiency.")
elif opr_company < opr_industry:
    print("The company's OPR is below the industry average, suggesting potential areas for improvement.")
else:
    print("The company's OPR is on par with the industry average.")