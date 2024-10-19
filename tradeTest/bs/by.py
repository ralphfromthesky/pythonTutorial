import ccxt
import importingGlobal as imp

bin = ccxt.binance({
    'apiKey': imp.ak,
    'secret': imp.pk
})

symbol = 'BAKE/USDT'
usdt_amount = 100

# Fetch the ticker for the specified symbol to get the current price
ticker = bin.fetch_ticker(symbol)
current_price = ticker['last']

# Calculate the amount of the symbol to buy with the provided USDT amount
amount_to_buy = usdt_amount / current_price

try:
    order = bin.create_market_buy_order(symbol, amount_to_buy)
    print("Buy order placed successfully:", order)
except ccxt.NetworkError as e:
    print("Network error:", e)
except ccxt.binError as e:
    print("bin error:", e)
except Exception as e:
    print("Error:", e)
    
updated_balance = bin.fetch_balance()

# Print the updated balances for all assets
print("\nUpdated Balances:")
for asset, amount in updated_balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")
