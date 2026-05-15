stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 200,
    "AMZN": 150
}

print(" Stock Portfolio Tracker")

total_investment = 0

while True:

    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        quantity = int(input("Enter quantity: "))

        investment = stocks[stock_name] * quantity

        total_investment += investment

        print("Investment added:", investment)

    else:
        print(" Stock not found!")

print("\n Total Investment Value:", total_investment)