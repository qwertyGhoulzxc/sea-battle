import pygame
from Enums import BoardState

class Ship(pygame.sprite.Sprite):
	def __init__(self, size,player_number):
		super().__init__()
		self.areaAroundShip = []
		self.ship_coords = []
		self.ship_coords_for_kill = []
		self.board = None
		self.boardField = None
		self.size = size
		self.horizontal = True
		self.rect = pygame.Rect(0, 0, size * 33, 33)
		self.dragging = False
		self.placed = False
		self.initial_position = None

		self.player_number = player_number
		self.image = pygame.image.load(f"./assets/{size}_{"R" if self.player_number == 2 else "B"}.png").convert_alpha()
		self.position_adjusted = False

	def placeShip(self, board, _coords):
		self.delete_ship_from_board(board)
		coords =  [list(t) for t in _coords]
		self.boardField = board.board
		self.board = board
		for x, y in coords:
			if self.boardField[y][x] != BoardState.NO_SHIP.value:
				return False
		self.ship_coords = coords
		self.ship_coords_for_kill = coords.copy()
		self.areaAroundShip = []
		for x, y in self.ship_coords:
			self.board.set_cell(x, y, BoardState.SHIP.value)
			self.__mark_area_around(x, y)
		self.areaAroundShip = [coord for coord in self.areaAroundShip if coord not in self.ship_coords]
		for x, y in self.areaAroundShip:
			self.board.set_cell(x, y, BoardState.AREA_AROUND_SHIP.value)
		self.board.add_ship(self)
		return True

	def delete_ship_from_board(self,board):
		self.board = board
		dupl_board = [[BoardState.NO_SHIP.value for _ in range(10)] for _ in range(10)]
		for _ship in self.board.ships:
			if _ship != self and len(_ship.ship_coords) != 0:
				for x, y in _ship.ship_coords:
					dupl_board[y][x] = BoardState.SHIP.value
				for x, y in _ship.areaAroundShip:
					dupl_board[y][x] = BoardState.AREA_AROUND_SHIP.value
		board.set_board(dupl_board)
		self.boardField = dupl_board
		self.areaAroundShip = []
		self.ship_coords = []
		self.ship_coords_for_kill = []
		board.removeShip(self)


	def __mark_area_around(self, x, y):
		directions = [
			(1, 0), (-1, 0), (0, 1), (0, -1),
			(1, 1), (1, -1), (-1, 1), (-1, -1)
		]
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx < len(self.boardField[0]) and 0 <= ny < len(self.boardField):
				if self.boardField[ny][nx] in [BoardState.NO_SHIP.value, BoardState.AREA_AROUND_SHIP.value]:

					self.board.set_cell(nx, ny, BoardState.AREA_AROUND_SHIP.value)
					self.areaAroundShip.append([nx, ny])

	def getAttacked(self, x, y):
		self.ship_coords.remove([x, y])
		self.board.set_cell(x, y, BoardState.HIT_SHIP.value)
		if not self.ship_coords:
			for x, y in self.areaAroundShip:
				self.board.set_cell(x, y, BoardState.MISS.value)
			self.board.removeShip(self,)

	def is_on_position(self, x, y):
		return [x, y] in self.ship_coords

	def rotateShip(self):
		if not self.placed or not self.ship_coords:
			return

		sorted_ship_coord = sorted(self.ship_coords.copy(), key=lambda item: item[0])
		start_x, start_y = sorted_ship_coord[0]
		new_coords = []
		isPlaced = False
		tries = 0
		max_tries = 2

		self.delete_ship_from_board(self.board)
		_horizontal = not self.horizontal

		while not isPlaced and tries < max_tries:
			new_coords = []
			success = True

			for i in range(len(sorted_ship_coord)):
				if not _horizontal:
					new_x = start_x
					new_y = start_y + i
				else:
					new_x = start_x + i
					new_y = start_y

				if not (0 <= new_x < len(self.boardField[0]) and 0 <= new_y < len(self.boardField)):
					success = False
					break

				if self.boardField[new_y][new_x] != BoardState.NO_SHIP.value:
					success = False
					break

				new_coords.append([new_x, new_y])

			if success:
				isPlaced = True
				self.horizontal = _horizontal
			else:
				tries += 1
				_horizontal = not _horizontal

		if not isPlaced:
			new_coords = sorted_ship_coord

		self.placeShip(self.board, new_coords)


	def draw_ship(self, surface, x, y, color=(100, 100, 100), cell_size=35):
		vertical = not self.horizontal
		width = cell_size if vertical else cell_size * self.size
		height = cell_size * self.size if vertical else cell_size
		self.rect = pygame.Rect(x, y, width, height)


		image = pygame.transform.scale(self.image, (width, height))
		if vertical and self.size != 1:
			image = pygame.transform.rotate(image, -90)
			image = pygame.transform.scale(image, (width, height))

		surface.blit(image, (x, y))
