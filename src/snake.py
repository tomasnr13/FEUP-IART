"""
Initial State: (len(board)-1,0)
Operators: (checkBounds) up -> (y, x) => (y-1, x)
           (checkBounds) down -> (y, x) => (y+1, x)
           (checkBounds) left -> (y, x) => (y, x-1)
           (checkBounds) right -> (y, x) => (y, x+1)

All operators have a cost of 1.
Objective State: (0, len(board)-1)
"""
import chess, fileparser, utils, node_algorithms
import copy

class SnakeNode:

    def __init__(self, board, posY=-1, posX=0, previousNode=None, distance=0):
        if (posY==-1):
            posY += len(board)
        self.posY = posY
        self.posX = posX
        self.board = board
        self.previousNode = previousNode
        self.distance = distance

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.posY == other.posY and self.posX == other.posX
        return False

    def __repr__(self):
        return f'({self.posY}, {self.posX})'
    
    def __str__(self):
        return f'({self.posY}, {self.posX})'

    def __lt__(self, other):
        return self.distance < other.distance

    def edgeNodes(self, distance=0):
        edgeNodesList = []

        y, x = self.posY, self.posX

        #down
        if y < len(self.board)-1 and self.board[y+1][x] == 0:
            newPos = (y+1, x)
            
            visited_adjs = 0

            adjs = [(newPos[0]-1,newPos[1]), (newPos[0]+1,newPos[1]), (newPos[0],newPos[1]-1), (newPos[0],newPos[1]+1)]
            for pos in adjs:
                if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(self.board) and pos[1] < len(self.board):
                    if self.board[pos[0]][pos[1]] == 1:
                        visited_adjs += 1
            print(newPos, "down")
            
            if visited_adjs <= 1: 
                boardCopy = copy.deepcopy(self.board)           
                boardCopy[y+1][x] = 1
                utils.printBoard(boardCopy)

                edgeNodesList.append(SnakeNode(boardCopy, newPos[0], newPos[1], self, distance))
        #up
        if y > 0 and self.board[y-1][x] == 0:
            newPos = (y-1, x)
            
            visited_adjs = 0
            adjs = [(newPos[0]-1, newPos[1]), (newPos[0]+1,newPos[1]), (newPos[0],newPos[1]-1), (newPos[0],newPos[1]+1)]
            
            for pos in adjs:
                if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(self.board) and pos[1] < len(self.board):
                    if self.board[pos[0]][pos[1]] == 1:
                        visited_adjs += 1

            print(newPos, "up")

            if visited_adjs <= 1:   
                boardCopy = copy.deepcopy(self.board)           
                boardCopy[y-1][x] = 1
                utils.printBoard(boardCopy)

                edgeNodesList.append(SnakeNode(boardCopy, newPos[0], newPos[1], self, distance))

        
        #right
        if x < len(self.board)-1 and self.board[y][x+1] == 0:
            newPos = (y, x+1)
            
            adjs = [(newPos[0]-1,newPos[1]), (newPos[0]+1,newPos[1]), (newPos[0],newPos[1]-1), (newPos[0],newPos[1]+1)]
            
            visited_adjs = 0

            for pos in adjs:
                if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(self.board) and pos[1] < len(self.board):
                    if self.board[pos[0]][pos[1]] == 1:
                        visited_adjs += 1

            print(newPos, "right")

            if visited_adjs <= 1:   
                boardCopy = copy.deepcopy(self.board)           
                boardCopy[y][x+1] = 1
                utils.printBoard(boardCopy)

                edgeNodesList.append(SnakeNode(boardCopy, newPos[0], newPos[1], self, distance))

        #left
        if x > 0 and self.board[y][x-1] == 0:
            newPos = (y, x-1)
            
            adjs = [(newPos[0]-1,newPos[1]), (newPos[0]+1,newPos[1]), (newPos[0],newPos[1]-1), (newPos[0],newPos[1]+1)]
            
            visited_adjs = 0
            
            for pos in adjs:
                if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(self.board) and pos[1] < len(self.board):
                    if self.board[pos[0]][pos[1]] == 1:
                        visited_adjs += 1
            print(newPos, "left")

            if visited_adjs <= 1:   
                boardCopy = copy.deepcopy(self.board)           
                boardCopy[y][x-1] = 1
                utils.printBoard(boardCopy)
                edgeNodesList.append(SnakeNode(boardCopy, newPos[0], newPos[1], self, distance))

        return edgeNodesList

def condition(node):
    return node.posY == 0 and (node.posX == len(node.board)-1) and chess.checkCaptures(node.board)

def heuristics(node):
    pos = (node.posY, node.posX)
    d = utils.getDistance(pos, board)
    return chess.captureDiff(node.board) + d/4

board = fileparser.fileParser("resources/level1.txt")
s = SnakeNode(board)
# print(s.edgeNodes())


print(node_algorithms.bfs(s, condition))
