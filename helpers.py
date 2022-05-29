import pygame as pg
import random


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

