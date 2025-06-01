from enum import Enum

class BoardState(Enum):
	NO_SHIP = 0
	SHIP = 1
	HIT_SHIP = 2
	MISS = 3
	AREA_AROUND_SHIP = 4

class Screens(Enum):
	MENU = 'MENU'
	PLACE_SHIPS_1 = 'PLACE_SHIPS_1'
	PLACE_SHIPS_2 = 'PLACE_SHIPS_2'
	GAME = 'GAME'

class Colors(Enum):
	BLUE = (0, 0, 255)
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	CORAL = (245, 122, 138)
	GRAY = (194, 194, 194)
	GREEN = (0, 255, 0)

class Constants(Enum):
	CELL_SIZE = 35
	OFFSET = 100
