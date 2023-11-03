# Contribution Margin Calculator
# ------------------------------
# Overview:
# The Contribution Margin measures the amount of sales that remain after deducting variable costs.
# It helps in understanding how much each sale contributes to fixed costs and profits.
#
# Formula:
# Contribution Margin = (Sales - Variable Costs) / Sales
#
# Desired Value:
# A higher contribution margin indicates that a larger portion of each sale is contributing 
# to fixed costs and profit. This suggests strong pricing or lower variable costs.
# A lower contribution margin indicates potential pricing challenges or higher variable costs.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# actual sales and variable costs values should be input.

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# For the company
sales_company = 50.00  # Example value representing $50 million
variable_costs_company = 20.00  # i.e COGS

# For the industry average
sales_industry = 45.00  # Example, you can replace this with actual values
variable_costs_industry = 18.00  # Example, you can replace this with actual values

def calculate_contribution_margin(sales, variable_costs):
    """Calculate the Contribution Margin based on sales and variable costs."""
    return (sales - variable_costs) / sales * 100  # Convert to percentage

# Calculate Contribution Margins
contribution_margin_company = calculate_contribution_margin(sales_company, variable_costs_company)
contribution_margin_industry = calculate_contribution_margin(sales_industry, variable_costs_industry)

# Output the results
print(f"Company's Contribution Margin: {contribution_margin_company:.2f}%")
print(f"Industry Average Contribution Margin: {contribution_margin_industry:.2f}%")

if contribution_margin_company > contribution_margin_industry:
    print("The company's contribution margin is above the industry average, indicating strong pricing or lower variable costs relative to peers.")
elif contribution_margin_company < contribution_margin_industry:
    print("The company's contribution margin is below the industry average, indicating potential pricing challenges or higher variable costs compared to peers.")
else:
    print("The company's contribution margin is in line with the industry average.")