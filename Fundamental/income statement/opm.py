# Operating Profit Margin Calculation
# -----------------------------------
# Overview:
# The Operating Profit Margin ratio indicates the percentage of profit a company earns from its operations
# before considering the effects of interest and taxes. This provides insights into operational profitability 
# without the influence of the company's financial structure.
#
# Desired Value:
# A higher Operating Profit Margin suggests that the company is more efficient at converting sales into 
# genuine profit. It's essential to compare this ratio with industry peers for a comprehensive interpretation.

# Hardcoded values for the company (using the format where 1 million is represented as 1.00, etc.)
company_sales = 23606.00 # Revenues in Tikr
company_operating_expenses = 8337.00  # Operating Expenses in Tikr

# Hardcoded values for the industry
industry_sales_avg = 4840.00     
industry_operating_expenses_avg = 1350.00 

def calculate_operating_profit_margin(sales, op_expenses):
    """Calculate Operating Profit Margin as a percentage."""
    operating_profit = sales - op_expenses
    return (operating_profit / sales) * 100

company_op_margin = calculate_operating_profit_margin(company_sales, company_operating_expenses)

# Calculate industry average operating profit margin
industry_avg_op_margin = calculate_operating_profit_margin(industry_sales_avg, industry_operating_expenses_avg)

print(f"Company's Operating Profit Margin: {company_op_margin:.2f}%")
print(f"Industry Average Operating Profit Margin: {industry_avg_op_margin:.2f}%")

# Interpretation
if company_op_margin > industry_avg_op_margin:
    print("The company's Operating Profit Margin is above the industry average, indicating strong operational efficiency.")
elif company_op_margin == industry_avg_op_margin:
    print("The company's Operating Profit Margin aligns with the industry average.")
else:
    print("The company's Operating Profit Margin is below the industry average. This suggests potential operational inefficiencies or challenges in pricing.")
    