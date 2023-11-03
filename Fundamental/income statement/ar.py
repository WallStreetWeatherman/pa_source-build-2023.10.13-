# Accruals Ratio Calculator
# -------------------------
# Overview:
# The Accruals Ratio helps assess the quality of a company's earnings by comparing the difference between net income 
# and operating cash flow relative to total assets. A higher ratio can signal aggressive accounting practices, 
# such as prematurely recognizing revenue or delaying expense recognition.
#
# Formula:
# Accruals Ratio = (Net Income - Operating Cash Flow) / Total Assets
#
# Desired Value:
# Ideally, the Accruals Ratio should be low, as this would indicate that most of the company's earnings are backed 
# by actual cash flows. A high Accruals Ratio can be a red flag, signaling that earnings might not be as reliable or sustainable.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Net Income for the period (in $1M)
net_income = 1177.00  # Net Income in Tikr

# Operating Cash Flow for the period (in $1M)
operating_cash_flow = 1615.00  # Cash from Operations in Tikr

# Total Assets (in $1M)
total_assets = 16866.00  # Total Assest in Tikr

# Industry Average values (hypothetical for this example)
industry_avg_net_income = 324.00
industry_avg_operating_cash_flow = 803.00
industry_avg_total_assets = 7390.00

# Calculate Accruals Ratio
def calculate_accruals_ratio(net_income, operating_cash_flow, total_assets):
    """Calculate Accruals Ratio."""
    return (net_income - operating_cash_flow) / total_assets

company_accruals_ratio = calculate_accruals_ratio(net_income, operating_cash_flow, total_assets)
industry_accruals_ratio = calculate_accruals_ratio(industry_avg_net_income, industry_avg_operating_cash_flow, industry_avg_total_assets)

# Output the results
print(f"Company's Accruals Ratio: {company_accruals_ratio:.2%}")
print(f"Industry Average Accruals Ratio: {industry_accruals_ratio:.2%}")

if company_accruals_ratio > industry_accruals_ratio:
    print("\nThe company's Accruals Ratio is higher than the industry average, which could indicate potential issues with the quality of earnings.")
elif company_accruals_ratio == industry_accruals_ratio:
    print("\nThe company's Accruals Ratio aligns with the industry average.")
else:
    print("\nThe company's Accruals Ratio is lower than the industry average, suggesting that the quality of its earnings might be more reliable than peers in the industry.")
    
