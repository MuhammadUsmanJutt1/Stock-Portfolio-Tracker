def stock_portfolio():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 120,
        "AMZN": 90,
        "MSFT": 150
    }

    total_investment = 0
    n = int(input("How many stocks do you want to enter? "))

    portfolio = {}

    for _ in range(n):
        name = input("Enter stock name (AAPL/TSLA/GOOGL/AMZN/MSFT): ").upper()
        if name not in stock_prices:
            print("Stock not found!")
            continue
        qty = int(input(f"Enter quantity for {name}: "))
        portfolio[name] = qty
        total_investment += stock_prices[name] * qty

    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares at ${stock_prices[stock]} each")

    print(f"\nTotal Investment: ${total_investment}")

    # Optional: Save to a file
    with open("portfolio.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares at ${stock_prices[stock]} each\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")

    print("\nPortfolio saved to 'portfolio.txt'")

stock_portfolio()
