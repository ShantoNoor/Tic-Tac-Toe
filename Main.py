from TicTacToe import *
from HumanPlayer import *
from AiPlayer import *

def main():
	t = TicTacToe()

	while(True):
		print('(1) Ai vs Human.')
		print('(2) Human vs Human.')
		print('(3) Ai vs Ai (for fun only).')
		ch = input('Press 1, 2 or 3 : ')
		if ch == '1':
			name = input('Enter your name : ')
			h1 = HumanPlayer(name, 'X', '09')
			a = AiPlayer('Ai', 'O', '0A', h1.getChar())
			t.play([h1, a])
		elif ch == '2':
			name, name2 = input('Enter player\'s name : ')
			h1 = HumanPlayer(name, 'X', '09')
			h2 = HumanPlayer(name2, 'O', '0A')
			t.play([h1, h2])
		elif ch == '3':
			a1 = AiPlayer('Ai', 'O', '0A', 'X')
			a2 = AiPlayer('Ai2', 'X', '09', 'O')
			t.play([a1, a2])
		else:
			print('Entar a valid number (1 to 3): ')


if __name__ == '__main__':
	main()
