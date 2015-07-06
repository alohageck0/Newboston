__author__ = 'royalfiish'
numbersTaken = [4, 6, 7, 11, 15]

for n in numbersTaken:
    if n in numbersTaken:
        continue
    print(n)