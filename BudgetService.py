class Budget:
    def __init__(self, year_month: str, amount: float):
        self.year_month = year_month  # Format: 'YYYY-MM'
        self.amount = amount

class BudgetRepo:
    def __init__(self):
        # Sample data for demonstration purposes
        self.budgets = [
            Budget("2023-01", 1000.0),
            Budget("2023-02", 1500.0),
            Budget("2023-03", 2000.0),
            Budget("2023-04", 2500.0),
            Budget("2023-05", 3000.0),
            Budget("2023-06", 3500.0)
        ]

    def get_all(self):
        return self.budgets

class BudgetService:
    def __init__(self, budget_repo: BudgetRepo):
        self.budget_repo = budget_repo

    def total_amount(self, start: str, end: str) -> float:
        total = 0.0
        budgets = self.budget_repo.get_all()

        for budget in budgets:
            if start <= budget.year_month <= end:
                total += budget.amount

        return total

# Example usage
if __name__ == "__main__":
    budget_repo = BudgetRepo()
    budget_service = BudgetService(budget_repo)

    start_date = "2023-02"
    end_date = "2023-04"
    total = budget_service.total_amount(start_date, end_date)

    print(f"Total budget amount from {start_date} to {end_date}: {total}")
