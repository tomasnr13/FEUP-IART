import chess, utils
import fileparser
import sys, os
import copy
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'ui'))
from ui.menu import main_menu
from ui.game import Game
import node_algorithms
import snake
import ui.bot

game_obj = Game()

def resetBoard(size):

    board = []
    for _ in range(size):
        line = []
        for _ in range(size):
            line += [0]
        board += [line]
    
    return board

def getBoard(level):
    board = fileparser.fileParser("resources/level"+level+".txt")
    pos = (len(board)-1, 0)
    board[pos[0]][pos[1]] = 1
    drawBoard(board, pos)
    return board

def drawBoard(board, pos):
    game_obj.board.update(board, pos)

def runAlgorithm(board, algorithm):
    s = snake.SnakeNode(board)
    if algorithm == "depth first search":
        return(node_algorithms.dfs(s, snake.condition))
    elif algorithm == "breadth first search":
        return(node_algorithms.bfs(s, snake.condition))
    elif algorithm == "iterative deepening":
        return(node_algorithms.it_deep(s, snake.condition))
    elif algorithm == "uniform cost":
        return(node_algorithms.ucost(s, snake.condition))
    elif algorithm == "greedy":
        return(node_algorithms.greedy(s, snake.condition, snake.heuristics, board))
    elif algorithm == "a star":
        return(node_algorithms.astar(s, snake.condition, snake.heuristics, board))

def doMove(move,position):
    newpos = None
    if move == "up":
        newpos = (position[0]-1,position[1])
    elif move == "down":
        newpos = (position[0]+1,position[1])
    elif move == "left":
        newpos = (position[0],position[1]-1)
    elif move == "right" :
        newpos = (position[0],position[1]+1)
    else: 
        return None
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
    level = 1
    game_over = 0
    while True:

        if(game_over != 2 and game_over != 1):
            (mode, level) = main_menu(level)

        if game_over == 1 and mode == "player":
            level = int(level) + 1

        initialboard = getBoard(str(level))
        board = copy.deepcopy(initialboard)
        game_over = 0
        validMove = False

        position = (len(board) - 1, 0)
        visited = [position]

        if mode == "player":

            while not game_over:
                while not validMove:
                    move = game_obj.getMove(False)
                    if move:
                        if move == "restart":
                            game_over = 2
                            break

                        if move == "back":
                            game_over = 3
                            break

                        newpos = doMove(move,position)
                        validMove = utils.validPos(board, newpos, visited)
                        
                    #move is none when nothing is pressed, false if "x" option or esc is pressed
                    if move == False:
                        break

                if(game_over != 2 and game_over != 3):
                    if validMove:
                        validMove = False
                        position = newpos
                        board[position[0]][position[1]] = 1
                        visited.append(newpos)

                    game_obj.board.update(board, newpos)

                    game_over = gameOver(board)

            if game_over == 1:
                print('You won!')
                
            elif game_over == 2:
                print('Try again!')
                board = copy.deepcopy(initialboard)
                position = (len(board) - 1, 0)
                visited = [position]
        
        else:
            path = runAlgorithm(board, mode)
            bot = ui.bot.Bot(path, board)
            while not game_obj.getMove(True):
                bot.drawPath()



if __name__ == "__main__":
    game()

