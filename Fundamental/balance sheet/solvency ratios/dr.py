# Debt Ratio Calculator
# ---------------------
# Overview:
# The Debt Ratio measures the proportion of a company's assets that are financed by debt. 
# It provides an indication of the company's financial leverage and ability to cover its 
# liabilities with its assets.
#
# Formula:
# Debt Ratio = Total Liabilities / Total Assets
#
# Desired Value:
# A higher Debt Ratio indicates that a larger proportion of the company's assets are 
# financed by debt, which can be riskier. A lower ratio suggests that the company relies 
# more on equity to finance its assets, which can be seen as safer. However, a very low 
# ratio might suggest that the company is not leveraging its assets to its fullest potential.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Total Assets (in million dollars format for simplicity)
total_assets_in_millions = 16304.00  # Example value representing 100 million dollars
total_assets = convert_to_actual_value(total_assets_in_millions)

# Total Liabilities (in million dollars format for simplicity)
total_liabilities_in_millions = 12094.00  # Example value representing 60 million dollars
total_liabilities = convert_to_actual_value(total_liabilities_in_millions)

# Calculate Debt Ratio
debt_ratio = total_liabilities / total_assets

# Output the results
print(f"Debt Ratio: {debt_ratio:.2f}")

if debt_ratio > 0.5:
    print("More than half of the company's assets are financed by debt. This can be seen as riskier, especially if the firm encounters financial challenges.")
else:
    print("The majority of the company's assets are financed through equity. This can be seen as safer, though the company might not be fully leveraging its assets.")
