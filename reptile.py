# Inheritance

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles have 4 legs
        self.heart_chmabers = [3, 4]
        self.amniotic_eggs = None

    def __seek_heat(self):
        return "it's chilly outside, I need a sunbed"

    def _show_seek_heat(self):
        print(self.__seekheat())

    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("If I have it, may as well use it")

    def attract_mates_through_scent(self):
        print("Time to put on aftershave")


bulbasaur = Reptile()

#bulbasaur.hunt() # Reptile method
#bulbasaur.breathe() # Animal method