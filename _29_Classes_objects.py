__author__ = 'royalfiish'
class Enemy:
    life = 3

    def attack(self, x):
        print("Hit!")
        self.life -= x
        self.checkLife()

    def checkLife(self):
        if self.life <= 0:
            print("DEAD!")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack(5)
enemy2.checkLife()