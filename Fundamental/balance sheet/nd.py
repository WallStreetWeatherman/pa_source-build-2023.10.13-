# Net Debt Calculation
# ---------------------
# Overview:
# Net Debt is a measure of a company's financial health, calculated by subtracting 
# the company's cash and cash equivalents from its total debt.
#
# Desired Value:
# A lower net debt is generally better as it indicates the company has more liquidity. 
# It's essential to compare net debt across similar companies or industries for a more meaningful analysis.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values for the company's total debt, cash, and cash equivalents
company_total_debt = convert_to_actual_value(5972.00)  
company_cash = convert_to_actual_value(683.00)  
company_cash_equivalents = convert_to_actual_value(438.00)  

# Calculate Company's Net Debt
company_net_debt = company_total_debt - (company_cash + company_cash_equivalents)

# Hard-coded values for the industry average for total debt, cash, and cash equivalents
industry_average_total_debt = convert_to_actual_value(5900.00)  # Placeholder values, replace as needed
industry_average_cash = convert_to_actual_value(650.00)  # Placeholder values, replace as needed
industry_average_cash_equivalents = convert_to_actual_value(420.00)  # Placeholder values, replace as needed

# Calculate Industry Average Net Debt
industry_average_net_debt = industry_average_total_debt - (industry_average_cash + industry_average_cash_equivalents)

# Output the results
print("Net Debt Calculation:\n")
print(f"Company's Net Debt: ${company_net_debt/1000000:.2f} million")
print(f"Industry Average Net Debt: ${industry_average_net_debt/1000000:.2f} million")

# Compare the company's Net Debt with the industry average
if company_net_debt < industry_average_net_debt:
    print("\nThe company's net debt is lower than the industry average.")
elif company_net_debt > industry_average_net_debt:
    print("\nThe company's net debt is higher than the industry average.")
else:
    print("\nThe company's net debt aligns with the industry average.")
