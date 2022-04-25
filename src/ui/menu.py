from json.tool import main
from click import option
from os import path
import pygame
from config import screen, screen_width, font, black, green, yellow, white, text_format, clock, FPS

def menu_level():
    menu = True
    options = ["1","2","3","4","5","6","7", "BACK TO MENU"]
    selected = "1"
    idx_selected = 0

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    idx_selected -= 1
                    if(idx_selected < 0): 
                        idx_selected = 0
                    selected = options[idx_selected]
                elif event.key == pygame.K_RIGHT:
                    idx_selected += 1
                    if(idx_selected > len(options) - 1): 
                        idx_selected = len(options) - 1
                    selected = options[idx_selected]
                if event.key == pygame.K_RETURN:
                    if selected in options:
                        if selected == "BACK TO MENU":
                            return None
                        return menu_player(selected)
                    
    
        # Main Menu UI
        screen.fill(green)
        title = text_format("Chess Snake Puzzle", font, 90, yellow)

        for opt in options:
            if selected == opt:
                text_start = text_format(opt, font, 75, white)
                start_rect = text_start.get_rect()
                screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 200))

                if opt != "BACK TO MENU":
                    file = path.join('images', 'imgLevel'+opt+'.png')
                    image = pygame.image.load(file)
                    image = pygame.transform.scale(image, (300,300))
                    screen.blit(image, (screen_width/3 - (start_rect[2]), 250))
                
        

        title_rect = title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(
            "Choose Player Menu")

    

def menu_algorithms(level):
    menu = True
    options = ["breadth first search", "depth first search", "uniform cost", "iterative deepening","greedy", "a star", "BACK TO MENU" ]
    selected = "breadth first search"
    idx_selected = 0

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    idx_selected -= 1
                    if(idx_selected < 0): 
                        idx_selected = len(options) - 1
                    selected = options[idx_selected]
                elif event.key == pygame.K_DOWN:
                    idx_selected += 1
                    if(idx_selected > len(options) - 1): 
                        idx_selected = 0
                    selected = options[idx_selected]
                if event.key == pygame.K_RETURN:
                    if selected in options:
                        if selected == "BACK TO MENU":
                            return None
                        return (selected, level)
                    
    
        # Main Menu UI
        screen.fill(green)
        title = text_format("Chess Snake Puzzle", font, 90, yellow)
        size = 0
        for opt in options:
            size += 50
            if selected == opt:
                text_start = text_format(opt, font, 75, white)
            else:
                text_start = text_format(opt, font, 75, black)
            start_rect = text_start.get_rect()
            screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 150+size))

        title_rect = title.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(
            "Choose Player Menu")


def menu_player(level):

    menu = True
    options = ["player", "computer", "go_back"]
    selected = "player"
    idx_selected = 0

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    idx_selected -= 1
                    if(idx_selected < 0): 
                        idx_selected = len(options) - 1
                    selected = options[idx_selected]
                elif event.key == pygame.K_DOWN:
                    idx_selected += 1
                    if(idx_selected > len(options) - 1): 
                        idx_selected = 0
                    selected = options[idx_selected]
                if event.key == pygame.K_RETURN:
                    if selected == "player":
                        return ("player", level)
                    if selected == "computer":
                        return menu_algorithms(level)
                    if selected == "go_back":
                        return None
    
        # Main Menu UI
        screen.fill(green)
        title = text_format("Chess Snake Puzzle", font, 90, yellow)
        if selected == "player":
            text_start = text_format("PLAYER", font, 75, white)
        else:
            text_start = text_format("PLAYER", font, 75, black)
        if selected == "computer":
            text_level = text_format("COMPUTER", font, 75, white)
        else:
            text_level = text_format("COMPUTER", font, 75, black)
        if selected == "go_back":
            text_quit = text_format("BACK TO MENU", font, 75, white)
        else:
            text_quit = text_format("BACK TO MENU", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        level_rect = text_level.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 250))
        screen.blit(text_level, (screen_width/2 - (level_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 350))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(
            "Choose Player Menu")

def main_menu():
    level = 0
    menu = True
    result = None
    options = ["play", "choose_level", "quit"]
    selected = "play"
    idx_selected = 0

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    idx_selected -= 1
                    if(idx_selected < 0): 
                        idx_selected = len(options) - 1
                    selected = options[idx_selected]
                elif event.key == pygame.K_DOWN:
                    idx_selected += 1
                    if(idx_selected > len(options) - 1): 
                        idx_selected = 0
                    selected = options[idx_selected]
                if event.key == pygame.K_RETURN:
                    if selected == "play":
                        level = 1
                        result = menu_player(level)
                    if selected == "choose_level":
                        result = menu_level()
                    if selected == "quit":
                        pygame.quit()
                        quit()
        
        if result is not None:
            return result

        # Main Menu UI
        screen.fill(green)
        title = text_format("Chess Snake Puzzle", font, 90, yellow)
        if selected == "play":
            text_start = text_format("PLAY", font, 75, white)
        else:
            text_start = text_format("PLAY", font, 75, black)
        if selected == "choose_level":
            text_level = text_format("CHOOSE LEVEL", font, 75, white)
        else:
            text_level = text_format("CHOOSE LEVEL", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        level_rect = text_level.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 250))
        screen.blit(text_level, (screen_width/2 - (level_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 350))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption(
            "Main Menu")

