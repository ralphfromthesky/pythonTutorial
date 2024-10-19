import ccxt as cc

# Initialize the Binance exchange
binance = cc.binance()

# Fetch all available symbols
symbols = binance.fetch_markets()

# Define the symbol you want to search for
target_symbol = 'OMNI/USDT'

# Search for the target symbol
found_symbol = None
for symbol in symbols:
    if symbol['symbol'] == target_symbol:
        found_symbol = symbol
        break

# Check if the symbol was found
if found_symbol:
    print("Symbol found:", found_symbol)
else:
    print("Symbol not found:", target_symbol)
