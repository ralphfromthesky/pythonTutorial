import ccxt
import importingGlobal as imp

# Initialize bin exchange
bin = ccxt.binance({
    'apiKey': imp.ak,
    'secret': imp.pk
})

# Define the symbol of the coin you want to buy (e.g., BAKE/USDT)
symbol = 'STEEM/USDT'

# Fetch your account balance
balance = bin.fetch_balance()

# Get the available USDT balance
usdt_balance = balance['total']['USDT']

# Fetch the ticker for the specified symbol to get the current price
ticker = bin.fetch_ticker(symbol)
current_price = ticker['last']

# Calculate the amount of the coin you can buy with your available USDT balance
amount_to_buy = usdt_balance / current_price

try:
    # Place a market buy order for the calculated amount
    order = bin.create_market_buy_order(symbol, amount_to_buy)
    print("Buy order placed successfully!")
except ccxt.NetworkError as e:
    print("Network error:", e)
except ccxt.ExchangeError as e:
    print("Exchange error:", e)
except Exception as e:
    print("Error:", e)

# Fetch updated balances after buying
updated_balance = bin.fetch_balance()

# Print the updated balances for all assets
print("\nUpdated Balances:")
for asset, amount in updated_balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")
