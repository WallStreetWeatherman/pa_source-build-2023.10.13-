# Earnings Per Share (EPS) Calculation with Industry Comparison
# -------------------------------------------------------------
# Overview:
# Earnings Per Share (EPS) gauges the profit a company earns for each outstanding common stock share.
# It's derived by dividing the net income by the volume of outstanding shares.
#
# Desired Value:
# Generally, a more substantial EPS denotes better value since investors will offer more for a company's 
# stock if they anticipate the company to have a more significant profit relative to its share cost.
#
# Note: This script uses hard-coded values. For actual application, values should be extracted from financial
# reports and market data.

def convert_to_actual_value(value):
    """Converts the value where 1.00 represents $1 million into its actual value."""
    return value * 1000000

def calculate_eps(net_income, outstanding_shares):
    """
    Calculate Earnings Per Share (EPS).
    
    Parameters:
    - net_income (float): Company's net income
    - outstanding_shares (float): Count of outstanding shares
    Returns:
    - float: Calculated EPS
    """
    return net_income / outstanding_shares if outstanding_shares != 0 else 0

# Company hard-coded values for demonstration
net_income = convert_to_actual_value(749.00)  # Net income of the company in actual value
outstanding_shares = convert_to_actual_value(273.63)  # Number of outstanding shares in actual value

# Industry average hard-coded values for demonstration
industry_avg_net_income = convert_to_actual_value(700.00)  
industry_avg_outstanding_shares = convert_to_actual_value(250.00)  

# Calculating company and industry average EPS
company_eps = calculate_eps(net_income, outstanding_shares)
industry_eps = calculate_eps(industry_avg_net_income, industry_avg_outstanding_shares)

# Output the results and comparison
print("Earnings Per Share Calculation:\n")
print("Calculated EPS for the Company: {:.2f}".format(company_eps))
print("Industry Average EPS: {:.2f}".format(industry_eps))

# Interpretation based on desired value
if company_eps > industry_eps:
    print("The company's EPS is above the industry average, suggesting it may offer better value relative to its peers.")
elif company_eps == industry_eps:
    print("The company's EPS aligns with the industry average.")
else:
    print("The company's EPS is below the industry average, indicating it might be lagging in profitability relative to its peers.")
