from main import logger
from time import sleep


"""Задание 1"""
logger.info('Выполнение задания 1...')
sleep(2)


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
