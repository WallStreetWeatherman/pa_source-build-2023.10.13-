# Net Change in Working Capital Calculator
# ----------------------------------------
# Overview:
# This script calculates the net change in working capital for both a specific company 
# and the industry average. The net change in working capital is an essential measure 
# for understanding how much a company's short-term assets and liabilities have changed 
# over a period.
#
# Desired Value:
# A significant increase might indicate the company is not efficiently utilizing its 
# short-term assets or not effectively managing its short-term liabilities. Conversely, 
# a substantial decrease might indicate potential liquidity concerns. Comparing the 
# company's net change to the industry average can provide context.


def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000

# Hard-coded values for the company
start_current_assets_in_millions = 6758.00 # Total Current Assets in Tikr
end_current_assets_in_millions = 5853.00

start_current_liabilities_in_millions = 5416.00 # Total Current Liabilites in Tikr
end_current_liabilities_in_millions = 4861.00

# Hard-coded values for industry average 
industry_start_current_assets_in_millions = 9530.00 
industry_end_current_assets_in_millions = 2880.00

industry_start_current_liabilities_in_millions = 7650.00
industry_end_current_liabilities_in_millions = 1680.00

# Calculate net change in working capital for the company
company_net_change = (convert_to_actual_value(end_current_assets_in_millions) - convert_to_actual_value(start_current_assets_in_millions)) - \
                    (convert_to_actual_value(end_current_liabilities_in_millions) - convert_to_actual_value(start_current_liabilities_in_millions))

# Calculate net change in working capital for the industry
industry_net_change = (convert_to_actual_value(industry_end_current_assets_in_millions) - convert_to_actual_value(industry_start_current_assets_in_millions)) - \
                     (convert_to_actual_value(industry_end_current_liabilities_in_millions) - convert_to_actual_value(industry_start_current_liabilities_in_millions))

print(f"Company's Net Change in Working Capital: ${company_net_change:.2f}")
print(f"Industry Average Net Change in Working Capital: ${industry_net_change:.2f}\n")

if company_net_change > industry_net_change:
    print("The company's net change in working capital is greater than the industry average. It suggests the company might not be as efficient in managing its working capital compared to the industry.")
elif company_net_change < industry_net_change:
    print("The company's net change in working capital is less than the industry average, which may indicate better efficiency or potential liquidity concerns, depending on the context.")
else:
    print("The company's net change in working capital aligns with the industry standard.")
