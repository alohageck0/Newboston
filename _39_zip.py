__author__ = 'royalfiish'

first = ['XX', 'XXX', 'XXXX']
last = ['YY', 'YYY', 'YYYY']

full = zip(first, last)

for a, b in full:
    print(a, b)

# print(list(full))