# Price Per Share Calculation
# ---------------------------
# Overview:
# Price Per Share is calculated by dividing the company's market capitalization by its total number of outstanding shares.
# This gives you the price of a single share of the company's stock.
#
# Desired Value:
# Whether a high or low Price Per Share is beneficial depends on various factors, including the investor's strategy and 
# the company's valuation metrics. A high Price Per Share may indicate a more valuable company but may also suggest an 
# overvalued stock. On the other hand, a low Price Per Share might be a bargain but could also indicate a company in distress.
#
# Note: This script uses hard-coded values. For real-world application, input data should be sourced from financial
# statements and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def calculate_price_per_share(market_cap, outstanding_shares):
    """
    Calculate Price Per Share.
    
    Parameters:
    market_cap - Market capitalization of the company
    outstanding_shares - Number of outstanding shares of the company
    """
    return market_cap / outstanding_shares

# Hard-coded values for demonstration
market_cap = convert_to_actual_value(3141.00)  # Market capitalization of the company
outstanding_shares = convert_to_actual_value(273.63)  # Number of outstanding shares

price_per_share = calculate_price_per_share(market_cap, outstanding_shares)

# Output the result
print("Price Per Share Calculation:\n")
print("Calculated Price Per Share for the Company: {:.2f}".format(price_per_share))

# Interpretation based on desired value
if price_per_share >= 57:  # Replace 50 with any benchmark value for your industry
    print("The Price Per Share is relatively high, which could indicate a more valuable or overvalued company.")
else:
    print("The Price Per Share is relatively low, which may indicate a bargain or a company in distress.")
