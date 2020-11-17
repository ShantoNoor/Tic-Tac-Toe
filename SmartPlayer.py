from Player import *

class SmartPlayer(Player):
	def __init__(self, name, char, color, player2Char):
		super().__init__(name, char, color)
		self.player2Char = player2Char


	#@overide
	def getCellId(self, board):
		pass

