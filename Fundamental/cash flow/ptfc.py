# Price to Free Cash Flow (P/FCF) Ratio
# -------------------------------------
# Overview:
# The P/FCF ratio is similar to the P/E ratio, but it uses Free Cash Flow instead of earnings. 
# This ratio measures the price investors are willing to pay for each dollar of free cash flow. 
# Free Cash Flow represents the cash that a company can generate after required investments 
# to maintain or expand its asset base. It's considered a reliable measure as it's harder 
# to manipulate compared to earnings.
#
# Desired Value:
# A lower P/FCF suggests that a company might be undervalued relative to its free cash flow 
# generation ability, while a higher P/FCF might indicate potential overvaluation. 
# However, the "good" or "bad" value can vary by industry and the overall market conditions.

# Hardcoded values for the company
company_market_cap = 3029.00 # Market Cap in Tikr
company_annual_free_cash_flow = 162.00 # Unlevered Free Cash Flow in Tikr Screener

# Hardcoded values for the industry average
industry_avg_market_cap = 44750.00  
industry_avg_free_cash_flow = 442.00  

def calculate_pfcf_ratio(market_cap, free_cash_flow):
    """Calculate the Price to Free Cash Flow ratio."""
    if free_cash_flow == 0:
        raise ValueError("Free cash flow should not be zero to calculate the P/FCF ratio.")
    return market_cap / free_cash_flow

company_pfcf_ratio = calculate_pfcf_ratio(company_market_cap, company_annual_free_cash_flow)
industry_avg_pfcf_ratio = calculate_pfcf_ratio(industry_avg_market_cap, industry_avg_free_cash_flow)

print(f"Company's P/FCF Ratio: {company_pfcf_ratio:.2f}")
print(f"Industry Average P/FCF Ratio: {industry_avg_pfcf_ratio:.2f}")

# Interpretation
if company_pfcf_ratio < industry_avg_pfcf_ratio:
    print("\nThe company may be undervalued compared to the industry average based on its P/FCF ratio.")
elif company_pfcf_ratio == industry_avg_pfcf_ratio:
    print("\nThe company's valuation is in line with the industry average based on its P/FCF ratio.")
else:
    print("\nThe company may be overvalued compared to the industry average based on its P/FCF ratio.")
    