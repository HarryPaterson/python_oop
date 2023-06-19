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

