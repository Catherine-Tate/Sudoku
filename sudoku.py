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

#recursive function to build the rest of the board from a given board.
#also takes a set of "notes" which are possible numbers for each square.
#filled squares have no value in their notes section
def gridFill(board, notes):
    #find the square with the fewest possible numbers
    min = 0
    for i in range(0,81):
        if(len(notes[i] < len(notes[min]))):
            min = i
    row = min/9
    col = min%9
    #for i in range(0, len(notes[min])):


def makeNotes(board):
    #start with each number being possible for each square
    notes = []
    for i in range(0, 9):
        rowNotes = []
        for j in range(0, 9):
            rowNotes.append({1, 2, 3, 4, 5, 6, 7, 8, 9})
        notes.append(rowNotes)
    #remove numbers as possibilities from the notes
    for i in range(0, 9):
        for j in range(0, 9):
            #if a square is filled:
            if(board[i][j] != 0):
                #remove the notes for that square
                notes[i][j].clear()
                #remove that number from the notes of all related squares (row, column, 3x3)
                for k in range(0, 9):
                    notes[k][j] -= {board[i][j]}
                    notes[i][k] -= {board[i][j]}
                row = i%3
                col = j%3

#fill in the leftmost column
def lCol(board):
    base = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(0, 3):
        base = base - set({board[i][0]})
    #print(base)
    lColNums = list(base)
    random.shuffle(lColNums)
    for i in range(0, 6):
        board[i+3][0] = lColNums[i]
    return(board)

#fill in the last box based on the first 6 numbers in each filled row
def boxThree(board):
    base = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    R1N = base - set(board[0][:6])
    R2N = base - set(board[1][:6])
    R3N = base - set(board[2][:6])

    R1N = list(R1N)
    R2N = list(R2N)
    R3N = list(R3N)

    random.shuffle(R1N)
    random.shuffle(R2N)
    random.shuffle(R3N)

    for i in range(0, 3):
        board[0][6+i] = R1N[i]
        board[1][6+i] = R2N[i]
        board[2][6+i] = R3N[i]

    return(board)

def boxTwo(board, seed):
    #fill in the first column of the second box
    random.shuffle(seed)
    for i in range(0, 3):
        board[0][3+i] = seed[i]

    #possible values fo rows 2 and 3 in box 2
    R2I = list((set(board[0][:3]).union(set(board[2][:3]))) - set(board[0][3:6]))
    R3I = (set(board[0][:3]).union(set(board[1][:3]))) - set(board[0][3:6])
    #print(R2I, R3I)

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

#Generate numbers 1-9 in a random order to fill the first 3x3 box
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
def solveBoard(board):
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

    #fill in the 2nd box
    board = boxTwo(board, seed2)

    #fill in the third box
    board = boxThree(board)

    board = lCol(board)

    notes = makeNotes(board)
    board = gridfill(board, notes)

    printBoard(board)


def printMenu():
    print("\t\t" + "="*24)
    print("\t\t   Welcome to SUDOKU")
    print("\t\t" + "="*24)
    board = makeBoard()

printMenu()
