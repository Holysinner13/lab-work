import numpy as np
from random import randint


"""Задание 4"""


def calculate_pi(n=0):
    result = 3
    for i in range(n + 1):
        if i:
            delta = ((-1) ** (i + 1)) * 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
            print(delta)
            result += delta
    return result


for i in range(5):
    print(calculate_pi(i))


"""Задание 5"""


print('Загадай число от 1 до 100.')
start = 1
finish = 100
while True:
  number = (start + finish) // 2
  print('Твоё число равно, меньше или больше, чем число:', number)
  prompt = int(input('1 - равно, 2 - больше, 3 - меньше: '))
  if prompt == 2:
    start = number
  elif prompt == 3:
    finish = number
  else:
    print('Ты загадал число -', number)
    break
print('Угадал! Молодец!')


"""Задание 6"""


matrix = np.array([[randint(0, 10) for i in range(3)] for x in range(3)])
print('Матрица - \n', matrix, '\n')

print('Сумма всех чисел в матрице: ', sum(map(sum, matrix)))
print('Максимальный элемент в матрице: ', max(map(max, matrix)))
print('Сумма чисел в первой строке: ', sum(matrix[0]))

result = []

for i in matrix:
    result.append(i[1])

print('Минимальный элемент во втором столбце: ', min(result))

max_num = 0
count = 0
result2 = []

for i in matrix:
    result2.append(i[count])
    count += 1

print('Максимальный элемент по главной диагонали', max(result2))


# import string
#
# sentence = 'i am@Python@senior^pomidor'
# c = ''.join(c if c not in string.punctuation else ' ' for c in sentence)
# s = ''.join(filter(lambda x: x not in string.punctuation, sentence))
#
# print(c)
# print(s)
