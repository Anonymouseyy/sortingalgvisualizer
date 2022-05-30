import pygame as pg
import sys
import time
from helpers import generate, update_rects, display_info, OptionBox

pg.init()
size = width, height = 1000, 600

# Colors
white = (255, 255, 255)
gray = (138, 135, 128)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

screen = pg.display.set_mode(size)
pg.display.set_caption('Sorting')

# Fonts
smallFont = pg.font.Font("Roboto-Black.ttf", 14)
mediumFont = pg.font.Font("Roboto-Black.ttf", 28)
largeFont = pg.font.Font("Roboto-Black.ttf", 40)

current_arr = generate()
current_rects = update_rects(current_arr)
sort_types = ["Bubble", "Insertion"]
st = None
sort_type = None
sorting = False
sort_options = OptionBox(width/2, 50, width/3-20, 85, white, gray, mediumFont, sort_types)


def draw_arr(rects, selected=[], end=False):
    '''
    Take in arr and draw the rectangles for it
    '''
    for count, rect in enumerate(rects):
        if count in selected:
            if not end:
                pg.draw.rect(screen, red, rect)
            else:
                pg.draw.rect(screen, green, rect)
        else:
            pg.draw.rect(screen, white, rect)


while True:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            sys.exit()

    screen.fill(black)
    draw_arr(current_rects)

    if not sorting:
        # Display generate button
        gen_button = pg.Rect(0, 0, width / 3, 80)
        gen_button.center = ((width / 3 - width / 6 + 10), 50)
        gen = mediumFont.render("Generate", True, black)
        gen_rect = gen.get_rect()
        gen_rect.center = gen_button.center
        pg.draw.rect(screen, white, gen_button)
        screen.blit(gen, gen_rect)

        # Display sort options
        sort_options.draw(screen)
        selected_option = sort_options.update(event_list)

        # Display sort button
        sort_button = pg.Rect(0, 0, width / 3, 80)
        sort_button.center = ((width - width / 6 - 10), 50)
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
                current_rects = update_rects(current_arr)
            elif sort_button.collidepoint(mouse):
                time.sleep(0.2)
                sorting = True
                st = time.time()
                sort_type = sort_types[selected_option]

    elif sorting:
        et = None
        if sort_type == "Bubble":
            for i in range(len(current_arr)-1):
                count = 0
                for j in range(len(current_arr)-i-1):
                    if current_arr[j] > current_arr[j+1]:
                        current_arr[j], current_arr[j+1] = current_arr[j+1], current_arr[j]
                        screen.fill(black)
                        current_rects = update_rects(current_arr)
                        draw_arr(current_rects, [j, j+1])
                        count += 1

                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            sys.exit()

                    text = display_info("Bubble", st, time.time(), smallFont)
                    screen.blit(text[0][0], text[0][1])
                    screen.blit(text[1][0], text[1][1])
                    pg.display.flip()

                if not count:
                    break

        elif sort_type == "Insertion":
            for i in range(1, len(current_arr)):
                key = current_arr[i]

                j = i-1
                while j >= 0 and key < current_arr[j]:
                    current_arr[j+1] = current_arr[j]
                    j -= 1

                    screen.fill(black)
                    current_rects = update_rects(current_arr)
                    draw_arr(current_rects, [j, i])

                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            sys.exit()

                    text = display_info("Insertion", st, time.time(), smallFont)
                    screen.blit(text[0][0], text[0][1])
                    screen.blit(text[1][0], text[1][1])
                    pg.display.flip()

                current_arr[j+1] = key

        et = time.time()
        text = display_info(sort_type, st, et, smallFont)

        for count, i in enumerate(current_arr):
            lst = [x for x in range(len(current_arr)) if x < i]
            screen.fill(black)
            screen.blit(text[0][0], text[0][1])
            screen.blit(text[1][0], text[1][1])
            current_rects = update_rects(current_arr)
            draw_arr(current_rects, lst, True)
            pg.display.flip()
            time.sleep(0.01)

        sorting = False
        sort_type = None
        st = None

    pg.display.flip()
