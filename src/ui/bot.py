import pygame
from board import ChessBoard
import time

class Bot:
    def __init__(self, path, board):
        self.path = path
        self.board = board
    
    def drawPath(self):
        draw_board = ChessBoard()
        for pos in self.path:
            for y in range(len(self.board)):
                for x in range(len(self.board)):
                    if y == pos.posY and x == pos.posX:
                        self.board[y][x] = 1
                        draw_board.update(self.board,(y,x))
                        time.sleep(0.2)

