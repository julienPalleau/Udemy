class Dog:
    # Class Object Atrribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


# Les 2 syntaxes ci-dessous sont valide
sam = Dog(breed='Lab', name='Sam')
frank = Dog('Huske', 'Medor')

print(sam.breed, sam.name, sam.species)
print(frank.breed, frank.name, frank.species)

""" Methods """


class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * radius**2

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = Circle.pi * new_radius**2

    # Method for getting Circonference
    def getCircumference(self):
        return self.radius*Circle.pi*2


c = Circle()
print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

c.setRadius(2)
print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

""" Inheritance """
