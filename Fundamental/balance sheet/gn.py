# Graham Number Calculation
# -------------------------
# Overview:
# The Graham Number is a metric that provides an estimate of a stock's maximum fair price.
# It's derived from the book value per share and the earnings per share (EPS).
#
# Desired Value:
# A higher Graham Number relative to the current stock price may indicate that the stock is undervalued. 
# Conversely, if the stock price is significantly higher than the Graham Number, 
# it could suggest overvaluation.

import math

# Hardcoded values (in the format where 1 million is represented as 1.00, etc.)
book_value_per_share = 5.00  # For example, $5 million
earnings_per_share = 2.50   # For example, $2.5 million

def calculate_graham_number(bvps, eps):
    """Calculate the Graham Number based on book value per share and earnings per share."""
    return math.sqrt(22.5 * bvps * eps)

graham_number = calculate_graham_number(book_value_per_share, earnings_per_share)
print(f"Graham Number: ${graham_number:.2f} million")
