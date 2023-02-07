from main import logger
from time import sleep


"""Задание 2"""
logger.info('Выполнение задания 2...')
sleep(2)


def new_power(a, b):
    result = a ** b
    return f'Число {a} в степени {b} = {result}'


nums = input('Введите два целых числа (через пробел): ')
print(new_power(int(nums.split()[0]), int(nums.split()[1])))
print()
