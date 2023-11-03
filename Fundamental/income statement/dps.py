# Dividends Per Share Calculation
# -------------------------------
# Overview:
# Dividends Per Share (DPS) represents the total dividends paid out over a year 
# per share of outstanding stock. It provides insights into a company's profitability 
# and its policy of returning cash to shareholders.
#
# Desired Value:
# A higher DPS suggests a company's strong profitability and willingness to 
# return cash to shareholders. However, an exceptionally high and unsustainable 
# DPS might indicate a lack of investment in future growth.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values
total_dividends_paid = convert_to_actual_value(10.00)  # Example: $10 million in total dividends paid
total_shares_outstanding = convert_to_actual_value(1.50) # Example: 1.5 million shares outstanding

# Calculate Dividends Per Share
dps = total_dividends_paid / total_shares_outstanding

# Output the result
print("Dividends Per Share Calculation:\n")
print("Dividends Per Share (DPS): ${:,.2f}".format(dps))
