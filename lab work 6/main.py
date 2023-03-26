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
            num_task = int(input('Enter the number of the task (from 1 to 3) whose answer you want to see '
                                 '(press "q" to exit): '))
        except ValueError:
            if keyboard.read_key('q'):
                goodbye()
            print('Error. Enter the number.')
            continue

        if num_task < 0:
            print('Input Error. The number must be greater than 0.')
        elif num_task > 3:
            print('There are only 3 tasks in the catalog. Enter a number from 1 to 3.')
        else:
            runpy.run_module(mod_name=f'task{num_task}')


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
