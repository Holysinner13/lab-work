from main import logger
from time import sleep
import requests
from bs4 import BeautifulSoup


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


def get_film():
    url = 'https://kinogo.biz/istoricheskie'

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    with open('test.txt', 'w', encoding='utf-8') as f:
        ad = html.find('div', class_='shortstory__title')
        f.write(ad)


get_film()
