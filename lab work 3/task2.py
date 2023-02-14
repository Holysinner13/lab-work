from main import logger
from time import sleep
import math


"""Exercise 2"""
logger.info('Completing task 2...')
sleep(2)


class Circle:
    """A class, that allows you to create a circle"""

    def __init__(self, radius, a, b):
        """
        Initializing class variables
        :param a: circle center coordinate
        :param b: circle center coordinate
        :param radius: circle radius
        """
        self.radius = radius
        self.a = a
        self.b = b

    def area(self):
        """A method, that allows you to calculate the area of a circle"""
        s = math.pi * self.radius ** 2
        return f'The area of the circle is {round(s, 2)}'

    def perimeter(self):
        """A method, that allows you to calculate the perimeter of a circle"""
        p = 2 * math.pi * self.radius
        return f'The perimeter of the circle is {round(p, 2)}'

    def test_belongs(self, x, y):
        """
        A method, that allows you to check whether point A belongs to circle C or not
        :param x: point A coordinate
        :param y: point A coordinate
        """
        if (x - self.a) ** 2 + (y - self.b) ** 2 <= self.radius ** 2:
            return f'point A with coordinates {x, y} belongs to circle C with radius {self.radius}'
        return f'point A with coordinates {x, y} does not belong to circle C with radius {self.radius}'


circle = Circle(1, 0, 0)
print(circle.area())
print(circle.perimeter())
print(circle.test_belongs(2, 2))
print()
