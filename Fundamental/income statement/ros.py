# Return on Sales (ROS) Calculator
# --------------------------------
# Overview:
# Return on Sales (ROS) is a measure of a company's operational profitability. It represents 
# how much profit a company generates for every dollar of sales.
#
# Formula:
# ROS = Net Income / Net Sales
# 
# Desired Value:
# A higher ROS indicates that the company is more efficient in converting sales into profit.
# It means the company has a good grip on its costs relative to its sales.
# A low ROS can suggest inefficiencies or issues in pricing or cost management.
#

# Company's data:
net_income_company = 1177.00  # Net Income in Tikr
net_sales_company = 24442.00  # Revenues in Tikr

# Industry average data:
net_income_industry = 322.00  
net_sales_industry = 4840.00  

# Calculate ROS for the company
ros_company = (net_income_company / net_sales_company) * 100

# Calculate ROS for the industry average
ros_industry = (net_income_industry / net_sales_industry) * 100

# Output the results
print(f"Company's Return on Sales (ROS): {ros_company:.2f}%")
print(f"Industry Average Return on Sales (ROS): {ros_industry:.2f}%")

if ros_company > ros_industry:
    print("The company's ROS is above the industry average, indicating better operational efficiency.")
elif ros_company < ros_industry:
    print("The company's ROS is below the industry average, suggesting potential operational inefficiencies.")
else:
    print("The company's ROS is in line with the industry average.")