# Times Interest Earned Ratio (TIE) Calculator
# -------------------------------------------
# Overview:
# The Times Interest Earned Ratio (TIE) is a measure of a company's ability to cover its interest expenses with its operating income.
# It helps investors and analysts understand how comfortably a company can pay interest on its outstanding debt.
# The TIE is often referred to as the interest coverage ratio and used interchangeably.
#
# Formula:
# TIE = Operating Income / Interest Expense
#
# Desired Value:
# A higher TIE value indicates a better ability to cover interest expenses. A lower value may suggest potential difficulty in meeting interest obligations.
#

# Company's data:
operating_income_company = 1681.00 # operating income in tikr
interest_expense_company = 175.00 # interest expense in tikr

# Industry average data:
operating_income_industry = 479.00
interest_expense_industry = 37.00

# Company's TIE calculation
TIE_company = operating_income_company / interest_expense_company

# Industry average TIE calculation
TIE_industry = operating_income_industry / interest_expense_industry

# Display results
print(f"Company's Operating Income (in $1M): ${operating_income_company:.2f}M")
print(f"Company's Interest Expense (in $1M): ${interest_expense_company:.2f}M")
print(f"Company's Times Interest Earned Ratio (TIE): {TIE_company:.2f}\n")

print(f"Industry Average Operating Income (in $1M): ${operating_income_industry:.2f}M")
print(f"Industry Average Interest Expense (in $1M): ${interest_expense_industry:.2f}M")
print(f"Industry Average Times Interest Earned Ratio (TIE): {TIE_industry:.2f}\n")

if TIE_company > TIE_industry:
    print("The company's TIE is above the industry average, signifying a robust capacity to meet interest obligations.")
elif TIE_company < TIE_industry:
    print("The company's TIE is below the industry average, suggesting potential challenges in covering interest expenses.")
else:
    print("The company's TIE aligns with the industry average.")