from json.tool import main
import chess, utils
import fileparser
import sys, os
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
    else :
        newpos = (position[0],position[1]+1)
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
    (mode, level) = main_menu()

    initialboard = getBoard(str(level))
    board = initialboard
    game_over = 0
    validMove = False

    position = (len(board) - 1, 0)
    visited = [position]

    if mode == "player":

        while not game_over:
            while not validMove:
                move = game_obj.getMove()
                if move:
                    newpos = doMove(move,position)
                    validMove = utils.validPos(board, newpos, visited)
                    # print(move, '<- move, validMove ->', validMove)
                #move is none when nothing is pressed, false if "x" option or esc is pressed
                if move == False:
                    return 0

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
            board=initialboard
    
    else:
        path = runAlgorithm(board, mode)
        bot = ui.bot.Bot(path, board)
        bot.drawPath()

    return 0

if __name__ == "__main__":
    game()

