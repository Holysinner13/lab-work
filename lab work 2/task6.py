from main import logger
from time import sleep


"""Задание 6"""
logger.info('Выполнение задания 6...')
sleep(2)


some_list = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, -2, 8), (0, 0, 0), (3, -4, -5)]

print('Дан некоторый список -', some_list)
sort_by_sum_dict = sorted(some_list, key=sum)
print('Отсортированный список по сумме кортежей -', sort_by_sum_dict)
sort_by_3_item = sorted(some_list, key=lambda x: x[2])
print('Отсортированный список по третьим элементам из кортежей -', sort_by_3_item)

some_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}

print('\nДан словарь -', some_dict)
sort_dict_keys_by_alphabet = sorted(some_dict.keys())
print('Ключи словаря в алфавитном порядке -', *sort_dict_keys_by_alphabet)
sort_dict_by_wane = {i: some_dict[i] for i in sorted(some_dict, key=some_dict.get)}
print('Ключи словаря в порядке убывания по значениям -', *sort_dict_by_wane.keys())
print()
