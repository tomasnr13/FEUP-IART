import chess
import fileparser
from ui import draw, getMove

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
    board[len(board)-1][0] = 1
    drawBoard(board)
    return board

def drawBoard(board):
    draw(board)
    # for line in board:
    #     print(line)
    # return

def evalPos(board, newpos, visited):
    #check:
    #out of bounds
    l = len(board)
    if newpos[0] < 0 or newpos[0] >= l or newpos[1] < 0 or newpos[1] >= l:
        return False
    #collide with piece
    if board[newpos[0]][newpos[1]] != 0 : 
        return False
    #visited position  
    if newpos in visited :
        return False
    #adjacent position 
    adjs=0
    if (newpos[0]-1,newpos[1]) in visited : 
        adjs+=1
    if (newpos[0]+1,newpos[1]) in visited : 
        adjs+=1
    if (newpos[0],newpos[1]-1) in visited : 
        adjs+=1
    if (newpos[0],newpos[1]+1) in visited : 
        adjs+=1
    if adjs>1:
        return False

    return True

def doMove(move,position):
    if move == "up":
        newpos = (position[0]-1,position[1])
    elif move == "down":
        newpos = (position[0]+1,position[1])
    elif move == "left":
        newpos = (position[0],position[1]-1)
    else :
        newpos = (position[0],position[1]+1)
    print(position, newpos)
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
    if board[0][-1] != 1:
         return False
    
    #check attacks
    if checkCaptures(board):
        return True
    else:
        return False


def game():
    #level = int(input("Choose level: "))
    #board = resetBoard(size)
    
    initialboard = defaultBoard()

    board = initialboard
    game_over = 0
    validMove = False

    position = (len(board) - 1, 0)
    visited = [position]

    while game_over == 0:

        while not validMove:
            move = getMove()
            if move:
                newpos = doMove(move,position)
                validMove = evalPos(board, newpos, visited)
                print(move, '<- move, validMove ->', validMove)
            #move is none when nothing is pressed, false if "x" option or esc is pressed
            if move == False:
                return 0

        validMove = False
        position = newpos
        board[position[0]][position[1]] = 1
        visited.append(newpos)

        draw(board)

        game_over = gameOver(board)

        if game_over == 1:
            print('You won!')
        elif game_over == 2:
            print('Try again!')
            board=initialboard
    
    return 0

game()


