from operator import truediv
import pygame
from config import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT
import board

class Game:
    def __init__(self):
        self.board = board.ChessBoard()
    
    def setLevel(self,level):
        self.level = level
    
    def getLevel(self):
        return self.level
    
    def setPlayMode(self, mode):
        self.play_mode = mode
    
    def getPlayMode(self):
        return self.play_mode
    
    def getMove(self, ret_value):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if(ret_value):
                    return True

                if event.key == K_UP:
                    return('up')
                    
                if event.key == K_DOWN:
                    return('down')
                    
                    
                if event.key == K_RIGHT:
                    return('right')

                if event.key == K_LEFT:
                    return('left')
            
                if event.key == K_ESCAPE:
                    return False

            elif event.type == QUIT :
                return False
            
            
            
            
            
         
    
    