from main import logger
from time import sleep


"""Задание 2"""
logger.info('Выполнение задания 2...')
sleep(2)


def camelcase(letter):
    if letter.upper() == letter:
        return f'Символ {letter} имеет верхний регистр'
    return f'Символ {letter} имеет нижний регистр'


print(camelcase('w'), '\n')
