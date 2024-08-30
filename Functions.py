from Settings import *
from jnius import autoclass
from random import randint


def show_android_keyboard():
    InputMethodManager = autoclass("android.view.inputmethod.InputMethodManager")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    activity = PythonActivity.mActivity
    service = activity.getSystemService(Context.INPUT_METHOD_SERVICE)
    service.toggleSoftInput(InputMethodManager.SHOW_FORCED, 0)


def hide_android_keyboard():
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    activity = PythonActivity.mActivity
    service = activity.getSystemService(Context.INPUT_METHOD_SERVICE)
    service.hideSoftInputFromWindow(activity.getContentView().getWindowToken(), 0)


def get_x(c):
	x = board_start + wide_line + (wide_line * (c // 3)) + narrow_line * int(narrow_set[c]) + tile_size * c
	return x


def get_y(r):
	y = 60 + wide_line + (wide_line * (r // 3)) + narrow_line * int(narrow_set[r]) + tile_size * r
	return y


def set_new_sudoku(collection, sudoku, default):
	for i in range(len(sudoku)):
		for j in range(len(sudoku[i])):
			number = sudoku[i][j]
			tile = collection.get((i, j))
			if default:
				tile.current_color = bool(number)
			else:
				if not tile.current_number:
					tile.locked = False
					tile.current_color = False
			tile.current_number = number


def get_cords():
	for cord, object in s.items():
		if not object.current_number:
			continue
		row, column = cord
		yield [row, column, object.current_number]


def get_square(sudoku_list, square_num):
	for row in range(9):
		if row // 3 != square_num // 3:
			continue
		for column in range(9):
			if column // 3 != square_num % 3:
				continue
			yield sudoku_list[row][column]


def get_field(complete_sudoku: list):
	field =[]
	for square in range(9):
		field.append(list(get_square(complete_sudoku, square)))
	return field


def get_new_sudoku_list(field: list):
	r0 = []
	r1 = []
	r2 = []
	r3 = []
	r4 = []
	r5 = []
	r6 = []
	r7 = []
	r8 = []
	result = [r0, r1, r2, r3, r4, r5, r6, r7, r8]
	
	for result_row in range(9):
		for square in range(9):
			for tile in range(9):
				if result_row == (square // 3) * 3 + tile // 3:
					result[result_row].append(field[square][tile])
		
	return result


def get_incomplete_sudoku(sudoku: list):
	field = get_field(sudoku)
	new_field = field.copy()
	for square in range(9):
		for i in range(difficulty_level):
			del_tile = randint(0, 8)
			new_square = new_field[square].copy()
			new_square[del_tile] = 0
			new_field[square] = new_square.copy()
	return get_new_sudoku_list(new_field)


def refresh_outer(color):
	pg.draw.rect(outer_h_surf, color, outer_h_rect)
	pg.draw.rect(outer_v_surf, color, outer_v_rect)

	screen.blit(outer_h_surf, outer_h1)
	screen.blit(outer_h_surf, outer_h2)
	screen.blit(outer_v_surf, outer_v1)
	screen.blit(outer_v_surf, outer_v2)
