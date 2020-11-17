from TicTacToe import *
from HumanPlayer import *
from AiPlayer import *

def main():
	t = TicTacToe()

	h1 = HumanPlayer('Shanto', 'X', '09')
	# h2 = HumanPlayer('Noor', 'O', '0A')
	# t.play([h1, h2])

	a = AiPlayer('Ai', 'O', '0A', h1.getChar())
	t.play([h1, a])


if __name__ == '__main__':
	main()
