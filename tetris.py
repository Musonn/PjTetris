import tkinter as tk
from tkinter import Frame, font
from tkinter.constants import LEFT

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TetrisGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tetris")
        self.geometry('800x640')
        self.resizable(False,False)

        self.screen = tk.Canvas(self, bg="white", width=300, height=400)# dimension of the screen

    currentGameConsole = [[0 for x in range(10)] for y in range(20)]    # width 10, height 20
    nextGameConsole = [[0 for x in range(10)] for y in range(20)]    # width 10, height 20

    # def set_game_screens(self, game_screens):
    #     self.set_game_screens = game_screens

    # def display_screen(self, ):#game_screen_number):
    #     #self.active_screen = self.game_screens
    #     self.screen.delete("all")
    #     self.screen.create_image((250,400),image=self.active_screen.image)
    
    # def show_next_screen(self):
    #     self.display_screen

    def Check(self):
        pass


class Tetrismino():
    def __init__(self, data):
        self.prev = data  # prev origin at left up corner be (0,0)
        self.location = self.prev

    def Left(self):
        self.location = list(self.prev)
        self.location[0] -= 1
        if Check():
            self.prev = tuple(self.location)
        return self.location, self.prev


    def Right(self):
        self.location = list(self.prev)
        self.location[0] += 1
        if Check():
            self.prev = tuple(self.location)

    def Down(self):
        self.location = list(self.prev)
        self.location[1] += 1
        if Check():
            self.prev = tuple(self.location)

    def Chi(self):
        return '10'

class iBlock(Tetrismino):
    def __init__(self, data):
        super().__init__(data)

    type = 'I'
    node_1 = Node(((0, 1), (1, 1), (2, 1), (3, 1)))
    node_2 = Node(((2, 0), (2, 1), (2, 2), (2, 3)))

    node_1.next = node_2
    node_2.next = node_1

if __name__=="__main__":
    game=TetrisGame()
    origin = (0,0)
    t = Tetrismino(origin)

    iblock = iBlock(t)
    iblock.Down()
    #game.mainloop()
    x=10