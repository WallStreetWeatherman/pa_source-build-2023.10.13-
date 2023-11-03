# Earnings Yield Calculator
# -------------------------
# Overview:
# The Earnings Yield is a financial metric that indicates how much a company earns for each dollar of its stock price.
# It's essentially the inverse of the Price-to-Earnings (P/E) ratio.
#
# Formula:
# Earnings Yield = Earnings per Share (EPS) / Price per Share
#
# Desired Value:
# A higher Earnings Yield can indicate that a stock is undervalued and may represent a better value to investors.
# A lower Earnings Yield may suggest that a stock is overvalued relative to its earnings.
# 
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Earnings per Share (EPS) (This might be in dollars and cents format, so no conversion may be needed, but we'll consider it in millions for this example)
eps_in_millions = 2.74  # Example value representing an EPS of $50,000
eps = convert_to_actual_value(eps_in_millions)

# Price per Share (in million dollars format)
price_per_share_in_millions = 11.48  # Example value representing $1,000,000 for a share price
price_per_share = convert_to_actual_value(price_per_share_in_millions)

# Calculate Earnings Yield
earnings_yield = eps / price_per_share

# Output the results
print(f"Earnings Yield: {earnings_yield:.2%}")

if earnings_yield > 0.05:  # 5% as a threshold
    print("The stock has a high Earnings Yield, which might suggest it's undervalued relative to its earnings.")
else:
    print("The stock has a low Earnings Yield, which could suggest it's overvalued relative to its earnings.")
