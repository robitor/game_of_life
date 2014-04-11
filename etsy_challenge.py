"""
An implementation of Conway's Game of Life
for the Etsy coding assignment.

Helper methods are also included.

Created by Rohan Shah
rohan.shah@utexas.edu
"""

import time
import Tkinter as Tk

#Dimensions
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

#Initial board location
BOARD_PATH = "./conway_board"

#Number of Generations
NUM_GENERATIONS = 20

def board_from_file():
    """
    Returns a 2D list from initial state written in file at BOARD_PATH
    0 is off, 1 is on
    Board dimensions must match those specified
    """
    board = []
    with open(BOARD_PATH) as board_file:
        for row in board_file:
            row_list = list(row.rstrip())
            row_int_list = [int(i) for i in row_list]
            if len(row_int_list) != BOARD_WIDTH:
                raise Exception("Invalid row length")
            board.append(row_int_list)
        if len(board) != BOARD_HEIGHT:
            raise Exception("Invalid board height")
    return board

def num_on_cells(board, col, row):
    """
    Counts the number of "on" cells surrounding the specified cell
    with wrapping
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x_idx = (col + j) % BOARD_WIDTH
            y_idx = (row + i) % BOARD_HEIGHT
            if x_idx != col or y_idx != row:
                if board[x_idx][y_idx]:
                    count += 1
    return count

def is_cell_on(board, col, row):
    """
    Determines if current cell should be on or off for next generation
    """
    num = num_on_cells(board, col, row)
    current_state = board[col][row]
    if num < 2:
        return False
    elif num == 2:
        return current_state
    elif num == 3:
        return True
    return False

def print_board(board):
    """
    Prints the board to STDOUT
    """
    for row in board:
        print row

    print

def play_game():
    """
    Main method for playing Conway's Game of Life
    """
    board = board_from_file()
    root = Tk()
    for _ in range(NUM_GENERATIONS):
        #create new board
        newboard = [[0]*BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                newboard[row][col] = int(is_cell_on(board, row, col))
        print_board(newboard)
        board = newboard
        time.sleep(1)

play_game()
