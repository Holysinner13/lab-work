import json
import functools
from main import logger
from time import sleep


"""Задание 7"""
logger.info('Выполнение задания 7...')
sleep(2)


def func_json(func):
    """Декоратор, который модифицирует функцию таким образом, что результат ее выполнения возвращается в формате json"""

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


print(func_json.__doc__)
