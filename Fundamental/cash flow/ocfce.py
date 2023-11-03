# Operating Cash Flow to Capital Expenditure Ratio Calculator
# -----------------------------------------------------------
# Overview:
# The Operating Cash Flow to Capital Expenditure (OCF to CapEx) Ratio assesses how many times a company 
# can cover its capital expenditures from its operating cash flows. It provides insights into the company's 
# ability to sustain its capital spending without the need for external funding.
#
# Formula:
# OCF to CapEx Ratio = Cash Flow from Operations / Capital Expenditures
#
# Desired Value:
# A higher ratio indicates that the company has strong operating cash flows relative to its capital spending.
# A ratio less than 1 suggests that the company's operating cash flows are insufficient to cover its capital expenditures.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

cash_flow_from_operations_in_millions = 1615.00  # Cash from Operations
cash_flow_from_operations = convert_to_actual_value(cash_flow_from_operations_in_millions)

capital_expenditures_in_millions = 888.00  # Capital Expenditure in Tikr
capital_expenditures = convert_to_actual_value(capital_expenditures_in_millions)

# Calculate the company's OCF to CapEx Ratio
ocf_to_capex_ratio = cash_flow_from_operations / capital_expenditures

# Hard-coded values for industry average

industry_avg_cash_flow_from_operations_in_millions = 803.00  # Placeholder value
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

industry_avg_capital_expenditures_in_millions = 182.00  # Placeholder value
industry_avg_capital_expenditures = convert_to_actual_value(industry_avg_capital_expenditures_in_millions)

# Calculate Industry Average OCF to CapEx Ratio
industry_avg_ocf_to_capex_ratio = industry_avg_cash_flow_from_operations / industry_avg_capital_expenditures

# Output the results
print(f"Company's Operating Cash Flow to Capital Expenditure Ratio: {ocf_to_capex_ratio:.2f}")
print(f"Industry Average OCF to CapEx Ratio: {industry_avg_ocf_to_capex_ratio:.2f}\n")

if ocf_to_capex_ratio > 3:
    print("The company is generating robust operating cash flows in comparison to its capital spending. This may indicate potential for internal growth financing and higher shareholder returns.")
elif ocf_to_capex_ratio > 1:
    print("The company's operating cash flows adequately cover its capital expenditures, indicating a healthy operational balance.")
else:
    print("The company's operating cash flows are less than its capital expenditures, suggesting potential reliance on external financing or strategic investments for future growth.")

if ocf_to_capex_ratio > industry_avg_ocf_to_capex_ratio:
    print("The company's OCF to CapEx ratio exceeds the industry average, suggesting superior cash flow management or less capital intensity compared to peers. This may provide a competitive advantage.")
elif ocf_to_capex_ratio < industry_avg_ocf_to_capex_ratio:
    print("The company's OCF to CapEx ratio is below the industry average, highlighting potential operational inefficiencies or a more aggressive investment strategy. A closer look into the company's financials and strategy is advised.")
else:
    print("The company's OCF to CapEx ratio aligns with the industry benchmark, indicating it operates similarly to its peers in terms of cash flow and capital expenditure.")
    
