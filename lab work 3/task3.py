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

    def table_mult(self, num):
        """Метод, который создает и отображает таблицу умножения заданного целого числа"""
        print(f'Таблица умножения числа {num}')
        for i in range(1, 11):
            print(num, 'x', i, '=', num * i)

    def all_table_mult(self):
        """Метод для отображения всех таблиц целочисленного умножения"""
        print('Таблица умножения всех чисел от 1 до 9')
        for i in range(1, 10):
            print(*range(i, i * 10, i), sep='\t')

    def list_div(self, num):
        """Метод, который получает все делители заданного числа в новом списке с именем Ldiv"""
        ldiv = [i for i in range(2, num + 1) if num % i == 0]

        return ldiv

    def list_div_prim(self, num):
        """Метод, который получает все простые делители заданного целого числа"""
        result = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))),
                             [i for i in range(2, num + 1) if num % i == 0]))

        return result


some_num = Copulation()
print(some_num.__doc__, '\n')
print(some_num.factorial(5))
print(some_num.sum(10))
print(some_num.test_prim(8))
print(some_num.test_prims(1, 17))
some_num.table_mult(2)
some_num.all_table_mult()
print(some_num.list_div(24))
print(some_num.list_div_prim(9990))
print()
