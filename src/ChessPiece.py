from abc import ABC, abstractmethod
import src.main as main

class ChessPiece(ABC):

	@abstractmethod
	def possibleMoves(self):
		pass


class Tower(ChessPiece):
    
    def possibleMoves(self, board, line, col):
        count = 0
        
        size = len(board)
        
        for x in range(max(col-1, 0), -1, -1):
            if board[line][x] == 0:
                count +=1
            else:
                break
            
        for x in range(min(col+1, size-1), size): #len(board[line])
            if board[line][x] == 0:
                count+=1
            else:
                break
        
        for y in range(max(line-1, 0), -1, -1):
            if board[y][col] == 0:
                count += 1
            else:
                break
            
        for y in range(min(line+1, size-1), size):
            if board[y][col] == 0:
                count += 1
            else:
                break
        
        return count
    
class Horse(ChessPiece):
    def possibleMoves(self, board):
        return

class Bishop(ChessPiece):
    def possibleMoves(self, board):
        return

class Queen(ChessPiece):
    def possibleMoves(self, board):
        return

class King(ChessPiece):
    def possibleMoves(self, board):
        return 

board = main.defaultBoard()

tower = Tower()
print(Tower.possibleMoves(Tower, board, 1, 3))

