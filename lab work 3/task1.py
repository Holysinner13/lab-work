from main import logger
from time import sleep
from tkinter import *


"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)


class BankAccount:
    """A class, that represents a bank account"""

    def __init__(self, balance: float | int, name: str, account_number: int) -> None:
        """
        Initializing class variables
        :param account_number: owner account number
        :param name: account holder name as a string type
        :param balance: account holder's balance
        :return
        """
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, summa: int | float) -> int | float:
        """Method, that manages deposit actions"""
        self.balance += summa
        return self.balance

    def withdrawal(self, summa: int | float) -> int | float:
        """Method, that manages withdrawal actions"""
        if summa > self.balance:
            exit('Insufficient funds')
        self.balance = self.balance - summa
        return self.balance

    def bank_fes(self) -> int | float:
        """Method for applying bank charges in the amount of 5% of the account balance"""
        self.balance += self.balance * 0.05
        return self.balance

    def display(self) -> str:
        """Method to display account information"""
        total = f'Account holder name {self.name}\n' \
                f'Owner account number {self.account_number}\n' \
                f'Balance {self.balance}'
        return total


bank = BankAccount(12, 'Andrew', 5000)

deposit_summa = 25000
print(f'Deposit amount {deposit_summa}. Current balance {bank.deposit(deposit_summa)}')

withdrawal_summa = 10000
print(f'Write-off amount {withdrawal_summa}. Current balance {bank.withdrawal(withdrawal_summa)}')

print(f'Баланс с учетом комиссии равен {bank.bank_fes()}')

print(bank.display())
print()
