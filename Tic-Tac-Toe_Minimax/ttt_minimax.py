#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################################
#  _____ _          _____               _____                                        __    __  #
# /__   (_) ___    /__   \__ _  ___    /__   \___   ___      /\/\    /\/\         /\ \ \/\ \ \ #
#   / /\/ |/ __| __  / /\/ _` |/ __| __  / /\/ _ \ / _ \    /    \  /    \ _____ /  \/ /  \/ / #
#  / /  | | (__ (__)/ / | (_| | (__ (__)/ / | (_) |  __/   / /\/\ \/ /\/\ \_____/ /\  / /\  /  #
#  \/   |_|\___|    \/   \__,_|\___|    \/   \___/ \___|   \/    \/\/    \/     \_\ \/\_\ \/   #
#                                                                                              #
# (c) July 2017 by Luca Mannella                                                               #
# Tic-Tac-Toe Minimax-Neural Network is distributed under GNU GENERAL PUBLIC LICENSE v.3       #
#                                                                                              #
################################################################################################

import logging
import math


COMBINATIONS = 19683
WIN_SCORE = 10
VERSION = "v0.1"

""" Modify these variable to enable/disable debug functionalities """
TEST = True
VERBOSE = True


def main():
    """ That's Main! """
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    out_file = open("ttt_config.txt", "w")

    for i in range(COMBINATIONS):
        if is_playable(board):
            players = who_is_next(board)
            for p in players:
                if p == 0:  # additional check to be sure to not generate wrong configurations
                    logging.error("Invalid configuration generated!!! ", generate_output(board, p, -11))
                else:
                    move = next_move(board, p)
                    output = generate_output(board, p, move)
                    out_file.write(output)
                    if VERBOSE:
                        logging.info(output)

    out_file.close()
    print("Program is over! :D")


def is_playable(board):
    """ This function checks if the configuration is considerable playable or not.
        A configuration is considered playable if in the board the difference between X and O is at most equal to 1.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :return: True if the configuration is acceptable, False otherwise.
    """
    if is_winner(board):
        return False

    x_count = board.count(1)
    o_count = board.count(-1)

    if math.fabs(x_count - o_count) > 1:
        return False
    else:
        return True


def is_playable_for(board, player):
    """ This function checks if the configuration is considerable playable or not for a given player.
        A configuration is considered playable if in the board the difference between X and O is at most equal to 1.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :param player: Who is the player that has to play now [ +1 (X) or -1 (O) ]
    :return: True if the configuration is acceptable, False otherwise.
    """
    if is_winner(board):
        return False

    x_count = board.count(1)
    o_count = board.count(-1)

    if math.fabs(x_count - o_count) > 1:
        return False
    elif(x_count > o_count) and player == 1:
        return False
    elif(o_count > x_count) and player == -1:
        return False
    else:
        return True


def who_is_next(board):
    """ This function returns a value or an array that contains the player(s) that can play the next move.
        If the game is already won or if the configuration is not valid the function returns 0.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :return: 0 if the game is already won or if it is invalid, +1 or -1 if only one of the two players can play or
             an array with both values if the board is in a tie state.
    """
    if is_winner(board):
        return [0]

    x_count = board.count(1)
    o_count = board.count(-1)

    if math.fabs(x_count - o_count) > 1:
        return [0]
    elif x_count > o_count:
        return [-1]
    elif x_count < o_count:
        return [1]
    else:
        return [1, -1]


def is_winner(board):
    """ This function return true if the board is in a winning state.

        :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
        :return: True if the board is in a winning state, False otherwise.
    """
    # checking rows
    # when we have a winning configuration we will have only one element in the set
    for i in range(3):
        value_set = set(board[i * 3: i * 3 + 3])
        if len(value_set) is 1 and board[i * 3] is not 0:
            return True

    # checking columns
    for i in range(3):
        if (board[i] is board[i + 3]) and (board[i] is board[i + 6]) and board[i] is not 0:
            return True

    # checking diagonals
    if board[0] is board[4] and board[4] is board[8] and board[4] is not 0:
        return True
    if board[2] is board[4] and board[4] is board[6] and board[4] is not 0:
        return True

    # There is no winning configuration
    return False


