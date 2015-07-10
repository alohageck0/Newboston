__author__ = 'royalfiish'

movies = {'Titanic': 1999, 'Terminator': 1994, 'Avatar': 2004}

movies1 = dict(Titanic=1999, Terminator=1994, Avatar=2004)

print(movies["Titanic"])
print(movies1['Titanic'])

for k, v in movies1.items():
    print(k, "-", v)
