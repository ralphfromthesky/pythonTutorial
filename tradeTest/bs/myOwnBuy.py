import ccxt as cc
import importingGlobal as imp
import pandas as pan

bin = cc.binance({
        'apiKey': imp.ak,
        'secret': imp.pk
})

def buy_order():
    try:
        symbol = 'TNSR/USDT'
        last_price = bin.fetch_ticker(symbol)['last']
        balance = bin.fetch_balance()['total']['USDT']
        remaining_balance = balance / last_price
        if remaining_balance:     
            bin.create_market_buy_order(symbol=symbol, amount=remaining_balance)
            print('succesfully placed!')
        else:
            print('buy fails!')
            
    except cc.NetworkError as e:
        print('network error: ', e)
    except cc.ExchangeError as e:
        print('exchange error: ',e)
    except Exception as e:
        print('error : ', e)
     

buy_order()    
bal = bin.fetch_balance()['total']
for a, b in bal.items():
    if b > 0:
        print(a, b)
