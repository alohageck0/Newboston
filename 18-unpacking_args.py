__author__ = 'royalfiish'

def foo(name='Boston', action = 'eat', item = 'apple'):
    print(name, action, item)

data1 = ['LA', '222', '333']
data2 = ['NY', '444', '555']

foo(*data1)
foo(*data2)