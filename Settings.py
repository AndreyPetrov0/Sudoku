import pygame as pg
import sys, os
from pygame.locals import *
from Create_Sudoku import *
from Solving_Sudoku import *
from Validate_Sudoku import *


## Editable configuration block
difficulty_level = 6


s = {}
rs = {}
d = {}
rd = {}
buttons = []
but_func = {"Решение": "solution", "Заполненное": "complete", "Новое судоку": "new", "Стереть всё": "clear"}


pg.init()
default_font = pg.font.get_default_font()


## Screen block
display_size = pg.display.Info().current_w, pg.display.Info().current_h
screen = pg.display.set_mode(display_size, FULLSCREEN)
scr_width, scr_height = pg.display.get_surface().get_size()

a_fingers = 0


## Sudoku size block
board_size = round(scr_width * 0.9)
board_start = (scr_width - board_size) // 2
board_start_top = 60
wide_line = board_size // 60
narrow_line = board_size // 120
narrow_set = '012234456'

all_outer_colors = {"default": "aqua", False: "red", True: "green"}
outer_color = all_outer_colors.get("default", "black")
outer_line = wide_line * 2
outer_len_h = board_size + outer_line * 2
outer_h1 = (
				board_start - outer_line,
				board_start_top - outer_line
				)
outer_h2 = (
				board_start - outer_line,
				board_start_top + board_size
				)
outer_v1 = (
				board_start - outer_line,
				board_start_top
				)
outer_v2 = (
				board_start + board_size,
				board_start_top
				)


tile_size = round((board_size - 4 * wide_line - 6 * narrow_line) / 9)
dial_size = round((board_size - 4 * wide_line) / 5)
dial_start = round(board_size * 1.2)

dial_font = pg.font.Font(default_font, round(dial_size * 0.8))
dial_font_height = dial_font.metrics("0")[0][-2]

button_font = pg.font.Font(default_font, round(tile_size * 0.8))
button_font_height = button_font.metrics("0")[0][-2]


## Rect position block
board_rect = pg.rect.Rect(0, 0, board_size, board_size)
board_surf = pg.surface.Surface((board_size, board_size), 0, screen)

outer_h_rect = pg.rect.Rect(0, 0, outer_len_h, outer_line)
outer_h_surf = pg.surface.Surface((outer_len_h, outer_line), 0, screen)

outer_v_rect = pg.rect.Rect(0, 0, outer_line, board_size)
outer_v_surf = pg.surface.Surface((outer_line, board_size), 0, screen)

tile_rect = pg.rect.Rect(0, 0, tile_size, tile_size)
tile_surf = pg.surface.Surface((tile_size, tile_size), 0, board_surf)

dial_rect = pg.rect.Rect(0, 0, dial_size, dial_size)
dial_surf = pg.surface.Surface((dial_size, dial_size), 0, screen)


## Buttons block
font_scale = 0.7
buttons_height = max((board_size * 0.12, scr_height // 22))
blank_space = buttons_height // 3
buttons_starts = round((dial_start + dial_size * 2 + wide_line) * 1.06)
STEP = round(buttons_height * 1.3)

buttons_font = pg.font.Font(default_font, round(buttons_height * font_scale))
buttons_width = blank_space + sum(c[-1] for c in buttons_font.metrics(max(but_func, key=len)))
buttons_size = buttons_width, buttons_height
