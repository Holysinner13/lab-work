from main import logger
from time import sleep


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


def fac(n):
    """
    Функция, возвращающая факториал числа
    :param n: число
    :return: None
    """
    result = 1

    for i in range(2, n + 1):
        result *= i

    return f'Факториал числа {n} = {result}'


print(fac(5))


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(f'Факториал числа 6 =', fac(6), '\n')
