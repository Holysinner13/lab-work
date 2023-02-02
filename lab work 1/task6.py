import random
import numpy as np

"""Задание 6"""


# matrix = np.array([[randint(0, 10) for i in range(3)] for x in range(3)])
matrix = np.random.randint(10, size=(3, 4))
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
