# Price to Cash Flow Ratio Calculator
# -----------------------------------
# Overview:
# The Price to Cash Flow Ratio evaluates the relationship between a company's stock price and its cash flow per share.
# This metric provides insights into the company's valuation in terms of its ability to generate cash flow.
#
# Formula:
# Price to Cash Flow Ratio = Market Price per Share / Cash Flow per Share
#
# Cash Flow per Share = Total Operating Cash Flow / Total Outstanding Shares
#
# Desired Value:
# A lower Price to Cash Flow Ratio suggests that the company might be undervalued, considering its cash flows.
# A higher ratio might indicate overvaluation. However, the 'good' range for this ratio can vary widely across industries.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Total Operating Cash Flow (in million dollars format for simplicity)
operating_cash_flow_in_millions = 1583.00
operating_cash_flow = convert_to_actual_value(operating_cash_flow_in_millions)

# Total Outstanding Shares (in millions for simplicity)
total_outstanding_shares_in_millions = 273.63 
total_outstanding_shares = convert_to_actual_value(total_outstanding_shares_in_millions)

# Market Price per Share (actual value)
market_price_per_share = 11.11  

# Calculate Cash Flow per Share
cash_flow_per_share = operating_cash_flow / total_outstanding_shares

# Calculate Price to Cash Flow Ratio
price_to_cash_flow_ratio = market_price_per_share / cash_flow_per_share

# Output the results
print(f"Price to Cash Flow Ratio: {price_to_cash_flow_ratio:.2f}")

if price_to_cash_flow_ratio < 10:
    print("The company has a low Price to Cash Flow Ratio, suggesting it might be undervalued based on its cash flows.")
elif price_to_cash_flow_ratio < 20:
    print("The company's Price to Cash Flow Ratio is moderate. It's fairly valued based on its cash flows.")
else:
    print("The company has a high Price to Cash Flow Ratio, indicating it might be overvalued considering its cash flows.")