def is_tie(board):
    """ This function returns True if there are empty cell on the board, False otherwise.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :return: True if there are empty cell on the board, False otherwise.
    """
    for i in board:
        if i == 0:
            return False
    return True


def someone_won(board):
    """ This function returns true if the board is in a winning state and a value that represents who is the winner.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :return: True if the board is in a winning state, False and 0 otherwise.
             If the board is in a winning state, the function returns also who is the winner.
    """
    # checking rows
    # when we have a winning configuration we will have only one element in the set
    for i in range(3):
        value_set = set(board[i*3: i*3 + 3])
        if len(value_set) is 1 and board[i*3] is not 0:
            return True, value_set.pop()

    # checking columns
    for i in range(3):
        if (board[i] is board[i+3]) and (board[i] is board[i+6]) and board[i] is not 0:
            return True, board[i]

    # checking diagonals
    if board[0] is board[4] and board[4] is board[8] and board[4] is not 0:
        return True, board[4]
    if board[2] is board[4] and board[4] is board[6] and board[4] is not 0:
        return True, board[4]

    # There is no winning configuration
    return False, 0


def next_move(board, player):
    """ Computes the next move for a player given the current board state.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :param player: Who is the player that has to play now [ +1 (X) or -1 (O) ]
    :return: The position where the player have to play the next move
    """
    # If the board is empty the best move is to put your symbol in the center
    if len(set(board)) == 1:
        return 4

    n_move, score = minimax(board, player)
    return n_move


def minimax(board, player):
    """ This function returns the best move and the relative score for the given player.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :param player: Who is the player that has to play now [ +1 (X) or -1 (O) ]
    :return: The position where the player have to play the next move and the relative score
    """
    # Termination condition
    x = someone_won(board)
    if x[0]:
        return -1, x[1] * 10
    elif is_tie(board):
        return -1, 0

    # Next player initialization
    next_player = 1 if player == -1 else -1

    # empty cells evaluations
    empty_cells = []  # list for storing the indexes where "0" appears
    for i in range(len(board)):
        if board[i] == 0:
            empty_cells.append(i)

    res_list = []  # list for appending the result
    # evaluate all the possibilities
    for i in empty_cells:
        board[i] = player
        score = evaluation_function(board)
        res_list[i] = score

        n_move, next_score = minimax(board, next_player)
        res_list[i] += next_score
        board[i] = 0  # backtracking

    # fetching the best move
    if player == 1:
        # X is playing, we have to maximize
        best_score = max(res_list)
        best_move = res_list.index(best_score)
    else:
        # O is playing, we have to minimize
        best_score = min(res_list)
        best_move = res_list.index(best_score)

    return best_move, best_score


def evaluation_function(board):
    """ This function return the evaluation value of the grid at the actual state of the game.
        The score will be positive if X (+1) is winning or negative if O (-1) is winning

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :return: The score of the current situation of the grid
    """
    result = someone_won(board)
    if result[0]:
        return WIN_SCORE * result[1]

    x_score = partial_score(board, 1)
    o_score = partial_score(board, -1)

    return x_score - o_score


def partial_score(board, player):
    """ This function calculate the score of a player given the actual situation o the board.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :param player: The player that we have to consider in the score calculation [ +1 (X) or -1 (O) ]
    :return: The score of the given player
    """
    score = 0
    acceptable_values = (0, player)

    # counting rows
    if board[0] in acceptable_values and board[1] in acceptable_values and board[2] in acceptable_values:
        score += 1
    if board[3] in acceptable_values and board[4] in acceptable_values and board[5] in acceptable_values:
        score += 1
    if board[6] in acceptable_values and board[7] in acceptable_values and board[8] in acceptable_values:
        score += 1

    # counting columns
    if board[0] in acceptable_values and board[3] in acceptable_values and board[6] in acceptable_values:
        score += 1
    if board[1] in acceptable_values and board[4] in acceptable_values and board[7] in acceptable_values:
        score += 1
    if board[2] in acceptable_values and board[5] in acceptable_values and board[8] in acceptable_values:
        score += 1

    # counting diagonals
    if board[0] in acceptable_values and board[4] in acceptable_values and board[8] in acceptable_values:
        score += 1
    if board[2] in acceptable_values and board[4] in acceptable_values and board[6] in acceptable_values:
        score += 1

    return score


