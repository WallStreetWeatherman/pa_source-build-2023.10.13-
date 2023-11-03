# Operating Cash Flow Calculator
# ------------------------------
# Overview:
# The Operating Cash Flow (OCF) indicates the cash generated from the core operations of a business.
# It serves as a key indicator of the health and profitability of a business's primary activities.
#
# Formula:
# Operating Cash Flow (OCF) = Earnings Before Interest and Taxes (EBIT) + Depreciation - Taxes - Change in Working Capital
#
# Note: The change in working capital is the difference between current assets and current liabilities 
# from one period to the next.
#
# Desired Value:
# A positive OCF suggests that the company is generating enough cash from its core operations to maintain 
# and grow the business. A negative OCF may indicate challenges in the company's primary operational profitability.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings Before Interest and Taxes (EBIT) (in million dollars format for simplicity)
ebit_in_millions = 451.00  # Example value representing 20 million dollars
ebit = convert_to_actual_value(ebit_in_millions)

# Depreciation (in million dollars format for simplicity)
depreciation_in_millions = 620.00  # Example value representing 2 million dollars
depreciation = convert_to_actual_value(depreciation_in_millions)

# Taxes (in million dollars format for simplicity)
taxes_in_millions = 365.00  # 'cash taxes paid' in tikr
taxes = convert_to_actual_value(taxes_in_millions)

# Change in Working Capital (in million dollars format for simplicity)
change_in_working_capital_in_millions = -208.00  # Example value representing a decrease of 1 million dollars
change_in_working_capital = convert_to_actual_value(change_in_working_capital_in_millions)

# Calculate Operating Cash Flow
ocf = ebit + depreciation - taxes - change_in_working_capital

# Output the results
print(f"Operating Cash Flow (OCF): ${ocf/1000000:.2f} million")

if ocf > 0:
    print("The company is generating a positive cash flow from its core operations.")
else:
    print("The company is facing challenges in generating cash from its core operations.")
