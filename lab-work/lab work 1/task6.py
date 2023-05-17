import random
import numpy as np
from main import logger
from time import sleep


"""Задание 6"""
logger.info('Выполнение задания 6...')
sleep(2)


# matrix = np.array([[randint(0, 10) for i in range(3)] for x in range(3)])
matrix = np.random.randint(10, size=(3, 4))
print('Матрица - \n', matrix, '\n')

print('Сумма всех чисел в матрице: ', sum(map(sum, matrix)), '.', ' Аналог ', np.sum(matrix), sep='')
print('Максимальный элемент в матрице: ', max(map(max, matrix)), '.', ' Аналог ', np.max(matrix), sep='')
print('Сумма чисел в первой строке: ', sum(matrix[0]), '.', ' Аналог ', np.sum(matrix[0]), sep='')

result = []

for i in matrix:
    result.append(i[1])

print('Минимальный элемент во втором столбце: ', min(result), '.', ' Аналог ', np.amin(matrix, 1), sep='')

max_num = 0
count = 0
result2 = []

for i in matrix:
    result2.append(i[count])
    count += 1

print('Максимальный элемент по главной диагонали', max(result2), '.', 'Аналог', np.max(np.diag(matrix)), '\n')
