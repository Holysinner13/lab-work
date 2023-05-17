from main import logger
from time import sleep


"""Задание 2"""
logger.info('Выполнение задания 2...')
sleep(2)


def new_power(a, b):
    """
    Функция, которая находит a в степени b
    :param a: целое число
    :param b: целое число
    :return: None
    """
    result = a ** b
    return f'Число {a} в степени {b} = {result}'


nums = input('Введите два целых числа (через пробел): ').split()
print(new_power(int(nums[0]), int(nums[1])))
print()
