import ccxt as cc
import importingGlobal as imp
import pandas as pan

bin = cc.binance({
        'apiKey': imp.ak,
        'secret': imp.pk
})
balance = bin.fetch_balance()
for a, b in balance['total'].items():
    if b > 0:
        print(pan.DataFrame(balance))

