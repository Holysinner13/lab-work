import re
import string
from main import logger
from time import sleep


"""Задание 5"""
logger.info('Выполнение задания 5...')
sleep(2)


print('Произвести рефакторинг программы')
sentence = 'i am@Python@senior^pomidor'
c = ''.join(c if c not in string.punctuation else ' ' for c in sentence)
s = ''.join(filter(lambda x: x not in string.punctuation, sentence))
# не могу понять как добавить в filter замену на" "
d = re.sub(r'[\W]', ' ', sentence)


print(c)
print(s)
print(d)
print()
