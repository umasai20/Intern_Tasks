def stock_portfolio_tracker():
    # Hardcoded stock prices (you can add more stocks here)
    stock_prices = {
        "AAPL": 180.25,   # Apple
        "TSLA": 238.50,    # Tesla
        "MSFT": 320.75,    # Microsoft
        "AMZN": 135.20,    # Amazon
        "GOOGL": 145.30,   # Google
        "META": 350.40,    # Meta
        "NVDA": 450.60,    # Nvidia
        "PYPL": 62.15      # PayPal
    }
    
    print("\nWelcome to Simple Stock Portfolio Tracker")
    print("=" * 40)
    print("Available stocks and their current prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")
    print("=" * 40)
    
    portfolio = {}
    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"Error: {stock_name} is not in our database. Please try again.")
            continue
            
        try:
            quantity = float(input(f"Enter quantity of {stock_name} shares: "))
            if quantity <= 0:
                print("Quantity must be positive. Please try again.")
                continue
                
            portfolio[stock_name] = {
                'quantity': quantity,
                'price': stock_prices[stock_name],
                'value': quantity * stock_prices[stock_name]
            }
            
            print(f"Added {quantity} shares of {stock_name} at ${stock_prices[stock_name]:.2f} per share.")
            
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
    
    if not portfolio:
        print("\nNo stocks were added to the portfolio.")
        return
    
    # Calculate total portfolio value
    total_value = sum(item['value'] for item in portfolio.values())
    
    # Display portfolio summary
    print("\n" + "=" * 40)
    print("Your Portfolio Summary:")
    print("=" * 40)
    for stock, data in portfolio.items():
        print(f"{stock}: {data['quantity']} shares @ ${data['price']:.2f} = ${data['value']:.2f}")
    print("-" * 40)
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}")
    print("=" * 40)
    
    # Option to save to file
    save_option = input("\nWould you like to save this portfolio to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter filename to save (e.g., portfolio.txt): ")
        try:
            with open(filename, 'w') as f:
                f.write("Stock Portfolio Summary\n")
                f.write("=" * 40 + "\n")
                for stock, data in portfolio.items():
                    f.write(f"{stock}: {data['quantity']} shares @ ${data['price']:.2f} = ${data['value']:.2f}\n")
                f.write("-" * 40 + "\n")
                f.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
                f.write("=" * 40 + "\n")
            print(f"Portfolio saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

# Run the portfolio tracker
if __name__ == "__main__":
    stock_portfolio_tracker()