from random import randint
from main import logger
from time import sleep

"""Задание 5"""
logger.info('Выполнение задания 5...')
sleep(2)


name = input('Введите свое имя: ')
random_num = randint(1, 10)
attempt = 1

while True:
    user_answer = int(input('Угадайте число от 1 до 10. У Вас 3 попытки. Введите число: '))
    if user_answer == random_num:
        print('Угадал! Молодец!')
        break
    elif attempt == 3:
        print(f'Ошибка. {name}, игра окончена.')
        break
    elif user_answer > random_num:
        print(f'Ошибка. Ваша попытка № {attempt} неверна. Подсказка: задуманное число меньше чем {user_answer}.')
        attempt += 1
    else:
        print(f'Ошибка. Ваша попытка № {attempt} неверна. Подсказка: задуманное число больше {user_answer}.')
        attempt += 1

print()
