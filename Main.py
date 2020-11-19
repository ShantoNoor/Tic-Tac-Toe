from TicTacToe import *
from HumanPlayer import *
from AiPlayer import *

def aiVsHuman(ticTacToe):
	name = input('Enter your name : ')
	h1 = HumanPlayer(name, 'X', '09')
	a = AiPlayer('Ai', 'O', '0A', h1.getChar())
	ticTacToe.play([h1, a])


def humanVsHuman(ticTacToe):
	name, name2 = input('Enter player\'s name : ')
	h1 = HumanPlayer(name, 'X', '09')
	h2 = HumanPlayer(name2, 'O', '0A')
	ticTacToe.play([h1, h2])


def aiVsAi(ticTacToe):
	a1 = AiPlayer('Ai', 'O', '0A', 'X')
	a2 = AiPlayer('Ai2', 'X', '09', 'O')
	ticTacToe.play([a1, a2])


def main():
	ticTacToe = TicTacToe()
	while(True):
		os.system('cls')
		print('(1) Ai vs Human.')
		print('(2) Human vs Human.')
		print('(3) Ai vs Ai (for fun only).')
		ch = input('Press 1, 2 or 3 (x for exit): ')
		if ch == '1':
			aiVsHuman(ticTacToe)
		elif ch == '2':
			humanVsHuman(ticTacToe)
		elif ch == '3':
			aiVsAi(ticTacToe)
		elif ch.lower() == 'x':
			print('Exiting...')
			break
		else:
			print('Entar a valid number from 1 to 3 (x for exit.): ')


if __name__ == '__main__':
	main()
