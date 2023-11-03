# Earnings Power Value (EPV) Analysis
# ------------------------------------
# Overview:
# The Earnings Power Value (EPV) is a valuation technique that evaluates a company's ability to generate earnings, 
# independent of the current state of its finances. 
# Ideally, for a deep value investor, you'd want the EPV to be significantly higher than the current stock price, 
# suggesting the stock may be undervalued.
# 
# Formula:
# EPV = Adjusted Earnings / Cost of Capital

class Company:
    def __init__(self, name, adjusted_earnings, cost_of_capital):
        self.name = name
        self.adjusted_earnings = adjusted_earnings  # In format: 1.00 means $1 million
        self.cost_of_capital = cost_of_capital  # As a percentage, e.g., 0.07 for 7%

        # Validate the data upon initialization
        self._validate_data()

    def _validate_data(self):
        """Validate data to ensure positive values."""
        if self.adjusted_earnings <= 0:
            raise ValueError("Adjusted Earnings must be positive.")
        if not (0 < self.cost_of_capital < 1):
            raise ValueError("Cost of Capital should be between 0 and 1 (0% to 100%).")

    def compute_epv(self):
        """Compute the Earnings Power Value."""
        return self.adjusted_earnings / self.cost_of_capital

    def display_epv(self):
        try:
            print(f"Earnings Power Value (EPV) for {self.name}: ${self.compute_epv():.2f} million")
        except Exception as e:
            print(f"An error occurred while processing the data for {self.name}. Error: {str(e)}")

# Hardcoded values for two hypothetical companies
company_A = Company("Company A", 10.00, 0.07)  # Adjusted earnings of $10 million and cost of capital of 7%
company_B = Company("Company B", 25.00, 0.05)  # Adjusted earnings of $25 million and cost of capital of 5%

company_A.display_epv()
company_B.display_epv()

# Comparing EPV of the two companies
if company_A.compute_epv() > company_B.compute_epv():
    print(f"\n{company_A.name} has a higher Earnings Power Value compared to {company_B.name}.")
elif company_A.compute_epv() < company_B.compute_epv():
    print(f"\n{company_B.name} has a higher Earnings Power Value compared to {company_A.name}.")
else:
    print(f"\nBoth {company_A.name} and {company_B.name} have the same Earnings Power Value.")
