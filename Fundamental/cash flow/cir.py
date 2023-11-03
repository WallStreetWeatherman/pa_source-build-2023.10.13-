# Cash to Income Ratio Calculator
# -------------------------------
# Overview:
# The Cash to Income Ratio shows the relationship between cash generated from operations 
# and a company's net income. It helps to evaluate the quality of a company's earnings 
# and its ability to turn those earnings into actual cash.
#
# Formula:
# Cash to Income Ratio = Cash Flow from Operations / Net Income
#
# Desired Value:
# A ratio close to or above 1 indicates that the company is generating cash equivalent 
# to its reported net income, suggesting high-quality earnings. A ratio significantly below 1 
# might indicate that net income is not translating into actual cash, which could be a red flag.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash Flow from Operations (in million dollars format for simplicity)
company_cash_flow_from_operations_in_millions = 1583.00 
company_cash_flow_from_operations = convert_to_actual_value(company_cash_flow_from_operations_in_millions)

# Net Income (in million dollars format for simplicity)
company_net_income_in_millions = 749.00  
company_net_income = convert_to_actual_value(company_net_income_in_millions)

# Hard-coded values for the industry average

# Industry Average Cash Flow from Operations (in million dollars format for demonstration)
industry_avg_cash_flow_from_operations_in_millions = 1500.00  # Example value
industry_avg_cash_flow_from_operations = convert_to_actual_value(industry_avg_cash_flow_from_operations_in_millions)

# Industry Average Net Income (in million dollars format for demonstration)
industry_avg_net_income_in_millions = 720.00  # Example value
industry_avg_net_income = convert_to_actual_value(industry_avg_net_income_in_millions)

# Calculate Cash to Income Ratio for the company and industry
company_cash_to_income_ratio = company_cash_flow_from_operations / company_net_income
industry_cash_to_income_ratio = industry_avg_cash_flow_from_operations / industry_avg_net_income

# Output the results
print(f"Company's Cash to Income Ratio: {company_cash_to_income_ratio:.2f}")
print(f"Industry Average Cash to Income Ratio: {industry_cash_to_income_ratio:.2f}")

if company_cash_to_income_ratio > industry_cash_to_income_ratio:
    print("The company exceeds the industry average in Cash to Income Ratio, indicating superior quality of earnings relative to its peers.")
elif company_cash_to_income_ratio == industry_cash_to_income_ratio:
    print("The company's Cash to Income Ratio aligns with the industry average. Its earnings quality is comparable to other firms in the industry.")
else:
    print("The company is below the industry average in Cash to Income Ratio. This might suggest potential challenges in converting earnings into actual cash compared to its peers.")
