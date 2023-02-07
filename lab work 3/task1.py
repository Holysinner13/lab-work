from main import logger
from time import sleep
from tkinter import *


"""Задание 1"""
logger.info('Выполнение задания 1...')
sleep(2)


class BankAccount:
    """Класс, который представляет банковский счет"""

    def __init__(self, account_number, name, balance):
        """
        Инициализация переменных класса
        :param account_number: номер аккаунта владельца
        :param name: имя владельца счета в виде строкового типа
        :param balance: баланс владельца счета
        """
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, summa):
        """Метод, который управляет действиями по депозиту"""
        self.balance += summa
        return f'Сумма внесения {summa}. Текущий баланс {self.balance}'

    def withdrawal(self, summa):
        """Метод, который управляет действиями по снятию средств"""
        if summa > self.balance:
            exit('Недостаточно средств')
        self.balance = self.balance - summa
        return f'Сумма списания {summa}. Текущий баланс {self.balance}'

    def bank_fes(self, ):
        """Метод для применения банковских комиссий в размере 5% от баланса счета"""
        self.balance += self.balance * 0.05
        return f'Баланс с учетом комиссии равен {self.balance}'

    def display(self):
        """Метод для отображения сведений об учетной записи"""
        total = f'Имя владельца счета {self.name}\n,' \
                f'Номер аккаунта владельца {self.account_number}\n,' \
                f'Баланс {self.balance}'
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
window.title("Самый полезный банк")
window.geometry('600x400')
lbl = Label(window, text="Выберите тип операции", font=("Arial Bold", 30))
lbl_2 = Label(window, text="", font=("Arial Bold", 30))
update_info = decorator_info(set_text, bank, lbl_2)
btn = Button(window, text="Информация о карте", bg='green', fg='white', command=update_info)

lbl.grid(column=0, row=0)
btn.grid(column=0, row=1)
lbl_2.grid(column=0, row=2)

window.mainloop()

print()
