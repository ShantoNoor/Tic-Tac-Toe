from TicTacToe import *
from HumanPlayer import *
from AiPlayer import *

def main():
	t = TicTacToe()

	# h1 = HumanPlayer('Shanto', 'X', '09')
	# h2 = HumanPlayer('Noor', 'O', '0A')
	# t.play([h1, h2])

	h1 = HumanPlayer('Shanto', 'X', '09')
	a = AiPlayer('Ai', 'O', '0A', h1.getChar())
	t.play([h1, a])

	# a1 = AiPlayer('Ai', 'O', '0A', 'X')
	# a2 = AiPlayer('Ai2', 'X', '09', 'O')
	# t.play([a1, a2])


if __name__ == '__main__':
	main()
