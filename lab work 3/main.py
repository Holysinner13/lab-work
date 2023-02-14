from loguru import logger
import runpy
import keyboard


def user_enter():
    while True:
        try:
            num_task = int(input('Enter the number of the task (from 1 to 4) whose answer you want to see '
                                 '(press "q" to exit): '))
        except ValueError:
            if keyboard.read_key('q'):
                goodbye()
            print('Error. Enter the number.')
            continue

        if num_task < 0:
            print('Input Error. The number must be greater than 0.')
        elif num_task > 4:
            print('There are only 4 tasks in the catalog. Enter a number from 1 to 4.')
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
