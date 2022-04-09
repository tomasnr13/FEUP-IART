import fileparser
import ui

def resetBoard(size):

    board = []
    for _ in range(size):
        line = []
        for _ in range(size):
            line += [0]
        board += [line]
    
    return board

def defaultBoard():
    board = fileparser.fileParser("level1.txt")
    drawBoard(board)
    return board


def drawBoard(board):
    for line in board:
        print(line)
    return

def evalPos(position):
    #check:
    #out of bounds
    #collide with piece
    #adjacent/visited position
    return True

def doMove(move,position):
    if move == "up":
        newpos = (position[0],position[1]+1)
    elif move == "down":
        newpos = (position[0],position[1]-1)
    elif move == "left":
        newpos = (position[0]-1,position[1])
    else :
        newpos = (position[0]+1,position[1])
    return newpos


def checkBoard(board):
    #check if last piece in corner
    #check attacks
    #verify if n of attacks match
    return 0

def game():
    #level = int(input("Choose level: "))
    #board = resetBoard(size)
    
    initialboard = defaultBoard()

    board = initialboard
    gameOver = 0
    validMove = False

    position = (len(board),0)
    passedpositions = [position]

    ui.drawBoard(board)

    while gameOver == 0:
        while not validMove:
            move = ui.getMove()
            newpos = doMove(move,position)
            validMove = evalPos(board, newpos, passedpositions)

        validMove = False
        position = newpos
        passedpositions.append(newpos)

        ui.drawBoard(board)

        gameOver = checkBoard(board)

        if gameOver == 1:
            print('You won!')
        elif gameOver == 2:
            print('Try again!')
            board=initialboard
    
    return 0

game()