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

#function for checking if the board has multiple solutions
def solveGrid(board, count):
    notes = makeNotes(board)
    row = 0
    col = 0
    tot = 0
    for i in range(0,9):
        for j in range(0, 9):
            tot += len(notes[i][j])
            if(board[i][j] == 0 and board[row][col] != 0):
                row, col = i,j
            #dont count filled in squares
            if((len(notes[i][j]) < len(notes[row][col])) and board[i][j] == 0):
                row, col = i,j

    #no possible numbers for any square, board is complete
    if(tot == 0):
        count+=1
        return(count)

    spot = list(notes[row][col])
    #the function got stuck, restart and try again
    if(len(spot) == 0):
        return(count)

    random.shuffle(spot)
    for i in range(0, len(spot)):
        newBoard = board
        newBoard[row][col] = spot[i]
        return(solveGrid(newBoard))

#recursive function to build the rest of the board from a given board.
#also takes a set of "notes" which are possible numbers for each square.
#filled squares have no value in their notes section
def gridFill(board, notes):
    #print("\n")
    #printBoard(board)
    #find the square with the fewest possible numbers
    row = 0
    col = 0
    tot = 0
    for i in range(0,9):
        for j in range(0, 9):
            tot += len(notes[i][j])
            if(board[i][j] == 0 and board[row][col] != 0):
                row, col = i,j
            #dont count filled in squares
            if((len(notes[i][j]) < len(notes[row][col])) and board[i][j] == 0):
                row, col = i,j
    #no possible numbers for any square, board is complete
    if(tot == 0):
        return(board, 0)

    spot = list(notes[row][col])
    #the function got stuck, restart and try again
    if(len(spot) == 0):
        return(board, 1)

    random.shuffle(spot)
    for i in range(0, len(spot)):
        newBoard = board
        newBoard[row][col] = spot[i]
        newNotes = makeNotes(newBoard)
        return(gridFill(newBoard, newNotes))

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
        #xbox and ybox are used for tracking which 3x3 square the index falls under
        xbox = (int(i/3))*3
        for j in range(0, 9):
            ybox = (int(j/3))*3
            #if a square is filled:
            if(board[i][j] != 0):
                #remove the notes for that square
                notes[i][j].clear()
                #remove that number from the notes of all indices in the same row/column
                for k in range(0, 9):
                    notes[k][j] -= {board[i][j]}
                    notes[i][k] -= {board[i][j]}
                #remove that number from the notes of all indices in the same 3x3 square
                for k in range(xbox, xbox+3):
                    for l in range(ybox, ybox+3):
                        notes[k][l] -= {board[i][j]}
    return(notes)

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
    x = 1
    #band-aid fix to make sure the generation always makes a completed board
    while(x == 1):
        board, x = gridFill(board, notes)
    #print(notes)

    # next, remove numbers at random from the board
    # resulting "problems" must have only 1 unique solution

    printBoard(board)


def printMenu():
    print("\t\t" + "="*24)
    print("\t\t   Welcome to SUDOKU")
    print("\t\t" + "="*24)
    board = makeBoard()

printMenu()
