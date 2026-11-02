import time
from math import inf as infinity
import os
import platform
from random import choice


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


HUMAN = -1
COMPUTER = +1
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


# connect 4, or however many
def wins(board_state, win_condition=4):
    # all possible lines are stored in a single list
    lines = []
    # get rows
    lines.extend(board_state)
    # get columns
    lines.extend(list(zip(*board_state)))

    # check all diagonals possibilities in the length of win_condition, upwards and downwards
    row, cols = len(board_state), len(board_state[0])
    for r in range(row - win_condition + 1):
        for c in range(cols - win_condition + 1):
            lines.append([board_state[r + i][c + i] for i in range(win_condition)])
            lines.append([board_state[r - 1 + win_condition - i][c + i] for i in range(win_condition)])

    # check who won by sum the cells in length of win_condition
    for line in lines:
        for i in range(len(line) - win_condition + 1):
            segment_sum = sum(line[i: i + win_condition])
            if segment_sum == win_condition:
                return 1  # computer wins
            if segment_sum == -win_condition:
                return -1  # human wins

    if any(0 in row for row in board_state):
        return 0  # ongoing

    return 0  # draw


def game_over(board_state):
    if wins(board_state) == HUMAN:
        return True
    elif wins(board_state) == COMPUTER:
        return True
    return False


def get_valid_columns(board_state):
    valid_columns = []

    for col in range(len(board_state[0])):
        if board_state[0][col] == 0:
            valid_columns.append(col)

    return valid_columns


def get_next_open_row(board_state, column_move):
    row = len(board_state) - 1
    while row >= 0:
        if board_state[row][column_move] == 0:
            return row
        row -= 1
    return None


def drop_disc(column_move, player):
    row = len(board) - 1
    while row >= 0:
        if board[row][column_move] == 0:
            board[row][column_move] = player
            return True
        row -= 1
    return False


def set_move(column_move, player):
    if not drop_disc(column_move, player):
        return False
    return True


def minimax(board_state, depth, player, alpha, beta):
    if player == COMPUTER:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(board_state):
        score = wins(board_state)
        return [-1, -1, score]

    for col in get_valid_columns(board_state):
        row = get_next_open_row(board_state, col)
        if row is not None:
            board_state[row][col] = player
            score = minimax(board_state, depth - 1, -player, alpha, beta)
            board_state[row][col] = 0

            if player == COMPUTER:
                if score[2] > best[2]:
                    best = [row, col, score[2]]  # max value
                    alpha = max(alpha, score[2])
            else:
                if score[2] < best[2]:
                    best = [row, col, score[2]]  # min value
                    beta = min(beta, score[2])
            if beta <= alpha:
                break

    return best


def render(board_state, c_choice, h_choice):
    chars = {
        -1: bcolors.OKCYAN + h_choice + bcolors.ENDC,
        +1: bcolors.OKGREEN + c_choice + bcolors.ENDC,
        0: ' ',
    }
    str_line = '-----------------------------------'

    print('\n' + str_line)
    for row in board_state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def computer_turn(c_choice, h_choice):
    depth = len(get_valid_columns(board))
    if depth == 0 or game_over(board):
        return

    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 0:
        column = choice([0, 1, 2, 3, 4, 5, 6])
    else:
        move = minimax(board, depth, COMPUTER, -float(infinity), float(infinity))
        print("AI Chose Move:", move)
        column = move[1]

    set_move(column, COMPUTER)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    depth = len(get_valid_columns(board))
    if depth == 0 or game_over(board):
        return

    # list of valid moves
    move = -1
    moves = [0, 1, 2, 3, 4, 5, 6]

    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 0 or move > 7:
        try:
            move = int(input('Use numpad (1..7): ')) - 1
            if not move in moves:
                print('Invalid move!')
                move = -1
            if not set_move(move, HUMAN):
                print('Invalid move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Invalid choice')


def main():
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # determine if human is first to move

    while h_choice != 'X' and h_choice != 'O':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Invalid choice')

    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # main loop
    while len(get_valid_columns(board)) > 0 and not game_over(board):
        if first == 'N':
            computer_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        computer_turn(c_choice, h_choice)

    if wins(board) == HUMAN:
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board) == COMPUTER:
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        render(board, c_choice, h_choice)
        print('DRAW!')
    exit()


if __name__ == '__main__':
    main()
