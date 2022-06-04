import pygame as pg
import random

white = (255, 255, 255)
black = (0, 0, 0)
width, height = 1500, 800


def generate():
    '''
    Generate new list of values
    '''
    lst = set()

    while len(lst) < 1500:
        lst.add(random.uniform(1, 800))

    lst = list(lst)
    random.shuffle(lst)
    return lst


def update_rects(arr):
    '''
    Take in arr and generate pg.Rect() objects for it
    '''
    lst = list()

    for count, i in enumerate(arr):
        lst.append(pg.Rect((count*1, 800-i), (1, i)))

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


class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected=0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pg.Rect(0, 0, w, h)
        self.rect.center = (x, y)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pg.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pg.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pg.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center=rect.center))
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pg.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pg.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.selected
        return self.selected



