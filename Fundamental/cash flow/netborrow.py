# Net Borrowing Calculator
# ------------------------
# Overview:
# This script calculates Net Borrowing based on new debt issued and debt repaid.
#
# Desired Value:
# A positive Net Borrowing indicates the company has taken on more debt than it has repaid, 
# which could be a signal for expansion or leveraging. A negative value indicates the company 
# has repaid more debt than it has taken on, which could be a sign of deleveraging.
#
# Note: This script uses hard-coded values for demonstration. For real-world applications,
# replace these values with actual financial data.

def convert_to_actual_value(value_in_millions):
    return value_in_millions * 1000000  # Convert to actual dollar amounts

# Hard-coded values (in millions, e.g., 1.00 = $1 million)
new_debt_issued = 850.00  # New debt issued
debt_repaid = 1140.00  # Debt repaid

# Convert to actual values
new_debt_issued_actual = convert_to_actual_value(new_debt_issued)
debt_repaid_actual = convert_to_actual_value(debt_repaid)

# Calculate Net Borrowing
net_borrowing = new_debt_issued_actual - debt_repaid_actual
net_borrowing_in_millions = net_borrowing / 1000000  # Convert back to million-dollar format

# Output the result
print(f"Net Borrowing: ${net_borrowing_in_millions:.2f} million")

if net_borrowing_in_millions > 0:
    print("The company has taken on more debt than it has repaid, possibly for expansion or leveraging.")
elif net_borrowing_in_millions < 0:
    print("The company has repaid more debt than it has taken on, possibly deleveraging.")
else:
    print("The company's new debt and repayments are balanced.")
