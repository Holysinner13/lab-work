from main import logger
from time import sleep
import math


"""Задание 2"""
logger.info('Выполнение задания 2...')
sleep(2)


class Circle:
    """Класс, который позволяет создать круг"""

    def __init__(self, radius, a, b):
        """
        Инициализация переменных класса
        :param a: координата центра круга
        :param b: координата центра круга
        :param radius: радиус круга
        """
        self.radius = radius
        self.a = a
        self.b = b

    def area(self):
        """Метод, который позволяет вычислить площадь круга"""
        s = math.pi * self.radius ** 2
        return f'Площадь круга равна {round(s, 2)}'

    def perimeter(self):
        """Метод, который позволяет вычислить периметр круга"""
        p = 2 * math.pi * self.radius
        return f'Периметр круга равен {round(p, 2)}'

    def test_belongs(self, x, y):
        """
        Метод, который позволяет проверить, принадлежит ли точка А окружности С или нет
        :param x: координата точки А
        :param y: координата точки А
        """
        if (x - self.a) ** 2 + (y - self.b) ** 2 <= self.radius ** 2:
            return f'точка А с координатами {x, y} принадлежит кругу С с радиусом {self.radius}'
        return f'точка А с координатами {x, y} не принадлежит кругу С с радиусом {self.radius}'


circle = Circle(1, 0, 0)
print(circle.area())
print(circle.perimeter())
print(circle.test_belongs(2, 2))
print()
