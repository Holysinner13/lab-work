from main import logger
from time import sleep


"""Задание 7"""
logger.info('Выполнение задания 7...')
sleep(2)


def custom():
    dict_name = {}

    while True:
        name = input('Введите имя кто пересекает границу (Если хотите завершить напишите END): ')
        if name == 'END':
            break
        dict_name[name] = dict_name.get(name, 0) + 1

    return [print(key, ':', value) for key, value in dict_name.items()]


custom()
print()
