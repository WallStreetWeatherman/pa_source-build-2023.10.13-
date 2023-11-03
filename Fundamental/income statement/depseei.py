# Diluted EPS Excluding Extraordinary Items Calculation
# -----------------------------------------------------
# Overview:
# Diluted EPS Excluding Extraordinary Items offers a clearer picture of a company's profitability 
# by considering only core operations and excluding one-time, non-recurring items.
# It takes into account potential shares that could come into existence, like from stock options.
#
# Desired Value:
# A higher Diluted EPS Excl. Extra Items is preferable, as it indicates greater profitability 
# and more earnings available for shareholders. Conversely, a declining EPS might signify potential problems.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values for demonstration:
net_income = convert_to_actual_value(20.00)  # Net income of the company
extraordinary_items = convert_to_actual_value(5.00)  # Extraordinary items value
diluted_shares_outstanding = convert_to_actual_value(10.00)  # Diluted number of shares outstanding

# Diluted EPS calculation excluding extraordinary items
diluted_eps_excl_extra_items = (net_income - extraordinary_items) / diluted_shares_outstanding

# Output the result
print("Diluted EPS Excluding Extraordinary Items Calculation:\n")
print("Diluted EPS Excl. Extra Items: ${:,.2f} per share".format(diluted_eps_excl_extra_items))

