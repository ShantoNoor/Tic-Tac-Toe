from Player import *

class HumanPlayer(Player):
	def __init__(self, name, char, color):
		super().__init__(name, char, color)


	#@overide
	def getCellId(self, board):
		os.system('color ' + self.color)
		freeCells = TicTacToe.getFreeCellIds(board)
		while True:
			cellId = input(self.name + '\'s time to play (1-9): ')
			try:
				cellId = int(cellId)
			except:
				print('Entar a vaid integer number...')

			if cellId in freeCells: break
			else: print('Entar a number from the list :', freeCells)


		return cellId

