from main import logger
from time import sleep


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


def get_price(price):
    for i in range(1, 11):
        print(f'Цена за {i} кг апельсин равна {i * price} тенге')

    count = 1
    while count < 11:
        print(f'Цена за {count} кг апельсин равна {count * price} тенге')
        count += 1


get_price(50)
print()
