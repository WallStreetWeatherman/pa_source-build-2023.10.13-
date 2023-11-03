# FCF Yield Calculation
# ---------------------
# Overview:
# The FCF Yield measures the firm's ability to generate cash relative to its size.
# It is calculated by dividing the company's Free Cash Flow by its Market Capitalization.

# Hardcoded values for the company (in the format where 1 million is represented as 1.00, etc.)
company_free_cash_flow = 5.00  # Company's Free Cash Flow (e.g., $5 million)
company_market_cap = 100.00    # Company's Market Capitalization (e.g., $100 million)

# Hardcoded industry average values
industry_average_free_cash_flow = 60.00  # Industry's Average Free Cash Flow (e.g., $60 million)
industry_average_market_cap = 1200.00  # Industry's Average Market Capitalization (e.g., $1200 million)

# Calculate FCF Yield
def calculate_fcf_yield(free_cash_flow, market_cap):
    """Calculate the Free Cash Flow Yield based on the free cash flow and market cap."""
    return free_cash_flow / market_cap

company_fcf_yield = calculate_fcf_yield(company_free_cash_flow, company_market_cap)
industry_fcf_yield = calculate_fcf_yield(industry_average_free_cash_flow, industry_average_market_cap)

print(f"Company's Free Cash Flow (FCF) Yield: {company_fcf_yield:.2f} or {company_fcf_yield*100:.2f}%")
print(f"Industry Average FCF Yield: {industry_fcf_yield:.2f} or {industry_fcf_yield*100:.2f}%")

# Interpretation
if company_fcf_yield > industry_fcf_yield:
    print("The company's FCF Yield is above the industry average, suggesting it might be undervalued relative to its peers.")
elif company_fcf_yield == industry_fcf_yield:
    print("The company's FCF Yield is in line with the industry average.")
else:
    print("The company's FCF Yield is below the industry average, indicating it might be overvalued compared to its peers.")
