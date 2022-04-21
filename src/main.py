import src.fileparser as fileparser

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

#def move():
#    chooseMove()
#    if (validMove()):
#        return newPos
#    return -1
#    
#def play(board):
#    move()



def game():
    #size = int(input("Select Board Size: "))
    #board = resetBoard(size)
    
    board = defaultBoard()
    
    drawBoard(board)
    
#    play(board)
    
    return board

