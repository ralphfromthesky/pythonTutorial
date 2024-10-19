import ccxt as cc

# Initialize the Binance exchange
binance = cc.binance()

# Fetch all available symbols
symbols = binance.fetch_markets()

# Print the symbols paired with USDT and their current prices
for symbol in symbols:
    if 'USDT' in symbol['symbol']:
        # Fetch the ticker for the symbol to get the current price
        ticker = binance.fetch_ticker(symbol['symbol'])
        current_price = ticker['last']
        
        print(f"Symbol: {symbol['symbol']}, Current Price: {current_price}")
