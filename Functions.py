from Settings import *


def get_x(c):
	x = board_start + wide_line + (wide_line * (c // 3)) + narrow_line * int(narrow_set[c]) + tile_size * c
	return x


def get_y(r):
	y = 60 + wide_line + (wide_line * (r // 3)) + narrow_line * int(narrow_set[r]) + tile_size * r
	return y


def set_new_sudoku(collection, sudoku):
	for i in range(len(sudoku)):
		for j in range(len(sudoku[i])):
			collection.get((i, j)).current_number = sudoku[i][j]


def get_cords():
	for cord, object in s.items():
		if not object.current_number:
			continue
		row, column = cord
		yield [row, column, object.current_number]
