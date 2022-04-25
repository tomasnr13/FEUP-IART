import chess, utils
import fileparser
import copy
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
    draw(board, (len(board)-1, 0))


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


def gameOver(board):
    #check if last piece in corner
    if board[0][-1] != 1:
         return 0
    
    #check attacks
    if chess.checkCaptures(board):
        return 1
    else:
        return 2

def askForHint(position, path, board):
    neq = False
    if not chess.checkCaptures(board):
        neq = True
        print("The number of attacks doesnt match!")
    
    newboard = copy.deepcopy(board)

    for idx in range(len(path)):
        if path[idx] == position:
            nextpos=path[idx+1]
            if nextpos == (position[0]+1,position[1]):
                print("Move down")
            elif nextpos == (position[0]-1,position[1]):
                print("up")
            elif nextpos == (position[0],position[1]+1):
                print("right")
            elif nextpos == (position[0],position[1]-1):
                print("left")
            if neq:
                newboard[nextpos[0]][nextpos[1]] = 1
                if chess.checkCaptures(newboard):
                    print("This move can balance the number of attacks!")
            return
    print("You might want to redo your path")


def game():
    #level = int(input("Choose level: "))
    #board = resetBoard(size)
    
    initialboard = defaultBoard()

    board = copy.deepcopy(initialboard)
    game_over = 0
    validMove = False

    position = (len(board) - 1, 0)
    visited = [position]
    while game_over != 1:
        while not validMove:
            move = getMove()
            if move:
                newpos = doMove(move,position)
                validMove = utils.validPos(board, newpos, visited)
                print(move, '<- move, validMove ->', validMove)
            #move is none when nothing is pressed, false if "x" option or esc is pressed
            if move == False:
                return 0

        if validMove:
            position = newpos
            board[position[0]][position[1]] = 1
            visited.append(newpos)

        validMove = False
        draw(board, newpos)

        game_over = gameOver(board)

        if game_over == 1:
            print('You won!')
            return 0
        elif game_over == 2:
            print('Try again!')
            board = copy.deepcopy(initialboard)
            position = (len(board) - 1, 0)
            visited = [position]
    
    return 0

if __name__ == "__main__":
    game()

