# Tax Expense Ratio Calculator
# ----------------------------
# Overview:
# The Tax Expense Ratio indicates the proportion of a company's profits that are paid out as taxes. 
# It provides an insight into the company's tax efficiency and its effective tax rate.
#
# Formula:
# Tax Expense Ratio = Tax Expense / Pre-Tax Income
#
# Desired Value:
# The Tax Expense Ratio provides an understanding of the tax burden on a company's profits. 
# While a low ratio indicates tax efficiency, it could also result from tax incentives, credits, 
# or aggressive tax strategies. A ratio that's too low might signal unsustainably aggressive 
# tax avoidance which can be risky.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Pre-Tax Income for the period (in $1M)
pre_tax_income = 10.00  # Example value representing $10 million

# Tax Expense for the period (in $1M)
tax_expense = 2.50  # Example value representing $2.5 million paid as taxes

# Calculate Tax Expense Ratio
tax_expense_ratio = tax_expense / pre_tax_income

# Output the results
print(f"Pre-Tax Income (in $1M): ${pre_tax_income:.2f}M")
print(f"Tax Expense (in $1M): ${tax_expense:.2f}M")
print(f"Tax Expense Ratio: {tax_expense_ratio:.2%}")
print("This ratio gives insight into the effective tax rate the company is experiencing relative to its earnings.")

