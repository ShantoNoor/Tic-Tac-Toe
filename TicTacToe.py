import os

class TicTacToe:
	def __init__(self):
		self.board = [' ' for cell in range(9)]
		self.freeCellCount = 9


	def printBoard(self):
		os.system('cls')
		for i in range(3):
			if i > 0: print('-'*5)
			row = self.board[3*i:3*i+3]
			for j, cell in enumerate(row):
				if j > 0: print('|', end='')
				if cell == ' ': print(3*i+j+1, end='')
				else: print(cell, end='')
			print()
		print()


	def placeCellInBoard(self, cellId, playerChar):
		self.board[cellId-1] = playerChar
		self.freeCellCount -= 1


	@staticmethod
	def isWinner(board, playerChar):
		winner = False
		winningCombinations = [
			[1, 2, 3], # 1st row
			[4, 5, 6], # 2nd row
			[7, 8, 9], # 3rd row
			[1, 4, 7], # 1st column
			[2, 5, 8], # 2nd column
			[3, 6, 9], # 3rd column
			[1, 5, 9], # \ corner
			[3, 5, 7]  # / corner
		]
		for row in winningCombinations:
			cellMatchCount = 0
			for cell in row:
				if board[cell-1] == playerChar:
					cellMatchCount += 1
				else:
					cellMatchCount = 0
					break
			if cellMatchCount == 3:
				winner = True
				break

		return winner


	@staticmethod
	def getFreeCellIds(board):
		emptyCellIds = []
		for cellId, cell in enumerate(board):
			if cell == ' ':
				emptyCellIds.append(cellId+1)

		return emptyCellIds


	def retry(self, players):
		char = input('Press any key to retry(x to exit): ')
		if(char.lower() == 'x'):
			print('Exiting...')
		else:
			self.__init__()
			self.play(players)


	def play(self, players):
		isAnyOneWinner = False
		while self.freeCellCount > 0 and not isAnyOneWinner:
			for player in players:
				self.printBoard()
				self.placeCellInBoard(player.getCellId(self.board), player.getChar())
				if(self.freeCellCount < 5 and TicTacToe.isWinner(self.board, player.getChar())):
					isAnyOneWinner = True
					self.printBoard()
					print(f'{player.getName()}[{player.getChar()}] is the winner!...')
					break
				elif(self.freeCellCount == 0):
					os.system('color 0C')
					print('It\'s a tie...')
					break
		self.retry(players)

