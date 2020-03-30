'''from tkinter import *
import random
root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
'''
from tkinter import *
import random

class Game:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Tic tac toe')
        self.field = []
        self.status_game = True
        self.cross_count = 0
        self.smb = 'X'

    def new_game(self):
        for row in range(3):
            for col in range(3):
                self.field[row][col]['text'] = ' '
                self.field[row][col]['background'] = 'lavender'
        self.status_game = True
        self.cross_count = 0

    def click(self,row,col):
        if self.status_game and self.field[row][col]['text'] == ' ':
            self.field[row][col]['text'] = "X"
            self.check_win('X')
            self.cross_count+=1
            if self.cross_count<5 and self.status_game:
                self.computer_move()
                self.check_win('O')

    def check_win(self, current_smb):
        for i in range(3):
            self.check_line(self.field[i][0], self.field[i][1], self.field[i][2], current_smb)
            self.check_line(self.field[0][i], self.field[1][i], self.field[2][i], current_smb)
        self.check_line(self.field[0][0], self.field[1][1], self.field[2][2], current_smb)
        self.check_line(self.field[2][0], self.field[1][1], self.field[0][2], current_smb)
    
    def check_line(self, b1,b2,b3, current_smb):
        if b1['text'] == current_smb and b2['text'] == current_smb and b3['text'] == current_smb:
            b1['background'] = b2['background'] = b3['background'] = 'red'
            self.status_game = False
    
    def can_win(self, b1,b2,b3, current_smb):
        res = False
        if b1['text'] == current_smb and b2['text'] == current_smb and b3['text'] ==' ':
            b3['text'] = 'O'
            res = True
        elif b1['text'] == current_smb and b2['text'] == ' ' and b3['text'] == current_smb:
            b2['text'] = 'O'
            res = True
        elif b1['text'] == ' ' and b2['text'] == current_smb and b3['text'] == current_smb:
            b1['text'] = 'O'
            res = True
        return res
    
    def computer_move(self):
        for i in range(3):
            self.smb = 'O'
            if self.can_win(self.field[i][0], self.field[i][1], self.field[i][2], self.smb):
                return
            if self.can_win(self.field[0][i], self.field[1][i], self.field[2][i], self.smb):
                return
        if self.can_win(self.field[0][0], self.field[1][1], self.field[2][2], self.smb):
            return
        if self.can_win(self.field[2][0], self.field[1][1], self.field[0][2], self.smb):
            return
        for i in range(3):
            self.smb = 'X'
            if self.can_win(self.field[i][0], self.field[i][1], self.field[i][2], self.smb):
                return
            if self.can_win(self.field[0][i], self.field[1][i], self.field[2][i], self.smb):
                return
        if self.can_win(self.field[0][0], self.field[1][1], self.field[2][2], self.smb):
            return
        if self.can_win(self.field[2][0], self.field[1][1], self.field[0][2], self.smb):
            return
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if self.field[row][col]['text']==' ':
                self.field[row][col]['text'] = 'O'
                break
    def start(self):
        for row in range(3):
            line = []
            for col in range(3):
                button = Button(self.main_window, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command= lambda row=row, col=col: self.click(row,col))
                button.grid(row=row, column=col, sticky='nsew')
                line.append(button)
            self.field.append(line)
        new_button = Button(self.main_window, text='new game', command=self.new_game)
        new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
        self.main_window.mainloop()

Game().start()
