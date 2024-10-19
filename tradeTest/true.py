import ccxt
import configKey as ck
import time

# Connect to Bitrue exchange
bitrue = ccxt.bitrue({
    'apiKey': ck.aKey,
    'secret': ck.secret
})

symbol = 'BTC/USDT'
initialInvestment = 100
buySuccesful = False

def buy_and_monitor():
    global buySuccesful
    
    # Fetch the current ticker price
    ticker = bitrue.fetch_ticker(symbol)
    currentPrice = ticker["last"]
    currentValue = initialInvestment * currentPrice
    
    try:
        # Create a market buy order
        order = bitrue.create_market_buy_order(symbol, initialInvestment)
        print("Buy order placed successfully:", order)
        buySuccesful = True
    except ccxt.NetworkError as e:
        print("Network error:", e)
    except ccxt.ExchangeError as e:
        print("Exchange error:", e)
    except Exception as e:
        print("Error:", e)
    
    # Check for the condition to sell
    if buySuccesful and currentValue >= initialInvestment * 5:
        try:
            # Create a market sell order
            sell_order = bitrue.create_market_sell_order(symbol, order['filled'])
            print("Sell order placed successfully:", sell_order)
        except ccxt.NetworkError as e:
            print("Network error:", e)
        except ccxt.ExchangeError as e:
            print("Exchange error:", e)
        except Exception as e:
            print("Error:", e)

# Schedule the buy_and_monitor function to run every minute
while True:
    buy_and_monitor()
    time.sleep(60)  # Check every minute
