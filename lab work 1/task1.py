from main import logger
from time import sleep


"""Задание 1"""
logger.info('Выполнение задания 1...')
sleep(2)


def func(num):
    if num % 2 == 0:
        return f'Число {num} является четным'
    return f'Число {num} является нечетным'


print(func(6), '\n')
