from main import logger
from time import sleep
from tkinter import *


"""Exercise 1"""
logger.info('Completing task 1...')
sleep(2)


class BankAccount:
    """A class, that represents a bank account"""

    def __init__(self, account_number, name, balance):
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

    def deposit(self, summa):
        """Method, that manages deposit actions"""
        self.balance += summa
        return f'Deposit amount {summa}. Current balance {self.balance}'

    def withdrawal(self, summa):
        """Method, that manages withdrawal actions"""
        if summa > self.balance:
            exit('Insufficient funds')
        self.balance = self.balance - summa
        return f'Write-off amount {summa}. Current balance {self.balance}'

    def bank_fes(self, ):
        """Method for applying bank charges in the amount of 5% of the account balance"""
        self.balance += self.balance * 0.05
        return f'Баланс с учетом комиссии равен {self.balance}'

    def display(self):
        """Method to display account information"""
        total = f'Account holder name {self.name}\n,' \
                f'Owner account number {self.account_number}\n,' \
                f'Balance {self.balance}'
        print(total)
        return total


bank = BankAccount(12, 'Andrew', 5000)


def set_text(bank_account: BankAccount, lbl_info: Label):
    lbl_info.config(text=bank_account.display)
    # lbl_info.text = bank_account.display


def decorator_info(func, bank_account, lbl):

    def wrapper():
        func(bank_account, lbl)

    return wrapper


window = Tk()
window.title("Most Helpful Bank")
window.geometry('600x400')
lbl = Label(window, text="Select operation type", font=("Arial Bold", 30))
lbl_2 = Label(window, text="", font=("Arial Bold", 30))
update_info = decorator_info(set_text, bank, lbl_2)
btn = Button(window, text="Credit card information", bg='green', fg='white', command=update_info)

lbl.grid(column=0, row=0)
btn.grid(column=0, row=1)
lbl_2.grid(column=0, row=2)

window.mainloop()

print()
