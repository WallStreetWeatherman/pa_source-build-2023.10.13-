# Free Cash Flow Calculator
# -------------------------
# Overview:
# The Free Cash Flow (FCF) indicates the amount of cash available to investors after capital expenditures
# have been accounted for. It provides insight into a company's ability to generate surplus cash which 
# can be used for potential dividends, debt repayment, reinvestment, or other purposes.
#
# Formula:
# Free Cash Flow (FCF) = Operating Cash Flow (OCF) - Capital Expenditures (CapEx)
#
# Desired Value:
# A positive FCF implies the company has leftover cash after maintaining or expanding its asset base, 
# suggesting it's in a good position to enhance shareholder value. A negative FCF might signal a company 
# is investing heavily for future growth or having issues with cash flows.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

def convert_to_actual_value(value_in_millions):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value_in_millions * 1000000

# Hard-coded values for the company
company_ocf_in_millions = 1583.00  # Company's Operating Cash Flow
company_ocf = convert_to_actual_value(company_ocf_in_millions)

company_capex_in_millions = -900.00  # Company's Capital Expenditures (negative as it's an outflow)
company_capex = convert_to_actual_value(company_capex_in_millions)

# Calculate the company's Free Cash Flow
company_fcf = company_ocf - company_capex

# Hard-coded values for industry average (for demonstration purposes)
industry_avg_ocf_in_millions = 1450.00  # Example value for industry average operating cash flow
industry_avg_ocf = convert_to_actual_value(industry_avg_ocf_in_millions)

industry_avg_capex_in_millions = -850.00  # Example value for industry average capital expenditures
industry_avg_capex = convert_to_actual_value(industry_avg_capex_in_millions)

# Calculate the industry average Free Cash Flow
industry_avg_fcf = industry_avg_ocf - industry_avg_capex

# Output the results
print("Free Cash Flow Calculation:\n")
print(f"Company's Free Cash Flow (FCF): ${company_fcf/1000000:.2f} million")
print(f"Industry Average Free Cash Flow (FCF): ${industry_avg_fcf/1000000:.2f} million")

# Interpretation
if company_fcf > industry_avg_fcf:
    print("The company's FCF is higher than the industry average, suggesting robust financial health relative to its peers.")
elif company_fcf == industry_avg_fcf:
    print("The company's FCF is in line with the industry average.")
else:
    print("The company's FCF is lower than the industry average, which may indicate challenges or heavy investments compared to peers.")