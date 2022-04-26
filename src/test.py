import pygame
 
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
 
pygame.init()
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class BoardSquare:
    def __init__(self, x_start, y_start, width_height, is_white):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.is_white = is_white

def calculate_coordinates(x_array, y_array, is_white):
    if SCREEN_WIDTH < SCREEN_HEIGHT or SCREEN_WIDTH == SCREEN_HEIGHT:
        width_height = SCREEN_WIDTH / 4
    else:
        width_height = SCREEN_HEIGHT / 4
 
    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height
 
    return BoardSquare(x_coordinate, y_coordinate, width_height, is_white)

chess_board = []
is_white = False
for y in range(8):
    chess_row = []
    is_white = not is_white
    for x in range(8):
        chess_row.append(calculate_coordinates(x, y, is_white))
        is_white = not is_white
    chess_board.append(chess_row)   


for row in chess_board:
    for square in row:
        surf = pygame.Surface((square.width_height, square.width_height))
        print((square.width_height, square.width_height))
 
        if square.is_white:
            surf.fill((255, 255, 255))
        else:
            surf.fill((0, 0, 0))
 
        rect = surf.get_rect()
        print(square.x_start, square.y_start)
        screen.blit(surf, (square.x_start, square.y_start))
        pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
 
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        elif event.type == QUIT:
            running = False

