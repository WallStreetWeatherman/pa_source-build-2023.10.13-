# % Free Cash Flow (FCF) Margins Analysis
# ---------------------------------------
# Overview:
# Free Cash Flow (FCF) Margin indicates the percentage of revenue left over after accounting for operating costs and capital expenditures.
# It's a strong measure of a company's profitability and ability to generate investor value.
#
# Desired Value:
# Higher FCF Margins are generally favorable as they suggest that the company can efficiently turn sales into cash. Low FCF Margins may
# indicate inefficiencies or high capital spending relative to revenue.
#
# Note: This script uses hard-coded values. For real-world application, data should be fetched and updated accordingly.

def convert_to_actual_value(value_in_millions):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value_in_millions * 1000000

# Hard-coded values for the company
company_ebit_in_millions = 1680.00
company_ebit = convert_to_actual_value(company_ebit_in_millions)

company_tax_rate = 0.21  
company_depreciation_amortization_in_millions = 642.00 # Total Depreciation & Amortization in Tikr
company_depreciation_amortization = convert_to_actual_value(company_depreciation_amortization_in_millions)

company_change_nwc_in_millions = -208.00 # Change in Net Working Capital in Tikr
company_change_nwc = convert_to_actual_value(company_change_nwc_in_millions)

company_capex_in_millions = 900.00 # Capital Expenditure in Tikr
company_capex = convert_to_actual_value(company_capex_in_millions)

# Calculate the company's FCFF
company_fcff = (company_ebit * (1 - company_tax_rate)) + company_depreciation_amortization - company_change_nwc - company_capex

# Hard-coded values for industry average (for demonstration purposes)
industry_avg_ebit_in_millions = 22000.00
industry_avg_ebit = convert_to_actual_value(industry_avg_ebit_in_millions)

industry_avg_depreciation_amortization_in_millions = 600.00
industry_avg_depreciation_amortization = convert_to_actual_value(industry_avg_depreciation_amortization_in_millions)

industry_avg_change_nwc_in_millions = -200.00
industry_avg_change_nwc = convert_to_actual_value(industry_avg_change_nwc_in_millions)

industry_avg_capex_in_millions = 850.00
industry_avg_capex = convert_to_actual_value(industry_avg_capex_in_millions)

# Calculate the industry average FCFF
industry_avg_fcff = (industry_avg_ebit * (1 - company_tax_rate)) + industry_avg_depreciation_amortization - industry_avg_change_nwc - industry_avg_capex

# Output the results
print("Free Cash Flow to the Firm Calculation:\n")
print(f"Company's Free Cash Flow to the Firm (FCFF): ${company_fcff/1000000:.2f} million")
print(f"Industry Average Free Cash Flow to the Firm (FCFF): ${industry_avg_fcff/1000000:.2f} million")

# Interpretation
if company_fcff > industry_avg_fcff:
    print("The company's FCFF is higher than the industry average, indicating a stronger financial position and efficiency relative to its peers.")
elif company_fcff == industry_avg_fcff:
    print("The company's FCFF is in line with the industry average.")
else:
    print("The company's FCFF is lower than the industry average, indicating potential challenges or lesser efficiency compared to its peers.")