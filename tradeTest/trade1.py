import ccxt
import schedule
import time

def check_new_listings():
    # Connect to Binance exchange
    exchange = ccxt.binance()

    # Fetch the list of markets
    markets = exchange.fetch_markets()

    # Define the base currency you want to trade with (e.g., USDT)
    base_currency = 'USDT'

    # Define the time you want to check for new listings (e.g., 9 PM)
    target_time = "21:00"

    # Check if any new markets (coins) are listed
    new_listings = [market for market in markets if market['quote'] == base_currency and market['timestamp'] == target_time]

    # If there are new listings, print them and execute buy orders
    if new_listings:
        print("New listings found at", target_time)
        for market in new_listings:
            symbol = market['symbol']
            # Specify the amount of the new coin you want to buy
            amount = 100  # Change this to the desired amount
            # Specify the price at which you want to execute the trade
            # You can fetch the current price using exchange.fetch_ticker(symbol)
            # For simplicity, let's assume a market order
            try:
                order = exchange.create_market_buy_order(symbol, amount)
                print("Buy order placed successfully for", symbol, ":", order)
            except ccxt.NetworkError as e:
                print("Network error:", e)
            except ccxt.ExchangeError as e:
                print("Exchange error:", e)
            except Exception as e:
                print("Error:", e)

# Schedule the check_new_listings function to run every minute
schedule.every(1).minutes.do(check_new_listings)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
