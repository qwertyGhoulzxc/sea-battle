from Player import Player
import pygame

class Game(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.player1 = Player('player 1',1)
		self.player2 = Player('player 2',2)
		self.turn = 1
		self.gameOver = 0


	def attack(self,coords):
		if self.turn == 1:
			turn = self.player2.getAttacked(coords)
			if self.player2.isGameOver():
				self.gameOver = 2
				self.player1.score += 1
				return True
			if turn == False:
				self.turn = 2
		else:
			turn = self.player1.getAttacked(coords)
			if self.player1.isGameOver():
				self.gameOver = 1
				self.player2.score += 1
				return True
			if turn == False:
				self.turn = 1
		return False
		

	def draw(self,surface):

		self.player1.board.draw_game_board(surface)
		self.player2.board.draw_game_board(surface)

	def revenge(self):
		self.turn = self.gameOver
		self.gameOver = 0
		self.player1.reset()
		self.player2.reset()

	def newGame(self):
		self.player1.newGame()
		self.player2.newGame()
		self.turn = 1
		self.gameOver = 0

