from json.tool import main
from click import option
import pygame
from config import screen, screen_width, font, black, green, yellow, white, text_format, clock, FPS


def menu_algorithms():
    pass

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
                        idx_selected = 0
                    selected = options[idx_selected]
                elif event.key == pygame.K_DOWN:
                    idx_selected += 1
                    if(idx_selected > len(options) - 1): 
                        idx_selected = len(options) - 1
                    selected = options[idx_selected]
                if event.key == pygame.K_RETURN:
                    if selected == "player":
                        return ("player", level)
                    if selected == "computer":
                        menu_algorithms()
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
                        idx_selected = 0
                    selected = options[idx_selected]
                elif event.key == pygame.K_DOWN:
                    idx_selected += 1
                    if(idx_selected > len(options) - 1): 
                        idx_selected = len(options) - 1
                    selected = options[idx_selected]
                if event.key == pygame.K_RETURN:
                    if selected == "play":
                        level = 1
                        return menu_player(level)
                    if selected == "choose_level":
                        return("Choose Level")
                    if selected == "quit":
                        pygame.quit()
                        quit()

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

