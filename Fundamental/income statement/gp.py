# Gross Profit Calculation
# -------------------------
# Overview:
# Gross profit indicates the total sales revenue after accounting for the direct costs of producing 
# and selling the goods (Cost of Goods Sold - COGS). It's a fundamental measure to understand a 
# company's profitability before other operating costs, interest, and taxes.
#
# Desired Value:
# Generally, a higher gross profit indicates more funds available to cover operating expenses 
# and generate net income. A low gross profit can signify thin margins or issues with production costs. 
# Therefore, a high value is usually preferable.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded values for the company:
revenues_company = convert_to_actual_value(24442.00)  # Revenues from primary operations
cogs_company = convert_to_actual_value(15306.00)  # Cost of Goods Sold in Tikr

# Industry average values:
revenues_industry = convert_to_actual_value(4840.00)  # Industry average revenues
cogs_industry = convert_to_actual_value(3060.00)  # Industry average Cost of Goods Sold

# Gross profit calculation for the company
gross_profit_company = revenues_company - cogs_company

# Gross profit calculation for the industry average
gross_profit_industry = revenues_industry - cogs_industry

# Output the results
print("Gross Profit Calculation:\n")
print("Company's Gross Profit: ${:,.2f} million".format(gross_profit_company / 1000000))
print("Industry Average Gross Profit: ${:,.2f} million".format(gross_profit_industry / 1000000))

if gross_profit_company > gross_profit_industry:
    print("The company's gross profit is above the industry average, indicating better operational profitability.")
elif gross_profit_company < gross_profit_industry:
    print("The company's gross profit is below the industry average, suggesting potential issues with production costs or pricing.")
else:
    print("The company's gross profit aligns with the industry average, indicating a standard operational performance compared to its peers.")
