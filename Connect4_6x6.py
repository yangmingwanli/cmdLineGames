# connect4 game with 6x6 board
import numpy as np
class connect4:
    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

    def printboard(self):
        for row in self.board:
            print(row)
        print('------------')

    def make_move(self,col,type):
        if self.board[0,col] != 0:
            print('pos taken')
        else:
            for i in range(5,-1,-1):
                if self.board[i,col] == 0:
                    self.board[i,col] = type
                    break

    def board_full(self):
        full = True
        for i in range(6):
            if self.board[0,i] == 0:
                full = False
        return(full)

    def who_won(self,board):
        for row in board:
            if row.tolist().count(1) ==4:
                return((True,1))
            if row.tolist().count(2) ==4:
                return((True,2))
        for col in range(4):
            if board[:,col].tolist().count(1) == 4:
                return((True,1))
            if board[:,col].tolist().count(2) == 4:
                return((True,2))
        if [board[0,0], board[1,1], board[2,2], board[3,3]].count(1) == 4:
            return((True,1))
        if [board[0,0], board[1,1], board[2,2], board[3,3]].count(2) == 4:
            return((True,2))
        if [board[0,3], board[1,2], board[2,1], board[3,0]].count(1) == 4:
            return((True,1))
        if [board[0,3], board[1,2], board[2,1], board[3,0]].count(2) == 4:
            return((True,2))
        return((False,0))

    def get_move(self):
        col = input('please input col, e.g. 0, 1, 2 or 3:')
        type = input ('please input player number, e.g. 1 or 2:')
        return (int(col),type)

game = connect4()
game.printboard()
won = False
while(not won):
    (col, type) = game.get_move()
    game.make_move(col,type)
    game.printboard()
    for i in range(3):
        for j in range(3):
            board = game.board
            sub_board = board[i:i+4,j:j+4]
            won,who = game.who_won(sub_board)
            if won:
                break
print('player ' + str(who) + " won")
