import time

from main import logger
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


def get_film_info():
    with open('test.html', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    films_divs = soup.find_all('div', class_='shortstory__title')
    list_film_title = []
    list_film_year = []
    for film in films_divs:
        film_info_title = film.find('h2')
        list_film_title.append(str(film_info_title)[4:-12])
        list_film_year.append(str(film_info_title)[-10:-6])

    films_divs_country = soup.find_all('div', class_='shortstory__info')
    # print(films_divs_country)
    list_films_country = []
    for film in films_divs_country:
        country = film.find('<b>')
        list_films_country.append(country)

    films_divs_info = soup.find_all('div', class_='excerpt')
    films_info = []
    for film_info in films_divs_info:
        films_info.append(film_info.stripped_strings)

    print(list_film_year)
    print(list_film_title)
    print(list_films_country)
    print(films_info)


def get_content():
    driver = webdriver.Chrome(
        service=Service('distr/chromedriver.exe')
    )
    try:
        url = 'https://kinogo.biz/istoricheskie/'
        driver.get(url=url)
        time.sleep(3)
        find_element1 = driver.find_element(By.ID, 'dle-content')
        if find_element1:
            with open('test.html', 'w', encoding="utf-8") as file:
                file.write(driver.page_source)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_content()
    get_film_info()


main()
