"""Задание 1"""


def func(num):
    if num % 2 == 0:
        return f'Число {num} является четным'
    return f'Число {num} является нечетным'


print(func(6))
