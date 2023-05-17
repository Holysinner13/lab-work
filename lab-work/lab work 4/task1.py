import datetime
from dotenv import load_dotenv
import os
from main import logger
from time import sleep
from abc import ABC, abstractmethod
import logging
import logging.handlers
import bcrypt


"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)


class AbstractCustoms(ABC):
    """Abstract class"""

    @abstractmethod
    def person_registration(self, name: str):
        pass

    @abstractmethod
    def show_crossing_border_list(self):
        pass

    @abstractmethod
    def show_list_who_crossed_border_date(self, border_crossing_date):
        pass


class AirCustoms(AbstractCustoms):
    """Air customs class"""
    logging.info(f'Class Air customs instance created')
    person_registration_info = {}

    def person_registration(self, name: str):
        """Method that adds air border crossing information for the current date"""
        logging.info(f'Adding border crossing information - {datetime.datetime.today()}: {name}')
        if datetime.datetime.today().strftime("%d.%m.%Y") in AirCustoms.person_registration_info.keys():
            AirCustoms.person_registration_info.get(datetime.datetime.today().strftime("%d.%m.%Y")).append(name)
        else:
            AirCustoms.person_registration_info[datetime.datetime.today().strftime("%d.%m.%Y")] = [name]

    def show_crossing_border_list(self):
        """Method that returns information about who has crossed the air border"""
        logging.info('The entire list of those who crossed the air border')
        if AirCustoms.person_registration_info:
            return AirCustoms.person_registration_info

    def show_list_who_crossed_border_date(self, border_crossing_date: str):
        """Method that displays information about who crossed the air border on a specific date"""
        logging.info(f'Requested information on who crossed the land border on {border_crossing_date}')
        for k, v in AirCustoms.person_registration_info.items():
            if k == border_crossing_date:
                return len(v)


class LandCustoms(AbstractCustoms):
    """Land customs class"""
    logging.info(f'Class Land customs instance created')
    person_registration_info = {}

    def person_registration(self, name: str):
        """Method that adds land border crossing information for the current date"""
        logging.info(f'Adding border crossing information - {name} {datetime.datetime.today()}')
        if datetime.datetime.today().strftime("%d.%m.%Y") in LandCustoms.person_registration_info.keys():
            AirCustoms.person_registration_info.get(datetime.datetime.today().strftime("%d.%m.%Y")).append(name)
        else:
            LandCustoms.person_registration_info[datetime.datetime.today().strftime("%d.%m.%Y")] = [name]

    def show_crossing_border_list(self):
        """Method that returns information about who has crossed the land border"""
        logging.info('The entire list of those who crossed the land border')
        if LandCustoms.person_registration_info:
            return LandCustoms.person_registration_info

    def show_list_who_crossed_border_date(self, border_crossing_date: str):
        """Method that displays information about who crossed the land border on a specific date"""
        logging.info(f'Requested information on who crossed the land border on {border_crossing_date}')
        for k, v in LandCustoms.person_registration_info.items():
            if k == border_crossing_date:
                return len(v)


class MyLogger:
    """Class logging"""
    def __init__(self, name_log, name_format):
        self.logger = name_log
        self.log_format = name_format

    def logged(self, path):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.log_format = logging.FileHandler(path)
        basic_format_left = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
        self.log_format.setFormatter(basic_format_left)
        self.logger.addHandler(self.log_format)


def check_password():
    """Function that checks the admin password"""
    load_dotenv()
    password_admin = os.environ.get("ADMIN_PASSWORD")
    password = password_admin.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

    check = str(input('Input password: '))
    check = check.encode('utf-8')

    if bcrypt.checkpw(check, hashed):
        print('Login successfully')
        return True
    else:
        print('Password invalid.')
        return False


def main():
    while True:
        try:
            name = input('Enter the name of who crosses the border: ')
            border = input('Enter the type of border(air or land): ')
            left_log = MyLogger('log_left', 'fh_left')
            left_log.logged("log_customs/customs_info.log")
            right_log = MyLogger('log_right', 'fh_right')
            right_log.logged("copy_log_customs/copy_customs_info.log")
            if border.lower() == 'air':
                air_border_person = AirCustoms()
                air_border_person.person_registration(name)
                if check_password():
                    for key, value in air_border_person.show_crossing_border_list().items():
                        print(key, ':', value)
                    border_date = input('Enter the date of border crossing: ')
                    print(f'Number of people who crossed the border {border_date} - ',
                          air_border_person.show_list_who_crossed_border_date(border_date))
            elif border.lower() == 'land':
                land_border_person = LandCustoms()
                land_border_person.person_registration(name)
                if check_password():
                    print(land_border_person.show_crossing_border_list())
                    border_date = input('Enter the date of border crossing: ')
                    print(f'Number of people who crossed the border {border_date} - ',
                          land_border_person.show_list_who_crossed_border_date(border_date))
        except TypeError as error:
            print(f'Unexpected error: {error}')
            continue


main()
