"""Задание 7"""


def custom():
    dict_name = {}

    while True:
        name = input('Введите имя кто пересекает границу (Если хотите завершить напишите END): ')
        if name == 'END':
            break
        dict_name[name] = dict_name.get(name, 0) + 1

    return [print(key, ':', value) for key, value in dict_name.items()]


custom()
