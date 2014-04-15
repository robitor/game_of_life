"""
An implementation of Conway's Game of Life

Game requires the Tkinter library

Created by Rohan Shah
rohan.shah@utexas.edu
"""
import Tkinter as tk
import random


class GameOfLife(object):
    """This class plays Conway's Game of Life"""
    speed = 100 #speed of iteration in ms

    def __init__(self, width, height, path):
        self.root = tk.Tk()
        self.width = width
        self.height = height
        self.iterations = 700 #number of iterations to do
        self.alivelist = [] #keep track of the cells that are currently alive
        self.board = self.board_from_file(path)
        self.cell_list = self.board_init() #stores the cell widgets

    def board_from_file(self, path):
        """
        Returns a 2D list from initial pattern in file at self.path
        
        0 is off, 1 is on
        Board dimensions must match those specified
        """
        board = []
        with open(path) as board_file:
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
        Initializes the GUI representation of the board 

        Additionally, populates the alive
        """
        cell_list = []
        for row in range(self.height):
            for col in range(self.width):
                paint = False

                if self.board[row][col] == 1:
                    paint = True
                    bgcolor = '#000000'
                    self.alivelist.append((row, col))
                elif row == 0 or col == 0:
                    paint = True
                    bgcolor = '#FFFFFF'

                if paint:
                    cell_object = tk.Canvas(self.root, 
                        bg=bgcolor, width=8, height=8, highlightthickness=0)
                    cell_object.grid(column=col, row=row)
                    cell_list.append(cell_object)
                else:
                    cell_list.append(None)  
        return cell_list
 
    def board_update_gui(self, changelist):
        """
        Updates the GUI representation of the board
        """
        rand = lambda: random.randint(0, 255)
        new_color = ('#%02X%02X%02X' % (rand(), rand(), rand()))
 
        for cell in changelist:
            row = cell[0]
            col = cell[1]

            if self.board[row][col] == 1:
                new_state = 0
            else:
                new_state = 1

            if new_state:
                bgcolor = new_color
                #bgcolor = '#000000' #uncomment if you don't like colors
                if self.cell_list[row * self.width + col] is None:
                    cell_object = tk.Canvas(self.root, bg=bgcolor, 
                        width=8, height=8, highlightthickness=0)
                    cell_object.grid(column=col, row=row)
                    self.cell_list[row * self.width + col] = cell_object
                else:
                    self.cell_list[row * self.width
                     + col].config(bg=bgcolor)
            else:
                if self.cell_list[row * self.width + col] is not None:
                    self.cell_list[row
                     * self.width + col].config(bg="#FFFFFF")
    
    def board_update_map(self, changelist):
        """Updates the bit representation of the board"""
        for cell in changelist:
            row = cell[0]
            col = cell[1]
            if self.board[row][col] == 1:
                self.board[row][col] = 0
            else:
                self.board[row][col] = 1

    def is_cell_on(self, row, col):
        """
        Determines if current cell should be on or off for next generation
        """
        num = self.num_on_cells(row, col)
        current_state = self.board[row][col]
        if num < 2:
            return False
        elif num == 2:
            return current_state
        elif num == 3:
            return True
        return False   
  
    def iterate(self, iteration):
        """Main method for computing the next generation """

        changelist = []
        new_alivelist = []
        print "Iterations left: " + str(iteration)
        for cell in self.alivelist:
            row = cell[0]
            col = cell[1]
            new_state = int(self.is_cell_on(row, col))

            if new_state:
                new_alivelist.append((row, col))
            if self.board[row][col] != new_state:
                changelist.append((row, col))

            #Checking the alive cell's neighbors
            for i in range(-1, 2):
                for j in range(-1, 2):
                    x_idx = (col + j) % self.width
                    y_idx = (row + i) % self.height
                    neighbor = (y_idx, x_idx)

                    if ((x_idx != col or y_idx != row) and
                        neighbor not in self.alivelist and
                        neighbor not in new_alivelist and
                        neighbor not in changelist):

                        new_state = int(self.is_cell_on(y_idx, x_idx))

                        if new_state:
                            new_alivelist.append((y_idx, x_idx))

                        if self.board[y_idx][x_idx] != new_state:
                            changelist.append((y_idx, x_idx))


        self.board_update_gui(changelist)
        self.board_update_map(changelist)
        self.alivelist = new_alivelist
        if iteration > 1:
            self.root.after(self.speed, self.iterate, 
                iteration - 1)
        else:
            print "Finished."

    def num_on_cells(self, row, col):
        """
        Counts the number of "on" cells surrounding the specified cell
        with wrapping
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                x_idx = (col + j) % self.width
                y_idx = (row + i) % self.height
                if x_idx != col or y_idx != row:
                    if self.board[y_idx][x_idx]:
                        count += 1
        return count

    def play(self):
        """Starts the game"""
        self.root.after(1000, self.iterate, self.iterations)
        self.root.mainloop()
    
if __name__ == "__main__":
    game = GameOfLife(100, 32, "./glider32x100")
    game.play()




