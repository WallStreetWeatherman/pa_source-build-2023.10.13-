# Cash Flow to Debt Ratio Calculator
# ----------------------------------
# Overview:
# The Cash Flow to Debt Ratio assesses the company's capability to settle its total debt using the cash flows 
# from its primary operations. It signifies the financial strength of the firm concerning its debt obligations.
#
# Formula:
# Cash Flow to Debt Ratio = Operating Cash Flow / Total Debt
#
# Desired Value:
# A higher Cash Flow to Debt Ratio is preferred, signifying the company can more comfortably cover its debt 
# with its operating cash flows. Conversely, a lower ratio may indicate potential liquidity concerns regarding 
# debt obligations.
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

# Total Debt (in million dollars format for simplicity)
total_debt_in_millions = 5972.00  
total_debt = convert_to_actual_value(total_debt_in_millions)

# Hard-coded values for industry average

# Industry Average Operating Cash Flow (in million dollars format for simplicity)
industry_avg_operating_cash_flow_in_millions = 1550.00  # Example value
industry_avg_operating_cash_flow = convert_to_actual_value(industry_avg_operating_cash_flow_in_millions)

# Industry Average Total Debt (in million dollars format for simplicity)
industry_avg_total_debt_in_millions = 5800.00  # Example value
industry_avg_total_debt = convert_to_actual_value(industry_avg_total_debt_in_millions)

# Calculate Cash Flow to Debt Ratio for the company and the industry
cash_flow_to_debt_ratio = operating_cash_flow / total_debt
industry_avg_cash_flow_to_debt_ratio = industry_avg_operating_cash_flow / industry_avg_total_debt

# Output the results
print(f"Company's Cash Flow to Debt Ratio: {cash_flow_to_debt_ratio:.2f}")
print(f"Industry Average Cash Flow to Debt Ratio: {industry_avg_cash_flow_to_debt_ratio:.2f}")

if cash_flow_to_debt_ratio > 0.8:
    print("The company has a strong Cash Flow to Debt Ratio, indicating robust financial health and ability to cover its debts.")
    if cash_flow_to_debt_ratio > industry_avg_cash_flow_to_debt_ratio:
        print("Furthermore, the company's Cash Flow to Debt Ratio exceeds the industry average, showcasing superior financial strength in relation to peers.")
    else:
        print("However, it's below the industry average, suggesting potential competitiveness or leverage concerns.")
elif cash_flow_to_debt_ratio >= 0.5:
    print("The company has a moderate Cash Flow to Debt Ratio. It's in a decent position to cover its debts, but monitoring is essential.")
    if cash_flow_to_debt_ratio < industry_avg_cash_flow_to_debt_ratio:
        print("Note: The company's ratio is lower than the industry average, which might be a cause for further analysis.")
else:
    print("The company has a low Cash Flow to Debt Ratio, indicating potential challenges in covering its debt obligations with operating cash flows.")