__author__ = 'royalfiish'
magicNumber = 66
step = 1
for n in range(101):
    if n == magicNumber:
        print("Yes")
        break
    step +=1
print(step)