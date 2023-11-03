# Price to Earnings Growth (PEG) Ratio Calculation
# ------------------------------------------------
# Overview:
# The PEG ratio takes the P/E ratio and divides it by the projected growth in earnings. 
# It provides a more nuanced view of a stock's value by accounting for its growth potential.
#
# Desired Value:
# A lower PEG suggests that a stock may be undervalued given its earnings performance and future growth outlook.
# Typically, a PEG less than 1 might be considered undervalued, though context and industry specifics matter.

# Hardcoded values for the company
company_price_per_share = 50.00
company_earnings_per_share = 5.00
company_projected_growth_rate = 0.20

# Hardcoded values for the industry average
industry_avg_price_per_share = 50.50
industry_avg_earnings_per_share = 5.05
industry_avg_projected_growth_rate = 0.20

def calculate_pe_ratio(price, eps):
    """Calculate Price to Earnings Ratio."""
    return price / eps

def calculate_peg_ratio(pe_ratio, growth_rate):
    """Calculate Price to Earnings Growth Ratio."""
    return pe_ratio / growth_rate

company_pe_ratio = calculate_pe_ratio(company_price_per_share, company_earnings_per_share)
company_peg_ratio = calculate_peg_ratio(company_pe_ratio, company_projected_growth_rate)

industry_avg_pe_ratio = calculate_pe_ratio(industry_avg_price_per_share, industry_avg_earnings_per_share)
industry_avg_peg_ratio = calculate_peg_ratio(industry_avg_pe_ratio, industry_avg_projected_growth_rate)

print(f"Company's P/E Ratio: {company_pe_ratio:.2f}")
print(f"Company's PEG Ratio: {company_peg_ratio:.2f}")
print(f"Industry Average P/E Ratio: {industry_avg_pe_ratio:.2f}")
print(f"Industry Average PEG Ratio: {industry_avg_peg_ratio:.2f}")

# Interpretation
if company_peg_ratio < industry_avg_peg_ratio:
    print(f"The company's stock appears to be undervalued compared to the industry average, given its earnings performance and future growth outlook.")
elif company_peg_ratio == industry_avg_peg_ratio:
    print(f"The company's stock appears to be fairly valued compared to the industry average.")
else:
    print(f"The company's stock may be overvalued compared to the industry average based on its growth prospects.")
    