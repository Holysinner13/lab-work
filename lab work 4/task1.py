import datetime
from main import logger
from time import sleep
from abc import ABC, abstractmethod
import logging
import logging.handlers
from pathlib import *


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
    def add_person_registration(self, name: str):
        pass

    @abstractmethod
    def show_border_list(self):
        pass

    @abstractmethod
    def show_list_border_date(self, border_crossing_date):
        pass


class AirCustoms(AbstractCustoms):
    """Air customs class"""
    logging.info(f'Class Air customs instance created')

    def __init__(self) -> None:
        self.person_registration_info = {}

    def add_person_registration(self, name: str):
        """Method that adds air border crossing information for the current date"""
        logging.info(f'Adding border crossing information - {name} {datetime.datetime.today()}')
        self.person_registration_info.update({name: datetime.datetime.today().strftime("%d.%m.%Y")})

    def show_border_list(self):
        """Method that returns information about who has crossed the air border"""
        logging.info('The entire list of those who crossed the air border')
        if self.person_registration_info:
            for i in self.person_registration_info:
                print(i)
                print(self.person_registration_info)

    def show_list_border_date(self, border_crossing_date):
        """"""
        logging.info('')
        pass


class LandCustoms(AbstractCustoms):
    """Land customs class"""
    logging.info(f'Class Land customs instance created')

    def __init__(self) -> None:
        self.person_registration_info = {}

    def add_person_registration(self, name: str):
        """Method that adds land border crossing information for the current date"""
        logging.info(f'Adding border crossing information - {name} {datetime.datetime.today()}')
        self.person_registration_info.update({name: datetime.datetime.today().strftime("%d.%m.%Y")})

    def show_border_list(self):
        """Method that returns information about who has crossed the land border"""
        logging.info('The entire list of those who crossed the land border')
        if self.person_registration_info:
            for i in self.person_registration_info:
                print(i)

    def show_list_border_date(self, border_crossing_date):
        """"""
        logging.info('')
        pass


def main():
    while True:
        try:
            name = input('Введите имя: ')
            border = input('Введите вид границы: ')
            if border.lower() == 'air':
                air_border_person = AirCustoms()
                air_border_person.add_person_registration(name)
                air_border_person.show_border_list()
            elif border.lower() == 'land':
                land_border_person = LandCustoms()
                land_border_person.add_person_registration(name)
                land_border_person.show_border_list()
        except BaseException as error:
            print(f'Unexpected error: {error}')
        finally:
            # print('Для выхода нажмите q, для продолжения n')
            # if keyboard.read_key('q'):
            #     exit()
            continue


main()
