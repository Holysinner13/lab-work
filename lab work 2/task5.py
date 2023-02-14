import re
import string
from main import logger
from time import sleep


"""Задание 5"""
logger.info('Выполнение задания 5...')
sleep(2)


print('Произвести рефакторинг программы')
sentence = 'i am@Python@senior^pomidor'
c = ''.join(i if i not in string.punctuation else ' ' for i in sentence)
s = ''.join(list(map(lambda x: x if x not in string.punctuation else " ", sentence)))
d = re.sub(r'\W', ' ', sentence)


print(c)
print(s)
print(d)
print()
