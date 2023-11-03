# Operating Cash Flow to Sales Ratio Calculator
# ---------------------------------------------
# Overview:
# The Operating Cash Flow to Sales Ratio measures the proportion of a company's sales revenue that 
# is converted into cash flow from operations. This provides insights into the company's 
# ability to turn sales into actual cash, which is crucial for meeting obligations and supporting growth.
#
# Formula:
# OCF to Sales Ratio = Cash Flow from Operations / Sales Revenue
#
# Desired Value:
# A higher ratio suggests that a larger portion of sales is being converted into cash. 
# This can indicate efficient operations and effective cash management. Conversely, a low ratio 
# may raise concerns about the company's ability to generate cash from its sales.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
cash_flow_from_operations_in_millions = 1583.00 
cash_flow_from_operations = convert_to_actual_value(cash_flow_from_operations_in_millions)

# Sales Revenue (in million dollars format for simplicity)
sales_revenue_in_millions = 23606.00
sales_revenue = convert_to_actual_value(sales_revenue_in_millions)

# Calculate OCF to Sales Ratio for the company
ocf_to_sales_ratio_company = cash_flow_from_operations / sales_revenue

# Hard-coded values for the industry average
industry_average_cash_flow_from_operations_in_millions = 1600.00  # Placeholder value
industry_average_cash_flow_from_operations = convert_to_actual_value(industry_average_cash_flow_from_operations_in_millions)

industry_average_sales_revenue_in_millions = 24000.00  # Placeholder value
industry_average_sales_revenue = convert_to_actual_value(industry_average_sales_revenue_in_millions)

# Calculate OCF to Sales Ratio for the industry
ocf_to_sales_ratio_industry = industry_average_cash_flow_from_operations / industry_average_sales_revenue

# Output the results
print(f"Company's Operating Cash Flow to Sales Ratio: {ocf_to_sales_ratio_company:.2f}")
print(f"Industry Average Operating Cash Flow to Sales Ratio: {ocf_to_sales_ratio_industry:.2f}\n")

if ocf_to_sales_ratio_company > 0.5:
    print("For the company, a significant portion of sales is being converted into cash, indicating efficient operations and effective cash management.")
elif ocf_to_sales_ratio_company > 0.2:
    print("For the company, a moderate portion of sales is being converted into cash.")
else:
    print("For the company, a smaller portion of sales is being converted into cash, which might raise concerns about its ability to generate cash from sales.")

if ocf_to_sales_ratio_company > ocf_to_sales_ratio_industry:
    print("The company's ratio is above the industry average, suggesting superior operational efficiency in converting sales to cash.")
elif ocf_to_sales_ratio_company < ocf_to_sales_ratio_industry:
    print("The company's ratio is below the industry average, suggesting potential areas for improvement.")
else:
    print("The company's ratio is on par with the industry average.")