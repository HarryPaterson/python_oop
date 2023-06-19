# Animal class

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print('One breath at time, in and out')

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print ('Time to find a mate')

    def move(self):
        print('Onwards and upwards')

cat =  Animal()

#cat.breathe()
