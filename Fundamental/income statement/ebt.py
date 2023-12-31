# EBT (Earnings Before Taxes) Calculation
# ---------------------------------------
# Overview:
# EBT represents a company's profit from all its activities before considering 
# income tax expenses. This measure provides a comprehensive picture of a company's 
# profitability excluding the influence of its tax strategy.
#
# Desired Value:
# A higher EBT suggests a company is generating significant profits from both 
# its operations and non-operating activities. However, comparing EBT values 
# within the same industry or sector is important for a relative understanding 
# of a company's performance.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values
revenues = convert_to_actual_value(200.00)       # Example: $200 million
cost_of_goods_sold = convert_to_actual_value(70.00)   # Example: $70 million
operating_expenses = convert_to_actual_value(50.00)  # Example: $50 million
interest_expense = convert_to_actual_value(10.00)    # Example: $10 million

# Calculate EBT
ebt = revenues - cost_of_goods_sold - operating_expenses - interest_expense

# Output the result
print("EBT (Earnings Before Taxes) Calculation:\n")
print("EBT: ${:,.2f}".format(ebt))
