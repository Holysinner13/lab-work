from main import logger
from time import sleep


import random


"""Задание 4"""
logger.info('Выполнение задания 4...')
sleep(2)


new_list = map(lambda y: y + random.random(), filter(lambda x: not x % 2, list(range(10))))

print(list(new_list))
print()
