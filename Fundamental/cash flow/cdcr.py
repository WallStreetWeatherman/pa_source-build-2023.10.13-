# Cash Dividend Coverage Ratio Calculator
# ---------------------------------------
# Overview:
# The Cash Dividend Coverage Ratio assesses a firm's ability to pay dividends 
# from its operating cash flow. It gives investors an idea of a company's 
# ability to sustain or increase its dividend payments.
#
# Formula:
# Cash Dividend Coverage Ratio = Cash Flow from Operations / Total Dividends Paid
#
# Desired Value:
# A ratio greater than 1 indicates that the company can cover its dividend payments 
# from its operating cash flow, suggesting a sustainable dividend. A ratio below 1 
# might signify that the company is potentially using external financing or eating 
# into its retained earnings to pay dividends.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
cash_flow_from_operations_in_millions = 1583.00  
cash_flow_from_operations = convert_to_actual_value(cash_flow_from_operations_in_millions)

# Total Dividends Paid (in million dollars format for simplicity)
total_dividends_paid_in_millions = -176.00  
total_dividends_paid = convert_to_actual_value(total_dividends_paid_in_millions)

# Hard-coded values for industry average

# Industry Average Cash Flow from Operations (in million dollars format for simplicity)
industry_avg_cash_flow_from_operations_in_millions = 1400.00  # Example value
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

# Industry Average Total Dividends Paid (in million dollars format for simplicity)
industry_avg_total_dividends_paid_in_millions = -160.00  # Example value
industry_avg_total_dividends_paid = convert_to_actual_value(industry_avg_total_dividends_paid_in_millions)

# Calculate Cash Dividend Coverage Ratio for the company and the industry
cash_dividend_coverage_ratio = cash_flow_from_operations / total_dividends_paid
industry_avg_cash_dividend_coverage_ratio = industry_avg_cash_flow_from_operations / industry_avg_total_dividends_paid

# Output the results
print(f"Company's Cash Dividend Coverage Ratio: {cash_dividend_coverage_ratio:.2f}")
print(f"Industry Average Cash Dividend Coverage Ratio: {industry_avg_cash_dividend_coverage_ratio:.2f}")

if cash_dividend_coverage_ratio > 1:
    print("The company can comfortably cover its dividend payments from its operating cash flow.")
    if cash_dividend_coverage_ratio > industry_avg_cash_dividend_coverage_ratio:
        print("The company's Cash Dividend Coverage Ratio is above the industry average, indicating stronger sustainability relative to peers.")
    else:
        print("The company's Cash Dividend Coverage Ratio is below the industry average. It's essential to investigate the reasons and potential areas of improvement.")
else:
    print("The company might be using external financing or dipping into retained earnings to cover its dividend payments. Caution advised.")
