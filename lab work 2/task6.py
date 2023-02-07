from main import logger
from time import sleep


"""Задание 6"""
logger.info('Выполнение задания 6...')
sleep(2)


some_list = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, -2, 8), (0, 0, 0), (3, -4, -5)]

print('Дан некоторый список -', some_list)
print('Отсортированный список по сумме кортежей -', sorted(some_list, key=sum))
print('Отсортированный список по третьим элементам из кортежей -', sorted(some_list, key=lambda x: x[2]))

some_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}
print('\nДан словарь -', some_dict)
print('Ключи словаря в алфавитном порядке -', *sorted(some_dict.keys()))
new_dict = {i: some_dict[i] for i in sorted(some_dict, key=some_dict.get)}
print('Ключи словаря в порядке убывания по значениям -', *new_dict.keys())
print()
