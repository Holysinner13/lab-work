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

    def __init__(self, x, y):
        """
        Initializing class variables
        :param x: point coordinates
        :param y: point coordinates
        """
        self.x = x
        self.y = y

    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)


vector = Vector(3, 4)
print(vector.__len__())
