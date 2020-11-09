board = [' ' for x in range(10)]

def moveInput(letter, pos):
    board[pos] = letter

def isEmpty(pos):
    return board[pos] == ' '

def boardPrint(board):
    print('           '+board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('           '+board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('           '+board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('- - - - - - - - - - - - - - - - - -')


def isWin(board, el):
    return ((board[1] == el and board[2] == el and board[3] == el) or
    (board[4] == el and board[5] == el and board[6] == el) or
    (board[7] == el and board[8] == el and board[9] == el) or
    (board[1] == el and board[4] == el and board[7] == el) or
    (board[2] == el and board[5] == el and board[8] == el) or
    (board[3] == el and board[6] == el and board[9] == el) or
    (board[1] == el and board[5] == el and board[9] == el) or
    (board[3] == el and board[5] == el and board[7] == el))

def isClear(board):
    if board.count(' ') <= 1:
        return True
    return False

def playerTurn():
    turn = True
    while turn:
        move = input('Please select your choice (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isEmpty(move):
                    turn = False
                    moveInput('X', move)
                else:
                    print('It has been occupied!')
            else:
                print('Please input within range')
                
        except:
            print('Please input a number')

def cpuTurn():
    possibleMove = [x for x,letter in enumerate(board) if letter == ' ' and x != 0]

    #Almost Win Condition
    for x in ['X', 'O']:
        for i in possibleMove:
            boardCopy = board[:]
            boardCopy[i] = x
            if isWin(boardCopy, x):
                return i

    #5 Empty Condition
    if 5 in possibleMove:
        return 5

    #Corner and Side Empty Condition
    corner = []
    side = []
    for i in possibleMove:
        if i in [1,3,7,9]:
            corner.append(i)
        elif i in [2,4,6,8]:
            side.append(i)
    
    if len(corner) > 0:
        return randMove(corner)
    if len(side) > 0:
        return randMove(side)
    return 0
def randMove(board):
    import random
    ln = len(board)
    rVal = random.randrange(0,ln)
    return board[rVal]

def main():
    print('   WELCOME to Tic Tac Toe game')
    print('- - - - - - - - - - - - - - - - - -')
    boardPrint(board)

    while not(isClear(board)):
        if not(isWin(board, 'O')):
            playerTurn()
            boardPrint(board)
        else:
            print('You Lose!')
            break
        if not(isWin(board, 'X')):
            move = cpuTurn()
            if move == 0:
                print('Tie!')
                break
            else:
                moveInput('O', move)
                print('CPU placed on: ',move)
                boardPrint(board)
        else:
            print('Congratulations!\nYou Win!')
            break
    
    if isClear(board):
        print('Game Over')



if __name__ == '__main__':
    main()