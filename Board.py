import pygame as pg
import sys, os
import android
import Godot_logic as GL
from pygame._sdl2 import touch
from Classes import *


pg.init()


touch_scr = touch.get_num_devices()

device = touch.get_device(touch_scr - 1)

clock = pg.time.Clock()
running = True

pg.draw.rect(board_surf, "black", board_rect)

chosen_number = 0
first_touch = Global(True)

hide_android_keyboard()


while running:
		for event in pg.event.get():
			#open("error.txt", "a").write(str(event.type) + ";")
			
			if event.type == pg.WINDOWFOCUSGAINED:
				buttons = []
				buttons_step.value = 0
				screen.fill("dark blue")
				screen.blit(board_surf, (board_start, board_start_top))

				refresh_outer(outer_color)
				
				for i in range(81):
					row, column = i // 9, i % 9
					try:
						tile = s[(row, column)]
						tile.locked = tile.current_color
						
					except:
						s[(row, column)] = Tile.create_tile(row, column)

				for i in range(10):
					row, column = i // 5, i % 5
					try:
						c = d[list(d.keys())[i]].current_color
					except:
						c = "green"
					finally:
						d[(row, column)] = Dial.create_dial(i, c)
					
				buttons.append(Button((scr_width // 2 - buttons_width // 2,\
					 buttons_starts + buttons_step.value), buttons_size, "Решение")) 
				buttons.append(Button((scr_width // 2 - buttons_width // 2,\
					 buttons_starts + buttons_step.value), buttons_size, "Заполненное"))
				buttons.append(Button((scr_width // 2 - buttons_width // 2,\
					 buttons_starts + buttons_step.value), buttons_size, "Новое судоку"))
				buttons.append(Button((scr_width // 2 - buttons_width // 2,\
					 buttons_starts + buttons_step.value), buttons_size, "Стереть всё"))
				
				set_new_sudoku(s, empty_board.value, False)

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
						s[k].locked = True
						
						outer_color = all_outer_colors.get("default", "black")
						refresh_outer(outer_color)
				
				for k, v in rd.items():
					if v.collidepoint((tx, ty)):
						chosen_number = k
						d[list(d.keys())[k]]._on_Dial_pressed()
			
				for b in buttons:
					if b._global_coordinates.collidepoint((tx, ty)):
						
						match b.function:
							case "solution":
								cords = list(get_cords())
								if len(cords) >= 16:
									my_sudoku = Solving_sudoku(*cords)
									my_sudoku.completing_sudoku()
									solution = my_sudoku.sudoku_solution()
									
									set_new_sudoku(s, solution, False)
									
									R = Validate_sudoku(my_sudoku.empty_sudoku)
									sudoku_validation = R.is_valid()
									
									outer_color = all_outer_colors.get(sudoku_validation, "black")
									refresh_outer(outer_color)
									print(sudoku_validation)
							
							case "complete":
								#complete_sudoku = Create_sudoku().create()
								complete_sudoku = GL.get_new_sudoku()
								
								set_new_sudoku(s, complete_sudoku, True)
								
								R = Validate_sudoku(complete_sudoku)
								sudoku_validation = R.is_valid()
								
								outer_color = all_outer_colors.get(sudoku_validation, "black")
								refresh_outer(outer_color)
							
							case "new":
								#complete_sudoku = Create_sudoku().create()
								complete_sudoku = GL.get_new_sudoku()
								
								new_sudoku = get_incomplete_sudoku(complete_sudoku)
								set_new_sudoku(s, new_sudoku, True)
								
								outer_color = all_outer_colors.get("default", "black")
								refresh_outer(outer_color)
							
							case "clear":
								for tile in s.values():
									tile.current_number = 0
								outer_color = all_outer_colors.get("default", "black")
								refresh_outer(outer_color)
				
				first_touch.value = Button._on_Button_pressed()
		else:
			first_touch.value = True
		
		
		clock.tick(300)
		pg.display.flip()
