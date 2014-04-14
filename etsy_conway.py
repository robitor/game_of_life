"""
An implementation of Conway's Game of Life
for the Etsy coding assignment.

Game requires the Tkinter library

Created by Rohan Shah
rohan.shah@utexas.edu
"""
import Tkinter as tk



class GameOfLife(object):
    """This class plays Conway's Game of Life"""

    def __init__(self):
        self.root = tk.Tk()
        self.width = 100
        self.height = 25
        self.root.geometry(str(self.width * 8) + 'x' + str(self.height * 8))

        self.path = "./pattern_convert"
        self.generation = 200
        self.board = self.board_from_file()
        self.cell_list = self.board_init()

    def board_from_file(self):
        """
        Returns a 2D list from initial state written in file at BOARD_PATH
        
        0 is off, 1 is on
        Board dimensions must match those specified
        """
        board = []
        with open(self.path) as board_file:
            for row in board_file:
                row_list = list(row.rstrip())
                row_int_list = [int(i) for i in row_list]
                if len(row_int_list) != self.width:
                    raise Exception("Invalid row length " + 
                        str(len(row_int_list)))
                board.append(row_int_list)
            if len(board) != self.height:
                print len(board)
                raise Exception("Invalid board height")
        return board

    def board_init(self):
        """
        Initializes the GUI board with the cell objects

        Returns an array containing the cell objects
        """
        cell_list = []
        for row in range(self.height):
            for col in range(self.width):
                bgcolor = '#FFFFFF'

                if self.board[row][col] == 1:
                    bgcolor = '#000000'
                    cell_object = tk.Canvas(self.root, 
                        bg=bgcolor, width=8, height=8, highlightthickness=0)
                    cell_object.grid(column=col, row=row)
                    cell_list.append(cell_object)

                else:
                    cell_list.append(None)  
        return cell_list
    
    def play(self):
        """Starts the game"""
        self.root.mainloop()

if __name__ == "__main__":
    game = GameOfLife()
    game.play()




