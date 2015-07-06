__author__ = 'royalfiish'


def foo(*args):
    total = 0
    for n in args:
        total += n
    print(total)


foo(5, 4, 1)
foo(55, 33, 22, 55, 66, 44)
