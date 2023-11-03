# Net Operating Income (NOI) Analysis
# -----------------------------------
# Overview:
# Net Operating Income (NOI) is the income generated from the core business operations, excluding other forms of income and expenses.
# It provides a measure of a company's operating performance.
#
# Desired Value:
# A higher NOI is generally favorable, indicating strong operational efficiency. A lower NOI may require further analysis.
#
# Note: This script uses hard-coded values. For real-world application, data should be fetched and updated accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values for the company
company_revenue = convert_to_actual_value(23606.00)  # Example: $23,606 million in revenue
company_total_operating_expenses = convert_to_actual_value(8337.00)  # Example: $8,337 million in total operating expenses

# Calculating Net Operating Income for the company
company_net_operating_income = company_revenue - company_total_operating_expenses

# Hard-coded values for industry average
industry_average_revenue = convert_to_actual_value(22000.00)  # Example: $22,000 million as industry average revenue
industry_average_total_operating_expenses = convert_to_actual_value(8100.00)  # Example: $8,100 million as industry average total operating expenses

# Calculating Net Operating Income for the industry
industry_net_operating_income = industry_average_revenue - industry_average_total_operating_expenses

# Output the result
print("Net Operating Income (NOI) Analysis:\n")
print(f"Company's NOI based on given assumptions: ${company_net_operating_income / 1000000:.2f} million")
print(f"Industry Average NOI: ${industry_net_operating_income / 1000000:.2f} million")

# Comparison with the industry average
if company_net_operating_income > industry_net_operating_income:
    print("The company's NOI exceeds the industry average, indicating a strong operational performance relative to peers.")
else:
    print("The company's NOI is below the industry average. It's essential to understand the reasons and areas of potential improvement.")
