"""Задание 2"""


def new_power(a, b):
    result = a ** b
    return print(f'Число {a} в степени {b} = {result}')


nums = input('Введите два целых числа (через пробел): ')
new_power(int(nums.split()[0]), int(nums.split()[1]))
