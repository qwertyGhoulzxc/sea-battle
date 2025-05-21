#ux ui
#irish dance music
from Game import Game

game = Game()

isGameStart = game.placeShips()

isGameOver = False
while not isGameOver:
	isGameOver = game.attack()
