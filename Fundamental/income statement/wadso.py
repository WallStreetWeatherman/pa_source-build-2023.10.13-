# Weighted Average Diluted Shares Outstanding Calculation
# -------------------------------------------------------
# Overview:
# This represents the average number of diluted shares over a specified period, 
# taking into account any changes in share count and potential dilutive securities.
#
# Desired Value:
# The impact of a rising or declining number of Weighted Average Diluted Shares Outstanding 
# depends on the context. Generally, a rising share count can dilute shareholder value 
# unless earnings growth is commensurate.
#
# Note: This script uses hard-coded values. For real-world application, data should be adjusted accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Example periods with hard-coded values (in months for this example, but could be quarters, etc.)
# Each tuple contains the period length and the average number of diluted shares during that period
# For example, for 2 months there were an average of 5 million diluted shares outstanding
periods = [
    (2, convert_to_actual_value(5.00)), 
    (4, convert_to_actual_value(5.50)),
    (3, convert_to_actual_value(6.00)),
    (3, convert_to_actual_value(5.75))
]

# Calculate the weighted average
total_period_length = sum(period[0] for period in periods)
weighted_average_diluted_shares = sum(period[0] * period[1] for period in periods) / total_period_length

# Output the result
print("Weighted Average Diluted Shares Outstanding Calculation:\n")
print("Weighted Average Diluted Shares: {:,.2f}".format(weighted_average_diluted_shares))

