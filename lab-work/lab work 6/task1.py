from main import logger
from time import sleep
import re

"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)

'''Subtask 1'''


def create_file(file: str) -> None:
    """A function that checks if the name of the created file is valid, if so, then creates it with this name."""
    try:
        if re.search(r'^[A-Za-z]{1,20}\.[A-Za-z]{1,3}$', file):
            with open(f'distr/{file}', 'w'):
                pass
        else:
            raise Exception
    except:
        print(f'Error. Invalid name.')


'''Subtask 2'''


def create_spec_file(row: int, symbol: int) -> None:
    """A function that creates a file and writes N lines and K characters to it"""
    with open('distr/some_file.txt', 'w') as file:
        [file.writelines('*' * symbol + '\n') for _ in range(row)]


'''Subtask 3'''


def delete_first_line() -> None:
    """A function that removes the first line in a file"""

    with open('distr/some text.txt', 'r') as f:
        lines = f.readlines()

    with open('distr/some text.txt', 'w') as f:
        f.writelines(lines[1:])


'''Subtask 4'''


def delete_some_symbol(num: int) -> None:
    with open('distr/some text for 1(4).txt', 'r') as file:
        lines = file.readlines()

    with open('distr/some text for 1(4).txt', 'w+') as file:
        file.writelines([i[num:] for i in lines])


def main():
    file_name = input('Enter file name: ')
    create_file(file_name)

    num_row = int(input('Enter the number of lines: '))
    num_sym = int(input('Enter number of characters: '))
    create_spec_file(num_row, num_sym)

    delete_first_line()

    num_symbol = int(input('Enter the number: '))
    delete_some_symbol(num_symbol)


main()
