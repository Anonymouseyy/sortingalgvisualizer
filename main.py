import pygame as pg
import sys
import time
from helpers import generate, update_rects

pg.init()
size = width, height = 1000, 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

screen = pg.display.set_mode(size)
pg.display.set_caption('Sorting')

# Fonts
mediumFont = pg.font.Font("Roboto-Black.ttf", 28)
largeFont = pg.font.Font("Roboto-Black.ttf", 40)

current_arr = generate()
sorting = False


def draw_arr(arr, selected=[], end=False):
    '''
    Take in arr and draw the rectangles for it
    '''
    rects = update_rects(arr)

    for count, rect in enumerate(rects):
        if count in selected:
            if not end:
                pg.draw.rect(screen, red, rect)
            else:
                pg.draw.rect(screen, green, rect)
        else:
            pg.draw.rect(screen, white, rect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill(black)

    if not sorting:
        # Display generate button
        gen_button = pg.Rect(0, 0, width / 3, 80)
        gen_button.center = ((width / 3 - width / 6 + 10), 50)
        gen = mediumFont.render("Generate", True, black)
        gen_rect = gen.get_rect()
        gen_rect.center = gen_button.center
        pg.draw.rect(screen, white, gen_button)
        screen.blit(gen, gen_rect)

        # Display sort button
        sort_button = pg.Rect(0, 0, width / 3, 80)
        sort_button.center = ((width-width/6-10), 50)
        sort = mediumFont.render("Sort", True, black)
        sort_rect = sort.get_rect()
        sort_rect.center = sort_button.center
        pg.draw.rect(screen, white, sort_button)
        screen.blit(sort, sort_rect)

        click, _, _ = pg.mouse.get_pressed()
        if click == 1:
            mouse = pg.mouse.get_pos()
            if gen_button.collidepoint(mouse):
                time.sleep(0.2)
                current_arr = generate()
            elif sort_button.collidepoint(mouse):
                time.sleep(0.2)
                sorting = True

    elif sorting:
        for i in range(len(current_arr)-1):
            count = 0
            for j in range(len(current_arr)-i-1):
                if current_arr[j] > current_arr[j+1]:
                    current_arr[j], current_arr[j+1] = current_arr[j+1], current_arr[j]
                    screen.fill(black)
                    draw_arr(current_arr, [j, j+1])
                    pg.display.flip()
                    count += 1

            if not count:
                break

        for count, i in enumerate(current_arr):
            lst = [x for x in range(len(current_arr)) if x < i]
            screen.fill(black)
            draw_arr(current_arr, lst, True)
            pg.display.flip()
            time.sleep(0.01)

        sorting = False

    draw_arr(current_arr)
    pg.display.flip()
