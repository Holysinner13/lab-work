from main import logger
from time import sleep
from easygui import *
import requests
import json
import datetime


"""Задание 2"""
logger.info('Выполнение задания 2...')
sleep(2)


def get_available_country():
    url = 'https://date.nager.at/api/v3/AvailableCountries'

    response = requests.get(url)
    if response.status_code == 200:
        res = response.json()
        new_res = []
        for i in res:
            new_res.append(i['countryCode'] + ' - ' + i['name'])

        return new_res


def get_holiday(year, country_code):
    url = f'https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}'

    response = requests.get(url)
    if response.status_code == 200:
        with open('./distr/holiday.txt', 'w') as f:
            res = response.json()
            holidays_info = []
            for i in res:
                holidays_info.append('Holiday date - ' + i['date'] + ', ' +
                                     'Local name - ' + i['localName'] + ', ' +
                                     'Usual name - ' + i['name'])
            result = json.dumps(holidays_info, indent=4)

            f.write(result)


while True:
    title = 'Календарь праздников по странам'
    msg_1 = 'Выберите страну, в которой хотите посмотреть праздники'
    country_answer = choicebox(msg_1, title, choices=get_available_country())

    msg_2 = 'Введите год, в котором хотите посмотреть праздники'
    some_year = integerbox(msg_2, title, upperbound=datetime.datetime.now().year)

    get_holiday(some_year, country_answer[:2])
    msg_3 = f'Все праздники в {some_year} году в {country_answer[5:]}'
    with open('./distr/holiday.txt', 'r') as file:
        textbox(msg_3, title, text=file.read())

    msg_4 = 'Посмотрим еще?'
    return_answer = ynbox(msg_4, title,)
    if return_answer:
        continue
    break
