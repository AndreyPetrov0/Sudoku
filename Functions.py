from Settings import *
from jnius import autoclass


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


def set_new_sudoku(collection, sudoku):
	for i in range(len(sudoku)):
		for j in range(len(sudoku[i])):
			number = sudoku[i][j]
			tile = collection.get((i, j))
			tile.current_color =  tile.current_number > 0
			tile.current_number = number


def get_cords():
	for cord, object in s.items():
		if not object.current_number:
			continue
		row, column = cord
		yield [row, column, object.current_number]
