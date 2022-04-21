import pygame

from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class BoardSquare:
    def __init__(self, x, y, is_white, value):
        self.x = x
        self.y = y
        self.width_height = SCREEN_WIDTH / 6
        self.is_white = is_white
        self.value = value

    def calculate_coordinates(self):
        width_height = self.width_height

        x_coordinate = self.x * width_height
        y_coordinate = self.y * width_height

        return (x_coordinate, y_coordinate)
    
    


class ChessBoard:
    def __init__(self, board):
        self.size = len(board)
        self.drawBoard(board)

    def drawBoard(self, board):
        is_white = False
        self.chess_board = []

        for y in range(self.size):
            row = board[y]
            chess_row = []
            is_white = not is_white
            for x in range(self.size):
                chess_row.append(BoardSquare(x, y, is_white, row[x]))
                is_white = not is_white
            self.chess_board.append(chess_row)

        for row in self.chess_board:

            for square in row:
                print(square.is_white, square.value)
                surf = pygame.Surface((square.width_height, square.width_height))


                if (square.value == 0):
                    if square.is_white:
                        surf.fill((255, 255, 255))
                    else:
                        surf.fill((0, 0, 0))
                elif (square.value == 1):
                    if square.is_white:
                        surf.fill((108, 187, 60))
                    else:
                        surf.fill((0, 128, 0))

                rect = surf.get_rect()
                screen.blit(surf, square.calculate_coordinates())
                pygame.display.flip()

        print(self.size)
    


board = ChessBoard([[0,0,0,0,0,1], [0,0,0,1,1,1], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]])
size = board.size

#     def get_square_for_position(self, pos):
#         for row in self.chess_board:  
#             if row[0].y_start < pos[1] < row[0].y_start + row[0].width_height:
#                 for square in row:
#                     if square.x_start < pos[0] < square.x_start + square.width_height:
#                         return square
#     def draw(self):

#         is_white = False
#         for y in range(8):
#             chess_row = []
#             is_white = not is_white
#             for x in range(8):
#                 chess_row.append(calculate_coordinates(x, y, is_white))
#                 is_white = not is_white
#             self.chess_board.append(chess_row)

#         for row in self.chess_board:
#             for square in row:
#                 surf = pygame.Surface((square.width_height, square.width_height))

#                 if square.is_white:
#                     surf.fill((255, 255, 255))
#                 else:
#                     surf.fill((0, 0, 0))

#                 rect = surf.get_rect()
#                 screen.blit(surf, (square.x_start, square.y_start))
#                 pygame.display.flip()


# def calculate_coordinates(x_array, y_array, is_white):
#     if SCREEN_WIDTH < SCREEN_HEIGHT or SCREEN_WIDTH == SCREEN_HEIGHT:
#         width_height = SCREEN_WIDTH / 8
#     else:
#         width_height = SCREEN_HEIGHT / 8

#     x_coordinate = x_array * width_height
#     y_coordinate = y_array * width_height

#     return BoardSquare(x_coordinate, y_coordinate, width_height, is_white)


# board = ChessBoard(5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print('1')
            if event.key == K_ESCAPE:
                print('2')
                running = False

        if event.type == MOUSEBUTTONUP:
            print('up')
            
        elif event.type == QUIT:
            print('4')
            running = False
