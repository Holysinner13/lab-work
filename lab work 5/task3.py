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
    print(soup)
    # with open('film_info', 'w+', encoding="utf-8") as file:
    items_divs = soup.find_all('div', class_='shortstory__title')
    for item in items_divs:
        item_title = item.find('h2')
        print(item_title)


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
