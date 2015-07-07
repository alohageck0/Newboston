__author__ = 'royalfiish'
class fish:

    breed = "grouper"

    def __init__(self, x, name):
        # print("object created")
        self.energy = x
        self.name = name

    def swim(self):
        print("I am swimming")

    def checkEnergy(self):
        print("Ammount of energy is " + str(self.energy))

fish1 = fish(10, 'Bobby')
fish2 = fish(15, 'Garry')

print(fish1.name)
print(fish2.name)
print(fish1.energy)
print(fish1.breed)
print(fish2.breed)