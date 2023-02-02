"""Задание 2"""


def camelcase(letter):
    if letter.upper() == letter:
        return f'Символ {letter} имеет верхний регистр'
    return f'Символ {letter} имеет нижний регистр'


print(camelcase('w'))
