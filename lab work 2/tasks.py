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

    return result


print(fac(5))


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(fac(6))


"""Задание 4"""


"""Задание 5"""


"""Задание 6"""


"""Задание 7"""
