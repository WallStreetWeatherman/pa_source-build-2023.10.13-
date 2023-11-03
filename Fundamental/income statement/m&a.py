# M&A Comps (Mergers and Acquisitions Comparables)
#
# Overview:
# M&A Comps analysis evaluates a company based on recent mergers and acquisitions 
# within an industry to determine the average going rate for similar companies. 
# This helps to identify whether a company might be undervalued or overvalued 
# compared to its peers that were recently acquired.
#
# Desired Value:
# If the target company's value is considerably lower than the average M&A 
# comp value, it might be undervalued. Conversely, if it's significantly higher, 
# it could be overvalued.

def ma_comps(target_company_value, recent_ma_values, industry_average):
    """
    Determine the position of the target company based on recent M&A values and industry average.
    
    Parameters:
    - target_company_value: Value of the target company (e.g., for $10,000,000 use 10.00)
    - recent_ma_values: List of recent M&A transaction values in the industry.
    - industry_average: The industry average company value
    
    Returns:
    - A string indicating whether the target company is undervalued, overvalued, or fairly valued.
    """
    average_ma_value = sum(recent_ma_values) / len(recent_ma_values)
    
    print(f"Average M&A Comparable Value: ${average_ma_value:.2f} million")
    print(f"Industry Average Value: ${industry_average:.2f} million")
    
    if target_company_value < industry_average * 0.9:  # 10% threshold for undervaluation
        return "The target company appears to be undervalued compared to the industry average."
    elif target_company_value > industry_average * 1.1:  # 10% threshold for overvaluation
        return "The target company appears to be overvalued compared to the industry average."
    else:
        return "The target company appears to be fairly valued."

# Hardcoded values for demonstration
target_company_value = 12.00  # Value of the target company ($12,000,000)
recent_ma_values = [10.00, 11.50, 13.00, 9.50, 12.50]  # Recent M&A transaction values in the industry
industry_average = sum(recent_ma_values) / len(recent_ma_values)  # Here, we've just used the M&A comps to determine industry average. In practice, this could be a separate figure.

result = ma_comps(target_company_value, recent_ma_values, industry_average)
print(result)
