#sudoku game
import numpy as np
import random
import os

#written by Catherine Tate in python 3

count = 0


"""
#how the user interacts with the puzzle
def takeComs():
    print("Select an option:")
    print("0. Place Letter")
    print("1. Make Note")
    print("2. Check Notes")
    print("2. ")


process for creating the board:
1. generate filled grid
2. remove some #s (more/less for different difficulties?)
3. check if grid w/ numbers taken out has only 1 solution
"""

#turn a filled grid into a puzzle by removing some number of spots
def makePuzzle(board):
    global count

    #choose how many squares to remove at random
    numRem = random.randrange(55, (81-17))
    removed = 0

    puzzle = np.copy(board)
    #print(puzzle)
    tries = 3
    #still tweaking how many squares to remove/when to stop removing squares
    while(removed < 50):
        count = 0

        #pick a square at random
        row = random.randrange(9)
        col = random.randrange(9)
        while(puzzle[row][col] == 0):
            row = random.randrange(9)
            col = random.randrange(9)

        #save the value there in case we need it again
        save = puzzle[row][col]
        puzzle[row][col] = 0

        copyBoard = np.copy(puzzle)
        solveGrid(copyBoard)
        #print(count)
        if(count > 1):
            print("puzzle doesnt have unique solution")
            puzzle[row][col] = save
            tries -= 1
        else:
            removed += 1
    return(puzzle)

def validateBoard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if(board[i][j] == 0):
                return(False)
    return(True)




#function for checking if the board has multiple solutions
def solveGrid(board):
    global count

    if(count > 1): return(True)
    notes = makeNotes(board)

    #print(board)

    #check if board is full
    if(validateBoard(board)):
        count += 1
        return(True)

    #get first empty square
    for i in range(0, 9):
        for j in range(0, 9):
            if(board[i][j] == 0):
                break
        if(board[i][j] == 0):
            break

    spot = list(notes[i][j])
    random.shuffle(spot)
    #print(spot)

    for num in spot:
        board[i][j] = num
        if(solveGrid(board)):
            return(True)
        board[i][j] = 0
    return(False)

#recursive function to build the rest of the board from a given board.
def gridFill(board):
    notes = makeNotes(board)

    #check if board is full
    if(validateBoard(board)):
        return(True, board)

    #get first empty square
    for i in range(0, 9):
        for j in range(0, 9):
            if(board[i][j] == 0):
                break
        if(board[i][j] == 0):
            break

    spot = list(notes[i][j])
    random.shuffle(spot)

    for num in spot:
        board[i][j] = num
        if(gridFill(board)[0]):
            return(True, board)
        board[i][j] = 0
    return(False, board)


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
            if(board[i][j] != 0):
                print(" " + str(board[i][j]), end='')
            else:
                print("  ", end = '')
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
    filled, board = gridFill(board)

    solution = np.copy(board)

    board = makePuzzle(board)
    #print(notes)

    # next, remove numbers at random from the board
    # resulting "problems" must have only 1 unique solution

    printBoard(board)
    return(board, solution)

def solveBoard():
    fileName = input("Please enter filename of puzzle: ")

    try:
        puzzleFile = open(fileName, "r")
    except IOError:
        print("File not found")
        return

    puzzle = []
    lines = puzzleFile.readlines()
    #print(lines)
    for i in range(len(lines)):
        line = lines[i].strip("\n")
        row = []
        #print(line)
        for j in range(len(line)):
            if(line[j] == "X"):
                row.append(0)
            else:
                row.append(int(line[j]))
        puzzle.append(row)

    puzzleFile.close()

    printBoard(puzzle)

    x, solution = gridFill(puzzle)
    printBoard(solution)

    solFileName = fileName.split(".")[0] + ".sln.txt"

    solFile = open(solFileName, "w")
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            solFile.write(str(solution[i][j]))
        solFile.write("\n")
    solFile.close()

def genBoard():
    print("Generating Puzzle.....")
    #get number of existing puzzle files in the folder
    puzCount = 1
    for file in os.listdir("."):
        if "puzzle"in file:
            if ".sln.txt" not in file:
                puzCount+=1
    puzName = "puzzle" + str(puzCount) + ".txt"

    board = makeBoard()[0]
    #printBoard(board)

    puzFile = open(puzName, "w")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                puzFile.write("X")
            else:
                puzFile.write(str(board[i][j]))
        puzFile.write("\n")
    puzFile.close()

def printMenu():
    print("\t\t" + "="*24)
    print("\t\t   Welcome to SUDOKU")
    print("\t\t" + "="*24)
    #print("\n[Preparing Board]")
    #board, solution = makeBoard()

    print("Menu:")
    print("0. Generate Puzzle")
    print("1. Solve Puzzle")
    choice = ""

    while(choice != "0" and choice != "1"):
        print("Invalid option")
        choice = input("\nGenerate Puzzle or Solve Puzzle? ")[0]

    if(choice == "0"):
        genBoard()
        return
    elif(choice == "1"):
        solveBoard()
        return

printMenu()
