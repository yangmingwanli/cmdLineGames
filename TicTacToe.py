def createboard():
    board = ['-|-|-','-|-|-','-|-|-']
    return(board)

def printboard(board):
    for row in board:
        print(row)

def make_move(board,pos,type):
    row,col = pos
    if board[row][2*col] == '-':
        board[row] = board[row][:2*col] + type + board[row][2*col+1:]
    else:
        print('pos taken')


def board_full(board):
    full = True
    for row in board:
        if row.find('-') >= 0:
            full = False
    return(full)

def who_won(board):
    for row in board:
        if row.count('x') ==3:
            return((True,'x'))
        if row.count('o') ==3:
            return((True,'o'))
    for col in range(3):
        if (board[0][2*col] + board[1][2*col] + board[2][2*col]).count('x') == 3:
            return((True,'x'))
        if (board[0][2*col] + board[1][2*col] + board[2][2*col]).count('o') == 3:
            return((True,'o'))
    if (board[0][0] + board[1][2] + board[2][4]).count('x') ==3:
        return((True,'x'))
    if (board[0][0] + board[1][2] + board[2][4]).count('o') ==3:
        return((True,'o'))
    if (board[0][4] + board[1][2] + board[2][0]).count('x') ==3:
        return((True,'x'))
    if (board[0][4] + board[1][2] + board[2][0]).count('o') ==3:
        return((True,'o'))
    return((False,'-'))

def get_move():
    row = input('please input row, e.g. 0, 1 or 2\n')
    col = input('please input col, e.g. 0, 1 or 2\n')
    type = input ('please input type, e.g. o or x\n')
    return ((int(row),int(col)),type)

# board = createboard()
#
# make_move(board,(0,0),'o')
# make_move(board,(0,0),'x')
# make_move(board,(1,1),'o')
#
# printboard(board)
# print(board_full(board))
# print(who_won(board))
#
# (pos, type) = get_move()
# make_move(board,pos,type)
#
# printboard(board)
# print(board_full(board))
# print(who_won(board))

board = createboard()
won = False
while(not won):
    (pos, type) = get_move()
    make_move(board,pos,type)
    won,who = who_won(board)
print(who + " won")
