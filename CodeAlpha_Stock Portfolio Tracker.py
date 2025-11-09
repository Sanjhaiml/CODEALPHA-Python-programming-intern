# --- Step 1: Define hardcoded stock prices ---
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 310,
    "AMZN": 130
}

# --- Step 2: Take user input for portfolio ---
portfolio = {}
print(" Welcome to Stock Portfolio Tracker!")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print(" Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print(" Please enter a valid number!")

# --- Step 3: Calculate total investment ---
total_investment = 0
print("\n Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} - Quantity: {qty}, Price: ${stock_prices[stock]}, Value: ${value}")

print("\n Total Investment Value: $", total_investment)

# --- Step 4 (Optional): Save to file ---
save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("-----------------------\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock} - Quantity: {qty}, Price: ${stock_prices[stock]}, Value: ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(" Summary saved successfully as 'portfolio_summary.txt'")
