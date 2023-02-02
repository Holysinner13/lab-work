import re
import string

"""Задание 5"""


sentence = 'i am@Python@senior^pomidor'
c = ''.join(c if c not in string.punctuation else ' ' for c in sentence)
s = ''.join(filter(lambda x: x not in string.punctuation, sentence))
# не могу понять как добавить в filter замену на" "
d = re.sub(r'[\W]', ' ', sentence)


print(c)
print(s)
print(d)
