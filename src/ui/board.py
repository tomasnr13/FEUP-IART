import pygame
import snakeDraw
from config import screen, screen_width, white, black, little_green, green
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'src'))
import chess
import chessPiece

class BoardSquare:
    def __init__(self, x, y, is_white, value):
        self.x = x
        self.y = y
        self.width_height = screen_width / 6
        self.is_white = is_white
        self.value = value

    def calculate_coordinates(self):
        width_height = self.width_height

        x_coordinate = self.x * width_height
        y_coordinate = self.y * width_height

        return (x_coordinate, y_coordinate)

class ChessBoard:
    
    def update(self, board, cur_pos):
        self.size = len(board)
        self.draw(board)
        self.cur_pos = cur_pos

    def setCurPos(self, pos):
        self.cur_pos = pos

    def setMove(self, move):
        self.move = move
    
    def getMove(self):
        return self.move

    def paint(self, square):
        surf = pygame.Surface(
                    (square.width_height, square.width_height))

        if square.is_white:
            surf.fill(white)
        else:
            surf.fill(black)
        screen.blit(surf, square.calculate_coordinates())

    def draw(self, board):
        self.size = len(board)
        is_white = False
        self.chess_board = []
        print(self.size, 'size')
        for y in range(self.size):
            if(self.size % 2 == 0):
                is_white = not is_white
            row = board[y]
            chess_row = []
            # if the number of squares per row is even, it's necessary to change the color at the beginning of each row
            
            for x in range(self.size):
                chess_row.append(BoardSquare(x, y, is_white, row[x]))
                is_white = not is_white
            self.chess_board.append(chess_row)

        for row in self.chess_board:
            for square in row:
                self.paint(square)

                # if(square.value == 1):
                #     snake = snakeDraw.Snake(square)
                #     snake.paintSnake()

                if (isinstance(square.value, chess.ChessPiece)):
                    piece = None
                    if (isinstance(square.value, chess.Tower)):
                        piece = chessPiece.Tower(square)
                    elif (isinstance(square.value, chess.Horse)):
                        piece = chessPiece.Hourse(square)
                    elif (isinstance(square.value, chess.King)):
                        piece = chessPiece.King(square)
                    elif (isinstance(square.value, chess.Queen)):
                        piece = chessPiece.Queen(square)
                    elif (isinstance(square.value, chess.Bishop)):
                        piece = chessPiece.Bishop(square)
                    piece.displayPiece()    

                pygame.display.flip()
