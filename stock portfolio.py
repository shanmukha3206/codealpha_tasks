# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "INFY": 100
}

# Step 1: Take user input
print("Enter your stock investments (stock name and quantity). Type 'done' to finish.\n")
portfolio = {}

while True:
    stock = input("Stock name (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in our list. Try again.")
        continue
    quantity = int(input(f"Quantity of {stock}: "))
    portfolio[stock] = quantity

# Step 2: Calculate total investment
total = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = qty * price
    print(f"{stock} - {qty} shares x ₹{price} = ₹{investment}")
    total += investment

print(f"\nTotal Investment Value: ₹{total}")

# Step 3: (Optional) Save to a text file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = qty * price
            file.write(f"{stock} - {qty} shares x ₹{price} = ₹{investment}\n")
        file.write(f"\nTotal Investment Value: ₹{total}")
    print("Summary saved to 'portfolio_summary.txt'")

