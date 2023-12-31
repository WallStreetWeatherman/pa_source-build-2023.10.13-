# Equity Growth Rate Calculator
# -----------------------------
# Overview:
# The Equity Growth Rate measures the annual rate of growth of shareholders' equity.
# It helps investors understand how effectively a company's management is using shareholders' funds to generate profit.
#
# Formula:
# Equity Growth Rate = [(Equity in Current Period - Equity in Previous Period) / Equity in Previous Period] x 100
#
# Desired Value:
# A high equity growth rate suggests that the company is effectively using shareholders' 
# equity to generate profits and grow the business. However, growth that's too high might not be sustainable.
# On the contrary, a declining or negative rate might point to inefficient use of shareholders' equity.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications, 
# actual financial data values should be input.

# Convert amounts where 1 million dollars is represented as 1.00, 10 million as 10.00, etc.
def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values

# Equity in Previous Period (in million dollars format)
equity_previous_period_in_millions = 10.00  # Example value representing equity of $10,000,000 in the previous period
equity_previous_period = convert_to_actual_value(equity_previous_period_in_millions)

# Equity in Current Period (in million dollars format)
equity_current_period_in_millions = 12.50  # Example value representing equity of $12,500,000 in the current period
equity_current_period = convert_to_actual_value(equity_current_period_in_millions)

# Calculate Equity Growth Rate
if equity_previous_period == 0:
    equity_growth_rate = 0
else:
    equity_growth_rate = ((equity_current_period - equity_previous_period) / equity_previous_period) * 100

# Output the results
print(f"Equity Growth Rate: {equity_growth_rate:.2f}%")

if equity_growth_rate > 0:  
    print("The company's equity is growing, suggesting efficient utilization of shareholders' capital.")
elif equity_growth_rate == 0:
    print("The company's equity remains consistent.")
else:
    print("The company's equity is declining, which may indicate challenges in utilizing shareholders' funds.")
