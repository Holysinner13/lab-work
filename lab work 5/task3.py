import time

from main import logger
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


"""Задание 3"""
logger.info('Выполнение задания 3...')
sleep(2)


def get_film():
    driver = webdriver.Chrome(
        service=Service('distr/chromedriver.exe')
    )
    url = 'https://kinogo.biz/istoricheskie'

    try:
        driver.get(url=url)
        time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_film()


main()
