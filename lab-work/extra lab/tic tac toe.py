from loguru import logger


class Board:
    """Класс поля"""
    def draw_board(self):
        for i in range(3):
            print(f' {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} ')
            print('---+---+---')

    def check_win(self):
        wins_combs = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for each in wins_combs:
            if (board[each[0]]) == (board[each[1]]) == (board[each[2]]):
                return board[each[0]]
        return False


class Player:
    """Класс игрока"""
    def take_input(self, player_token):
        flag = True
        while flag:
            value = input('Куда поставить: ' + player_token + ' ? ')
            try:
                value = int(value)
            except:
                print('Некорректный ввод. Введите число.')
                continue
            if 1 <= value <= 9:
                if str(board[value - 1]) not in 'X0':
                    board[value - 1] = player_token
                    flag = False
                else:
                    print('Эта клетка уже занята.')
            else:
                print('Некорректный ввод. Введите число от 1 до 9.')


def main():
    counter = 0
    the_board = Board()
    player = Player()
    while True:
        the_board.draw_board()
        if counter % 2 == 0:
            player.take_input('X')
        else:
            player.take_input('0')
        if counter > 3:
            winner = the_board.check_win()
            if winner:
                the_board.draw_board()
                print(winner, 'выиграл')
                break
        counter += 1
        if counter == 9:
            print('Ничья!')
            the_board.draw_board()
            break


if __name__ == "__main__":
    try:
        board = list(range(1, 10))
        main()
    except Exception as e:
        logger.opt(exception=True).error(f'Unexpected error: {e}')
