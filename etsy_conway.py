import Tkinter as tk



class GameOfLife(tk.Frame):
    #Dimensions
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 10

    def __init__(self, master=None):
        self.grid(column=0,row=0)
      #  for i in range(BOARD_HEIGHT):
       #     for j in range(BOARD_WIDTH):

 
game = GameOfLife()
game.mainloop()




