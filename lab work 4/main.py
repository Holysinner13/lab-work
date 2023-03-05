from loguru import logger
import runpy
import keyboard
from dotenv import load_dotenv, find_dotenv
import os


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")


def user_enter():
    while True:
        try:
            num_task = int(input('Enter the number of the task (from 1 to 10) whose answer you want to see '
                                 '(press "q" to exit): '))
        except ValueError:
            if keyboard.read_key('q'):
                goodbye()
            print('Error. Enter the number.')
            continue

        print('But no, there is only one task in this module, and it will be launched.')
        runpy.run_module(mod_name=f'task1')


def goodbye() -> None:
    """
    Displays a message on exit and exits
    """
    logger.info('End')
    exit()


if __name__ == "__main__":
    try:
        user_enter()
    except Exception as e:
        logger.opt(exception=True).error(f'Unexpected error: {e}')
