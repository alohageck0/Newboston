__author__ = 'royalfiish'

var1, var2, var3 = ['item1', 'item2', 33]
print(var2)


def count_avg(list):
    first, *middle, last = list
    avg = sum(middle) / len(middle)
    return avg


count_avg([11, 44, 55, 33, 22, 66, 55])
var = int(count_avg([11, 44, 55, 33, 22, 66, 55, 33, 22, 55, 44, 22]))
print(var)