import ccxt as cc
import importingGlobal as imp

bin = cc.binance({
        'apiKey': imp.ak,
    'secret': imp.pk
})
updated_balance = bin.fetch_balance()

print("\nUpdated Balances:")
for asset, amount in updated_balance['total'].items():
    if amount > 0:
        print(f"{asset}: {amount}")