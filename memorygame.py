#Martins memory game
import pygame
import pygame_gui
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
grey = (80,80,80)
Width = 800
Height = 600
pygame.display.set_caption('Memory game')
screen = pygame.display.set_mode((Width, Height))
manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()
screen.fill(black)

font = pygame.font.SysFont('arial', 40)
title = font.render('Memory Game', True, white)
box = title.get_rect(midtop = (Width // 2,10))
screen.blit(title,box)

JACK = 'jack'
QUEEN ='queen'
KING ='king'
ACE ='ace'
JOKER ='joker'

all_cards= (JACK, QUEEN, KING, ACE, JOKER)

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()
    manager.update(time_delta)

pygame.quit()
