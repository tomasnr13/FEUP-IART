from curses import KEY_F0
import pygame

from pygame.locals import (
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from chess import Tower, Queen, Bishop, King, Horse


pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class BoardSquare:
    def __init__(self, x, y, is_white, value):
        self.x = x
        self.y = y
        self.width_height = SCREEN_WIDTH / 5
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
    
    def updateBoard(self, board):
        self.size = len(board)
        self.drawBoard(board)
    
    def setMove(self, move):
        self.move = move
    
    def getMove(self):
        return self.move

    def drawBoard(self, board):
        is_white = False
        self.chess_board = []

        for y in range(self.size):
            row = board[y]
            chess_row = []
            # if the number of squares per row is even, it's necessary to change the color at the beginning of each row
            if(self.size // 2 == 0):
                is_white = not is_white
            for x in range(self.size):
                chess_row.append(BoardSquare(x, y, is_white, row[x]))
                is_white = not is_white
            self.chess_board.append(chess_row)

        for row in self.chess_board:
            for square in row:
                surf = pygame.Surface(
                    (square.width_height, square.width_height))

                if square.is_white:
                    surf.fill((255, 255, 255))
                else:
                    surf.fill((0, 0, 0))
                screen.blit(surf, square.calculate_coordinates())

                if (square.value == 1):
                    if square.is_white:
                        surf.fill((108, 187, 60))
                    else:
                        surf.fill((0, 128, 0))

                    screen.blit(surf, square.calculate_coordinates())

                elif (isinstance(square.value, Tower)):
                    image = pygame.image.load(r'images/towerPiece.png')
                    image = pygame.transform.scale(image, (square.width_height, square.width_height))
                    screen.blit(image, square.calculate_coordinates())

                elif (isinstance(square.value, Bishop)):
                    image = pygame.image.load(r'images/bishopPiece.png')
                    image = pygame.transform.scale(image, (square.width_height, square.width_height))
                    screen.blit(image, square.calculate_coordinates())

                elif (isinstance(square.value, Queen)):
                    image = pygame.image.load(r'images/queenPiece.png')
                    image = pygame.transform.scale(image, (square.width_height, square.width_height))
                    screen.blit(image, square.calculate_coordinates())

                elif (isinstance(square.value, King)):
                    image = pygame.image.load(r'images/kingPiece.png')
                    image = pygame.transform.scale(image, (square.width_height, square.width_height))
                    screen.blit(image, square.calculate_coordinates())

                elif (isinstance(square.value, Horse)):
                    image = pygame.image.load(r'images/horsePiece.png')
                    image = pygame.transform.scale(image, (square.width_height, square.width_height))
                    screen.blit(image, square.calculate_coordinates())

                pygame.display.flip()

b = ChessBoard([])

def getMove():
    print(b.getMove())
    return b.getMove()

def draw(board):
    b.updateBoard(board)
    size = b.size

    running = True
    while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_UP:
                        b.setMove('up')
                        print('up')
                        return

                    if event.key == K_DOWN:
                        b.setMove('down')
                        print('down')
                        return
                        
                    if event.key == K_RIGHT:
                        b.setMove('right')
                        print('right')
                        return

                    if event.key == K_LEFT:
                        b.setMove('left')
                        print('left')
                        return

                elif event.type == QUIT or event.type == K_ESCAPE:
                    running = False
