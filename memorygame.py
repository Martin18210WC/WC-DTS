# Martins memory game
import pygame
import pygame_gui
import random

pygame.init()

#colors and window size
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
gray = (128, 128, 128)
width = 450
height = 600


timer = pygame.time.Clock()

#board layout
rows = 6
cols = 6

correct = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
#other variables
options_list = []
spaces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0
game_over = False

# screen and font sizes
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Memory Game")
title_font = pygame.font.SysFont('arial', 60)
small_font = pygame.font.SysFont('arial', 30)
restart_font = pygame.font.SysFont('arial', 50)
winner_font = pygame.font.SysFont('arial', 40)

#define draw background function
def draw_backgrounds():
    top_menu = pygame.draw.rect(screen, blue, [0, 0, width, 100])
    title_text = title_font.render('Memory Game', True, white)
    screen.blit(title_text, (65, 15))
    board_space = pygame.draw.rect(screen, gray, [0, 100, width, height - 200])
    bottom_menu = pygame.draw.rect(screen, blue, [0, height - 100, width, 100])
    restart_button = pygame.draw.rect(screen, gray, [10, height - 90, 150, 80], 0, 5)
    restart_text = restart_font.render('Restart', True, white)
    screen.blit(restart_text, (10, 520))
    score_text = small_font.render(f'Current Turns: {score}', True, white)
    screen.blit(score_text, (250, 520))
    best_text = small_font.render(f'High Score: {best_score}', True, white)
    screen.blit(best_text, (250, 560))
    return restart_button

#define generate memory board function
def generate_board():
    global options_list
    global spaces
    global used
    for item in range(rows * cols // 2):
        options_list.append(item)

    for item in range(rows * cols):
        piece = options_list[random.randint(0, len(options_list)-1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)

# define draw board function
def draw_board():
    global rows
    global cols
    global correct
    board_list = []
    for y in range(cols):
        for x in range(rows):
            piece = pygame.draw.rect(screen, white, [y * 75 + 12, x * 65 + 112, 50, 50], 0, 4)
            board_list.append(piece)



    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, green, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)
                piece_text = small_font.render(f'{spaces[c * rows + r]}', True, black)
                screen.blit(piece_text, (c * 75 + 18, r * 65 + 120))
    return board_list

#define guess checking function
def check_guesses(first, second):
    global spaces
    global correct
    global score
    global matches
    if spaces[first] == spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 = first - (col1 * rows)
        row2 = second - (col2 * rows)
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1

    else:
        score += 1

#main function
running = True
while running:
    timer.tick(60)/1000.0 #FPS
    screen.fill(white)
#board
    if new_board:
        generate_board()
        new_board = False

    restart = draw_backgrounds()
    board = draw_board()

#guesses
    if first_guess and second_guess:
        check_guesses(first_guess_num, second_guess_num)
        pygame.time.delay(1000)
        first_guess = False
        second_guess = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #to leave (X on the top right)
            running = False
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if not game_over:
                   if button.collidepoint(event.pos) and not first_guess:
                       first_guess = True
                       first_guess_num = i
                   if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
            if restart.collidepoint(event.pos):
                options_list = []
                used = []
                spaces = []
                new_board = True
                score = 0
                matches = 0
                first_guess = False
                second_guess = False
                correct = [[0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0]]
                game_over = False
#game over
    if matches == rows * cols // 2:
        game_over = True
        winner = pygame.draw.rect(screen, gray, [10, HEIGHT - 300, WIDTH - 20, 80], 0, 5)
        winner_text = winner_font.render(f'YOU WIN SCORE: {score} TURNS', True, blue)
        screen.blit(winner_text, (10, HEIGHT - 290))
        if best_score > score or best_score == 0:
            best_score = score


    if first_guess:
        piece_text = small_font.render(f'{spaces[first_guess_num]}', True, blue)
        location = (first_guess_num // rows * 75 + 18, (first_guess_num - (first_guess_num // rows * rows)) * 65 + 120)
        screen.blit(piece_text, (location))

    if second_guess:
        piece_text = small_font.render(f'{spaces[second_guess_num]}', True, blue)
        location = (second_guess_num // rows * 75 + 18, (second_guess_num - (second_guess_num // rows * rows)) * 65 + 120)
        screen.blit(piece_text, (location))


    pygame.display.flip()
pygame.quit()
