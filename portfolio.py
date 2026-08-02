def stock_portfolio_tracker():
    # Hardcoded dictionary defining stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT": 400, "AMZN": 175}

    print("--- 📈 Stock Portfolio Tracker ---")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    total_portfolio_value = 0
    portfolio_details = []

    # Get user input
    while True:
        stock_name = input("\nEnter stock name (or type 'exit' to finish): ").upper().strip()
        if stock_name == 'EXIT':
            break
        if stock_name not in stock_prices:
            print("❌ This stock is not in our list. Please choose from the available options.")
            continue

        try:
            quantity = int(input(f"How many shares of {stock_name} do you own? "))
            if quantity <= 0: 
                print("❌ Quantity must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            continue

        # Calculation
        stock_value = quantity * stock_prices[stock_name]
        total_portfolio_value += stock_value
        detail_line = f"{stock_name}: {quantity} shares | Value: ${stock_value}"
        portfolio_details.append(detail_line)

    # Display results
    print("\n💰 Total Portfolio Value: $" + str(total_portfolio_value))

    # Save output to a text file (File Handling)
    try:
        with open("portfolio_report.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(portfolio_details) + f"\n\nTotal Portfolio Value: ${total_portfolio_value}")
        print("💾 Report saved successfully to 'portfolio_report.txt'.")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

if __name__ == "__main__":
    stock_portfolio_tracker()
