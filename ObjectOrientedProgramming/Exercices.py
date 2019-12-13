""" Problem 1 """
import math


class line:

    def __init__(self, coor1, coor2):
        self.x1 = coor1[0]
        self.x2 = coor2[0]
        self.y1 = coor1[1]
        self.y2 = coor2[1]

    def distance(self):
        distance = math.sqrt((self.x2 - self.x1) ** 2 +
                             (self.y2 - self.y1) ** 2)
        return distance

    def slope(self):
        slope = (self.y2 - self.y1)/(self.x2 - self.x1)
        return slope


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = line(coordinate1, coordinate2)

print(line.distance(li))
print(line.slope(li))


""" Problem 2 """


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.h = height
        self.r = radius

    def volume(self):
        volume = Cylinder.pi * self.r ** 2 * self.h
        return volume

    def surface_area(self):
        aire = 2 * Cylinder.pi * self.r * (self.h + self.r)
        return aire


c = Cylinder(2, 3)
print(Cylinder.volume(c))
print(Cylinder.surface_area(c))
