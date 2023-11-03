# Expense Ratio Calculator
# -------------------------
# Overview:
# The Expense Ratio is a measure primarily used in the mutual fund industry. It represents 
# the annual operating expenses as a percentage of the average assets under management (AUM). 
# It provides an indication of the efficiency of a fund's management – the lower the expense ratio, 
# the less the fund's management is taking from its assets to run the fund.
#
# Formula:
# Expense Ratio = (Operating Expenses / Average AUM) x 100%
# 
# Desired Value:
# A lower Expense Ratio is generally more favorable for investors, as it implies lower operating 
# costs relative to the size of the fund. However, it should be compared with industry benchmarks and 
# the services provided by the fund.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual operating expenses and average assets under management should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# For the mutual fund
operating_expenses_fund = 2.50  # Example value representing $2.5 million
average_aum_fund = 100.00  # Example value representing $100 million

# Industry averages
operating_expenses_industry = 3.00  # Industry's average operating expenses in $ million
average_aum_industry = 125.00  # Industry's average assets under management in $ million

# Calculate Expense Ratio for the fund
expense_ratio_fund = (operating_expenses_fund / average_aum_fund) * 100

# Calculate Expense Ratio for the industry
expense_ratio_industry = (operating_expenses_industry / average_aum_industry) * 100

# Output the results
print(f"Fund's Expense Ratio: {expense_ratio_fund:.2f}%")
print(f"Industry Average Expense Ratio: {expense_ratio_industry:.2f}%")

if expense_ratio_fund < expense_ratio_industry:
    print("The fund's expense ratio is below the industry average, which can be favorable for investors.")
elif expense_ratio_fund > expense_ratio_industry:
    print("The fund's expense ratio is above the industry average. Investors might want to further investigate the reasons.")
else:
    print("The fund's expense ratio is in line with the industry average.")