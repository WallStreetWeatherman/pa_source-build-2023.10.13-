# Dividend Coverage Ratio (from Cash Flows) Calculator
# ----------------------------------------------------
# Overview:
# The Dividend Coverage Ratio (from Cash Flows) measures the extent to which a company's cash flow from operations 
# covers its dividend payments. It provides insights into the sustainability of the company's dividends.
#
# Formula:
# Dividend Coverage Ratio (from Cash Flows) = Cash Flow from Operations / Total Dividends Paid
#
# Desired Value:
# A ratio greater than 1 indicates that the company generates sufficient cash flow to cover its dividend payments.
# A value less than 1 may suggest potential dividend sustainability issues in the future.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
company_cash_flow_from_operations_in_millions = 1615.00 # Cash from Operations in Tikr
company_cash_flow_from_operations = convert_to_actual_value(company_cash_flow_from_operations_in_millions)

# Company Total Dividends Paid (in million dollars format for simplicity)
company_total_dividends_paid_in_millions = 173.00  # Common Dividends Paid in Tikr
company_total_dividends_paid = convert_to_actual_value(company_total_dividends_paid_in_millions)

# Hard-coded values for industry average

# Industry Average Cash Flow from Operations (in million dollars format for demonstration)
industry_avg_cash_flow_from_operations_in_millions = 803.00  
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

# Industry Average Total Dividends Paid (in million dollars format for demonstration)
industry_avg_total_dividends_paid_in_millions = 16.00  
industry_avg_total_dividends_paid = convert_to_actual_value(industry_avg_total_dividends_paid_in_millions)

# Calculate Dividend Coverage Ratio (from Cash Flows) for the company and industry
company_dividend_coverage_ratio = company_cash_flow_from_operations / company_total_dividends_paid
industry_dividend_coverage_ratio = industry_avg_cash_flow_from_operations / industry_avg_total_dividends_paid

# Output the results
print(f"Company's Dividend Coverage Ratio (from Cash Flows): {company_dividend_coverage_ratio:.2f}")
print(f"Industry Average Dividend Coverage Ratio (from Cash Flows): {industry_dividend_coverage_ratio:.2f}\n")

if company_dividend_coverage_ratio > industry_dividend_coverage_ratio:
    print("The company exceeds the industry average in Dividend Coverage Ratio, suggesting a more comfortable position to cover its dividends relative to its peers.")
    print("Implication: With a higher ratio, the company has a buffer in its cash flows, potentially providing more reliability in its dividend payments. This might appeal to income-focused investors and possibly indicate the company's financial strength and management's confidence in the business.")
    
elif company_dividend_coverage_ratio == industry_dividend_coverage_ratio:
    print("The company's Dividend Coverage Ratio aligns with the industry average, indicating a similar capacity to cover its dividends as its industry peers.")
    print("Implication: The company maintains an industry standard when it comes to dividend payments. It's neither particularly aggressive nor conservative in its dividend policy. Investors should further investigate the company's growth prospects, competitive positioning, and other factors before making decisions.")
    
else:
    print("The company is below the industry average in Dividend Coverage Ratio, potentially indicating tighter cash flows relative to its dividend commitments.")
    print("Implication: A lower ratio may raise concerns about the sustainability of future dividend payments, especially if this trend continues. The company might face challenges in maintaining or growing its dividends without additional financing or improvements in operations. Income-focused investors might exercise caution.")
