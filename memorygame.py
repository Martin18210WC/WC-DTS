import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('memory game')
window_surface = pygame.display.set_mode((600 , 600))

background = pygame.Surface((600, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

card1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 50), (100, 100)),
                                            text='click',
                                            manager=manager)
card2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 50), (100, 100)),
                                            text='click',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card1:
                print("clicked")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == card2:
                print("clicked")


        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
