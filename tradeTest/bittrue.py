import ccxt

# Create an instance of the Bitrue exchange
bitrue = ccxt.bitrue()

try:
    # Fetch all available markets (symbols)
    markets = bitrue.fetch_markets()

    # Extract base and quote currencies from market symbols
    coins = set()
    for market in markets:
        base_currency, quote_currency = market['base'], market['quote']
        coins.add(base_currency)
        coins.add(quote_currency)

    # Print the list of all available coins
    print("Available coins on Bitrue:")
    for coin in coins:
        print(coin)

except Exception as e:
    print("An error occurred:", e)
