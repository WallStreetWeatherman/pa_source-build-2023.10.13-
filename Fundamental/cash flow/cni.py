# Cash to Net Income Ratio Calculator
# -----------------------------------
# Overview:
# The Cash to Net Income Ratio compares the cash provided by operating activities to the net income 
# of a company. It is an essential metric for evaluating the quality of a company's earnings.
# If the ratio is significantly different from 1, it could suggest that the reported net income 
# may not fully represent the cash-generating ability of the company.
#
# Formula:
# Cash to Net Income Ratio = Cash from Operations / Net Income
#
# Desired Value:
# A ratio close to 1 is generally favorable as it suggests that the net income closely 
# matches the cash generated from operations. A ratio significantly higher than 1 may 
# indicate that the company is generating more cash than is reflected in the net income, 
# whereas a ratio significantly less than 1 might suggest potential issues with the 
# quality of earnings.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company

# Cash from Operations (in million dollars format for simplicity)
company_cash_from_operations_in_millions = 1615.00  # Cash from Operations in Tikr
company_cash_from_operations = convert_to_actual_value(company_cash_from_operations_in_millions)

# Company Net Income (in million dollars format for simplicity)
company_net_income_in_millions = 1177.00  # Net Income in Tikr
company_net_income = convert_to_actual_value(company_net_income_in_millions)

# Hard-coded values for industry average

# Industry Average Cash from Operations (in million dollars format for demonstration)
industry_avg_cash_from_operations_in_millions = 803.00  
industry_avg_cash_from_operations = convert_to_actual_value(industry_avg_cash_from_operations_in_millions)

# Industry Average Net Income (in million dollars format for demonstration)
industry_avg_net_income_in_millions = 324.00  
industry_avg_net_income = convert_to_actual_value(industry_avg_net_income_in_millions)

# Calculate Cash to Net Income Ratio for the company and industry
company_cash_to_net_income_ratio = company_cash_from_operations / company_net_income
industry_cash_to_net_income_ratio = industry_avg_cash_from_operations / industry_avg_net_income

# Output the results
print(f"Company's Cash to Net Income Ratio: {company_cash_to_net_income_ratio:.2f}")
print(f"Industry Average Cash to Net Income Ratio: {industry_cash_to_net_income_ratio:.2f}")

if company_cash_to_net_income_ratio > industry_cash_to_net_income_ratio:
    print("The company exceeds the industry average in Cash to Net Income Ratio, suggesting a higher quality of earnings relative to its peers.")
elif company_cash_to_net_income_ratio == industry_cash_to_net_income_ratio:
    print("The company's Cash to Net Income Ratio aligns with the industry average, indicating a comparable quality of earnings.")
else:
    print("The company is below the industry average in Cash to Net Income Ratio, which might raise concerns about its earnings quality compared to its peers.")