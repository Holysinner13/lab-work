from main import logger
from time import sleep
from easygui import *
import requests
import json
import datetime


"""Exercise 2"""
logger.info('Completing task 2...')
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


def main():
    while True:
        title = 'Holiday calendar by country'
        msg_1 = 'Select the country in which you want to view the holidays'
        country_answer = choicebox(msg_1, title, choices=get_available_country())

        msg_2 = 'Enter the year in which you want to view the holidays'
        some_year = integerbox(msg_2, title, upperbound=datetime.datetime.now().year)

        get_holiday(some_year, country_answer[:2])
        msg_3 = f'All holidays in {some_year} in {country_answer[5:]}'
        with open('./distr/holiday.txt', 'r') as file:
            textbox(msg_3, title, text=file.read())

        msg_4 = "Let's see again?"
        return_answer = ynbox(msg_4, title,)
        if return_answer:
            continue
        break


main()
