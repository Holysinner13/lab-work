from loguru import logger
import runpy
import keyboard


def user_enter():
    while True:
        try:
            num_task = int(input('Введите номер задания (от 1 до 4), ответ которого Вы хотите посмотреть '
                                 '(для выхода нажмите "q"): '))
        except ValueError:
            if keyboard.read_key('q'):
                goodbye()
            print('Ошибка. Введите число.')
            continue

        if num_task < 0:
            print('Ошибка ввода. Число должно быть больше 0.')
        elif num_task > 4:
            print('В каталоге только 4 задания. Введите число от 1 до 4.')
        else:
            runpy.run_module(mod_name=f'task{num_task}')


def goodbye() -> None:
    """
    Выводит сообщение при выходе
    """
    logger.info('Завершение')
    exit()


if __name__ == "__main__":
    try:
        user_enter()
    except Exception as e:
        logger.opt(exception=True).error(f'Unexpected error: {e}')
