from Board import Board
from Ship import Ship



# создать 2 игрока, каждому игроку надо присвоить свою доску;
# дать игрокам по очереди расставить корабли из списка (делать проверку на то чтобы игрок не мог поставит 4 2хпаловник)
# 
#counter =10
#кнопка accept которая бы работала только если все корабли поставлены
#создаем player1
#он ставит корабли
#player2
#он ставит корабли

board = Board()
# Ship(board,[(1,1)])
# Ship(board,[(3,0)])
Ship(board,[[7,1], [7,2], [7,0]])
board.getAttacked(7,1)
board.getAttacked(7,2)
board.getAttacked(7,3)
board.getAttacked(7,0)

board.printBoard()


