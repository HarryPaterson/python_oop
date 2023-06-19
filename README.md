<h1 style="text-align: center;">Object Orientated Programming (OOP)</h1>

### Contents
* Classes and Instantiation
* The Four Pillars of OOP:
  * Abstraction
  * Inheritance
  * Encapsulation
  * Polymorphism

### Classes and Instantiation

Classes are blueprints or templates that define the structure and behavior of objects in object-oriented programming.
Classes encapsulate data (attributes) and behavior (methods) that operate on that data.
Objects are instances of classes; they are created from a class and represent individual entities with their own attributes and behaviors.
Instantiation is the process of creating an object from a class.
The __init__ method is a special method in Python classes that is automatically called when an object is instantiated.
The __init__ method is used to initialize the attributes of an object and perform any setup or initialization tasks.
The self parameter in the __init__ method refers to the instance of the class being created.

#### Example
```
# Classes

# Creating a class - this is like a template
class Dog:

    animal_kind = "canine"
    def bark(self): # class function # methods
        self.animal_kind
        return "woof"

#print(Dog.animal_kind)
#print(Dog.bark(Dog))

# Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
print(lassie.bark())

# Class variables can be overwritten

fido.animal_kind = "Big Dog"
print(fido.animal_kind) # Big Dog
print(lassie.animal_kind) # canine

print(lassie.bark())
```

### The Four Pillars of OOP:

The Four Pillars of OOP refers to four key features of OOP which collectively provide a foundation for designing and building robust, scalable, and maintainable software systems.

#### Abstraction
Abstraction focuses on representing essential features and behavior while hiding unnecessary details. It allows the creation of abstract classes and interfaces that define a common set of methods without specifying their implementation. Abstraction helps in managing complexity, providing a high-level view, and enabling code modularity and maintainability.

#### Example
```
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
```

#### Inheritance

Inheritance is the mechanism by which one class acquires the properties and behavior of another class. It allows for code reuse and the creation of hierarchical relationships between classes. Inheritance enables the derived class to inherit attributes and methods from the base class, facilitating code extensibility and promoting the "is-a" relationship.

#### Example
```
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
```
#### Encapsulation

Encapsulation is the bundling of data and methods into a single unit called a class. It hides the internal details of an object and provides a public interface for interacting with the object. Encapsulation helps in data protection and promotes modular and organized code.

#### Example
```
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
```

#### Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It allows methods with the same name but different implementations to be invoked based on the type of the object. Polymorphism enables code flexibility, extensibility, and the ability to write generic code that can operate on objects of different types.

#### Example
```
# Polymorphism

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")

    def constrict(self):
        print("and...squeeeeeze")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("I'm growing out of this now")

    def breathe(self):
        print("I am breathing but I am a Python!")
```