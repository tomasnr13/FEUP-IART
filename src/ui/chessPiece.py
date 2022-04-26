import pygame
from abc import ABC, abstractmethod
from config import screen

class ChessPiece(ABC):
    def __init__(self, square):
        self.square = square

    @abstractmethod
    def setImage(self, image):
        pass

    def displayPiece(self):
        image = pygame.image.load(self.image)
        image = pygame.transform.scale(image, (self.square.width_height, self.square.width_height))
        screen.blit(image, self.square.calculate_coordinates())

class Tower(ChessPiece):
    def __init__(self, square):
        super().__init__(square)
        self.setImage()

    def setImage(self):
        self.image = r'images/towerPiece.png'

class Hourse(ChessPiece):
    def __init__(self, square):
        super().__init__(square)
        self.setImage()

    def setImage(self):
        self.image = r'images/horsePiece.png'

class Bishop(ChessPiece):
    def __init__(self, square):
        super().__init__(square)
        self.setImage()

    def setImage(self):
        self.image = r'images/bishopPiece.png'

class King(ChessPiece):
    def __init__(self, square):
        super().__init__(square)
        self.setImage()

    def setImage(self):
        self.image = r'images/kingPiece.png'

class Queen(ChessPiece):
    def __init__(self, square):
        super().__init__(square)
        self.setImage()

    def setImage(self):
        self.image = r'images/queenPiece.png'