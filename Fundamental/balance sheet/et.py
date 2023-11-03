# Equity Turnover Calculator
# --------------------------
# Overview:
# The Equity Turnover ratio provides insight into the effectiveness with which a company 
# utilizes its equity to generate revenue. It's an important metric in assessing operational 
# efficiency and investment attractiveness.
#
# Formula:
# Equity Turnover = Net Sales / Average Shareholder's Equity
#
# Desired Value:
# A high equity turnover ratio suggests that a company is effectively using its equity to 
# generate sales. Conversely, a low ratio may indicate inefficiency or over-capitalization.
# It's crucial to compare the ratio with industry benchmarks as standards can vary.
#

# Hard-coded values in millions as decimals (e.g., 1.00 is $1 million)

# Net Sales for the period (in $1M)
net_sales = 749.00  

# Average Shareholder's Equity for the period (in $1M)
# This can be calculated as (Beginning Equity + Ending Equity) / 2
beginning_equity = 6436.00  
ending_equity = 4082.00  
average_equity = (beginning_equity + ending_equity) / 2

# Calculate Equity Turnover for the company
equity_turnover = net_sales / average_equity

# Industry average hard-coded values (in millions as decimals)
industry_avg_net_sales = 700.00  # Example value
industry_avg_beginning_equity = 6000.00  # Example value
industry_avg_ending_equity = 4200.00  # Example value
industry_avg_equity = (industry_avg_beginning_equity + industry_avg_ending_equity) / 2

# Calculate Industry Average Equity Turnover
industry_avg_equity_turnover = industry_avg_net_sales / industry_avg_equity

# Output the results
print(f"Net Sales (in $1M): ${net_sales:.2f}M")
print(f"Average Shareholder's Equity (in $1M): ${average_equity:.2f}M")
print(f"Company's Equity Turnover: {equity_turnover:.2f} times")
print(f"Industry Average Equity Turnover: {industry_avg_equity_turnover:.2f} times")

if equity_turnover > industry_avg_equity_turnover:
    print("The company's Equity Turnover is above the industry average, indicating effective utilization of shareholder equity to generate sales compared to peers.")
elif equity_turnover == industry_avg_equity_turnover:
    print("The company's Equity Turnover matches the industry average.")
else:
    print("The company's Equity Turnover is below the industry average, suggesting potential inefficiency or over-capitalization in using equity to drive sales compared to peers.")
