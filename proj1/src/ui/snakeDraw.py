import pygame
from config import screen, green, little_green

class Snake:
    def __init__(self, square):
        self.square = square
    
    def paintSnake(self):
        surf = pygame.Surface(
                    (self.square.width_height, self.square.width_height))
        if self.square.is_white:
            #round cur pos
            # if(self.square.cur_pos == (self.square.y, self.square.x)):
            #     surf.fill(little_green)
            # else:
                surf.fill(little_green)
        else:
            # round cur pos
            # if(self.cur_pos == (self.square.y, self.square.x)):
            #     surf.fill(green)
            # else:
                surf.fill(green)

        screen.blit(surf, self.square.calculate_coordinates()) 

