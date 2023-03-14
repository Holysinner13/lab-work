import requests
from easygui import *
from main import logger
from time import sleep


"""Задание 1"""
logger.info('Выполнение задания 1...')
sleep(2)


def get_img():
    url = 'https://cataas.com/cat?type=:md'

    response = requests.get(url)
    if response.status_code == 200:
        with open(f'distr/cat.jpg', 'wb') as file:
            file.write(response.content)


msg = 'Хочешь скачать картинку котика?:) '
title = 'Милота от котиков'
out = ccbox(msg, title, image='distr/hello.jpeg', choices=['да', 'нет'])

while True:
    try:
        if out:
            get_img()
            msg = 'Держи-лови милоту\n\nЕще хочешь? :)'
            title = 'Мимимишно'
            answer = ccbox(msg, title, image='distr/cat.jpg', choices=['да', 'нет'])
            if answer:
                continue
            else:
                break
        else:
            break
    except Exception as error:
        print(f'Ошибка {error}. Что-то пошло не так.')
