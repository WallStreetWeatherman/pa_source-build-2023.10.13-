# Cash Interest Coverage Ratio Calculator
# ---------------------------------------
# Overview:
# The Cash Interest Coverage Ratio is an indicator of a company's ability to pay interest 
# on its outstanding debt using the cash generated from its operations. This ratio provides 
# insights into the solvency of an entity and its long-term financial stability.
#
# Formula:
# Cash Interest Coverage Ratio = Cash Flow from Operations / Interest Expense
#
# Desired Value:
# A higher Cash Interest Coverage Ratio is generally preferred, indicating the company's 
# ability to comfortably service its debt interest from operating cash flows. A ratio below 
# 1 suggests that the company might struggle to cover its interest obligations.
#

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
company_cash_flow_from_operations_in_millions = 1615.00 # Cash from Operations in Tikr
company_cash_flow_from_operations = convert_to_actual_value(company_cash_flow_from_operations_in_millions)

# Interest Expense (in million dollars format for simplicity)
company_interest_expense_in_millions = abs(-175.00) # Interest Expense in Tikr
company_interest_expense = convert_to_actual_value(company_interest_expense_in_millions)

# Hard-coded values for industry average

# Industry Average Cash Flow from Operations (in million dollars format for demonstration)
industry_avg_cash_flow_from_operations_in_millions = 803.00  
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

# Industry Average Interest Expense (in million dollars format for demonstration)
industry_avg_interest_expense_in_millions = -37.00  
industry_avg_interest_expense = convert_to_actual_value(industry_avg_interest_expense_in_millions)

# Calculate Cash Interest Coverage Ratio for the company and industry
company_cash_interest_coverage_ratio = company_cash_flow_from_operations / company_interest_expense
industry_cash_interest_coverage_ratio = industry_avg_cash_flow_from_operations / industry_avg_interest_expense

# Output the results
print(f"Company's Cash Interest Coverage Ratio: {company_cash_interest_coverage_ratio:.2f}")
print(f"Industry Average Cash Interest Coverage Ratio: {industry_cash_interest_coverage_ratio:.2f}")

if company_cash_interest_coverage_ratio > industry_cash_interest_coverage_ratio:
    print("The company exceeds the industry average in Cash Interest Coverage Ratio, suggesting a stronger ability to cover its interest expenses relative to its peers.")
elif company_cash_interest_coverage_ratio == industry_cash_interest_coverage_ratio:
    print("The company's Cash Interest Coverage Ratio aligns with the industry average, indicating a comparable ability to service its interest obligations.")
else:
    print("The company lags behind the industry average in Cash Interest Coverage Ratio. This may suggest financial challenges relative to its industry counterparts.")