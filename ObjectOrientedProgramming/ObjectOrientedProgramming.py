class Dog1:
    # Class Object Atrribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


# Les 2 syntaxes ci-dessous sont valide
sam = Dog1(breed='Lab', name='Sam')
frank = Dog1('Huske', 'Medor')

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


class Animal1:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog2(Animal1):
    def __init__(self):
        Animal1.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


d = Dog2()
d.whoAmI()
d.eat()
d.bark()


""" Polymorphism """


class Dog3:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'


class Cat1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


niko = Dog3('Niko')
felix = Cat1('Felix')

print(niko.speak())
print(felix.speak())

""" There are few different way to demonstrate polymorphisme. First, whith a loop:"""
for pet in [niko, felix]:
    print(pet.speak())

""" Another is with funtions """


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

""" 
In both cases we were able to pass in different object types, and we obtained object-specific results from the same mechanism.
A more common practice is to use abstract classes and inheritance. An abstract class is one that never expects to be instantiated. 
For example, we will never have an Animal object, only Dog and Cat objects, although Dogs and Cats are derived from Animals:
"""


class Animal2:
    def __init__(self, name):  # Consturctor of the class
        self.name = name

    def speak(self):    # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abastract method")


class Dog4(Animal2):
    def speak(self):
        return self.name+' says Woof!'


class Cat2(Animal2):
    def speak(self):
        return self.name+' says Meow!'


fido = Dog4('Fido')
isis = Cat2('Isis')

print(fido.speak())
print(isis.speak())

""" Special Methods """
""" Finally let's go over special methods. Classes in Python can implement 
certain operations with special method names. These methods are not actually 
called directly but by Python specific language syntax. For example let's 
create a Book class:"""


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "Jose Portilla", 159)
# special Methods
print(book)
print(len(book))
del book
