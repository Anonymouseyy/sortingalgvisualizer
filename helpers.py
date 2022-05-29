import pygame as pg
import random

white = (255, 255, 255)
black = (0, 0, 0)
width, height = 1000, 600


def generate():
    '''
    Generate new list of values
    '''
    lst = set()

    while len(lst) < 200:
        lst.add(random.randint(1, 500))

    lst = list(lst)
    random.shuffle(lst)
    return lst


def update_rects(arr):
    '''
    Take in arr and generate pg.Rect() objects for it
    '''
    lst = list()

    for count, i in enumerate(arr):
        lst.append(pg.Rect((count*5, 600-i), (4, i)))

    return lst


def display_info(sort_type, st, ct, font):
    tsort = font.render(f"Sort Type: {sort_type}", True, white, black)
    tsort_rect = tsort.get_rect()
    tsort_rect.left = 10
    tsort_rect.top = 5

    run_time = font.render(f"Run Time: {int((ct-st)*1000)}ms", True, white, black)
    run_time_rect = run_time.get_rect()
    run_time_rect.left = tsort_rect.right + 10
    run_time_rect.top = 5

    return [[tsort, tsort_rect], [run_time, run_time_rect]]



