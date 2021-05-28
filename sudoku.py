#sudoku game
import numpy as np
import random

#written by Catherine Tate in python 3


"""
process for creating the board:
1. generate filled grid
2. remove some #s (more/less for different difficulties?)
3. check if grid w/ numbers taken out has only 1 solution
"""

def printBoard(board):
    print("\t | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
    print("\t " + "-"*37)
    for i in range(0, 9):
        print("\t" + str(i) + "|", end = "")
        for j in range(0, 9):
            print(" " + str(board[i][j]) + " |", end='')
        print("")
def makeBoard():
    board = np.zeros((9,9), dtype=int)
    #make a random set of seed values to start the board off
    for i in range(1, 10):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        board[x][y] = i
    printBoard(board)

def printMenu():
	print("="*16)
	print("Welcome to SUDOKU")
	print("="*16)
	board = makeBoard()

printMenu()
