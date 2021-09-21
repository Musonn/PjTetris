import tkinter as tk
from tkinter import Frame, font

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

    CurBlock = None
    currentGameConsole = [[0 for x in range(10)] for y in range(20)]    # width 10, height 20
    nextGameConsole = [[0 for x in range(10)] for y in range(20)]    # width 10, height 20

    def create_a_block(self,x):
        a_block = iBlock(x)
        return a_block

    def updateGameConsole(self,a_block,a_currentGameConsole):
        for i in a_block.orientation.data:
            [x,y]=a_block.location    # abs location
            [z,w]=i                         # relative location
            a_currentGameConsole[y+w][x+z] = a_block.type
        return a_currentGameConsole

    # def set_game_screens(self, game_screens):
    #     self.set_game_screens = game_screens

    # def display_screen(self, ):#game_screen_number):
    #     #self.active_screen = self.game_screens
    #     self.screen.delete("all")
    #     self.screen.create_image((250,400),image=self.active_screen.image)
    
    # def show_next_screen(self):
    #     self.display_screen

class Tetrismino():
    def __init__(self, data):
        self.prev = data  # prev origin at left up corner be (0,0)
        self.location = self.prev

    def Left(self):
        self.location = list(self.prev)
        self.location[0] -= 1
        #if Check():
        self.prev = tuple(self.location)

    def Right(self):
        self.location = list(self.prev)
        self.location[0] += 1
        #if Check():
        self.prev = tuple(self.location)

    def Down(self):
        self.location = list(self.prev)
        self.location[1] += 1
        #if Check():
        self.prev = tuple(self.location)

class iBlock(Tetrismino):
    def __init__(self, data):
        super().__init__(data)
        self.orientation = Node(((0, 1), (1, 1), (2, 1), (3, 1)))
        self.orientation.next = Node(((2, 0), (2, 1), (2, 2), (2, 3)))
        self.orientation.next.next = self.orientation   # linked list

    type = 'I'

def fmtprt(x):  # format print gameconsole
    for i in range(len(x)):
        for j in (x[i]):
            print(j,end='')
        print('')

if __name__=="__main__":
    game=TetrisGame()
    origin = (0,0)
    GE = False # set GameEnd to False
    UC = False # set UpdateGameConsole to False

    game.CurBlock = game.create_a_block(origin)
    game.CurBlock.Right()
    for a in range(18):
        game.CurBlock.Down() 

#碰撞检测：先检查边界，再检查已有方块

    for i in game.CurBlock.orientation.data:
        [x,y]=game.CurBlock.location    # abs location
        [z,w]=i                         # relative location
        if x+z >= 10 and x+z < 0:   #超出左右边界
            game.CurBlock.location = game.CurBlock.prev
        elif y+w > 18: #触底
            game.CurBlock.location = game.CurBlock.prev
            game.currentGameConsole = game.updateGameConsole(game.CurBlock,game.currentGameConsole)
            break #更新GameConsole - 创建新tetrimino - 进入下一轮
        elif game.currentGameConsole[y+w][x+z] != 0: #触块或触顶
            if game.CurBlock.prev == (0,0):#触顶
                GE = True    #游戏结束
            else:   #触块
                game.CurBlock.location = game.CurBlock.prev
                game.currentGameConsole = game.updateGameConsole(game.CurBlock,game.currentGameConsole)
                break #更新GameConsole - 创建新tetrimino -  进入下一轮
    fmtprt(game.currentGameConsole)


    game.CurBlock = game.create_a_block(origin)
    for a in range(18):
        game.CurBlock.Down()

#碰撞检测：先检查边界，再检查已有方块

    for i in game.CurBlock.orientation.data:
        [x,y]=game.CurBlock.location    # abs location
        [z,w]=i                         # relative location
        if x+z >= 10 and x+z < 0:   #超出左右边界
            game.CurBlock.location = game.CurBlock.prev
        elif y+w > 18: #触底
            game.CurBlock.location = game.CurBlock.prev
            game.currentGameConsole = game.updateGameConsole(game.CurBlock,game.currentGameConsole)
            break #更新GameConsole - 创建新tetrimino - 进入下一轮
        elif game.currentGameConsole[y+w][x+z] != 0: #触块或触顶
            if game.CurBlock.prev == (0,0):#触顶
                GE = True    #游戏结束
            else:   #触块
                game.CurBlock.location = game.CurBlock.prev
                game.currentGameConsole = game.updateGameConsole(game.CurBlock,game.currentGameConsole)
                break #更新GameConsole - 创建新tetrimino -  进入下一轮
    fmtprt(game.currentGameConsole)

# #更新GameConsole: 更新self.prev并更新GameConsole，否则location回滚
#     for i in game.CurBlock.orientation.data:
#         [x,y]=game.CurBlock.location    # abs location
#         [z,w]=i                         # relative location
#         game.currentGameConsole[x+z][y+w] = game.CurBlock.type
#     fmtprt(game.currentGameConsole)