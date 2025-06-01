from pygame import surface

from Board import Board
from Ship import Ship
from Player import Player
import pygame



# создать 2 игрока, каждому игроку надо присвоить свою доску;
# дать игрокам по очереди расставить корабли из списка (делать проверку на то чтобы игрок не мог поставит 4 2хпаловник)
# 
#counter =10
#кнопка accept которая бы работала только если все корабли поставлены
#создаем player1
#он ставит корабли
#player2
#он ставит корабли

class Game(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.player1 = Player('paver')
		self.player2 = Player('andrey')
		self.turn = 1


	def attack(self,coords):
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
		

	def draw(self,surface):

		self.player1.board.draw_game_board(surface,1)
		self.player2.board.draw_game_board(surface,2)

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
