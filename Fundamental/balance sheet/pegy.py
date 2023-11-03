# PEGY Ratio Calculation
# ----------------------
# Overview:
# The PEGY (Price/Earnings to Growth and Dividend Yield) Ratio is an extension of the PEG ratio. 
# It takes into account both the projected earnings growth and the dividend yield of a company. 
# It is useful for valuing companies that return significant capital to shareholders through dividends.
#
# Desired Value:
# A lower PEGY ratio typically indicates an undervalued company, or less pay for each unit of earnings growth 
# and dividend yield. However, interpretation might vary depending on industry and other factors.

# Hardcoded values for the company
company_price_per_share = 50.00
company_earnings_per_share = 5.00
company_projected_growth = 0.10
company_dividend_yield = 0.04

# Hardcoded values for the industry average
industry_avg_price_per_share = 52.00
industry_avg_earnings_per_share = 5.20
industry_avg_projected_growth = 0.11
industry_avg_dividend_yield = 0.03

def calculate_pegy_ratio(price_per_share, earnings_per_share, projected_growth, dividend_yield):
    """Calculate the PEGY Ratio."""
    pe_ratio = price_per_share / earnings_per_share
    return pe_ratio / (projected_growth + dividend_yield)

company_pegy_ratio = calculate_pegy_ratio(company_price_per_share, company_earnings_per_share, company_projected_growth, company_dividend_yield)
industry_avg_pegy_ratio = calculate_pegy_ratio(industry_avg_price_per_share, industry_avg_earnings_per_share, industry_avg_projected_growth, industry_avg_dividend_yield)

print(f"Company's PEGY Ratio: {company_pegy_ratio:.2f}")
print(f"Industry Average PEGY Ratio: {industry_avg_pegy_ratio:.2f}")

# Interpretation
if company_pegy_ratio < industry_avg_pegy_ratio:
    print("The company's stock may be undervalued relative to the industry average, considering its earnings growth and dividend yield.")
elif company_pegy_ratio == industry_avg_pegy_ratio:
    print("The company's stock might be fairly priced compared to the industry average.")
else:
    print("The company's stock may be overvalued relative to the industry average, given its earnings growth and dividend yield.")
    