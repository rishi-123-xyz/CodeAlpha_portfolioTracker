# Stock Portfolio Tracker

> **CodeAlpha Python Development Internship — Task 2**

A command-line stock portfolio tracking application that calculates the total investment value based on manually defined stock prices, allows dynamic management of stock holdings, and provides export capabilities to `.txt` and `.csv` files.

---

## 📌 Project Overview

- **Goal**: Build a simple stock tracker that calculates total investment value based on manually defined stock prices.
- **Key Concepts Used**:
  - **Dictionaries**: Mapping stock ticker symbols to their respective share prices (`{"AAPL": 180.00, "TSLA": 250.00, ...}`) and tracking user holdings.
  - **Input/Output & Validation**: Robust handling for user input, case-insensitive symbols, and quantity validation.
  - **Basic Arithmetic**: Computing subtotal values per holding (`price * quantity`), portfolio percentage allocation, and cumulative portfolio total.
  - **File Handling**: Exporting structured text reports (`.txt`) and tabular data (`.csv`) using Python's standard file I/O and `csv` library.

---

## 🚀 Features

- **Hardcoded Price Dictionary**: Includes popular stocks (`AAPL`, `TSLA`, `MSFT`, `GOOGL`, `AMZN`, `NVDA`, `META`, `NFLX`).
- **Interactive Menu**:
  1. Add or update stock holdings (add shares to an existing position or set a new quantity).
  2. View real-time portfolio breakdown (Symbol, Price, Quantity, Subtotal, and Weight %).
  3. View the catalog of available stocks and current market prices.
  4. Remove individual stock positions.
  5. Export portfolio summaries to `.txt`, `.csv`, or both formats.
  6. Clear the entire portfolio with confirmation.
- **Input Error Prevention**: Rejects invalid tickers, non-numeric values, negative numbers, or empty inputs without crashing.
- **Clean Formatted Display**: Neatly formatted tables with comma-separated currency values and percentage allocations.
- **Unit Test Suite**: Includes automated unit tests covering calculations, exports, edge cases, and empty portfolios.

---

## 📂 Project Structure

```text
task 2/
│
├── portfolio_tracker.py        # Main application script
├── test_portfolio_tracker.py   # Automated unit test suite
├── portfolio_summary.txt       # Generated text report export
├── portfolio_summary.csv       # Generated CSV export
├── README.md                   # Documentation and usage guide
└── .gitignore                  # Git ignore rules for Python
```

---

## 🛠️ Requirements & Setup

### Prerequisites
- **Python 3.8+** installed on your system.

### How to Run

1. Open your terminal or PowerShell in the project directory:
   ```powershell
   cd "C:\Users\kumar\OneDrive\Desktop\task 2"
   ```

2. Run the portfolio tracker:
   ```powershell
   python portfolio_tracker.py
   ```
   *(Or using the full Python path if `python` is not in your PATH:)*
   ```powershell
   & "C:\Users\kumar\AppData\Local\Programs\Python\Python312\python.exe" portfolio_tracker.py
   ```

3. Run the automated test suite:
   ```powershell
   python -m unittest test_portfolio_tracker.py
   ```

---

## 🖥️ Example Usage & Output

### 1. Adding Stocks to Portfolio
```text
--- Available Stocks & Current Market Prices ---
Stock Symbol    Price Per Share (USD)   
----------------------------------------
AAPL            $  180.00
AMZN            $  130.00
GOOGL           $  140.00
META            $  310.00
MSFT            $  330.00
NFLX            $  400.00
NVDA            $  460.00
TSLA            $  250.00
----------------------------------------

Enter stock symbol (or 'list' to view, 'cancel' to return): AAPL
Enter quantity of AAPL shares: 10
[+] Added 10 shares of AAPL ($180.00 each) = $1,800.00

Do you want to add/update another stock? (y/n): y
Enter stock symbol (or 'list' to view, 'cancel' to return): TSLA
Enter quantity of TSLA shares: 5
[+] Added 5 shares of TSLA ($250.00 each) = $1,250.00
```

### 2. Portfolio Summary Table
```text
==================================================================
                     PORTFOLIO SUMMARY
==================================================================
Stock         Price ($)     Shares  Total Value ($)   Weight (%)
------------------------------------------------------------------
AAPL            $180.00         10        $1,800.00       59.02%
TSLA            $250.00          5        $1,250.00       40.98%
------------------------------------------------------------------
Total Portfolio Value:                    $3,050.00      100.00%
==================================================================
```

### 3. Generated Files

#### `portfolio_summary.txt`:
```text
==================================================================
                   STOCK PORTFOLIO REPORT
 Generated on: 2026-10-19 23:49:05
==================================================================
Stock         Price ($)     Shares  Total Value ($)   Weight (%)
------------------------------------------------------------------
AAPL            $180.00         10        $1,800.00       59.02%
TSLA            $250.00          5        $1,250.00       40.98%
------------------------------------------------------------------
Total Portfolio Value:                    $3,050.00      100.00%
==================================================================
```

#### `portfolio_summary.csv`:
```csv
Stock Symbol,Price Per Share ($),Quantity,Total Value ($),Portfolio Weight (%)
AAPL,180.00,10,1800.00,59.02%
TSLA,250.00,5,1250.00,40.98%
TOTAL,,,3050.00,100.00%
```

---

## 🧪 Unit Testing

All unit tests verify:
- Accuracy of arithmetic and percentage allocations.
- Empty portfolio handling without `ZeroDivisionError`.
- CSV and TXT file export functionality and file formatting.
- Dictionary integrity and non-zero prices.

Run the test suite with:
```powershell
python test_portfolio_tracker.py
```
Output:
```text
Ran 6 tests in 0.005s

OK
```

---

## 📜 License
This project is developed as part of the CodeAlpha Python Development Internship Program.
