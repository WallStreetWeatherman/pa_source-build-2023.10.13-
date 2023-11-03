# Capital Expenditure (CapEx) Analysis
# ------------------------------------
# Overview:
# Capital Expenditure (CapEx) reflects funds utilized by a company to acquire, maintain, or upgrade its physical assets.
#
# Desired Value:
# While higher CapEx can indicate significant investments in the future, consistently high CapEx without proportional returns
# may suggest inefficiencies or over-expansion. Ideally, CapEx should be balanced based on the company's growth and industry phase.
#
# Note: This script uses hard-coded values. For real-world application, data should be fetched and updated accordingly.

def convert_to_actual_value(value):
    """Converts the value in the format of 1.00 to actual $1 million."""
    return value * 1000000

# Hard-coded value for Capital Expenditure
capex = convert_to_actual_value(-900.00)  # Example: -$3.5 million in CapEx (CapEx is typically a negative value)

# Benchmark values
average_industry_capex = convert_to_actual_value(-1716.00)  # Example industry average CapEx value, say -$3 million

# Output the result
print("Capital Expenditure (CapEx) Analysis:\n")
print("Calculated CapEx based on given assumptions: ${:.2f}".format(capex))

if capex >= average_industry_capex:
    print("The company's CapEx is lower or in line with the industry average. This might indicate limited investments in physical assets.")
elif capex >= 1.2 * average_industry_capex:
    print("The company's CapEx is moderately higher than the industry average. It might be investing more for future growth or asset maintenance.")
else:
    print("The company's CapEx is significantly higher than the industry average. Analyze the ROI on these investments closely.")
