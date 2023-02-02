import random


"""Задание 4"""


new_list = map(lambda y: y + random.random(), filter(lambda x: not x % 2, list(range(10))))

print(list(new_list))
