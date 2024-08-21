from datetime import date
from calendar import monthrange

class Budget:
    def __init__(self, year_month: str, amount: float):
        self.year_month = year_month
        self.amount = amount
class BudgetRepo:
    def __init__(self):
        self.budgets = []

    def get_all(self) -> list[Budget]:
        return self.budgets

budget_repo = BudgetRepo()

class BudgetService:
    def __init__(self):
        pass

    def total_amount(self, start: date, end: date) -> float:
        total = 0.0
        budgets = budget_repo.get_all()

        if end < start:
            return 0.0

        for month in range(start.month, end.month + 1):
            for db_budget in budgets:
                y = int(db_budget.year_month[:4])
                m = int(db_budget.year_month[4:6])
                if m == month:
                    if m == start.month:
                        if m == end.month:
                            return (end.day - start.day + 1) / monthrange(y, m)[1] * db_budget.amount
                        total += (monthrange(y, m)[1] - start.day + 1) / monthrange(y, m)[1] * db_budget.amount
                        print("first total", total)
                        print("mongh", m)
                    elif m == end.month:
                        total += (end.day / monthrange(y, m)[1]) * db_budget.amount
                    else:
                        total += db_budget.amount
                    # total += (end.day - start.day + 1) / monthrange(year, month)[1] * db_budget.amount

        return total

# Example usage
if __name__ == "__main__":
    budget_repo = BudgetRepo()
    budget_service = BudgetService(budget_repo)

    start_date = "2023-02"
    end_date = "2023-04"
    total = budget_service.total_amount(start_date, end_date)

    print(f"Total budget amount from {start_date} to {end_date}: {total}")
