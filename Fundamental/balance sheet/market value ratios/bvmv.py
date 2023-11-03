# Book Value-to-Market Value Calculation
# --------------------------------------
# Overview:
# The Book Value-to-Market Value ratio compares a company's book value to its market value. 
# This ratio can be used to identify potential mismatches between the accounting value 
# of a company (book value) and how the market perceives its value.
#
# Desired Value:
# A ratio below 1 might suggest that the market undervalues the company compared to its 
# book value. However, it's crucial to understand the broader context, like industry 
# dynamics, growth prospects, and other financial metrics before drawing conclusions.
#
# Note: This script uses hard-coded values. For real-world application, input data 
# should be sourced from financial statements and market data.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def bv_to_mv_ratio(book_value, market_value):
    """
    Calculate Book Value-to-Market Value ratio.
    
    Parameters:
    book_value - Company's book value (total assets minus total liabilities)
    market_value - Current market value or market capitalization of the company
    
    """
    return book_value / market_value

# Hard-coded values for demonstration:
book_value = convert_to_actual_value(4210.00)     # Book value of the company
market_value = convert_to_actual_value(3141.00)   # Market value (market capitalization) of the company

ratio = bv_to_mv_ratio(book_value, market_value)

# Output the result
print("Book Value-to-Market Value Calculation:\n")
print("Calculated BV/MV Ratio for the Company: {:.2f}".format(ratio))

# Interpretation based on desired value
if ratio < 1:
    print("The BV/MV Ratio is below 1, suggesting that the market may be undervaluing the company compared to its book value.")
elif ratio == 1:
    print("The BV/MV Ratio is 1, indicating that the market values the company in line with its book value.")
else:
    print("The BV/MV Ratio is above 1, suggesting that the market may be overvaluing the company compared to its book value.")
