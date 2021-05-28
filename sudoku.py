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

"""
generate the first 3x3 square of the puzzle
"""
def iPerm(seed):
    board = np.zeros((9,9), dtype="int")
    #fill in one 3x3 grid first
    x = 0
    #put each seed value into the 3x3 grid
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = seed[x]
            x+=1
    return(board)

#takes a partially filled board w/ blank spaces and
def solvBoard(board):
    return

def printBoard(board):
    print("\t [ 1 | 2 | 3 ][ 4 | 5 | 6 ][ 7 | 8 | 9 ]")
    for i in range(0, 9):
        if(i %3 == 0):
            print("\t " + "-"*39)
        print("\t" + str(i) + "[", end = "")
        for j in range(0, 9):
            print(" " + str(board[i][j]), end='')
            if((j+1)%3 == 0):
                print(" ]", end='')
                if(j != 8): print("[", end='')
            else:
                print(" |", end = '')
        print("")

def makeBoard():
    #seed value
    seed = random.sample(range(1, 10), 9)
    board = iPerm(seed)
    #printBoard(board)

    #fill in the next two 3x3 squares


    #recursively generate a full board from this seed

    #solvBoard(board)

def printMenu():
    print("\t\t" + "="*24)
    print("\t\t   Welcome to SUDOKU")
    print("\t\t" + "="*24)
    board = makeBoard()

printMenu()
