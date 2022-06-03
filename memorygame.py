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

Card_count = 0
CardJ = 0
CardQ = 0
CardK = 0
CardJOKER = 0
CardA = 0
CardTWO = 0
CardTRES = 0
CardFOUR = 0

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if (Card_count < 3):
             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                 if event.ui_element == card1:
                     event.ui_element.set_text('jack')
                     Card_count += 1
                     CardJ += 1


             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                 if event.ui_element == card2:
                     event.ui_element.set_text("queen")
                     Card_count += 1
                     CardQ += 1


             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card3:
                    event.ui_element.set_text("king")
                    Card_count += 1
                    CardK += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card4:
                    event.ui_element.set_text("ace")
                    Card_count += 1
                    CardA += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card5:
                    event.ui_element.set_text("joker")
                    Card_count += 1
                    CardJOKER += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card6:
                    event.ui_element.set_text("two")
                    Card_count += 1
                    CardTWO += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card7:
                    event.ui_element.set_text("three")
                    Card_count += 1
                    CardTRES += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card8:
                    event.ui_element.set_text("four")
                    Card_count += 1
                    CardFOUR += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card9:
                    event.ui_element.set_text("jack")
                    Card_count += 1
                    CardJ += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card10:
                    event.ui_element.set_text("queen")
                    Card_count += 1
                    CardQ += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card11:
                    event.ui_element.set_text("king")
                    Card_count += 1
                    CardK += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card12:
                    event.ui_element.set_text("ace")
                    Card_count += 1
                    CardA += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card13:
                    event.ui_element.set_text("joker")
                    Card_count += 1
                    CardJOKER += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card14:
                    event.ui_element.set_text("two")
                    Card_count += 1
                    CardTWO += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card15:
                    event.ui_element.set_text("three")
                    Card_count += 1
                    CardTRES += 1

             if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == card16:
                    event.ui_element.set_text("four")
                    Card_count += 1
                    CardFOUR += 1




        else:
           print('no buttons closed')
           print("only two buttons allowed")
           card1.set_text('CLICK')
           card2.set_text('CLICK')
           card3.set_text('CLICK')
           card4.set_text('CLICK')
           card5.set_text('CLICK')
           card6.set_text('CLICK')
           card7.set_text('CLICK')
           card8.set_text('CLICK')
           card9.set_text('CLICK')
           card10.set_text('CLICK')
           card11.set_text('CLICK')
           card12.set_text('CLICK')
           card13.set_text('CLICK')
           card14.set_text('CLICK')
           card15.set_text('CLICK')
           card16.set_text('CLICK')

           Card_count = 0
            #only open two then close them both then set cardcount to 0


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

