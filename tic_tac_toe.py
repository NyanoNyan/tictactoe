# display board function
# input function

from IPython.display import clear_output
import numpy as np
import pandas as pd

clear_output()


# display board

def disp_board():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

    for i in range(len(board)):
        # board[i]=' | '.join(board[i])
        print(board[i])
        print('---------------')
    return board


# player input
def p_input():
    # Checking valid response
    condd = True
    while condd:
        p_ans = input('Player 1: Do you want to be X or O? ').upper()
        if p_ans == 'X' or p_ans == 'O':
            condd = False
        else:
            print('Please enter a valid response')

        # Set tick for player 1 and player 2
        if p_ans == 'X':
            p_ans2 = 'O'
        elif p_ans == 'O':
            p_ans2 = 'X'

    return p_ans, p_ans2

# player position input
def pos_input():
    condd = True
    while condd:
        p_ans = int(input('Chose your position (1-9): '))
        if p_ans in range(10):
            condd = False
        else:
            print('Please enter a valid response (1-9)')
    return p_ans


# Converter of the response

def converter_ans(ans):
    # For the first index position in which board top, middle bottom
    if ans in range(4):
        indx_1 = 2
    elif ans in range(4, 7):
        indx_1 = 1
    else:
        indx_1 = 0

    # For gettin the index position of location (element) of the board of top, middle, bottom
    if ans == 1 or ans == 4 or ans == 7:
        indx_2 = 0
    elif ans == 2 or ans == 5 or ans == 8:
        indx_2 = 1
    else:
        indx_2 = 2

    return indx_1, indx_2


# Win condition and draw condition
# if all space is taken and no three diagonal and across, draw
# if diag or across X or O, win X or O

def cond_win(board, tick_cross):
    win_cond = False

    pp = np.array(board)
    val_true1 = ['X', 'X', 'X']
    val_true2 = ['O', 'O', 'O']

    # left to right and right to left diagonal
    pp_l2r = list(np.diag(pp))
    pp_r2l = list(np.diag(pp[::-1]))

    # Check for diagonals
    if (pp_l2r == val_true1 or pp_r2l == val_true1):
        win_cond = True
        print(f'{tick_cross} has won the game!')

    elif (pp_l2r == val_true2 or pp_r2l == val_true2):
        win_cond = True
        print(f'{tick_cross} has won the game!')

    # For up and down | left and right

    # For up and down, pp[:,0] -- taking all the rows values from 1 column
    # For left and right, pp[0,:]-- taking all the row location and all the column values

    if (list(pp[:, 0]) == val_true1) or (list(pp[:, 0]) == val_true2) or (list(pp[0, :]) == val_true1) or (
            list(pp[0, :]) == val_true2):
        win_cond = True
        print(f'{tick_cross} has won the game!')

    elif (list(pp[:, 1]) == val_true1) or (list(pp[:, 1]) == val_true2) or (list(pp[1, :]) == val_true1) or (
            list(pp[1, :]) == val_true2):
        win_cond = True
        print(f'{tick_cross} has won the game!')

    elif (list(pp[:, 2]) == val_true1) or (list(pp[:, 2]) == val_true2) or (list(pp[2, :]) == val_true1) or (
            list(pp[2, :]) == val_true2):
        win_cond = True
        print(f'{tick_cross} has won the game!')

    return win_cond

# Already something there condition ,so players cannot put tick or cross if there is already one in the board

def disp_board_refresh(a, b, c, board):
    # a = idx_1,  b = idx_2,  c = X or O

    board[a][b] = c

    for i in range(len(board)):
        # board[i]=' | '.join(board[i])
        print(board[i])
        print('---------------')


def replay_game():
    val = input('Do you want to play again? (y/n)')
    print('\n'*100)
    if val == 'y':
        game_game()
    elif val == 'n':
        print('\nThank you for playing!')
        return False


### MAIN
## pp = win or lose
## replay_var = again or not

def game_game():
    print('Welcome to Tic Tac Toe !')
    [tick_cross1, tick_cross2] = p_input()
    board = disp_board()
    pp = False
    count = 1
    replay_var = True

    while pp == False:

        if count % 2 == 0:
            tick_cross = tick_cross2
        else:
            tick_cross = tick_cross1

        print(f'It is {tick_cross} turn')

        user_ans = pos_input()
        print('\n'*100)
        [indx_board_1, indx_board_2] = converter_ans(user_ans)
        disp_board_refresh(indx_board_1, indx_board_2, tick_cross, board)
        pp = cond_win(board, tick_cross)
        count += 1

    if pp == True:
        replay_game()

game_game()
