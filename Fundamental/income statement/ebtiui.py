# EBT Including Unusual Items Calculation
# ---------------------------------------
# Overview:
# EBT Including Unusual Items accounts for a company's profit before taxes 
# with the addition of non-recurring or unusual items. It gives a comprehensive 
# view of a company's earnings during periods when these one-off events occurred.
#
# Desired Value:
# Generally, a higher EBT suggests better profitability, but the inclusion of 
# unusual items can distort the underlying operating performance. It's crucial 
# to understand the nature of the unusual items and their impact on reported 
# earnings when analyzing this metric.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values
revenues = convert_to_actual_value(250.00)           # Example: $250 million
cost_of_goods_sold = convert_to_actual_value(80.00)   # Example: $80 million
operating_expenses = convert_to_actual_value(60.00)   # Example: $60 million
interest_expense = convert_to_actual_value(10.00)     # Example: $10 million
unusual_items = convert_to_actual_value(-15.00)       # Example: -$15 million (e.g., loss from asset sale)

# Calculate EBT Including Unusual Items
ebt_incl_unusual = revenues - cost_of_goods_sold - operating_expenses - interest_expense + unusual_items

# Output the result
print("EBT (Earnings Before Taxes) Including Unusual Items Calculation:\n")
print("EBT Including Unusual Items: ${:,.2f}".format(ebt_incl_unusual))
