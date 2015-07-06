__author__ = 'royalfiish'


def age_test(age):
    limit = age / 2 + 7
    return limit

for n in range(18, 45):
    test = age_test(n)
    print("Age", n, "limit is", test)