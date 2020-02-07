# example.py
#
# Example of calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

closing = {
   'ACME': 45.23,
   'MSFT': 610.78,
   'GOOG': 38.20,
   'FB': 20.75
}

print(prices.keys() & closing.keys())
print(prices.keys() - closing.keys())
# dict_values does not have set operations &, or even +
#print(prices.values() + closing.values())
print(prices.values())

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)

# zip iterator can only be iterated once
price_ticker = zip(prices.values(), prices.keys())
print('min:', min(price_ticker), sep=' ')
#print('max:', max(price_ticker), sep=' ')

