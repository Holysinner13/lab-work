from main import logger
from time import sleep
import math


"""Exercise 4"""
logger.info('Completing task 4...')
sleep(2)


class Vector:
    """
    Class Vector
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        """
        Initializing class variables
        :param x: point coordinates
        :param y: point coordinates
        """
        self.x = x
        self.y = y

    def __len__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y)
        return result

    def __lt__(self, other) -> bool:
        return self.x < other.x or self.x == other.x and self.y < other.y


vector = Vector(3, 4)
vector2 = Vector(1, 1)
vector3 = vector + vector2
print(vector3.x, vector3.y)
print(vector > vector2)
print(vector3 < vector)
