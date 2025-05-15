from enum import Enum

class BoardState(Enum):
	NO_SHIP = 0
	SHIP = 1
	HIT_SHIP = 2
	MISS = 3
	AREA_AROUND_SHIP = 4