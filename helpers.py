import pygame as pg
import random


def generate():
    '''
    Generate new list of values
    '''
    lst = list()

    for i in range(160):
        lst.append(random.randint(1, 500))

    return random.shuffle(lst)


def update_rects(arr):
    '''
    Take in arr and generate pg.Rect() objects for it
    '''
    pass