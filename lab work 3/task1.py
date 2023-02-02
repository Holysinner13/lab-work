from main import logger
from time import sleep


"""Задание 1"""
logger.info('Выполнение задания 1...')
sleep(2)


class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
