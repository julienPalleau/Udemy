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
