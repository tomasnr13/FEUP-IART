from abc import ABC, abstractmethod

class ChessPiece(ABC):
    @abstractmethod
    def possibleCaptures(self):
        pass
    
    def currentCaptures(self, board, line, col):
        return self.possibleCaptures(board, line, col, 1)
    
    def horizontalCaptures(board, line, col, place):
        positions = []
        size = len(board)
        
        for y in range(max(line-1, 0), -1, -1):
            if board[y][col] == place:
                positions += [[y, col]]
            elif board[y][col] == 0:
                continue
            else:
                break
            
        for y in range(min(line+1, size-1), size):
            if board[y][col] == place:
                positions += [[y, col]]
            elif board[y][col] == 0:
                continue
            else:
                break
        return positions
    
    def verticalCaptures(board, line, col, place):
        positions = []
        size = len(board)
        
        for x in range(max(col-1, 0), -1, -1):
            if board[line][x] == place:
                positions += [[line, x]]
            elif board[line][x] == 0:
                continue
            else:
                break
            
        for x in range(min(col+1, size-1), size): #len(board[line])
            if board[line][x] == place:
                positions += [[line, x]]
            elif board[line][x] == 0:
                continue
            else:
                break
            
        return sorted(positions)
    
    def obliqueCaptures(board, line, col, place):
        positions = []
        size = len(board)
          
        x = col
        for y in range(min(line+1, size-1), size):
            x += 1
            if x > size-1 or board[y][x] != place: 
                break
            else:
                positions += [[y, x]]
            
        x = col
        for y in range(min(line+1, size-1), size):
            x -= 1
            if x < 0 or board[y][x] != place: 
                break
            else:
                positions += [[y, x]]
            
        x = col
        for y in range(max(line-1, 0), -1, -1):
            x += 1
            if x > size-1 or board[y][x] != place: 
                break
            else:
                positions += [[y, x]]
            
        x = col
        for y in range(max(line-1, 0), -1, -1):
            x -= 1
            if x < 0 or board[y][x] != place: 
                break
            else:
                positions += [[y, x]]
        
        return sorted(positions)


class Tower(ChessPiece):
    
    def possibleCaptures(self, board, line, col, place=0):
        positions = []
        
        size = len(board)
        
        for x in range(max(col-1, 0), -1, -1):
            if board[line][x] == place:
                positions += [[line, x]]
            elif board[line][x] == 0:
                continue
            else:
                break
            
        for x in range(min(col+1, size-1), size): #len(board[line])
            if board[line][x] == place:
                positions += [[line, x]]
            elif board[line][x] == 0:
                continue
            else:
                break
        
        for y in range(max(line-1, 0), -1, -1):
            if board[y][col] == place:
                positions += [[y, col]]
            elif board[line][x] == 0:
                continue
            else:
                break
            
        for y in range(min(line+1, size-1), size):
            if board[y][col] == place:
                positions += [[y, col]]
            elif board[line][x] == 0:
                continue
            else:
                break
        
        return sorted(positions)

    
class Horse(ChessPiece):
    def possibleCaptures(self, board, line, col, place=0):
        positions = []
        size = len(board)
        
        if line+2 < size:
            if col+1 < size:
                if board[line+2][col+1] == place:
                    positions += [[line+2,col+1]]
            if col-1 >= 0:
                if board[line+2][col-1] == place:
                    positions += [[line+2, col-1]]
        if line-2 >= 0:
            if col+1 < size:
                if board[line-2][col+1] == place:
                    positions += [[line-2, col+1]]
            if col-1 >= 0:
                if board[line-2][col-1] == place:
                    positions += [[line-2, col-1]]
                    
        if col+2 < size:
            if line+1 < size:
                if board[line+1][col+2] == place:
                    positions += [[line+1, col+2]]
            if line-1 >= 0:
                if board[line-1][col+2] == place:
                    positions += [[line-1, col+2]]
                
        if col-2 >= 0:
            if line+1 < size:
                if board[line+1][col-2] == place:
                    positions += [[line+1, col-2]]
            if line-1 >= 0:
                if board[line-1][col-2] == place:
                    positions += [[line-1, col-2]]           
        
        return sorted(positions)

class Bishop(ChessPiece):
    
    def possibleCaptures(self, board, line, col, place=0):
        return super().obliqueCaptures(board, line, col, place)

class Queen(ChessPiece):
    
    def possibleCaptures(self, board, line, col, place=0):
        positions = super().obliqueCaptures(board, line, col, place)
        positions += super().verticalCaptures(board, line, col, place)
        positions += super().horizontalCaptures(board, line, col, place)
        return sorted(positions)

class King(ChessPiece):
    
    def possibleCaptures(self, board, line, col, place=0):
        size = len(board)
        positions = []
        
        for x in range(max(0,col-1), min(col+2, size)):
            if line >= 0 and board[line-1][x] == place:
                positions += [[line-1, x]] 
            if line < size-1 and board[line+1][x] == place:
                positions += [[line+1, x]] 
                
        if col < size-1 and board[line][col+1] == place:
                positions += [[line, col+1]]
        if col > 0 and board[line][col-1] == place:
                positions += [[line, col-1]]
                
        return sorted(positions)



def checkCaptures(board): # returns True if number of captures match among all chess pieces
    countCaptures = -1
    for y in range(len(board)):
        for x in range(len(board)):
            if isinstance(board[y][x], ChessPiece):
                elemCaptures = len(board[y][x].currentCaptures(board, y, x))
                if countCaptures == -1:
                    countCaptures = elemCaptures
                elif countCaptures != elemCaptures:
                    return False

    return True


def captureDiff(board):
    captures = {}
    for y in range(len(board)):
        for x in range(len(board)):
            if isinstance(board[y][x], ChessPiece):
                captures[(y, x)] = len(board[y][x].currentCaptures(board, y, x))
    return max(captures.values) - min(captures.values)

