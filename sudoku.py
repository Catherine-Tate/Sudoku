#sudoku game
import numpy as np

#written by Catherine Tate


"""
process for creating the board:
1. generate filled grid
2. remove some #s (more/less for different difficulties?)
3. check if grid w/ numbers taken out has only 1 solution
"""

def makeBoard():
	board = np.zeros((9,9))



def printMenu():
	print("="*16)
	print("Welcome to SUDOKU")
	print("="*16)
	board = makeBoard()

printMenu()
