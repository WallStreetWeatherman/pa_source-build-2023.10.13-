# Price to Research Ratio Calculation
# -----------------------------------
# Overview:
# The Price to Research Ratio provides insights into a company's valuation relative to its investment in research and development (R&D). 
# For companies where R&D is a significant factor, this ratio might be a better indicator of value than traditional P/E ratios.
#
# Desired Value:
# A lower Price to Research Ratio could indicate that the company is undervalued given its investment in R&D, 
# suggesting potential upside. Conversely, a higher ratio may signal overvaluation. However, it's important 
# to compare this ratio with peers in the same industry for meaningful insights.

# Hardcoded values for the company
current_market_cap = 100.00
annual_r_and_d_expenditure = 5.00

# Hardcoded values for the industry average
industry_avg_market_cap = 105.00  # Assuming for the sake of example
industry_avg_r_and_d_expenditure = 5.50  # Assuming for the sake of example

def calculate_price_to_research(market_cap, r_and_d):
    """Calculate Price to Research Ratio."""
    return market_cap / r_and_d

company_price_to_research_ratio = calculate_price_to_research(current_market_cap, annual_r_and_d_expenditure)
industry_avg_price_to_research_ratio = calculate_price_to_research(industry_avg_market_cap, industry_avg_r_and_d_expenditure)

print(f"Company's Price to Research Ratio: {company_price_to_research_ratio:.2f}")
print(f"Industry Average Price to Research Ratio: {industry_avg_price_to_research_ratio:.2f}")

# Interpretation
if company_price_to_research_ratio < industry_avg_price_to_research_ratio:
    print("\nThe company's Price to Research Ratio is below the industry average, suggesting it might be undervalued given its R&D investment compared to peers.")
elif company_price_to_research_ratio == industry_avg_price_to_research_ratio:
    print("\nThe company's Price to Research Ratio aligns with the industry average.")
else:
    print("\nThe company's Price to Research Ratio is above the industry average, indicating it might be overvalued relative to its R&D investment compared to peers.")
    