# Weighted Average Basic Shares Outstanding Calculation
# -----------------------------------------------------
# Overview:
# This represents the average number of basic shares over a specified period, 
# taking into account any changes in the share count.
#
# Desired Value:
# Generally, for an investor, a decreasing number of shares is preferred as it means 
# there's less dilution of ownership. However, understanding the context for why 
# shares are increasing or decreasing is essential (e.g., stock buybacks, secondary offerings).
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Example periods with hard-coded values (in months for this example, but could be quarters, etc.)
# Each tuple contains the period length and the average number of basic shares during that period
# For example, for 2 months there were an average of 5 million basic shares outstanding
periods = [
    (2, convert_to_actual_value(5.00)), 
    (4, convert_to_actual_value(5.25)),
    (3, convert_to_actual_value(5.40)),
    (3, convert_to_actual_value(5.20))
]

# Calculate the weighted average
total_period_length = sum(period[0] for period in periods)
weighted_average_basic_shares = sum(period[0] * period[1] for period in periods) / total_period_length

# Output the result
print("Weighted Average Basic Shares Outstanding Calculation:\n")
print("Weighted Average Basic Shares: {:,.2f}".format(weighted_average_basic_shares))

