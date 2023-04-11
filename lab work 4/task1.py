import datetime
from main import logger
from time import sleep
from abc import ABC, abstractmethod
import logging
import logging.handlers
import bcrypt
import os
from tkinter import *
from tkinter import ttk


"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)


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
    PERSON_REGISTRATION_INFO = {}

    def add_person_registration(self, name: str):
        """Method that adds air border crossing information for the current date"""
        logging_customs()
        logging.info(f'Adding border crossing information - {name} {datetime.datetime.today()}')
        AirCustoms.PERSON_REGISTRATION_INFO.update({name: datetime.datetime.today().strftime("%d.%m.%Y")})

    def show_border_list(self):
        """Method that returns information about who has crossed the air border"""
        logging.info('The entire list of those who crossed the air border')
        if AirCustoms.PERSON_REGISTRATION_INFO:
            if check_pwd():
                print(AirCustoms.PERSON_REGISTRATION_INFO)

    def show_list_border_date(self, border_crossing_date: str):
        """Method that displays information about who crossed the air border on a specific date"""
        logging.info(f'Requested information on who crossed the land border on {border_crossing_date}')
        count_border_crossing = 0
        for k, v in AirCustoms.PERSON_REGISTRATION_INFO.items():
            if v == border_crossing_date:
                count_border_crossing += 1
        return count_border_crossing


class LandCustoms(AbstractCustoms):
    """Land customs class"""
    logging.info(f'Class Land customs instance created')
    PERSON_REGISTRATION_INFO = {}

    def add_person_registration(self, name: str):
        """Method that adds land border crossing information for the current date"""
        logging.info(f'Adding border crossing information - {name} {datetime.datetime.today()}')
        LandCustoms.PERSON_REGISTRATION_INFO.update({name: datetime.datetime.today().strftime("%d.%m.%Y")})

    def show_border_list(self):
        """Method that returns information about who has crossed the land border"""
        logging.info('The entire list of those who crossed the land border')

        if LandCustoms.PERSON_REGISTRATION_INFO:
            if check_pwd():
                print(LandCustoms.PERSON_REGISTRATION_INFO)

    def show_list_border_date(self, border_crossing_date: str):
        """Method that displays information about who crossed the land border on a specific date"""
        logging.info(f'Requested information on who crossed the land border on {border_crossing_date}')
        count_border_crossing = 0
        for k, v in AirCustoms.PERSON_REGISTRATION_INFO.items():
            if v == border_crossing_date:
                count_border_crossing += 1
        return count_border_crossing


def check_pwd():
    password = 'Admin'
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

    check = str(input('Input password: '))
    check = check.encode('utf-8')

    if bcrypt.checkpw(check, hashed):
        print('Login successfully')
        return True
    else:
        print('Password invalid.')
        return False


def logging_customs():
    log_left = logging.getLogger()
    log_left.setLevel(logging.DEBUG)
    fh_left = logging.FileHandler("log_customs/customs_info.log")
    basic_format_left = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
    fh_left.setFormatter(basic_format_left)
    log_left.addHandler(fh_left)

    log_right = logging.getLogger()
    log_right.setLevel(logging.DEBUG)
    fh_right = logging.FileHandler("copy_log_customs/copy_customs_info.log")
    basic_format_right = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
    fh_right.setFormatter(basic_format_right)
    log_right.addHandler(fh_right)


def main():
    while True:
        try:
            # root = Tk()
            # root.title("Welcome, this is customs Matamoros")
            # root.geometry("500x300")
            #
            # entry = ttk.Entry()
            # entry.pack(anchor=NW, padx=6, pady=6)
            #
            # btn = ttk.Button(text="Click")
            # btn.pack(anchor=NW, padx=6, pady=6)
            #
            # label = ttk.Label()
            # label.pack(anchor=NW, padx=6, pady=6)
            #
            # root.mainloop()
            name = input('Введите имя: ')
            border = input('Введите вид границы: ')
            if border.lower() == 'air':
                air_border_person = AirCustoms()
                air_border_person.add_person_registration(name)
                air_border_person.show_border_list()
                border_date = input('Enter the date of border crossing: ')
                print(f'Number of people who crossed the border {border_date} - ',
                      air_border_person.show_list_border_date(border_date))
            elif border.lower() == 'land':
                land_border_person = LandCustoms()
                land_border_person.add_person_registration(name)
                land_border_person.show_border_list()
                border_date = input('Enter the date of border crossing: ')
                print(f'Number of people who crossed the border {border_date} - ',
                      land_border_person.show_list_border_date(border_date))
        except BaseException as error:
            print(f'Unexpected error: {error}')


main()
