# Cash Flow Margin Calculator
# ---------------------------
# Overview:
# The Cash Flow Margin measures the ability of a company to translate sales into cash. 
# It shows how efficiently a company is operating, highlighting the percentage of sales that result in actual cash flow.
#
# Formula:
# Cash Flow Margin = (Operating Cash Flow / Sales Revenue) * 100
#
# Desired Value:
# A higher Cash Flow Margin indicates that a larger portion of sales is being converted into cash, 
# showcasing better operational efficiency. On the other hand, a lower value might highlight inefficiencies or potential 
# issues in collecting revenue.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Operating Cash Flow (in million dollars format for simplicity)
operating_cash_flow_in_millions = 1583.00 
operating_cash_flow = convert_to_actual_value(operating_cash_flow_in_millions)

# Sales Revenue (in million dollars format for simplicity)
sales_revenue_in_millions = 23606.00 
sales_revenue = convert_to_actual_value(sales_revenue_in_millions)

# Hard-coded values for industry average

# Industry Average Operating Cash Flow (in million dollars format for simplicity)
industry_avg_operating_cash_flow_in_millions = 1530.00  # Example value
industry_avg_operating_cash_flow = convert_to_actual_value(industry_avg_operating_cash_flow_in_millions)

# Industry Average Sales Revenue (in million dollars format for simplicity)
industry_avg_sales_revenue_in_millions = 23000.00  # Example value
industry_avg_sales_revenue = convert_to_actual_value(industry_avg_sales_revenue_in_millions)

# Calculate Cash Flow Margin for the company and the industry
cash_flow_margin = (operating_cash_flow / sales_revenue) * 100
industry_avg_cash_flow_margin = (industry_avg_operating_cash_flow / industry_avg_sales_revenue) * 100

# Output the results
print(f"Company's Cash Flow Margin: {cash_flow_margin:.2f}%")
print(f"Industry Average Cash Flow Margin: {industry_avg_cash_flow_margin:.2f}%")

if cash_flow_margin >= 20:
    print("The company has a strong Cash Flow Margin, showcasing efficient cash generation from sales.")
    if cash_flow_margin > industry_avg_cash_flow_margin:
        print("Moreover, the company outperforms the industry average, indicating superior operational efficiency.")
    else:
        print("However, it lags behind the industry average, suggesting room for improvement.")
elif cash_flow_margin >= 10:
    print("The company has a moderate Cash Flow Margin. There might be room for operational efficiency improvements.")
    if cash_flow_margin < industry_avg_cash_flow_margin:
        print("Note: The company's Cash Flow Margin is below the industry average, indicating potential competitiveness concerns.")
else:
    print("The company has a low Cash Flow Margin, suggesting potential inefficiencies in converting sales to cash.")
