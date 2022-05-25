import pygame as pg
import sys
import time
from helpers import generate

pg.init()
size = width, height = 1000, 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen = pg.display.set_mode(size)
pg.display.set_caption('Sorting')

# Fonts
mediumFont = pg.font.Font("Roboto-Black.ttf", 28)
largeFont = pg.font.Font("Roboto-Black.ttf", 40)

current_arr = generate()
current_rects = list()


def draw_arr(arr):
    '''
    Take in arr and draw the rectangles for it
    '''
    for count, l in enumerate(arr):
        pass


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill(black)

    # Display generate button
    gen_button = pg.Rect(0, 0, width / 3, 80)
    gen_button.center = ((width / 3 - width / 6 + 10), 50)
    gen = mediumFont.render("Generate", True, black)
    gen_rect = gen.get_rect()
    gen_rect.center = gen_button.center
    pg.draw.rect(screen, white, gen_button)
    screen.blit(gen, gen_rect)

    click, _, _ = pg.mouse.get_pressed()
    if click == 1:
        mouse = pg.mouse.get_pos()
        if gen_button.collidepoint(mouse):
            time.sleep(0.2)
            current_arr = generate()

    pg.display.flip()
