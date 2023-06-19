#  Encapsulation

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        print("Do I say it smells nice, or tastes nice...?")

sidney = Snake()
sidney.breathe() # Animal method
sidney.seek_heat() # Reptile Method
sidney.use_tongue_to_smell() # Snake method

# Encapsulation is also really good, for protecting important variables/objects

# Types of modifiers in pyton
# Public
# Private
# Protected