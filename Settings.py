import pygame as pg
import sys, os
from pygame.locals import *


s = {}
rs = {}
d = {}
rd = {}
buttons = []
but_func = {"Решение": "solution"}


pg.init()
default_font = pg.font.get_default_font()


## Screen block
display_size = pg.display.Info().current_w, pg.display.Info().current_h
screen = pg.display.set_mode(display_size, FULLSCREEN)
scr_width, scr_height = pg.display.get_surface().get_size()

a_fingers = 0


## Sudoku size block
board_size = 600
board_start = (scr_width - board_size) // 2
wide_line = 10
narrow_line = 5
narrow_set = '012234456'

tile_size = round((board_size - 4 * wide_line - 6 * narrow_line) / 9)
dial_size = round((board_size - 4 * wide_line) / 5)
dial_start = 150 + board_size

dial_font = pg.font.Font(default_font, round(dial_size * 0.8))
dial_font_height = dial_font.metrics("0")[0][-2]

button_font = pg.font.Font(default_font, round(tile_size * 0.8))
button_font_height = button_font.metrics("0")[0][-2]


## Rect position block
board_rect = pg.rect.Rect(0, 0, board_size, board_size)
board_surf = pg.surface.Surface((board_size, board_size), 0, screen)

tile_rect = pg.rect.Rect(0, 0, tile_size, tile_size)
tile_surf = pg.surface.Surface((tile_size, tile_size), 0, board_surf)

dial_rect = pg.rect.Rect(0, 0, dial_size, dial_size)
dial_surf = pg.surface.Surface((dial_size, dial_size), 0, screen)


## Buttons block
solving_button_size = (solving_button_width := 400,
solving_button_height := 100)
