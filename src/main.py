import chess, utils
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
         return False
    
    #check attacks
    if chess.checkCaptures(board):
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

    while not game_over:

        while not validMove:
            move = getMove()
            if move:
                newpos = doMove(move,position)
                validMove = utils.validPos(board, newpos, visited)
                print(move, '<- move, validMove ->', validMove)
            #move is none when nothing is pressed, false if "x" option or esc is pressed
            if move == False:
                return 0

        validMove = False
        position = newpos
        board[position[0]][position[1]] = 1
        visited.append(newpos)

        draw(board, newpos)

        game_over = gameOver(board)

        if game_over == 1:
            print('You won!')
        elif game_over == 2:
            print('Try again!')
            board=initialboard
    
    return 0

if __name__ == "__main__":
    game()

