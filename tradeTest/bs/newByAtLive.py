import ccxt as cc
import importingGlobal as imp
import time

bn = cc.binance({
    'apiKey': imp.ak,
    'secret': imp.pk
})

# balance = bn.fetch_balance()
initial = 50
succesfullBuy = False
symbol = 'OMNI/USDT'

while not succesfullBuy:
    try:
        print('Attempting to buy...')
        ticker = bn.fetch_ticker(symbol)
        # current_price = ticker['last']
        # amount_to_buy = initial / current_price
        # order = bn.create_market_buy_order(symbol, amount_to_buy)
        print("Buy order placed successfully:", symbol)
        succesfullBuy = True
    except cc.NetworkError as e:
        print("Network error: --", e)
    except cc.ExchangeError as e:
        print("Exchange error: ---", e)
    except Exception as e:
        print("Error: --", e)
    # finally:
    #     time.sleep(0.1)  # Wait before retrying

balance = bn.fetch_balance()
print("Balances:")
for asset, amount in balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")
        

