import ccxt as cc
import time 
bin = cc.binance()
markets = bin.fetch_markets()
base_currency = 'USDT'
target_time = "21:00"
symbols = [market['symbol'] for market in markets]
# print('list icon symbols')
# for symbol in symbols:
#     print(symbol)
# coin = 'BAKE/USDT'
# interval = 1

# while True:
#     try:
#       ticker = bin.fetch_ticker(coin)
#       print(ticker['last'])
#       time.sleep(interval)

# # found = False
# # for market in markets:
# #     if market['symbol'] == coin:
# #         found = True
# #         print('found ' + coin)
# #         break
# # if not found:
# #     print('no coin')
#     except Exception as ex:
#         print('error occur')
#         time.sleep(interval)
# new_listings = [market for market in markets if market['quote'] == base_currency]
# for mar in markets:
#     if mar['quote'] == base_currency:
#         try:
#              print(mar)
#         except Exception as e:
#              print('error ' + e)
printeed = 0
while True:
    time.sleep(1)
    print(symbols)
    printeed += 1
    
    if printeed == 10:
        print('alraedy printed 10')
        break
