from TicTacToe import *

class Player:
	def __init__(self, name, char, color):
		self.char = char
		self.color = color
		self.name = name


	def getCellId(self, board):
		pass


	def getChar(self):
		return self.char

	def getName(self):
		return self.name


	def getColor(self):
		return self.color

