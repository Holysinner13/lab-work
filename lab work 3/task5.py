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
    def __init__(self):
        self.stroka = ''

    @property
    def get_str(self):
        return self.stroka

    @get_str.setter
    def get_str(self, new_word):
        self.stroka += new_word + ' '

    def del_str(self):
        self.stroka = ' '.join(list(self.stroka.split()[:-1]))


some_string = MyString()
some_string.get_str = 'Пиво'
some_string.get_str = 'Чипсы'
some_string.get_str = 'Раки'
print(some_string.get_str)
some_string.del_str()
print(some_string.get_str)
