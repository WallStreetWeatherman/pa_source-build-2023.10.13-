# Capital Employed Calculation
# ----------------------------
# Overview:
# Capital Employed is the total amount of capital that a company uses to run its business.
# It is calculated as the sum of Total Equity, Short Term Debt, Capital Lease Obligations, and Long Term Debt.
#
# Desired Value:
# A high Capital Employed value generally indicates a company that has significant resources invested in its business,
# which could be a sign of growth and expansion. However, excessive capital employed without generating adequate
# returns may be a sign of inefficiency. Conversely, a low Capital Employed might indicate underinvestment or high efficiency.
# Like many financial metrics, the 'right' level of Capital Employed depends on the industry and the specific circumstances of the company.
#
# Note: Check ROA, ROE, ROCE and ROI to assess efficency.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Total Equity (in million dollars format for simplicity)
total_equity_in_millions = 4082.00 # Total Equity in Tikr
total_equity = convert_to_actual_value(total_equity_in_millions)

# Short Term Debt (in million dollars format for simplicity) - (Current Liabilities)
short_term_debt_in_millions = 4861.00 # Current Liabilites in Tikr
short_term_debt = convert_to_actual_value(short_term_debt_in_millions)

# Capital Lease Obligations (in million dollars format for simplicity)
capital_lease_obligations_in_millions = 2963.00 # Capital Leases in Tikr
capital_lease_obligations = convert_to_actual_value(capital_lease_obligations_in_millions)

# Long Term Debt (in million dollars format for simplicity)
long_term_debt_in_millions = 2996.00 # Long-Term Debt in Tikr
long_term_debt = convert_to_actual_value(long_term_debt_in_millions)

# Calculate Capital Employed for the company
company_capital_employed = total_equity + short_term_debt + capital_lease_obligations + long_term_debt
company_capital_employed_in_millions = company_capital_employed / 1000000

# Hard-coded values for industry average
industry_avg_total_equity_in_millions = 4500.00  # Example values
industry_avg_short_term_debt_in_millions = 4000.00
industry_avg_capital_lease_obligations_in_millions = 2500.00
industry_avg_long_term_debt_in_millions = 3000.00

# Calculate Capital Employed for the industry average
industry_avg_capital_employed = (convert_to_actual_value(industry_avg_total_equity_in_millions) + 
                                 convert_to_actual_value(industry_avg_short_term_debt_in_millions) + 
                                 convert_to_actual_value(industry_avg_capital_lease_obligations_in_millions) + 
                                 convert_to_actual_value(industry_avg_long_term_debt_in_millions))
industry_avg_capital_employed_in_millions = industry_avg_capital_employed / 1000000

# Output the results
print(f"Company's Capital Employed: ${company_capital_employed_in_millions:.2f} million")
print(f"Industry Average Capital Employed: ${industry_avg_capital_employed_in_millions:.2f} million")

if company_capital_employed_in_millions > industry_avg_capital_employed_in_millions:
    print("The company exceeds the industry average in Capital Employed, suggesting a higher investment in business operations. Evaluation of return metrics is critical for a comprehensive insight.")
elif company_capital_employed_in_millions == industry_avg_capital_employed_in_millions:
    print("The company's Capital Employed aligns with the industry average. Assessing return metrics can offer additional clarity on efficiency.")
else:
    print("The company falls below the industry average in Capital Employed. This might indicate higher efficiency, but a closer look at return metrics and the company's strategic investments is recommended.")
    