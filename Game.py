from Board import Board
from Ship import Ship
from Player import Player



# создать 2 игрока, каждому игроку надо присвоить свою доску;
# дать игрокам по очереди расставить корабли из списка (делать проверку на то чтобы игрок не мог поставит 4 2хпаловник)
# 
#counter =10
#кнопка accept которая бы работала только если все корабли поставлены
#создаем player1
#он ставит корабли
#player2
#он ставит корабли

class Game:

	def __init__(self):
		self.player1 = Player('paver')
		self.player2 = Player('andrey')
		self.turn = 1

	def placeShips(self):
		isPlaced = False
		while not isPlaced:
			# coords = eval(input())
			ships_1 = [
    # 4-палубный
    [[3, 1], [4, 1], [5, 1], [6, 1]],

    # 3-палубные
    [[1, 3], [1, 4], [1, 5]],
    [[7, 2], [8, 2], [9, 2]],

    # 2-палубные
    [[3, 6], [4, 6]],
    [[6, 4], [6, 5]],
    [[0, 7], [0, 8]],

    # 1-палубные
    [[2, 9]],
    [[5, 9]],
    [[7, 7]],
    [[9, 9]],
]
			for ship in ships_1:
				isPlaced = self.player1.placeShip(ship)
			# self.player1.getBoard()
		isPlaced = False
		while not isPlaced:
			ships_2 = [
    [[5, 0], [5, 1], [5, 2], [5, 3]],

    [[0, 0], [1, 0], [2, 0]],
    [[7, 5], [7, 6], [7, 7]],

    # 2-палубные
    [[2, 4], [2, 5]],
    [[4, 7], [5, 7]],
    [[9, 1], [9, 2]],

    # 1-палубные
    [[0, 9]],
    [[3, 8]],
    [[6, 9]],
    [[9, 9]],
]
			for ship in ships_2:
				isPlaced = self.player2.placeShip(ship)
			# self.player1.getBoard()
		self.printBoardsSideBySide(self.player1.getBoard(),self.player2.getBoard())
		return True
	
	def attack(self):
		coords = eval(input())
		print(self.turn)
		if self.turn == 1:
			turn = self.player2.getAttacked(coords)
			print(turn)
			if self.player2.isGameOver():
				print('player1 - win')
				return True
			if turn == False:
				self.turn = 2
		else:
			turn = self.player1.getAttacked(coords)
			if self.player1.isGameOver():
				print('player2 - win')
				return True
			if turn == False:
				self.turn = 1
		self.printBoardsSideBySide(self.player1.getBoard(),self.player2.getBoard())
		return False
		


	def printBoardsSideBySide(self, board1, board2):
		for row1, row2 in zip(board1, board2):
			row1_str = " ".join(
            "x" if cell == 2 else 
            "*" if cell == 3 else 
            "0" if cell == 1 or 4 else 
            str(cell)
            for cell in row1
        )
			row2_str = " ".join(
            "x" if cell == 2 else 
            "*" if cell == 3 else 
            "0" if cell == 1 or 4 else 
            str(cell)
            for cell in row2
        )
			print(f"{row1_str}   ||   {row2_str}")




# board = Board()
# # Ship(board,[(1,1)])
# # Ship(board,[(3,0)])
# Ship(board,[[7,1], [7,2], [7,0]])
# board.getAttacked(7,1)
# board.getAttacked(7,2)
# board.getAttacked(7,3)
# board.getAttacked(7,0)

# board.printBoard()


