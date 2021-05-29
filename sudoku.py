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

def boxTwo(board, seed):
    #fill in the first column of the second box
    random.shuffle(seed)
    for i in range(0, 3):
        board[0][3+i] = seed[i]

    #possible values fo rows 2 and 3 in box 2
    R2I = list((set(board[0][:3]).union(set(board[2][:3]))) - set(board[0][3:6]))
    R3I = (set(board[0][:3]).union(set(board[1][:3]))) - set(board[0][3:6])
    print(R2I, R3I)

    #choose a set of values for row 2 that leaves enough values for row 3
    while(1):
        random.shuffle(R2I)
        R2N = R2I[:3]
        R3N = R3I - set(R2N)
        if(len(R3N) == 3):
            R3N = list(R3N)
            break

    #print(R2N, R3N)
    for i in range(0,3):
        board[1][i+3] = R2N[i]

    #numbers that can be in the 3rd row of the 2nd square

    for i in range(0,3):
        board[2][i+3] = R3N[i]

    return(board)

def boxOne(seed):
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
    print("\t " + "-"*39)


def makeBoard():
    #seed value
    seed = random.sample(range(1, 10), 9)
    board = boxOne(seed)
    #printBoard(board)

    #potential numbers for box 2 row 1
    seed2 = seed[3:]
    board = boxTwo(board, seed2)
    printBoard(board)

    #fill in the next two 3x3 squares


    #recursively generate a full board from this seed

    #solvBoard(board)

def printMenu():
    print("\t\t" + "="*24)
    print("\t\t   Welcome to SUDOKU")
    print("\t\t" + "="*24)
    board = makeBoard()

printMenu()
