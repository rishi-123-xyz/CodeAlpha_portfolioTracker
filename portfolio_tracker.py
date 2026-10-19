"""
Task 2: Stock Portfolio Tracker
Author: CodeAlpha Internship
Description: A simple stock tracker that calculates total investment value
             based on manually defined stock prices, with optional TXT/CSV export.
"""

from datetime import datetime
import csv
import os
import sys

# Ensure UTF-8 output where supported, with graceful fallback on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Hardcoded dictionary defining stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 330.00,
    "GOOGL": 140.00,
    "AMZN": 130.00,
    "NVDA": 460.00,
    "META": 310.00,
    "NFLX": 400.00,
}


def print_banner():
    """Prints the application header banner."""
    print("\n" + "=" * 68)
    print(" " * 22 + "STOCK PORTFOLIO TRACKER")
    print("=" * 68)


def display_available_stocks():
    """Displays all available stocks and their manually defined prices."""
    print("\n--- Available Stocks & Current Market Prices ---")
    print(f"{'Stock Symbol':<16}{'Price Per Share (USD)':<24}")
    print("-" * 40)
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"{symbol:<16}${price:>8.2f}")
    print("-" * 40)


def get_valid_stock_symbol():
    """
    Prompts the user for a stock symbol and validates it against STOCK_PRICES.
    Returns uppercase symbol or None if user cancels.
    """
    while True:
        symbol = input("\nEnter stock symbol (or 'list' to view, 'cancel' to return): ").strip().upper()
        if symbol == "CANCEL":
            return None
        if symbol == "LIST":
            display_available_stocks()
            continue
        if symbol in STOCK_PRICES:
            return symbol
        print(f"[!] Error: '{symbol}' is not in the price list. Type 'list' to view available stocks.")


def get_valid_quantity(prompt="Enter quantity of shares: "):
    """
    Prompts the user for a valid positive integer quantity of shares.
    """
    while True:
        val = input(prompt).strip()
        if not val:
            print("[!] Input cannot be empty.")
            continue
        try:
            qty = int(val)
            if qty <= 0:
                print("[!] Quantity must be a positive whole number greater than 0.")
                continue
            return qty
        except ValueError:
            print("[!] Invalid input. Please enter a positive integer.")


def calculate_portfolio_totals(portfolio):
    """
    Calculates detailed metrics for each holding and total portfolio value.
    Returns: (holdings_list, total_investment)
    """
    holdings = []
    total_investment = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = price * qty
        total_investment += subtotal
        holdings.append({
            "symbol": symbol,
            "price": price,
            "quantity": qty,
            "subtotal": subtotal
        })

    # Calculate portfolio weight percentages
    for item in holdings:
        item["weight"] = (item["subtotal"] / total_investment * 100) if total_investment > 0 else 0.0

    return holdings, total_investment


def display_portfolio_summary(portfolio):
    """
    Formats and prints a comprehensive summary of the current portfolio.
    """
    if not portfolio:
        print("\n[i] Your portfolio is currently empty.")
        return

    holdings, total_investment = calculate_portfolio_totals(portfolio)

    print("\n" + "=" * 66)
    print(" " * 21 + "PORTFOLIO SUMMARY")
    print("=" * 66)
    print(f"{'Stock':<10} {'Price ($)':>12} {'Shares':>10} {'Total Value ($)':>16} {'Weight (%)':>12}")
    print("-" * 66)

    for item in holdings:
        price_str = f"${item['price']:,.2f}"
        subtotal_str = f"${item['subtotal']:,.2f}"
        weight_str = f"{item['weight']:.2f}%"
        print(
            f"{item['symbol']:<10} "
            f"{price_str:>12} "
            f"{item['quantity']:>10} "
            f"{subtotal_str:>16} "
            f"{weight_str:>12}"
        )

    print("-" * 66)
    total_str = f"${total_investment:,.2f}"
    print(f"{'Total Portfolio Value:':<34} {total_str:>16} {'100.00%':>12}")
    print("=" * 66)


def save_to_txt(portfolio, filepath="portfolio_summary.txt"):
    """
    Saves the portfolio summary report to a .txt file.
    """
    if not portfolio:
        print("[!] Cannot save an empty portfolio.")
        return False

    holdings, total_investment = calculate_portfolio_totals(portfolio)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 66 + "\n")
        f.write(" " * 19 + "STOCK PORTFOLIO REPORT\n")
        f.write(f" Generated on: {timestamp}\n")
        f.write("=" * 66 + "\n")
        f.write(f"{'Stock':<10} {'Price ($)':>12} {'Shares':>10} {'Total Value ($)':>16} {'Weight (%)':>12}\n")
        f.write("-" * 66 + "\n")

        for item in holdings:
            price_str = f"${item['price']:,.2f}"
            subtotal_str = f"${item['subtotal']:,.2f}"
            weight_str = f"{item['weight']:.2f}%"
            f.write(
                f"{item['symbol']:<10} "
                f"{price_str:>12} "
                f"{item['quantity']:>10} "
                f"{subtotal_str:>16} "
                f"{weight_str:>12}\n"
            )

        f.write("-" * 66 + "\n")
        total_str = f"${total_investment:,.2f}"
        f.write(f"{'Total Portfolio Value:':<34} {total_str:>16} {'100.00%':>12}\n")
        f.write("=" * 66 + "\n")

    print(f"[+] Successfully exported text report to: {os.path.abspath(filepath)}")
    return True


