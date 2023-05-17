from main import logger
from time import sleep


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


def fac_with_cycle(n):
    """
    Функция, возвращающая факториал числа
    :param n: число
    :return: None
    """
    result = 1

    for i in range(2, n + 1):
        result *= i

    return f'Факториал числа {n} = {result}'


def fac_with_recursion(n):
    """
    Функция, возвращающая факториал числа
    :param n: число
    :return: None
    """
    if n == 0:
        return 1
    return fac_with_recursion(n - 1) * n


print(fac_with_cycle(5))
print(f'Факториал числа 6 =', fac_with_recursion(6), '\n')
