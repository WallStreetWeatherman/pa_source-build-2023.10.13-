# Relative Value Methods
# ----------------------
# Overview:
# The relative value method compares the company to other firms in the same industry or sector.
# Metrics like the Price-to-Sales (P/S) and Price-to-Free-Cash-Flow (P/FCF) ratios are used, 
# especially when earnings might not be a reliable indicator of value.
#
# Desired Value:
# A lower P/S or P/FCF ratio can indicate potential undervaluation compared to peers.
# However, industry and sector averages should be considered for a comprehensive analysis.

# Hardcoded values for the company
company_sales = 24442.00 # Revenues in Tikr
company_free_cash_flow = 162.00 # Unlevered Free Cash Flow in Tikr Screener
company_market_cap = 3029.00 # Market Cap in Tikr

# Hardcoded values for industry average (hypothetical values for this example)
industry_avg_sales = 4840.00  
industry_avg_free_cash_flow = 442.00  
industry_avg_market_cap = 44750.00  

# Calculate Price-to-Sales (P/S) ratio
def calculate_ps_ratio(market_cap, sales):
    """Calculate P/S ratio."""
    return market_cap / sales

# Calculate Price-to-Free-Cash-Flow (P/FCF) ratio
def calculate_pfcf_ratio(market_cap, free_cash_flow):
    """Calculate P/FCF ratio."""
    return market_cap / free_cash_flow

# Company's calculations
company_ps_ratio = calculate_ps_ratio(company_market_cap, company_sales)
company_pfcf_ratio = calculate_pfcf_ratio(company_market_cap, company_free_cash_flow)

# Industry's calculations
industry_avg_ps_ratio = calculate_ps_ratio(industry_avg_market_cap, industry_avg_sales)
industry_avg_pfcf_ratio = calculate_pfcf_ratio(industry_avg_market_cap, industry_avg_free_cash_flow)

print(f"Company's Price-to-Sales (P/S) Ratio: {company_ps_ratio:.2f}")
print(f"Company's Price-to-Free-Cash-Flow (P/FCF) Ratio: {company_pfcf_ratio:.2f}")
print(f"\nIndustry Average Price-to-Sales (P/S) Ratio: {industry_avg_ps_ratio:.2f}")
print(f"Industry Average Price-to-Free-Cash-Flow (P/FCF) Ratio: {industry_avg_pfcf_ratio:.2f}")

# Interpretation
if company_ps_ratio < industry_avg_ps_ratio:
    print("\nBased on P/S, the company might be undervalued compared to the industry average.")
else:
    print("\nBased on P/S, the company seems fairly valued or overvalued compared to the industry average.")

if company_pfcf_ratio < industry_avg_pfcf_ratio:
    print("Based on P/FCF, the company might be undervalued compared to the industry average.")
else:
    print("Based on P/FCF, the company seems fairly valued or overvalued compared to the industry average.")
    
