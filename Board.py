from Enums import BoardState

class Board:


	def __init__(self):
		self.board = [ [ 0 for i in range(10)] for _ in range(10) ]
		self.ships = []

	def set_cell(self,x,y,value):
		self.board[y][x] = value;

	def getBoard(self):
		return self.board

	def add_ship(self, ship):
		self.ships.append(ship)
	
	def getAttacked(self, x, y):
		for ship in self.ships:
			print(ship.is_on_position(x, y))
			if ship.is_on_position(x, y):
				ship.getAttacked(x, y)
				return True
		self.set_cell(x,y,BoardState.MISS.value)
		return False	
					


	def printBoard(self):
		for row in self.board:
			print(" ".join(str(cell) for cell in row))

board = Board()

board.getBoard()
1,2,3
# receiveHit 
# placeShip - кнопка развернуть корабль
# связка с Player 
# связка с Ship