from main import logger
from time import sleep
import math

"""Exercise 2"""
logger.info('Completing task 2...')
sleep(2)


class Circle:
    """A class, that allows you to create a circle"""

    def __init__(self, radius: int | float, a: int | float, b: int | float) -> None:
        """
        Initializing class variables
        :param a: circle center coordinate
        :param b: circle center coordinate
        :param radius: circle radius
        """
        self.radius = radius
        self.a = a
        self.b = b

    def area(self) -> float:
        """A method, that allows you to calculate the area of a circle"""
        s = math.pi * self.radius ** 2
        return s

    def perimeter(self) -> float:
        """A method, that allows you to calculate the perimeter of a circle"""
        p = 2 * math.pi * self.radius
        return p

    def test_belongs(self, x: int | float, y: int | float) -> bool:
        """
        A method, that allows you to check whether point A belongs to circle C or not
        :param x: point A coordinate
        :param y: point A coordinate
        """
        if (x - self.a) ** 2 + (y - self.b) ** 2 <= self.radius ** 2:
            return True
        return False


def main():
    circle = Circle(1, 0, 0)
    print(f'The area of the circle is {round(circle.area(), 2)}')
    print(f'The perimeter of the circle is {round(circle.perimeter(), 2)}')
    point = 2
    point_1 = 2
    print(f'point A with coordinates {point, point_1} %s to circle C with radius {circle.radius}'
          % ('belongs' if circle.test_belongs(point, point_1) else 'does not belong'))


main()
