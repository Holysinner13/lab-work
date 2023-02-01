import string
import random
import re
import functools
import json


"""Задание 1"""


def mistakes():
    try:
        print(2 / 0)
    except ZeroDivisionError:
        print(f'Ошибка {ZeroDivisionError}')

    try:
        c = 0
        print(c + b)
    except NameError:
        print(f'Ошибка {NameError}')

    # try:
    #     a = 8
    #     b = 10
    #     c = a b
    # except SyntaxError:
    #     print(f'Ошибка {SyntaxError}')

    # try:
    #     for i in range(10):
    #     print('Python')
    # except IndentationError:
    #     print(f'Ошибка {IndentationError}')

    try:
        names = [1, 2]
        print(names[2])
    except IndexError:
        print(f'Ошибка {IndexError}')

    try:
        def func():
            func()

        func()
    except RuntimeError:
        print(f'Ошибка {RuntimeError}')

    try:
        x = 'ich'
        call = x.update
    except AttributeError:
        print(f'Ошибка {AttributeError}')

    try:
        name_dict = {'Bob': 1, 'John': 2}
        print(name_dict['Andrew'])
    except KeyError:
        print(f'Ошибка {KeyError}')

    try:
        import myfile
    except ImportError:
        print(f'Ошибка {ImportError}')


mistakes()
print()

"""Задание 2"""


def new_power(a, b):
    result = a ** b
    return print(f'Число {a} в степени {b} = {result}')


nums = input('Введите два целых числа (через пробел): ')
new_power(int(nums.split()[0]), int(nums.split()[1]))
print()


"""Задание 3"""


def fac(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return f'Факториал числа {n} = {result}'


print(fac(5))


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(f'Факториал числа 6 =', fac(6))
print()


"""Задание 4"""


new_list = map(lambda y: y + random.random(), filter(lambda x: not x % 2, list(range(10))))

print(list(new_list))
print()


"""Задание 5"""


sentence = 'i am@Python@senior^pomidor'
c = ''.join(c if c not in string.punctuation else ' ' for c in sentence)
s = ''.join(filter(lambda x: x not in string.punctuation, sentence))
d = re.sub(r'[\W]', ' ', sentence)


print(c)
print(s)
print(d)
print()


"""Задание 6"""


some_list = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, -2, 8), (0, 0, 0), (3, -4, -5)]

print('Отсортированный список по сумме кортежей -', sorted(some_list, key=sum))
print('Отсортированный список по третьим элементам из кортежей -', sorted(some_list, key=lambda x: x[2]))

some_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}
print(*sorted(some_dict.keys()))
new_dict = {i: some_dict[i] for i in sorted(some_dict, key=some_dict.get)}
print(*new_dict.keys())


"""Задание 7"""


def func_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped
