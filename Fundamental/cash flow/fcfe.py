# Free Cash Flow to Equity Calculator
# -----------------------------------
# Overview:
# The Free Cash Flow to Equity (FCFE) indicates the amount of cash available to equity shareholders 
# after all operational expenses, taxes, interest, and net debt repayments have been deducted.
# It provides insight into how much cash can potentially be paid out to equity holders or be reinvested 
# back into the company.
#
# Formula:
# FCFE = Net Income + Depreciation - Capital Expenditures (CapEx) - Change in Net Working Capital + Net Borrowing
#
# Desired Value:
# A positive FCFE implies the company has surplus cash available to equity holders, suggesting potential 
# for dividends or reinvestment. A negative FCFE indicates the company might be consuming more cash 
# than it produces, indicating potential solvency issues.

def convert_to_actual_value(value_in_millions):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value_in_millions * 1000000

# Hard-coded values for the company
company_net_income_in_millions = 749.00
company_net_income = convert_to_actual_value(company_net_income_in_millions)

company_depreciation_in_millions = 4905.00
company_depreciation = convert_to_actual_value(company_depreciation_in_millions)

company_capex_in_millions = -900.00
company_capex = convert_to_actual_value(company_capex_in_millions)

company_change_nwc_in_millions = -208.00
company_change_nwc = convert_to_actual_value(company_change_nwc_in_millions)

company_net_borrowing_in_millions = -46.00
company_net_borrowing = convert_to_actual_value(company_net_borrowing_in_millions)

# Calculate the company's FCFE
company_fcfe = company_net_income + company_depreciation - company_capex - company_change_nwc + company_net_borrowing

# Hard-coded values for industry average (for demonstration purposes)
industry_avg_net_income_in_millions = 650.00  # Example value for industry average net income
industry_avg_net_income = convert_to_actual_value(industry_avg_net_income_in_millions)

industry_avg_depreciation_in_millions = 4700.00  # Example value for industry average depreciation
industry_avg_depreciation = convert_to_actual_value(industry_avg_depreciation_in_millions)

industry_avg_capex_in_millions = -850.00  # Example value for industry average CapEx
industry_avg_capex = convert_to_actual_value(industry_avg_capex_in_millions)

industry_avg_change_nwc_in_millions = -190.00  # Example value for industry average change in NWC
industry_avg_change_nwc = convert_to_actual_value(industry_avg_change_nwc_in_millions)

industry_avg_net_borrowing_in_millions = -40.00  # Example value for industry average net borrowing
industry_avg_net_borrowing = convert_to_actual_value(industry_avg_net_borrowing_in_millions)

# Calculate the industry average FCFE
industry_avg_fcfe = industry_avg_net_income + industry_avg_depreciation - industry_avg_capex - industry_avg_change_nwc + industry_avg_net_borrowing

# Output the results
print("Free Cash Flow to Equity Calculation:\n")
print(f"Company's Free Cash Flow to Equity (FCFE): ${company_fcfe/1000000:.2f} million")
print(f"Industry Average Free Cash Flow to Equity (FCFE): ${industry_avg_fcfe/1000000:.2f} million")

# Interpretation
if company_fcfe > industry_avg_fcfe:
    print("The company's FCFE is higher than the industry average, indicating potential for greater distributions to equity holders or reinvestment opportunities.")
elif company_fcfe == industry_avg_fcfe:
    print("The company's FCFE is in line with the industry average.")
else:
    print("The company's FCFE is lower than the industry average, which may indicate challenges or greater reinvestment needs compared to peers.")