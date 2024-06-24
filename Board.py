import pygame as pg
import sys, os
import android
from pygame._sdl2 import touch
from Create_Sudoku import *
from Solving_Sudoku import *
from Validate_Sudoku import *
from Classes import *
from Functions import *
from Settings import *


pg.init()


touch_scr = touch.get_num_devices()
device = touch.get_device(touch_scr - 1)

clock = pg.time.Clock()
empty_board = Solving_sudoku().empty_sudoku
complete_sudoku = Create_sudoku().create()
running = True

pg.draw.rect(board_surf, "black", board_rect)

chosen_number = 0
first_touch = Global(True)

hide_android_keyboard()


while running:
		for event in pg.event.get():
			#open("error.txt", "a").write(str(event.type) + ";")
			
			if event.type == 32785:  # WINDOWFOCUSGAINED
				buttons = []
				screen.fill("dark blue")
				screen.blit(board_surf, (board_start, 60))
			
				for i in range(81):
					row, column = i // 9, i % 9
					try:
						tile = s[(row, column)]
						number_is_default.value = tile.current_color
						
					except:
						s[(row, column)] = Tile.create_tile(row, column)

				for i in range(10):
					row, column = i // 5, i % 5
					d[(row, column)] = Dial.create_dial(i)
					
				buttons.append(Button((scr_width // 2 - solving_button_width // 2, scr_height - solving_button_height - 400), solving_button_size, "Решение")) 
				
				set_new_sudoku(s, empty_board)

		try:
			a_fingers = touch.get_num_fingers(device)
		
		except:
			a_fingers = 0
			
		if a_fingers:
			if first_touch.value:
				finger_data = touch.get_finger(device, 0)
				tx = finger_data["x"] * scr_width
				ty = finger_data["y"] * scr_height
				
				for k, v in rs.items():
					if v.collidepoint((tx, ty)):
						s[k].current_color = True
						s[k].current_number = chosen_number
						row, column = k
						empty_board[row][column] = chosen_number
						s[k].locked = bool(chosen_number)
				
				for k, v in rd.items():
					if v.collidepoint((tx, ty)):
						chosen_number = k
			
				for b in buttons:
					if b._global_coordinates.collidepoint((tx, ty)):
						
						match b.function:
							case "solution":
								my_sudoku = Solving_sudoku(*list(get_cords()))
								my_sudoku.completing_sudoku()
								solution = my_sudoku.sudoku_solution()
								
								set_new_sudoku(s, solution)
								
								R = Validate_sudoku(my_sudoku.empty_sudoku)
								print(R.is_valid())
						
				first_touch.value = Button._on_Button_pressed()
		else:
			first_touch.value = True
		
		
		clock.tick(300)
		pg.display.flip()
