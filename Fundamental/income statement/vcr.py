# Variable Cost Ratio Calculator
# ------------------------------
# Overview:
# The Variable Cost Ratio reveals the proportion of total revenue consumed by variable costs.
# This metric helps businesses understand the relationship between sales and the direct costs of producing those sales.
# By examining the variable cost ratio, businesses can get a clearer picture of their cost structure and profit potential at different sales levels.
#
# Formula:
# Variable Cost Ratio = Variable Costs / Total Revenue
#
# Desired Value:
# A lower Variable Cost Ratio indicates that a smaller portion of revenue is used up by variable costs, which can signal higher profitability per sale.
# A higher ratio may suggest thinner margins, especially if fixed costs are also significant.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual variable costs and total revenue values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Variable Costs for the period (in $1M)
variable_costs = 7.00  # Example value representing $7 million

# Total Revenue for the period (in $1M)
total_revenue = 25.00  # Example value representing $25 million

# Calculate Variable Cost Ratio
variable_cost_ratio = variable_costs / total_revenue

# Output the results
print(f"Variable Costs (in $1M): ${variable_costs:.2f}M")
print(f"Total Revenue (in $1M): ${total_revenue:.2f}M")
print(f"Variable Cost Ratio: {variable_cost_ratio:.2%}")
print("A lower Variable Cost Ratio suggests a smaller portion of revenue is consumed by variable costs, which can lead to higher profitability.")

