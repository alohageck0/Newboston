__author__ = 'royalfiish'

stocks = {'GOOG': 444, 'AAPL': 333, 'AMZN': 143, 'SONY': 532}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))
