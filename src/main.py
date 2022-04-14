import chess
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
    board = fileparser.fileParser("resources/level1.txt")
    drawBoard(board)
    return board


def drawBoard(board):
    for line in board:
        print(line)
    return

def evalPos(board, newpos, visited):
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


def checkCaptures(board): # returns True if number of captures match among all chess pieces
    countCaptures = -1
    for y in range(len(board)):
        for x in range(len(board)):
            if isinstance(board[y][x], chess.ChessPiece):
                elemCaptures = len(board[y][x].currentCaptures(board, y, x))
                if countCaptures == -1:
                    countCaptures = elemCaptures
                elif countCaptures != elemCaptures:
                    return False

    return True

def gameOver(board):
    #check if last piece in corner
    # if board[0][-1] == 1:
    #     return #something
    
    #check attacks
    #verify if n of attacks match
    return False


def game():
    #level = int(input("Choose level: "))
    #board = resetBoard(size)
    
    initialboard = defaultBoard()

    board = initialboard
    gameOver = 0
    validMove = False

    position = (len(board),0)
    visited = [position]

    ui.drawBoard(board)

    while gameOver == 0:
        while not validMove:
            move = ui.getMove()
            newpos = doMove(move,position)
            validMove = evalPos(board, newpos, visited)

        validMove = False
        position = newpos
        visited.append(newpos)

        ui.drawBoard(board)

        gameOver = gameOver(board)

        if gameOver == 1:
            print('You won!')
        elif gameOver == 2:
            print('Try again!')
            board=initialboard
    
    return 0

game()


