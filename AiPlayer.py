from Player import *

class AiPlayer(Player):
	def __init__(self, name, char, color, player2Char):
		super().__init__(name, char, color)
		self.player2Char = player2Char


	#@overide
	def getCellId(self, board):
		return self.minimax(True, board, board.count(' '))[1]


	def minimax(self, maximizer, board, freeCellCount):
		if not maximizer and TicTacToe.isWinner(board, self.char):
			return [1*(freeCellCount+1), 0]

		if maximizer and TicTacToe.isWinner(board, self.player2Char):
			return [-1*(freeCellCount+1), 0]

		if freeCellCount == 0:
			return [0, 0]

		freeCellIds = TicTacToe.getFreeCellIds(board)
		bestMove = 0

		if maximizer:
			maxValue = float('-inf')
			for cellId in freeCellIds:
				TicTacToe.placeCellInBoard(board, cellId, self.char) # Removing
				value, move = self.minimax(False, board, freeCellCount-1)
				TicTacToe.placeCellInBoard(board, cellId, ' ') # Removing
				if value > maxValue:
					maxValue = value
					bestMove = cellId

			return [maxValue, bestMove]

		else:
			minValue = float('inf')
			for cellId in freeCellIds:
				# board[cellId-1] = self.player2Char
				TicTacToe.placeCellInBoard(board, cellId, self.player2Char)
				value, move = self.minimax(True, board, freeCellCount-1)
				TicTacToe.placeCellInBoard(board, cellId, ' ') # Removing
				if value < minValue:
					minValue = value
					bestMove = cellId

			return [minValue, bestMove]


