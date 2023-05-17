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
    def __init__(self) -> None:
        self.stroka = ''

    @property
    def get_str(self) -> str:
        return self.stroka

    @get_str.setter
    def get_str(self, new_word: str) -> None:
        self.stroka += new_word + ' '

    def del_str(self, num: int) -> str:
        del_item = self.stroka.split()[num]
        self.stroka = ' '.join(list(self.stroka.split()[:num]+self.stroka.split()[num + 1:]))
        return del_item


def main():
    some_string = MyString()
    some_string.get_str = 'Пиво'
    some_string.get_str = 'Чипсы'
    some_string.get_str = 'Раки'
    some_string.get_str = 'Ничего'
    print(some_string.get_str)
    some_string.del_str(2)
    print(some_string.get_str)
    print(some_string.del_str(1))
    print(some_string.get_str)


main()
