import tkinter as tk
class Game():
    board = ['', '', '', '', '', '', '', '', '']
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (2, 5, 8), (1, 4, 7), (0, 4, 8), (2, 4, 6)]
    list_indexes = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    def print_board(self):
        for i, c in enumerate(self.board):
            if (i + 1) % 3 == 0:
                print(f'{c}')
            else:
                print(f'{c}|', end='')

    def getting_winner(self, state_board):
        for (x, y, z) in self.winning_combinations:
            if state_board[x] == state_board[y] and state_board[y] == state_board[z] and (
                    state_board[x] == 'X' or state_board[x] == '0'):
                return False
        return True

    def play_game(self):
        current_sign = "X"
        while self.getting_winner(self.board):
            index = input(f'Where do you want draw {current_sign}? ')
            if index not in self.list_indexes:
                print("Incorrect number, choose from " + (' '.join(map(str, self.list_indexes))))
                continue
            else:
                index = int(index)
            if self.board[index] == '':
                self.board[index] = current_sign
            else:
                print("This is taken position")
                continue
            self.print_board()
            if not self.getting_winner(self.board):
                print(f'Our winner is: {current_sign}')
                break
            if current_sign == "X":
                current_sign = "0"
            else:
                current_sign = "X"
            if "" not in self.board:
                print("Were is no winner")
                break


Game().play_game()
input()