def save_to_csv(portfolio, filepath="portfolio_summary.csv"):
    """
    Saves the portfolio holdings to a comma-separated values (.csv) file.
    """
    if not portfolio:
        print("[!] Cannot save an empty portfolio.")
        return False

    holdings, total_investment = calculate_portfolio_totals(portfolio)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock Symbol", "Price Per Share ($)", "Quantity", "Total Value ($)", "Portfolio Weight (%)"])
        for item in holdings:
            writer.writerow([
                item["symbol"],
                f"{item['price']:.2f}",
                item["quantity"],
                f"{item['subtotal']:.2f}",
                f"{item['weight']:.2f}%"
            ])
        writer.writerow(["TOTAL", "", "", f"{total_investment:.2f}", "100.00%"])

    print(f"[+] Successfully exported CSV data to: {os.path.abspath(filepath)}")
    return True


def prompt_save_portfolio(portfolio):
    """
    Prompts the user to choose an export format (.txt, .csv, both, or skip).
    """
    if not portfolio:
        print("\n[i] Portfolio is empty. Nothing to save.")
        return

    print("\nSave Options:")
    print("1. Save as Text file (.txt)")
    print("2. Save as CSV file (.csv)")
    print("3. Save as both (.txt and .csv)")
    print("4. Return to main menu (Skip)")

    choice = input("\nSelect an option (1-4): ").strip()
    if choice == "1":
        save_to_txt(portfolio)
    elif choice == "2":
        save_to_csv(portfolio)
    elif choice == "3":
        save_to_txt(portfolio)
        save_to_csv(portfolio)
    elif choice == "4":
        print("[i] Save cancelled.")
    else:
        print("[!] Invalid selection.")


def add_or_update_stock(portfolio):
    """
    Guides the user through adding or updating stock holdings.
    """
    display_available_stocks()
    while True:
        symbol = get_valid_stock_symbol()
        if symbol is None:
            break

        current_qty = portfolio.get(symbol, 0)
        if current_qty > 0:
            print(f"[i] You currently hold {current_qty} shares of {symbol}.")
            print("1. Add more shares to current holding")
            print("2. Set new total quantity")
            print("3. Cancel")
            sub_choice = input("Select an option (1-3): ").strip()
            if sub_choice == "1":
                add_qty = get_valid_quantity("Enter additional shares to add: ")
                portfolio[symbol] = current_qty + add_qty
                print(f"[+] Updated {symbol}: Now holding {portfolio[symbol]} shares.")
            elif sub_choice == "2":
                new_qty = get_valid_quantity("Enter new total shares: ")
                portfolio[symbol] = new_qty
                print(f"[+] Updated {symbol}: Now holding {portfolio[symbol]} shares.")
            else:
                print("[i] Update cancelled.")
        else:
            qty = get_valid_quantity(f"Enter quantity of {symbol} shares: ")
            portfolio[symbol] = qty
            subtotal = STOCK_PRICES[symbol] * qty
            print(f"[+] Added {qty} shares of {symbol} (${STOCK_PRICES[symbol]:.2f} each) = ${subtotal:,.2f}")

        more = input("\nDo you want to add/update another stock? (y/n): ").strip().lower()
        if more not in ("y", "yes"):
            break


def remove_stock(portfolio):
    """
    Removes a selected stock from the portfolio.
    """
    if not portfolio:
        print("\n[i] Your portfolio is empty. Nothing to remove.")
        return

    print("\nCurrent holdings:")
    for s in portfolio:
        print(f"- {s} ({portfolio[s]} shares)")

    symbol = input("\nEnter stock symbol to remove (or 'cancel'): ").strip().upper()
    if symbol in portfolio:
        removed_qty = portfolio.pop(symbol)
        print(f"[+] Removed all {removed_qty} shares of {symbol} from portfolio.")
    elif symbol == "CANCEL":
        print("[i] Removal cancelled.")
    else:
        print(f"[!] '{symbol}' is not in your portfolio.")


def main():
    """Main program loop."""
    portfolio = {}

    print_banner()
    print("Welcome! Track your investments with predefined stock market prices.")

    while True:
        print("\n" + "=" * 40)
        print("            MAIN MENU")
        print("=" * 40)
        print("1. Add / Update Stocks in Portfolio")
        print("2. View Current Portfolio Summary")
        print("3. View Available Stocks & Prices")
        print("4. Remove a Stock from Portfolio")
        print("5. Save Summary to File (.txt / .csv)")
        print("6. Clear Entire Portfolio")
        print("7. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_or_update_stock(portfolio)
            display_portfolio_summary(portfolio)
        elif choice == "2":
            display_portfolio_summary(portfolio)
        elif choice == "3":
            display_available_stocks()
        elif choice == "4":
            remove_stock(portfolio)
            display_portfolio_summary(portfolio)
        elif choice == "5":
            prompt_save_portfolio(portfolio)
        elif choice == "6":
            if portfolio:
                confirm = input("[!] Are you sure you want to clear your portfolio? (y/n): ").strip().lower()
                if confirm in ("y", "yes"):
                    portfolio.clear()
                    print("[+] Portfolio cleared.")
            else:
                print("[i] Portfolio is already empty.")
        elif choice == "7":
            if portfolio:
                save_prompt = input("\nWould you like to save your portfolio before exiting? (y/n): ").strip().lower()
                if save_prompt in ("y", "yes"):
                    prompt_save_portfolio(portfolio)
            print("\nThank you for using Stock Portfolio Tracker. Goodbye!\n")
            break
        else:
            print("[!] Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
