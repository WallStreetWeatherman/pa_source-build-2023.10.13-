# Excess Return Model Calculator
#
# Overview:
# The Excess Return Model focuses on the returns generated by a company relative to 
# its cost of capital. It aims to identify the extra value, beyond the expected return 
# from the cost of capital, that a company is creating for its shareholders.
#
# Desired Value:
# A positive Excess Return suggests that the company is generating a return higher 
# than its cost of capital, thereby creating true shareholder value. Conversely, a 
# negative Excess Return indicates that the company is not covering its cost of capital 
# and might be destroying shareholder value.

def excess_return(earnings, equity, cost_of_equity, debt, cost_of_debt, tax_rate):
    # Calculate the weighted average cost of capital (WACC)
    equity_ratio = equity / (equity + debt)
    debt_ratio = 1 - equity_ratio
    wacc = (equity_ratio * cost_of_equity) + (debt_ratio * cost_of_debt * (1 - tax_rate))
    
    # Calculate the Return on Invested Capital (ROIC)
    invested_capital = equity + debt
    roic = earnings / invested_capital
    
    # Calculate the Excess Return
    excess_return_value = (roic - wacc) * invested_capital

    # Convert the value to the desired format (1 million as 1.00)
    excess_return_value_millions = excess_return_value / 1_000_000
    return excess_return_value_millions

# Hardcoded example values
earnings = 20_000_000  # Example: $20 million in earnings
equity = 60_000_000  # Example: $60 million in equity
debt = 40_000_000  # Example: $40 million in debt
cost_of_equity = 0.08  # Example: 8% cost of equity
cost_of_debt = 0.05  # Example: 5% cost of debt
tax_rate = 0.3  # Example: 30% tax rate

excess_ret = excess_return(earnings, equity, cost_of_equity, debt, cost_of_debt, tax_rate)
print(f"Excess Return (in millions): ${excess_ret:.2f}")

# Remember to validate this model with other metrics and professional insights.