from Board import Board

class Player:
	def __init__(self,name,player_number):
		self.player_number = player_number
		self.name = name
		self.board = Board(self.player_number)
		self.score = 0


	def set_name(self,name):
		self.name = name

	def reset(self):
		self.board = Board(self.player_number)

	def get_name(self):
		return self.name

	def newGame(self):
		self.name = "player " + str(self.player_number)
		self.board = Board(self.player_number)
		self.score = 0

	def getBoard(self):
		return self.board.getBoard()
	
	def getAttacked(self,coords):
		return self.board.getAttacked(coords[0],coords[1])

	def isGameOver(self):
		return len(self.board.ships_list) == 0
