import pygame
from Enums import BoardState, Colors, Constants
from Ship import Ship

class Board(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.ships_list = []
		self.grid_size = 10
		self.board = [[BoardState.NO_SHIP.value for _ in range(self.grid_size)] for _ in range(self.grid_size)]
		self.cell_size = Constants.CELL_SIZE.value
		self.offset_x = Constants.OFFSET.value
		self.offset_y = Constants.OFFSET.value
		self.dupl_board = []

		self.grid_cells = self._generate_cells()
		self.ships = self._create_ships()

		self.last_placedShip = None
		self.selected_ship = None
		self.offset_x_drag = 0
		self.offset_y_drag = 0

	def _generate_cells(self):
		return [
			pygame.Rect(
				self.offset_x + col * self.cell_size,
				self.offset_y + row * self.cell_size,
				self.cell_size,
				self.cell_size
			)
			for row in range(self.grid_size)
			for col in range(self.grid_size)
		]

	def _create_ships(self):
		sizes = [4] + [3]*2 + [2]*3 + [1]*4
		ships = [Ship(size) for size in sizes]
		self.__layout_ships(ships)
		return ships

	def set_board(self,board):
		self.board = board
#generate aside
	def __layout_ships(self, ships):
		margin = 20
		start_x = 500
		start_y = 100
		cell_size = 33
		ships_by_size = {}
		for ship in ships:
			ships_by_size.setdefault(ship.size, []).append(ship)
		sorted_sizes = sorted(ships_by_size.keys(), reverse=True)
		current_y = start_y
		for size in sorted_sizes:
			current_x = start_x
			for ship in ships_by_size[size]:
				if ship.initial_position is None:
					ship.initial_position = (current_x, current_y)
				ship.rect.topleft = ship.initial_position
				w = cell_size * ship.size
				ship.rect.size = (w, cell_size)
				current_x += w + margin
			current_y += cell_size + margin

	def is_valid_placement(self, ship_cells,ship):
		self.dupl_board = [[BoardState.NO_SHIP.value for _ in range(self.grid_size)] for _ in range(self.grid_size)]
		for _ship in self.ships:
			if _ship != ship and len(_ship.ship_coords) !=0:
				for x,y in _ship.ship_coords:
					self.dupl_board[y][x] = BoardState.SHIP.value
				for x,y in _ship.areaAroundShip:
					self.dupl_board[y][x] = BoardState.AREA_AROUND_SHIP.value

		for x, y in ship_cells:
			if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
				return False
			if self.dupl_board[y][x] != BoardState.NO_SHIP.value:
				return False
		return True

	def clear_ship_cells(self, ship):
		if not ship.ship_coords:
			return
		for x, y in ship.ship_coords:
			self.set_cell(x, y, BoardState.NO_SHIP.value)
		ship.ship_coords = []

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for ship in reversed(self.ships):
					if ship.rect.collidepoint(event.pos):
						ship.dragging = True
						self.selected_ship = ship
						self.offset_x_drag = ship.rect.x - event.pos[0]
						self.offset_y_drag = ship.rect.y - event.pos[1]
						break

		elif event.type == pygame.MOUSEBUTTONUP:
			if self.selected_ship:
				self.selected_ship.dragging = False
				ship = self.selected_ship
				snapped = False
				for cell in self.grid_cells:
					if cell.collidepoint(event.pos):
						mouse_x, mouse_y = event.pos
						relative_x = mouse_x - ship.rect.x
						deck_index = relative_x // self.cell_size if ship.horizontal else 0
						cell_col = (cell.x - self.offset_x) // self.cell_size
						cell_row = (cell.y - self.offset_y) // self.cell_size
						start_col = cell_col - deck_index if ship.horizontal else cell_col
						start_row = cell_row if ship.horizontal else cell_row - deck_index
						ship_cells = [
							[start_col + i, start_row] if ship.horizontal else [start_col, start_row + i]
							for i in range(ship.size)
						]
						if self.is_valid_placement(ship_cells,ship):
							self.clear_ship_cells(ship)
							ship.rect.topleft = (
								self.offset_x + start_col * self.cell_size,
								self.offset_y + start_row * self.cell_size
							)
							ship.placeShip(self, ship_cells)
							self.last_placedShip = ship
							self.printBoard()
							snapped = True
							ship.placed = True
							break
				if not snapped:
					self.__layout_ships([ship])
					ship.delete_ship_from_board(self)
					ship.horizontal = True
					self.printBoard()
				self.selected_ship = None

		elif event.type == pygame.MOUSEMOTION:
			if self.selected_ship and self.selected_ship.dragging:
				mouse_x, mouse_y = event.pos
				self.selected_ship.rect.x = mouse_x + self.offset_x_drag
				self.selected_ship.rect.y = mouse_y + self.offset_y_drag

	def draw(self, surface):
		for cell in self.grid_cells:
			pygame.draw.rect(surface, Colors.GRAY.value, cell, 1)
		self.__drawShips(surface)

	def rotate_ship(self):
		if self.last_placedShip:
			self.last_placedShip.rotateShip()

	def __drawShips(self, surface):
		for ship in self.ships:
			ship.draw_ship(surface, ship.rect.x, ship.rect.y, Colors.BLACK.value, self.cell_size)

	def set_cell(self, x, y, value):
		self.board[y][x] = value

	def getBoard(self):
		return self.board

	def add_ship(self, ship):
		self.ships_list.append(ship)

	def removeShip(self, ship):
		if ship in self.ships_list:
			self.ships_list.remove(ship)

	def getAttacked(self, x, y):
		for ship in self.ships_list:
			if ship.is_on_position(x, y):
				ship.getAttacked(x, y)
				return True
		self.set_cell(x, y, BoardState.MISS.value)
		return False

	def printBoard(self):
		for row in self.board:
			print(" ".join(
				"x" if cell == 1 else
				"*" if cell == 4 else
				str(cell)
				for cell in row
			))
