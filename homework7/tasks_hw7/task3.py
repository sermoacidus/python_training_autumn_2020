"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from itertools import combinations
from typing import List

WINNER_COMBINATIONS = [
    ((1, 3), (2, 2), (3, 1)),
    ((1, 1), (2, 2), (3, 3)),
    ((1, 2), (2, 2), (3, 2)),
    ((1, 1), (2, 1), (3, 1)),
    ((3, 1), (3, 2), (3, 3)),
    ((2, 1), (2, 2), (2, 3)),
    ((3, 1), (3, 2), (3, 3)),
    ((2, 1), (2, 2), (2, 3)),
    ((1, 1), (1, 2), (1, 3)),
    ((1, 3), (2, 3), (3, 3)),
]


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    >>> tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'x', 'x']])
    'x wins!'
    >>> tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']])
    'unfinished'
    >>> tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['o', 'o', 'o']])
    'o wins!'

    draw in case of both players win
    >>> tic_tac_toe_checker([['x', 'x', 'x'], ['-', '-', '-'], ['o', 'o', 'o']])
    'draw'

    draw in case nobody wins and no space on board
    >>> tic_tac_toe_checker([['x', 'x', 'x'], ['x', 'o', 'x'], ['o', 'o', 'o']])
    'draw'
    """
    if x_wins(board) and o_wins(board):
        return "draw"
    elif not x_wins(board) and not o_wins(board) and unfinished(board):
        return "unfinished"
    elif x_wins(board):
        return "x wins!"
    else:
        return "o wins!"


def x_wins(board):
    x_info = []
    for number_of_line, line in enumerate(board, start=1):
        for ind, elem in enumerate(line, start=1):
            if elem == "x":
                x_info.append((number_of_line, ind))
    for combination in list(combinations(x_info, 3)):
        if combination in WINNER_COMBINATIONS:
            return True


def o_wins(board):
    o_info = []
    for number_of_line, line in enumerate(board, start=1):
        for ind, elem in enumerate(line, start=1):
            if elem == "o":
                o_info.append((number_of_line, ind))
    for combination in list(combinations(o_info, 3)):
        if combination in WINNER_COMBINATIONS:
            return True


def unfinished(board):
    for number_of_line, line in enumerate(board):
        for ind, elem in enumerate(line):
            if elem == "-":
                return True
