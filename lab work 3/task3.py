from main import logger
from time import sleep
from math import sqrt


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


class Copulation:
    """Класс, позволяющий выполнять различные действия над целыми числами"""

    def factorial(self, num):
        """Метод, который позволяет вычислить факториал целого числа"""
        result = 1

        for i in range(2, num + 1):
            result *= i

        return f'Факториал числа {num} = {result}'

    def sum(self, num):
        """Метод, позволяющий вычислить сумму первых n целых чисел """
        result = num * (num + 1) / 2
        return f'Сумма первых целых чисел от 1 до {num} равна {int(result)}'

    def test_prim(self, num):
        """Метод для проверки простоты заданного целого числа"""
        i = 2
        while i <= sqrt(num):
            if num % i == 0:
                return f'Число {num} - не является простым'
            i += 1
        if num > 1:
            return f'Число {num} простое число'

    def test_prims(self, num1, num2):
        """Метод, позволяющий проверить, являются ли два числа простыми между собой"""
        simple_num = []
        for number in range(num1, num2 + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    simple_num.append(number)

        return f'Простые числа в диапазоне от {num1} до {num2} - {simple_num}'

    def table_mult(self):
        """Метод, который создает и отображает таблицу умножения заданного целого числа"""

    def all_table_mult(self):
        """Метод для отображения всех таблиц целочисленного умножения"""

    def list_div(self):
        """Метод, который получает все делители заданного числа в новом списке с именем Ldiv"""

    def list_div_prim(self):
        """Метод, который получает все простые делители заданного целого числа"""


some_num = Copulation()
print(some_num.__doc__, '\n')
print(some_num.factorial(5))
print(some_num.sum(10))
print(some_num.test_prim(8))
print(some_num.test_prims(1, 17))
print()
