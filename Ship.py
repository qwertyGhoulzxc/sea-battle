import Board
from Enums import BoardState

class Ship():

	def __init__(self, board,coords):
		self.boardField = board.getBoard()
		self.board = board
		
		for x,y in coords:
			if self.boardField[y][x] == BoardState.SHIP.value or self.boardField[y][x] == BoardState.AREA_AROUND_SHIP.value:
				#TODO: обработать ошибку
				return None

		self.ship_coords = coords
		self.areaAroundShip = []
		for x,y in self.ship_coords:
			self.board.set_cell(x,y,BoardState.SHIP.value)
			self.__killAreaAroundShip(x,y)
		self.areaAroundShip = [coord for coord in self.areaAroundShip if coord not in self.ship_coords]
		for x,y in self.areaAroundShip:
			self.board.set_cell(x,y,BoardState.AREA_AROUND_SHIP.value)
		self.board.add_ship(self)


	def __killAreaAroundShip(self,x,y):
		directions = [
        (1, 0), (-1, 0),  
        (0, 1), (0, -1),  
        (1, 1), (1, -1),  
        (-1, 1), (-1, -1)
    ]

		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx <= len(self.boardField[0]) and 0 <= ny < len(self.boardField):
				if self.boardField[ny][nx] == BoardState.NO_SHIP.value or self.boardField[ny][nx] == BoardState.AREA_AROUND_SHIP.value:
					self.board.set_cell(nx,ny,BoardState.AREA_AROUND_SHIP.value)
					self.areaAroundShip.append([nx,ny])
	
	def getAttacked(self,x,y):
		self.ship_coords.remove([x,y])
		self.board.set_cell(x,y,BoardState.HIT_SHIP.value)
		if len(self.ship_coords) ==0:
			for x,y in self.areaAroundShip:
				self.board.set_cell(x,y,BoardState.MISS.value)


	def is_on_position(self,x,y):
	 return [x, y] in self.ship_coords

	
		



		