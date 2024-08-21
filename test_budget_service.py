import unittest
from unittest.mock import patch
from datetime import date
from BudgetService import BudgetService, BudgetRepo, Budget

class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService()

    # query scenarios
    def test_same_month_full(self):
        with patch('BudgetService.BudgetRepo.get_all') as mock_get_all:
            mock_get_all.return_value = [
                Budget('202303', 2800)
            ]
            start_date = date(2023, 3, 1)
            end_date = date(2023, 3, 31)
            total = self.budget_service.total_amount(start_date, end_date)
            self.assertEqual(total, 2800)

    def test_same_month_partial(self):
        with patch('BudgetService.BudgetRepo.get_all') as mock_get_all:
            mock_get_all.return_value = [
                Budget('202303', 3100)
            ]
            start_date = date(2023, 3, 1)
            end_date = date(2023, 3, 2)
            total = self.budget_service.total_amount(start_date, end_date)
            self.assertEqual(total, 200)

    # def test_across_two_months(self):
    #     with patch('BudgetService.BudgetRepo.get_all') as mock_get_all:
    #         mock_get_all.return_value = [
    #             Budget('202303', 3100),
    #             Budget('202304', 6000)
    #         ]
    #         start_date = date(2023, 3, 31)
    #         end_date = date(2023, 4, 1)
    #         total = self.budget_service.total_amount(start_date, end_date)
    #         self.assertEqual(total, 300)

    def test_across_three_months(self):
        pass

    def test_invalid_date_range(self):
        with patch('BudgetService.BudgetRepo.get_all') as mock_get_all:
            mock_get_all.return_value = [
                Budget('202303', 2800)
            ]
            start_date = date(2023, 4, 1)
            end_date = date(2023, 3, 20)
            total = self.budget_service.total_amount(start_date, end_date)
            self.assertEqual(total, 0)



if __name__ == '__main__':
    unittest.main()
