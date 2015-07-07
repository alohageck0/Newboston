__author__ = 'royalfiish'

class fish:

    def __init__(self, x):
        print("object created")
        self.energy = x

    def swim(self):
        print("I am swimming")

    def checkEnergy(self):
        print(self.energy)


shark = fish()

