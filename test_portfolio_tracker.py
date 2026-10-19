"""
Unit tests for portfolio_tracker.py
Tests core calculation logic, validation, and file exports.
"""

import unittest
import os
import csv
from portfolio_tracker import (
    STOCK_PRICES,
    calculate_portfolio_totals,
    save_to_txt,
    save_to_csv,
)


class TestPortfolioTracker(unittest.TestCase):

    def setUp(self):
        self.sample_portfolio = {
            "AAPL": 10,
            "TSLA": 5,
        }
        self.test_txt = "test_summary.txt"
        self.test_csv = "test_summary.csv"

    def tearDown(self):
        for path in (self.test_txt, self.test_csv):
            if os.path.exists(path):
                os.remove(path)

    def test_stock_prices_dictionary(self):
        """Verify hardcoded stock dictionary contains expected tickers with valid positive prices."""
        self.assertIn("AAPL", STOCK_PRICES)
        self.assertIn("TSLA", STOCK_PRICES)
        self.assertEqual(STOCK_PRICES["AAPL"], 180.00)
        self.assertEqual(STOCK_PRICES["TSLA"], 250.00)
        for symbol, price in STOCK_PRICES.items():
            self.assertIsInstance(price, (int, float))
            self.assertGreater(price, 0)

    def test_calculate_portfolio_totals(self):
        """Verify subtotal calculations, portfolio weights, and total investment."""
        holdings, total = calculate_portfolio_totals(self.sample_portfolio)

        # Expected:
        # AAPL: 10 * 180 = 1800
        # TSLA: 5 * 250 = 1250
        # Total: 3050
        self.assertEqual(len(holdings), 2)
        self.assertEqual(total, 3050.00)

        aapl = next(h for h in holdings if h["symbol"] == "AAPL")
        tsla = next(h for h in holdings if h["symbol"] == "TSLA")

        self.assertEqual(aapl["subtotal"], 1800.00)
        self.assertEqual(tsla["subtotal"], 1250.00)

        # AAPL weight ~ 59.016%, TSLA weight ~ 40.984%
        self.assertAlmostEqual(aapl["weight"], (1800 / 3050) * 100, places=2)
        self.assertAlmostEqual(tsla["weight"], (1250 / 3050) * 100, places=2)
        self.assertAlmostEqual(aapl["weight"] + tsla["weight"], 100.0, places=2)

    def test_empty_portfolio(self):
        """Verify handling of empty portfolio returns zero total without dividing by zero."""
        holdings, total = calculate_portfolio_totals({})
        self.assertEqual(holdings, [])
        self.assertEqual(total, 0.0)

    def test_save_to_txt(self):
        """Verify text report generation and file output."""
        success = save_to_txt(self.sample_portfolio, filepath=self.test_txt)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(self.test_txt))

        with open(self.test_txt, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("STOCK PORTFOLIO REPORT", content)
            self.assertIn("AAPL", content)
            self.assertIn("TSLA", content)
            self.assertIn("$3,050.00", content)

    def test_save_to_csv(self):
        """Verify CSV export writes valid rows and headers."""
        success = save_to_csv(self.sample_portfolio, filepath=self.test_csv)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(self.test_csv))

        with open(self.test_csv, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            # Header + 2 stocks + TOTAL row = 4 rows
            self.assertEqual(len(reader), 4)
            self.assertEqual(reader[0][0], "Stock Symbol")
            self.assertEqual(reader[1][0], "AAPL")
            self.assertEqual(reader[2][0], "TSLA")
            self.assertEqual(reader[3][0], "TOTAL")
            self.assertEqual(reader[3][3], "3050.00")

    def test_empty_save_prevention(self):
        """Verify empty portfolios are rejected from file saves."""
        self.assertFalse(save_to_txt({}, filepath=self.test_txt))
        self.assertFalse(save_to_csv({}, filepath=self.test_csv))


if __name__ == "__main__":
    unittest.main()
