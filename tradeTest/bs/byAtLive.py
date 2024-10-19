import ccxt as cc
import importingGlobal as imp
import time

bn = cc.binance({
    'apiKey': imp.ak,
    'secret': imp.pk
})

balance = bn.fetch_balance()
initial = 100
succesfullBuy = False
succesfullSell = False
symbol = 'BAKE/USDT'
ticker = bin.fetch_ticker(symbol)
current_price = ticker['last']
amount_to_buy = initial / current_price

def buy():
    global succesfullBuy
    while not succesfullBuy:
        try:
            print('Attempting to buy...')
            order = bn.create_market_buy_order(symbol, amount_to_buy)
            print("Buy order placed successfully:", order)
            succesfullBuy = True
        except cc.NetworkError as e:
            time.sleep(0.1) 
            print("Network error:", e)
        except cc.ExchangeError as e:
            time.sleep(0.1) 
            print("Exchange error:", e)
        except Exception as e:
            time.sleep(0.1) 
            print("Error:", e)
        finally:
            break
def sell():
    global succesfullSell
    while not succesfullSell:
        try:
            print('Attempting to Sell...')
            # order = bn.create_market_sell_order(symbol, initial)
            balance = bn.fetch_balance()
            amount_to_sell = balance['total'][symbol.split('/')[0]]
            order = bn.create_market_sell_order(symbol, amount_to_sell)
            print("Sell successfully:", order)
            succesfullSell = True
        except cc.NetworkError as e:
            print("Network error:", e)
            time.sleep(0.1)  # Retry after 1 second
        except cc.ExchangeError as e:
            print("Exchange error:", e)
            time.sleep(0.1)  # Retry after 1 second
        except Exception as e:
            print("Error:", e)
            time.sleep(0.1)  # Retry after 1 second
        finally:
            break


buy() 

balance = bn.fetch_balance()
print("Balances:")
for asset, amount in balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")

if succesfullBuy and initial * 5:
    sell()       

balance = bn.fetch_balance()
print("Balances:")
for asset, amount in balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")