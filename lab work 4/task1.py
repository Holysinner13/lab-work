import datetime
from main import logger
from time import sleep
from abc import ABC, abstractmethod
import logging
import logging.handlers
from pathlib import *
import keyboard


"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)


logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )


class AbstractCustoms(ABC):
    """Abstract class"""

    @abstractmethod
    def person_registration(self):
        pass

    @abstractmethod
    def show_border_list(self):
        pass

    # @abstractmethod
    # def show_date(self, ):
    #     pass


class AirCustoms(AbstractCustoms):
    BORDER_LIST = {}

    def __init__(self, name: str) -> None:
        self.name = name
        self.date = datetime.datetime.today().strftime("%d.%m.%Y")

    def show_border_list(self):
        for i in AirCustoms.BORDER_LIST:
            print(i)

    def person_registration(self):
        AirCustoms.BORDER_LIST[self.name] = str(self.date)


class LandCustoms(AbstractCustoms):
    BORDER_LIST = {}

    def __init__(self, name: str) -> None:
        self.name = name
        self.date = datetime.datetime.today().strftime("%d.%m.%Y")

    def show_border_list(self):
        for i in LandCustoms.BORDER_LIST:
            print(i)

    def person_registration(self):
        LandCustoms.BORDER_LIST[self.name] = self.date


def main():
    while True:
        try:
            name = input('Введите имя: ')
            border = input('Введите вид границы: ')
            if border.lower() == 'air':
                air_border_person = AirCustoms(name)
                air_border_person.person_registration()
                print(air_border_person.show_border_list())
            elif border.lower() == 'land':
                land_border_person = LandCustoms(name)
                land_border_person.person_registration()
                print(land_border_person.show_border_list())
        except BaseException as error:
            print(f'Unexpected error: {error}')
        finally:
            # print('Для выхода нажмите q, для продолжения n')
            # if keyboard.read_key('q'):
            #     exit()
            continue


main()
