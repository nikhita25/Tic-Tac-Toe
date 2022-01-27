import pygame, sys
import numpy as np 
import AI_Module as AI
from game import Pause_Menu
pygame.init()

#Constants
WIDTH = 600
HEIGHT = 600


#Colors
MENU_BG_COLOR = (0,0,0)
BG_COLOR = (28,170,156)
color = (255,255,255)
LINE_COLOR = (23,145, 135)
C_COLOR = (255,0,0)
X_COLOR = (0,0,255)

#menu for displaying stuff
def menu(screen):
    smallfont = pygame.font.SysFont('Corbel',35)
    quit1 = smallfont.render('Quit' , True , color)
    single = smallfont.render('Single' , True , color)
    multi = smallfont.render('Multi' , True , color)
    Title = smallfont.render('TIC TAC TOE' , True , color)
    #buttons to click on
    button = pygame.Rect(250, 150, 100, 50)
    button1 = pygame.Rect(250, 250, 100, 50)
    button2 = pygame.Rect(250, 350, 100, 50)
    
    while True:

        screen.fill((28,170,156))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if a mouse hits a button's hitbox we return a value based on button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    return 0
                if button1.collidepoint(mouse_pos):
                    return 1
                if button2.collidepoint(mouse_pos):
                    return 2
        #draw buttons and text
        pygame.draw.rect(screen, [255, 0, 0], button)
        pygame.draw.rect(screen, [255, 0, 0], button1)
        pygame.draw.rect(screen, [255, 0, 0], button2)
        screen.blit(single , (250,150)) 
        screen.blit(multi , (250,250)) 
        screen.blit(quit1 , (250,350))
        screen.blit(Title , (215,50))
        pygame.display.update()
def main():
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("TIC TAC TOE")
    scene = -1
    #cycles though menu and the actual game
    while True:
        if scene == -1:
            scene = menu(screen)
        elif scene == 0:
            scene = Pause_Menu(screen,0)
        elif scene == 1:
            scene = Pause_Menu(screen,1)
        elif scene == 2:
            pygame.quit()
            sys.exit()
main()
