import requests
from easygui import *
from main import logger
from time import sleep


"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)


def get_img():
    url = 'https://cataas.com/cat?type=:md'

    response = requests.get(url)
    if response.status_code == 200:
        with open(f'distr/cat.jpg', 'wb') as file:
            file.write(response.content)


def main():
    msg = 'Do you want to download a picture of a cat?:) '
    title = 'Cuteness from cats'
    out = ccbox(msg, title, image='distr/hello.jpeg', choices=['да', 'нет'])

    while True:
        try:
            if out:
                get_img()
                msg = 'Hold-catch cuteness\n\nYou want more? :)'
                title = 'Mimimishno'
                answer = ccbox(msg, title, image='distr/cat.jpg', choices=['да', 'нет'])
                if answer:
                    continue
                else:
                    break
            else:
                break
        except Exception as error:
            print(f'Error {error}. Something went wrong.')


main()
