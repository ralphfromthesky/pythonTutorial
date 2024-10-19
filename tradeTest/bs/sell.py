import ccxt
import importingGlobal as imp

bin = ccxt.binance({
    'apiKey': imp.ak,
    'secret': imp.pk
})

symbol = 'TNSR/USDT'

balance = bin.fetch_balance()

bake_balance = balance['total']['TNSR']

if bake_balance > 0:
    try:
        sell_order = bin.create_market_sell_order(symbol, bake_balance)
        if 'id' in sell_order:
            print("Sell order placed successfully. Order ID:", sell_order['id'])
        else:
            print("Failed to place sell order.")
    except ccxt.NetworkError as e:
        print("Network error:", e)
    except ccxt.ExchangeError as e:
        print("Exchange error:", e)
    except Exception as e:
        print("Error:", e)
else:
    print(f"You don't have any {symbol} tokens available to sell.")
    
    
updated_balance = bin.fetch_balance()

print("\nUpdated Balances:")
for asset, amount in updated_balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")