def generate_output(board, p, move):
    """ This function generate a string version of the data that have to be written on the output file.
        The string does not have parenthesis, comma or any other symbols, the first nine values represents the state of
        the grid, the 10th value represent who is the next player to play and the last value is the position in which
        the player should put his symbol.

    :param board: The board of the game (an array of 9 elements), it must contains only [-1, 0, +1] values
    :param p: Who is the player that has to play now [ +1 (X) or -1 (O) ]
    :param move: The cell in which the player should put its symbol (a value from 0 to 8)
    :return: A string value that could be printed on a file or on the screen
    """
    to_ret = ""
    for i in range(len(board)):
        to_ret += str(board[i]) + " "
    to_ret += str(p) + " "
    to_ret += str(move)
    return to_ret


def print_board(board):
    """ This function print a Tic-Tac-Toe board on the stdout """

    new_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    for i in range(len(board)):
        if board[i] == 1:
            new_grid[i] = "X"
        elif board[i] == -1:
            new_grid[i] = "O"

    print()
    print(" %s | %s | %s " % (new_grid[0], new_grid[1], new_grid[2]))
    print("-----------")
    print(" %s | %s | %s " % (new_grid[3], new_grid[4], new_grid[5]))
    print("-----------")
    print(" %s | %s | %s " % (new_grid[6], new_grid[7], new_grid[8]))


def test():
    """ This function is used to perform some testing, it should be removed in the final version of the program. """
    board1 = [1, 1, 0, -1, -1, 0, 0, 0, 0]
    test_function(board1)
    board2 = [1, 1, 0, -1, -1, 0, 1, 0, 0]
    test_function(board2)
    board3 = [1, 0, 0, -1, -1, 0, 1, 0, -1]
    test_function(board3)

    w_board = [0, 0, 0, 1, 1, 1, -1, -1, 0]
    l_board = [-1, 0, 1, 1, -1, 0, 1, 0, -1]
    test_function(w_board)
    test_function(l_board)


def test_function(board):
    """ This function performs tests on a board, it should be removed in the final version of the program. """
    print_board(board)
    res = someone_won(board)
    if res[1] is 1:
        logging.debug("X won")
    elif res[1] is -1:
        logging.debug("O won")
    else:
        logging.debug("No one won")
    logging.debug("Grid score = %d", evaluation_function(board))
    logging.debug("X score is %d and O score is %d", partial_score(board, +1), partial_score(board, -1))

    next_p = who_is_next(board)
    for n in next_p:
        logging.debug("Who is next? " + str(n))
        logging.debug(generate_output(board, n, -11))


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s")
    logging.getLogger().setLevel(level=logging.DEBUG)
    logging.info(r"         _       _                          _____           _       _    (!) %s    ", VERSION)
    logging.info(r"   /\/\ (_)_ __ (_)_ __ ___   __ ___  __   /__   \_ __ __ _(_)_ __ (_)_ __   __ _  ")
    logging.info(r"  /    \| | '_ \| | '_ ` _ \ / _` \ \/ /____ / /\/ '__/ _` | | '_ \| | '_ \ / _` | ")
    logging.info(r" / /\/\ \ | | | | | | | | | | (_| |>  <_____/ /  | | | (_| | | | | | | | | | (_| | ")
    logging.info(r" \/    \/_|_| |_|_|_| |_| |_|\__,_/_/\_\    \/   |_|  \__,_|_|_| |_|_|_| |_|\__, | ")
    logging.info(r"  Developed by Luca Mannella - July 2017                                    |___/  ")
    logging.getLogger().handlers[0].setFormatter(logging.Formatter(
        "%(asctime)s.%(msecs)04d %(levelname)s: %(message)s", datefmt="%H:%M:%S"))

    if TEST:
        test()
    else:
        main()
