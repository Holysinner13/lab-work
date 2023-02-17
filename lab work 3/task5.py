from main import logger
from time import sleep


"""Exercise 5"""
logger.info('Completing task 5...')
sleep(2)


class MyString(str):
    """
    A class, that allows you to endow strings with append() and pop()
    methods that perform the same operations as the list class
    """

    def str_append(self, stroka):
        string_list = []
        string_list.append(stroka)

        return ''.join(string_list), string_list


some_string = MyString()
print(some_string.str_append('Пиво'))
print(some_string.str_append('Чипсы'))
