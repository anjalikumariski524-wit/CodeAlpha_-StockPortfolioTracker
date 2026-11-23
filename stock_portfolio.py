# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

# Step 1: Define stock prices using a dictionary

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 190
}

# Step 2: Create an empty dictionary for user holdings

portfolio = {}

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter stock names and quantities.")
print("Type 'done' when you finish.")

# Step 3: Get stock name and quantity from user

while True:

    stock_name = input("\nEnter stock name: ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # Store stock quantity in portfolio

    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    print("Stock added successfully!")


# Step 4: Calculate total investment

print("\n====================================")
print("          PORTFOLIO SUMMARY")
print("====================================")

total_investment = 0

report = []

report.append("STOCK PORTFOLIO TRACKER")
report.append("=======================")

if not portfolio:
    print("No stocks were added to your portfolio.")
    report.append("No stocks were added.")

else:
    print("\nStock\tQuantity\tPrice\tInvestment")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]

        investment = price * quantity

        total_investment += investment

        print(f"{stock}\t{quantity}\t\t${price}\t${investment}")

        report.append(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}"
        )

    print("------------------------------------")
    print(f"Total Investment: ${total_investment}")

    report.append("--------------------------------")
    report.append(f"Total Investment: ${total_investment}")


# Step 5: Save report in a text file

save_choice = input(
    "\nDo you want to save the report? (yes/no): "
).lower().strip()

if save_choice == "yes":

    with open("portfolio_report.txt", "w") as file:
        file.write("\n".join(report))

    print("Report saved successfully!")

else:
    print("Report was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")