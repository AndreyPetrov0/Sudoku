import pygame as pg
from Functions import *
from Settings import *


class Tile:
	def __init__(self, number: int, coordinates: tuple):
		self.__coordinates = coordinates
		self.current_color = number_is_default.value
		
		x = get_x(coordinates[1])
		y = get_y(coordinates[0])
		rs[coordinates] = pg.rect.Rect(x, y, tile_size, tile_size)
		
		self._current_number = number
	
	
	@classmethod
	def create_tile(cls, row: int, column: int):
		tile_coordinates = row, column
		number = None
		
		try:
			number = s[tile_coordinates].current_number
		except:
			number = 0
		
		return cls(number, tile_coordinates)
	
	
	def set_number(self, number):
		row, column = self.__coordinates
		font_color = ["red", "black"][self.current_color]
		font_str = button_font.render(str(number), 0, font_color)
		fw = button_font.metrics(str(number))
		fx = get_x(column) + tile_size // 2 - fw[0][-1] // 2
		fy = get_y(row) + tile_size // 2 - button_font_height // 1.5
		
		screen.blit(font_str, (fx, fy))
	
	
	def erase_tile(self):
		pg.draw.rect(tile_surf, "yellow", tile_rect)
		row, column = self.__coordinates
		screen.blit(tile_surf, (get_x(column), get_y(row)))


	@property
	def current_number(self):
		return self._current_number
		
		
	@current_number.setter
	def current_number(self, new_number):
		self._current_number = new_number
		self.erase_tile()
		self.set_number(new_number)
		if not new_number:
			self.erase_tile()
	

class Dial(Tile):
	def __init__(self, number: int, coordinates: tuple):
		self.__coordinates = coordinates
		
		row, column = number // 5, number % 5
		pg.draw.rect(dial_surf, "green", dial_rect)
		x = board_start + wide_line * column + dial_size * column
		y = dial_start + wide_line * row + dial_size * row
		screen.blit(dial_surf, (x, y))
		
		font_str = dial_font.render(str(number), 0, "black")
		fw = dial_font.metrics(str(number))
		fx = x + dial_size // 2 - fw[0][-1] // 2
		fy = y + dial_size // 2 - dial_font_height // 1.5
		
		screen.blit(font_str, (fx, fy))
		
		rd[number] = pg.rect.Rect(x, y, dial_size, dial_size)
		
		self.number = number
	

	@classmethod
	def create_dial(cls, number: int):
		coordinates = number // 5, number % 5
		return cls(number, coordinates)


class Button:
	def __init__(self, coordinates: tuple, size: tuple, onscreen_text: str):
		self._global_coordinates = pg.rect.Rect(coordinates, size)
		self.color = "green"
		self.function = but_func.get(onscreen_text)
		self.font_scale = 0.7
		
		self.button_surf = pg.surface.Surface(size, 0, screen)
		pg.draw.rect(self.button_surf, self.color, self._global_coordinates)
		screen.blit(self.button_surf, coordinates)
		
		self.button_font = pg.font.Font(default_font, round(size[1] * self.font_scale))
		self.button_font_height = self.button_font.metrics(onscreen_text[0])[0][-2]
		self.fw = sum(c[-1] for c in self.button_font.metrics(onscreen_text))
		self.x, self.y = coordinates
		self.w, self.h = size
		self.fx = self.x + self.w // 2 - self.fw // 2
		self.fy = self.y + self.h // 2 - self.button_font_height // 1.5
		self.font_str = self.button_font.render(onscreen_text, 0, "white")
		screen.blit(self.font_str, (self.fx, self.fy))
	
	@staticmethod
	def _on_Button_pressed():
			return False
	
	def solution(self):
		pass


class Global:
	def __init__(self, value):
		self._value = value
		
	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, new_value):
		self._value = new_value

number_is_default = Global(True)
