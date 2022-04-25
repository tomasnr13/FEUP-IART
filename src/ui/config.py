import pygame
import os
from pygame.locals import (
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Game Initialization
pygame.init()
    
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
    
# Game Resolution
screen_width=700
screen_height=700
screen=pygame.display.set_mode((screen_width, screen_height))
    
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(None, textSize)
    newText=newFont.render(message, 0, textColor)
    
    return newText
    
    
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 128, 0)
little_green = (108, 187, 60)
blue=(0, 0, 255)
yellow=(255, 255, 0)
    
# Game Fonts
font = pygame.font.SysFont('Helvetica', 20)
    
    
# Game Framerate
clock = pygame.time.Clock()
FPS=30
