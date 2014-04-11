"""
An implementation of Conway's Game of Life
for the Etsy coding assignment.

Helper methods are also included.

Created by Rohan Shah
rohan.shah@utexas.edu
"""

import time
from Tkinter import *

#Dimensions
BOARD_WIDTH = 100
BOARD_HEIGHT = 25

#board location
BOARD_PATH = "./pattern_convert"

#Number of Generations
NUM_GENERATIONS = 700

#Speed in seconds
SPEED = 1

changelist = []
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
                raise Exception("Invalid row length " + str(len(row_int_list)))
            board.append(row_int_list)
        if len(board) != BOARD_HEIGHT:
            print len(board)
            raise Exception("Invalid board height")
    return board

def num_on_cells(board, row, col):
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
                if board[y_idx][x_idx]:
                    count += 1
    return count

def is_cell_on(board, row, col):
    """
    Determines if current cell should be on or off for next generation
    """
    num = num_on_cells(board, row, col)
    current_state = board[row][col]
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

def board_init(board):
    cell_list = []
    i = 0
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            bgcolor = '#FFFFFF'

            if board[row][col] == 1:
                bgcolor = '#000000'
                w = Canvas(root, bg=bgcolor, width=8, height=8, highlightthickness=0)
                w.grid(column=col, row=row)
                cell_list.append(w)
                changelist.append((row, col))
            else:
                cell_list.append(None)
               
            print i
            i+=1
    return cell_list

def board_update(board, cell_list):
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            bgcolor = '#FFFFFF'
            if board[row][col] == 1:
                bgcolor = '#000000'
                if cell_list[row * BOARD_WIDTH + col] is None:
                    w = Canvas(root, bg=bgcolor, width=8, height=8, highlightthickness=0)
                    w.grid(column=col,row=row)
                    cell_list[row * BOARD_WIDTH + col] = w
                else:
                    cell_list[row * BOARD_WIDTH + col].config(bg=bgcolor)
            else:
                if cell_list[row * BOARD_WIDTH + col] is not None:
                    cell_list[row * BOARD_WIDTH + col].config(bg=bgcolor)

def update_game2(board, cell_list, iteration):
    newboard = [[0]*BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    print "Iteration: " + str(iteration)
    for cell in changelist[:]:
        row = cell[0]
        col = cell[1]
        newboard[row][col] = int(is_cell_on(board, row, col))
        if board[row][col] == newboard[row][col]:
            if (row, col) in changelist:
                changelist.remove((row, col))

        for i in range(-1, 2):
            for j in range(-1, 2):
                x_idx = (col + j) % BOARD_WIDTH
                y_idx = (row + i) % BOARD_HEIGHT
                if x_idx != col or y_idx != row:
                    newboard[y_idx][x_idx] = int(is_cell_on(board, y_idx, x_idx))
                    if board[y_idx][x_idx] == newboard[y_idx][x_idx]:
                        if (y_idx, x_idx) in changelist:
                            changelist.remove((y_idx, x_idx))
                    else:
                        if (y_idx, x_idx) not in changelist:
                            changelist.append((y_idx, x_idx))
    board_update(newboard, cell_list)
    board = newboard
    if iteration > 0:
        root.after(2000, update_game2, board, cell_list, iteration - 1)

        #now check neighbors

def update_game(board, cell_list, iteration):
    """
    Main method for playing Conway's Game of Life
    """
    print "Iteration: " + str(iteration)
    #create new board
    newboard = [[0]*BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            newboard[row][col] = int(is_cell_on(board, row, col))

    board_update(newboard, cell_list)
    board = newboard
    if iteration > 0:
        root.after(50, update_game, board, cell_list, iteration - 1)

root = Tk()
board = board_from_file()
width = BOARD_WIDTH * 8
height = BOARD_HEIGHT * 8
root.geometry(str(width) + 'x' + str(height))
cell_list = board_init(board)
root.after(500, update_game, board, cell_list, NUM_GENERATIONS)
root.mainloop()
