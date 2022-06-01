# Martins memory game
import pygame
import pygame_gui
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (80, 80, 80)
Width = 800
Height = 600
pygame.display.set_caption('Memory game 1')
screen = pygame.display.set_mode((Width, Height))
background = pygame.Surface((Width, Height))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()
screen.fill(black)

font = pygame.font.SysFont('arial', 40)
title = font.render('Memory Game', True, white)
box = title.get_rect(midtop=(Width // 2, 5))
screen.blit(title, box)


card1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((55, 100), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((255, 100), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((455, 100), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((655, 100), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((55, 220), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((255, 220), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card7 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((455, 220), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card8 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((655, 220), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card9 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((55, 340), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card10 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((255, 340), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card11 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((455, 340), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card12 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((655, 340), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card13 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((55, 460), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card14 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((255, 460), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card15 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((455, 460), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
card16 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((655, 460), (100, 100)),
                                            text='CLICK',
                                            manager=manager)
JACK = 'jack'

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card1:
                pygame.time.wait(3000)
                event.ui_element.set_text(JACK)
                if event.ui_element == card1:
                    event.ui_element.set_text('click')


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card2:
                event.ui_element.set_text("queen")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card3:
                event.ui_element.set_text("king")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card4:
                event.ui_element.set_text("ace")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card5:
                event.ui_element.set_text("joker")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card6:
                event.ui_element.set_text("two")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card7:
                event.ui_element.set_text("three")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card8:
                event.ui_element.set_text("four")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card9:
                event.ui_element.set_text("jack")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card10:
                event.ui_element.set_text("queen")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card11:
                event.ui_element.set_text("king")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card12:
                event.ui_element.set_text("ace")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card13:
                event.ui_element.set_text("joker")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card14:
                event.ui_element.set_text("two")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card15:
                event.ui_element.set_text("three")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card16:
                event.ui_element.set_text("four")

        manager.process_events(event)

    pygame.display.update()
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    screen.blit(title, box)
    manager.draw_ui(screen)

    pygame.display.update()
    screen.blit(background, (0, 0))
    screen.blit(title, box)
    manager.draw_ui(screen)

pygame.display.update()

pygame.quit()
