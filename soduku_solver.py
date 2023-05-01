"""
Sudoku Solver
Completed November 2021 using Python
Author: Laura White
"""


board4x4_1 = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

board4x4_2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

board9x9_1 =[[0, 5, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 8, 0, 0, 0, 0, 2, 0],
       [6, 0, 0, 9, 0, 5, 0, 0, 7],
       [3, 0, 0, 0, 4, 0, 0, 0, 0],
       [0, 2, 0, 1, 0, 3, 0, 7, 0],
       [0, 0, 0, 0, 6, 0, 0, 0, 1],
       [5, 0, 0, 3, 0, 7, 0, 0, 9],
       [0, 0, 0, 0, 0, 4, 0, 0, 0],
       [0, 6, 0, 0, 0, 0, 5, 0, 0]]

board9x9_2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

board9x9_3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

board9x9_4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

board16x16_1 = [[ 0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [ 7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [ 1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [ 0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [ 8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [ 5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [ 0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [ 2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [ 0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [ 0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [ 0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [ 0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

board16x16_2 = [[ 0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [ 1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [ 0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [ 0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [ 4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [ 3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [ 0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [ 9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [ 0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [ 8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [ 0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

board16x16_3 = [[ 0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [ 0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [ 0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [ 3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [ 0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [ 6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [ 0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [ 0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [ 0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [ 1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [ 0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]


from math import sqrt
import random


def print_board(board):
    """
    Prints the list form of the sudoku board in a more visually appealing manner so that the user can
    see clearly each row and column and play the game more easily.

    Input : a Sudoku board (board) of size 4x4, 9x9, or 16x16
    Output: formatted sudoku board
    """
    leng=len(board)
    leng1=int(leng)
    sqr=sqrt(leng)
    sqr1= int(sqr)
    #count used for finished message
    count = 0
    #creates the top border for the board
    print(('-'*((leng*3)+sqr1)))
    #for each value in the list
    for i in range(leng):
        for j in range(leng):
            if j%sqr1==0:
                print("|", end=" ")
            if board[i][j] != 0 and board[i][j] < 10:
                print(f"{board[i][j]} ", end="")
            else:
                if board[i][j] == 0:
                    print(" ", end=" ")
                if board[i][j] == 10:
                    print("A", end=" ")
                if board[i][j] == 11:
                    print("B", end=" ")
                if board[i][j] == 12:
                    print("C", end=" ")
                if board[i][j] == 13:
                    print("D", end=" ")
                if board[i][j] == 14:
                    print("E", end=" ")
                if board[i][j] == 15:
                    print("F", end=" ")
                if board[i][j] == 16:
                    print("G", end=" ")
                #creating column borders
                #print list values
        print(f"", end="|")
        #print row borders
        if i in range(-1, leng, sqr1):
            print("\n" + ('-'*((leng*3)+sqr1)), end="")
        print('')
    #if 0/ empty space is in list i.e. board is not complete, increase count
    for lst in board:
        for i in lst:
            if i == 0:
                count+=1
    #if board complete print message
    if count == 0:
        print("Sudoku is complete")
        

 
def subgrid_values(board, r, c):
    """
    subgrid values is used to show all values that are in grid related to row and column values r and c            
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that are present in the subgrid of the board related to the
            field (r, c)
    """
    n = len(board)
    k = round(sqrt(n))
    res = []
    for i in range((r // k) * k, ((r // k) + 1) * k):
        for j in range((c // k) * k, ((c // k) + 1) * k):
            if board[i][j]:
                res.append(board[i][j])
    return res 
    pass


def options(board, i, j):
    """
    options function tells the user what they can enter into a position

    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that player is allowed to place on field (r, c),
        i.e., those that are not already present in row r, column c,
        and subgrid related to field (r, c)
     """
    if board[i][j]:
        return []
    res = []
    n = len(board)
    k = round(sqrt(n))    
    col_vals = [board[s][j] for s in range(n)]
    row_vals = board[i]
    subgrid_vals = subgrid_values(board, i, j)
    for x in range(1, n+1):
        if x not in col_vals and x not in row_vals and x not in subgrid_vals:
            res.append(x)
    return res
    pass
                        
def play(board):
    """
    Input : Sudoku board
    Output: None
    Effect: Allows user to play board via console
    """
    print_board(board)
    #lists used for undo/ restart functions
    new_board = []
    moves = []
    moves1=[]
    #converting useful/commonly used numbers to int
    leng=len(board)
    leng1=int(leng)
    sqr= sqrt(leng)
    sqr1= int(sqr)
    while True:
        #add board to moves, creating a large list with all moves documented
        for lst in range(0, len(board)):
            for i in range(0, len(board)):
                moves.append(board[lst][i])
        inp = input().split(' ')
        if len(inp) == 3 and inp[0].isdecimal() and inp[1].isdecimal() and inp[2].isdecimal():
            intinp = [int(x) for x in inp]
            a = int(inp[0])
            b = int(inp[1])
            c = int(inp[2])
            if a<(len(board)) and b<(len(board)) and c<(len(board)+1):
                i = int(inp[0])
                j = int(inp[1])
                x = int(inp[2])
                board[i][j] = x
                print_board(board)
                #print error message if input is over length of board eg. for small user cannot input 5
            elif a>len(board) and b>len(board) and c>(len(board)+1):
                print('input was out of length')
            else:
                print('input was out of length')
        elif len(inp)==3 and (inp[0] == 'n' or inp[0] == 'new') and inp[1].isdecimal() and inp[2].isdecimal():
            k = int(inp[1])
            d = int(inp[2])
            if k < len(sudokus) and 0 < d <= len(sudokus[k]):
                board = sudokus[k][d-1]
                print_board(board)
            else:
                print('board not found')
        #undo function
        elif inp[0] == 'u' or inp[0] == 'undo':
            #moves1 takes moves and turns it into list with sublists
            print(moves)
            #while i is in range of 0-length, every four items starting from moves[0] will become a sublist of 4 creating the rows of board
            moves1= [moves[i:i+leng] for i in range(0, len(moves), leng)]
            #clears board
            board = []
            #board takes the value of previous board
            for i in range((len(moves1)-(2*leng)), (len(moves1)-leng)):
                board.append(moves1[i])
            print_board(board)
        #restart function
        elif inp[0] == 'r' or inp[0] == 'restart':
            #same use as restart function however board takes value of first 4 sublists of moves1, the original board
            moves1= [moves[i:i+leng] for i in range(0, len(moves), leng)]
            board = []
            for i in range(0, leng):
                board.append(moves1[i])
            print_board(board)
        elif inp[0] == 'q' or inp[0] == 'quit':
            return
        elif inp[0] == 'i' or inp[0] == 'infer':
            playinfer(board)
            new_board += board
            inferred(new_board)
            print_board(new_board)
            play(board)
        elif inp[0] == 's' or inp[0] == 'solve':
            new_board += board
            solver(new_board)
            print_board(new_board)
            play(board)
        elif len(inp)==2 and (inp[0] == 'g' or inp[0] == 'generate') and inp[1].isdecimal():
            n = int(inp[1])
            generate(n)
        else:
            print('Invalid input')
        


def value_by_single(board, r, c):
    """
    Input : board, row, and column index
    Output: The correct value for field (i, j) in board if it can be inferred as
            either a forward or a backward single; or None otherwise.
    """
    rowvalue = []
    columnvalue = []
    gridvalue = []
    n = len(board)
    k = round(sqrt(n))
    option = options(board, r, c)
    solve = []
    #if there is only one item returned from options function, grid value must be equal to this
    if len(option) == 1:
        return option[0]
    else:
        #finds the options for all other grid values
        for i in range((r // k) * k, ((r // k) + 1) * k):
            for j in range((c // k) * k, ((c // k) + 1) * k):
                if board[i][j] == 0:
                    gridvalue += (options(board, i, j))
        #removes board[r][c] values from gridvalues list
        for x in option:
            if x in gridvalue:
                gridvalue.remove(x)
        #finds option values for row items
        for i in range(0, n):
            if board[r][i] == 0: 
                rowvalue += options(board, r, i)
            #finds option values for column items
            if board[i][c] == 0: 
                columnvalue += options(board, i, c)
        #removes r,c options from list
        for x in option:
            if x in rowvalue:
                rowvalue.remove(x)
        for x in option:
            if x in columnvalue:
                columnvalue.remove(x)
        #if there is an item that is an option for r,c that is not an option for any other row grid or column item, item is equal to this
        for item in option:
            if item not in rowvalue or item not in columnvalue or item not in gridvalue:
                solve.append(item)
        #return if solve is length of 1, else return None
        if len(solve) == 1:
            return solve[0]
        
    pass

def inferred(board):
    """initiates solve function if there are still zeros in board """
    #if no zeroes in board (board is solves) return board to user
    if (any(0 in i for i in board) == False):
        return board
    else:
        solve(board)


def solve(board):
    """
    Input : Sudoku board
    Output: new Soduko board with all values field from input board plus
            all values that can be inferred by repeated application of 
            forward and backward single rule
    """
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            #if item is equal to zero and value by single returns a value, change board value to value by single output
            if board[i][j] == 0:
                if value_by_single(board, i, j) != None:
                    board[i][j] = value_by_single(board, i, j)
    #loops back to inferred function, if there are still zeros in the function, solve function will repeat
    #this results in some recursion limits for some big and giant boards
    inferred(board)
    pass

def solver(board):
    """
    calls the necessary functions to solve the board
    """
    for i in range(0,50):
        infer_board(board)
    backtrack(board)
    play(board)


def checkfull(board):
    """
    checks if any remaining zero in the board

    """
    if not any(0 in i for i in board):
        return True
    else:
        return False


def backtrack(board):
    """
    solves boards using backtracking
    """
    if checkfull(board):
        return True
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                #search through options for each item
                for x in range(0, len(options(board, i, j))):
                        board[i][j] = (options(board, i, j)[x])
                        if backtrack(board):
                            return True
                        #if this option does not work, revert back to 0
                        board[i][j] = 0
                return False


def infer_board(board):
    """
    
    """
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            #if item is equal to zero and value by single returns a value, change board value to value by single output
            if board[i][j] == 0:
                if value_by_single(board, i, j) != None:
                    board[i][j] = value_by_single(board, i, j)


def generate(n):
    """
    Generates a playable sudoku board
    """
    board = []
    #first row in board is made up from numbers 1-9
    for i in range(0, 1):
        board.append([])
        for j in range(1, n**2+1):
            board[i].append(j)
    #all other rows made up of zeros
    for i in range(1, n**2):
        board.append([])
        for j in range(n**2):
            board[i].append(0)
    #shuffle numbers 1-9 in random order
    random.shuffle(board[0])
    #use backtracking function to solve/ fill in rest of the board
    backtrack(board)
    perc = int((n**2)*3/4)
    for i in random.sample(range(0, (n**2)), perc):
        for j in random.sample(range(0, (n**2)), perc):
            board[i][j] = 0
    play(board)





solver(board9x9_1)
print_board(board9x9_1)
