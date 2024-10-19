import importingGlobal as imp
import pandas as pan
import ccxt as cc


bin = cc.binance({
        'apiKey': imp.ak,
        'secret': imp.pk
})

def sell_order(coin):
        symbol = 'TNSR/USDT'
        ticker = bin.fetch_ticker(symbol)
        balance = bin.fetch_balance()['total']['TNSR']
        if balance > 0:
                try:
                        seling_coin = bin.create_market_sell_order(symbol=coin, amount=balance)    
                        if 'id' in seling_coin:
                                print(f'Succesffully sold with the id of, {seling_coin['id']}')    
                        else:
                                print('Failed selling')                
                except cc.NetworkError as e:
                        print("Network error:", e)
                except cc.ExchangeError as e:
                        print("Exchange error:", e)
                except Exception as e:
                        print("Error:", e)     
        else: 
                print('Selling Failed')

sell_order('TNSR/USDT')
balance = bin.fetch_balance()['total'].items()
for a, b in balance:
        if b > 0:
                print(f'{a} - {b}')