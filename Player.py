from Board import Board
from Ship import Ship

class Player:
	def __init__(self,name):
		self.name = name
		self.board = Board()
		self.score = 0
		self.ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

	def set_name(self,name):
		self.name = name

	def clearBoard(self):
		self.board.clearBoard()
		self.ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
	
	def placeShip(self,coords):
		if len(self.ship_sizes) == 0:
			return True
		if not len(coords) in self.ship_sizes:
			#TODO: error
			print('error')
			return False
		self.ship_sizes.remove(len(coords))
		ship = Ship(len(coords))
		ship.place

		return False
	
	def getBoard(self):
		return self.board.getBoard()
	
	def getAttacked(self,coords):
		return self.board.getAttacked(coords[0],coords[1])

	def isGameOver(self):
		return self.board.getShips() == 0;
	


# score 
