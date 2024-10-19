import ccxt as cc
import importingGlobal as imp
import schedule
import time

def buy_coin():
    bn = cc.binance({
        'apiKey': imp.ak,
        'secret': imp.pk
    })

    initial = 50
    symbol = 'OMNI/USDT'

    try:
        print('Attempting to buy...')
        ticker = bn.fetch_ticker(symbol)
        current_price = ticker['last']
        amount_to_buy = initial / current_price
        order = bn.create_market_buy_order(symbol, amount_to_buy)
        print("Buy order placed successfully:", order)
    except cc.NetworkError as e:
        print("Network error:", e)
    except cc.ExchangeError as e:
        print("Exchange error:", e)
    except Exception as e:
        print("Error:", e)

    balance = bn.fetch_balance()
    print("Balances:")
    for asset, amount in balance['total'].items():
        if amount > 0:
            print(f"{asset}: {amount}")

def stop_execution():
    print("Stopping execution...")
    exit()

# Schedule the buying function to run at 7:59 PM
schedule.every().day.at("19:59").do(buy_coin)

# Schedule the stop function to run 10 minutes after execution
schedule.every().day.at("20:09").do(stop_execution)

# Keep the script running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
