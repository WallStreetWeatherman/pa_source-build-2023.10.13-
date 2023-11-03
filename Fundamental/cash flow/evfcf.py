# Enterprise Value-to-Free Cash Flow Calculation
# ----------------------------------------------
# Overview:
# The Enterprise Value-to-Free Cash Flow (EV/FCF) ratio measures the valuation of a company 
# relative to its free cash flow. Unlike P/E which uses net earnings, EV/FCF uses the Free Cash 
# Flow as it represents the actual cash available to all the capital providers (both equity 
# and debt holders).
#
# Desired Value:
# A lower EV/FCF ratio may suggest that the company is undervalued, especially when compared 
# to peers in the same industry. It's essential to consider the company's growth prospects, 
# stability of cash flows, and industry dynamics when interpreting this ratio.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

def ev_to_fcf_ratio(enterprise_value, free_cash_flow):
    """
    Calculate EV/FCF ratio.
    
    Parameters:
    enterprise_value - Total value of a business
    free_cash_flow - Cash a business has after capital expenditures
    
    """
    return enterprise_value / free_cash_flow

# Hard-coded values for the company
company_enterprise_value = convert_to_actual_value(8497.32)
company_free_cash_flow = convert_to_actual_value(162.00)

# Hard-coded values for industry average
industry_avg_enterprise_value = convert_to_actual_value(48600.00)  
industry_avg_free_cash_flow = convert_to_actual_value(442.00)     

# Calculate EV/FCF ratios for the company and the industry average
company_ev_fcf_ratio = ev_to_fcf_ratio(company_enterprise_value, company_free_cash_flow)
industry_avg_ev_fcf_ratio = ev_to_fcf_ratio(industry_avg_enterprise_value, industry_avg_free_cash_flow)

# Output the results
print("Enterprise Value-to-Free Cash Flow Calculation:\n")
print(f"Company's EV/FCF Ratio: {company_ev_fcf_ratio:.2f}")
print(f"Industry Average EV/FCF Ratio: {industry_avg_ev_fcf_ratio:.2f}")

# Interpretation
if company_ev_fcf_ratio < industry_avg_ev_fcf_ratio:
    print("\nThe company has a lower EV/FCF ratio compared to the industry average. This may suggest it's potentially undervalued relative to its peers. However, a lower ratio could also indicate lower growth prospects or potential risks associated with the company's cash flow stability.")
elif company_ev_fcf_ratio == industry_avg_ev_fcf_ratio:
    print("\nThe company's EV/FCF ratio is in line with the industry average. It implies the market values the company similarly to its peers in terms of its cash generation abilities relative to its valuation.")
else:
    print("\nThe company has a higher EV/FCF ratio compared to the industry average. This might suggest the company is overvalued relative to its peers. A higher ratio can sometimes indicate high growth expectations, or it might be a sign that the market is overestimating the company's future cash flows.")