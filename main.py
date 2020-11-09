#Tic Tac Toe Game

board = [' ' for x in range(10)]

def moveInput(letter, pos):
    board[pos] = letter

def checkSpace(pos):
    return board[pos] == ' '

def printBoard(board):
    # print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('   |   |')
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isWin(board, el):
    '''
    Winning Line
    '''
    return ((board[1] == el and board[2] == el and board[3] == el) or
    (board[4] == el and board[5] == el and board[6] == el) or
    (board[7] == el and board[8] == el and board[9] == el) or
    (board[1] == el and board[4] == el and board[7] == el) or
    (board[2] == el and board[5] == el and board[8] == el) or
    (board[3] == el and board[6] == el and board[9] == el) or
    (board[1] == el and board[5] == el and board[9] == el) or
    (board[3] == el and board[5] == el and board[7] == el))


def playerTurn():
    turn = True
    while turn:
        move = input('Please select a position (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if checkSpace(move):
                    turn = False
                    moveInput('X', move)
                else:
                    print('Space is occupied!')
            else:
                print('Please select a position within range')
                
        except:
            print('Please type a number!')

def cpuTurn():
    # possibleMove = []
    # for x, letter in enumerate(board):
    #     if letter == ' ' and x!=0:
    #         possibleMove.append(x)
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWin(boardCopy, letter):
                move = i
                return move

    if 5 in possibleMoves:
        move = 5
        
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = randSelect(cornersOpen)

    sideOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            sideOpen.append(i)
    if len(sideOpen) > 0:
        move = randSelect(sideOpen)
    
    return move

def randSelect(board):
    import random
    boardLen = len(board)
    r = random.randrange(0, boardLen)
    return board[r]

def isBoardFull (board):
    if board.count(' ') > 1:
        return False
    return True

def main():
    print('Welcome to the game!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWin(board, 'O')):
            playerTurn()
            printBoard(board)
        else:
            print('You Lose...\nCPU Win!')
            break
        if not(isWin(board, 'X')):
            move = cpuTurn()
            if move == 0:
                print('Tied!')
            else:
                moveInput('O', move)
                print('CPU placed on: ',move)
                printBoard(board)
        else:
            print('Congratulations!!\nYou Win!')
            break

    if isBoardFull(board):
        print('Game Over')
        print('---------------------')
        print('Thank you for playing')
        print('---------------------')
        # playAgain = input('Play again? (Y/N): ')
        # if playAgain.lower() == 'y' or playAgain.lower =='yes':
        #     global board = [' ' for x in range(10)]
        # else:
        #     print('---------------------')
        #     print('Thank you for playing')
        #     print('---------------------')

if __name__ =='__main__':
    main()
