from loguru import logger
import runpy


def user_enter():
    while True:
        try:
            num_task = int(input('Введите номер задания (от 1 до 7), ответ которого Вы хотите посмотреть: '))
        except ValueError:
            print('Ошибка. Введите число.')
            continue

        if num_task < 0:
            print('Ошибка ввода. Число должно быть больше 0.')
        elif num_task > 7:
            print('В каталоге только 7 заданий. Введите число от 1 до 7.')
        else:
            runpy.run_module(mod_name=f'task{num_task}')


if __name__ == "__main__":
    try:
        user_enter()
    except Exception as e:
        logger.opt(exception=True).error(f'Unexpected error: {e}')
