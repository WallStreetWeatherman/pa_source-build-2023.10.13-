# Weighted Average Cost of Capital (WACC) Calculator
# ---------------------------------------------------
# Overview:
# The Weighted Average Cost of Capital (WACC) represents a firm's cost of capital from all sources, 
# weighted by the proportion of each source of capital in the firm's capital structure.
#
# Formula:
# WACC = (E / V) * Re + (D / V) * Rd * (1 - Tc)
#
# E = Market value of equity
# D = Market value of debt
# V = Total market value of a company's financed capital (E + D)
# Re = Cost of equity
# Rd = Cost of debt
# Tc = Corporate tax rate
#
# Desired Value:
# A lower WACC is generally preferable, as it indicates that a company is generating higher returns 
# against its cost of capital. However, extremely low WACC might indicate higher risks.
#

def convert_to_actual_value(value):
    """Converts the value in millions represented as 1.00, 10.00, etc., to its actual value."""
    return value * 1000000

# Hard-coded values (in millions for demonstration)
# For the Company
equity_company = convert_to_actual_value(3141.32)
debt_company = convert_to_actual_value(1047.11)
cost_of_equity_company = 0.07  # % as a decimal
cost_of_debt_company = 0.04   # % as a decimal
tax_rate_company = 0.2        # % as a decimal

# For the Industry Average
equity_industry = convert_to_actual_value(2000)
debt_industry = convert_to_actual_value(800)
cost_of_equity_industry = 0.08  # % as a decimal
cost_of_debt_industry = 0.05    # % as a decimal
tax_rate_industry = 0.2         # % as a decimal

# Calculating WACC
def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate):
    total_capital = equity + debt
    wacc = (equity / total_capital) * cost_of_equity + (debt / total_capital) * cost_of_debt * (1 - tax_rate)
    return wacc

# For the Company
wacc_company = calculate_wacc(equity_company, debt_company, cost_of_equity_company, cost_of_debt_company, tax_rate_company)
print(f"WACC for the Company: {wacc_company:.4f} or {wacc_company * 100:.2f}%")

# For the Industry
wacc_industry = calculate_wacc(equity_industry, debt_industry, cost_of_equity_industry, cost_of_debt_industry, tax_rate_industry)
print(f"WACC for the Industry: {wacc_industry:.4f} or {wacc_industry * 100:.2f}%")

# Comparative Analysis
if wacc_company < wacc_industry:
    print("The company has a lower WACC compared to the industry average, indicating a potential competitive advantage.")
else:
    print("The company has a higher or equal WACC compared to the industry, suggesting a need for improvement or caution.")
