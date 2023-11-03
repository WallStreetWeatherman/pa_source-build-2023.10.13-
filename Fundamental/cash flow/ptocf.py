# Price to Operating Cash Flow Ratio Calculation
# ----------------------------------------------
# Overview:
# The Price to Operating Cash Flow ratio compares a company's market cap to its operating cash flow.
# It assesses a company's ability to produce cash from its core business operations relative to its market value.
#
# Desired Value:
# A lower Price to Operating Cash Flow ratio may suggest that the company is undervalued relative to its cash-generating ability. 
# However, this interpretation may vary based on industry standards and market conditions.

# Hardcoded values for the company
company_market_cap = 3029.00 # Market Cap in Tikr
company_operating_cash_flow = 1615.00 # Cash from Operations in Tikr

# Hardcoded values for the industry average
industry_avg_market_cap = 44750.00  
industry_avg_operating_cash_flow = 803.00  

def calculate_pocf_ratio(market_cap, op_cash_flow):
    """Calculate Price to Operating Cash Flow Ratio."""
    return market_cap / op_cash_flow

company_pocf_ratio = calculate_pocf_ratio(company_market_cap, company_operating_cash_flow)
industry_avg_pocf_ratio = calculate_pocf_ratio(industry_avg_market_cap, industry_avg_operating_cash_flow)

print(f"Company's P/OCF Ratio: {company_pocf_ratio:.2f}")
print(f"Industry Average P/OCF Ratio: {industry_avg_pocf_ratio:.2f}")

# Interpretation
if company_pocf_ratio < industry_avg_pocf_ratio:
    print("\nThe company may be undervalued compared to the industry average based on its ability to generate operating cash flow.")
elif company_pocf_ratio == industry_avg_pocf_ratio:
    print("\nThe company's valuation is in line with the industry average based on its ability to produce operating cash flow.")
else:
    print("\nThe company may be overvalued compared to the industry average based on its cash-generating capabilities from operations.")
    