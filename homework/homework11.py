'''
Carlos Landaverde
12/2/2024
CS100 Section 001
Homework 11
'''

class Dog:
    '''a class to create dog objects'''

    species = 'Canis familiaris' # initialize a species attribute for every dog object

    def __init__(self, name, breed): # initialize dog object with name and breed
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick): # initialize the teach function
        self.tricks.append(trick)
        print(self.name + " knows " + trick + ".")

    def knows(self, trick): # initialize the knows function
        if trick in self.tricks:
            print("Yes, " + self.name + " knows " + trick + ".")
        else:
            print("No, " + self.name + " does not know " + trick + ".")

        return trick in self.tricks

sugar = Dog('Sugar', 'border collie') # create a dog object
print(sugar.name) # print its name attribute
print(sugar.breed) # print its breed attribute
print(sugar.tricks) # print its tricks attribute

sugar.teach('frisbee') # teach frisbee to sugar

print(sugar.knows('frisbee')) # check if sugar knows frisbee
print(sugar.knows('arithmetic')) # check if sugar knows arithmetic

print(Dog.species) # print the species attribute for the dog class
print(sugar.species) # print the species attribute for sugar


