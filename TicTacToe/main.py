from tkinter import *
import random
from AlphaBeta import AiTicTac
from functools import partial

#Configurações globais dos botões
btn_cfg = {
  "height": 10,
  "width": 10,
  "font": "Arial 50 normal",
  "bg": "gray",
  "fg": "white",
  "state": "disabled"
}

class Window():
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x425')
        self.window.title('Jogo da Velha')
        self.btnSet = []
        self.winner = None
        
        for row in range(3):
            btnRow = []

            for col in range (3):
                action_args = partial(self.update_btn, row, col, 'O')
                btn = Button(self.window, text = '-', **btn_cfg, command = action_args)
                btnRow.append(btn)

            self.btnSet.append(btnRow)
        
        for row in range(3):
            for col in range(3):
                self.btnSet[row][col].grid(row = row, column = col, sticky=NSEW)
        
        ## Estética da janela --
        for i in range(3):
            self.window.columnconfigure(i, weight=1)
            self.window.rowconfigure(i, weight=1)
            
        self.window.rowconfigure(3, minsize=25)
        self.window.rowconfigure(5, minsize=25)
        ##-------------
        
        self.display = Label(self.window, text = 'Aperte Start.', font = 'Helvetica 20 bold italic')
        self.display.grid(row = 4, column = 0, columnspan = 3)
        
        self.btnStart = Button(self.window, text='Start', fg = 'white', bg = 'green', 
                               font = 'Helvetica 16 bold italic', command = self.start)
        self.btnStart.grid(row = 6, column = 1)
        
        self.window.mainloop()

    def update_btn(self, row, col, player):
        row, col = self.game.play(row, col)
        self.display.configure(text = self.game.get_info())

        if player == 'X':
            self.btnSet[row][col].configure(text = player, state = 'disabled', bg = "light grey", disabledforeground = "indian red")
        else:
            self.btnSet[row][col].configure(text = player, state = 'disabled', bg = "light grey", disabledforeground = "DeepSkyBlue2")

        if self.game.status():
            info = self.game.get_info()

            if info == 'Nobody':
                self.winner = None
                text = 'Draw'
            else:
                self.winner = info
                text = 'Winner: {}'.format(info)

            for row in range(3):
                for col in range(3):
                    self.btnSet[row][col].configure(state = "disabled")

            self.display.configure(text = text)
            self.btnStart.configure(bg = 'green', state = "normal")
        elif player == 'O':
            self.update_btn(-1, -1, 'X')

    def start(self):
        players = ['X', 'O']

        if self.winner is None:
            turn = random.choice(players)
        else:
            turn = self.winner

        self.game = AiTicTac(turn)
        self.display.configure(text = self.game.get_info())
        
        for row in range(3):
            for col in range(3):
                value = self.game.get_position(row, col)
                self.btnSet[row][col].configure(text = value, bg = 'gray', state = 'normal')
        
        self.btnStart.configure(bg='indian red', state = 'disabled')

        if (turn == 'X'):
            row = random.choice(range(3))
            col = random.choice(range(3))
            self.update_btn(row, col, 'X')

if __name__ == '__main__':
    window = Window()