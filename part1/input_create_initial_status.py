import random

# Input to define the board size.
# It won't permit the number of queens less than 4, because 3-queens problem will not have a solution.
def take_input():

    while True:
        try:
            size = int(input('What is the size of the chessboard? n = \n'))
            if size == 1:
                print("Trivial solution, choose a board size of atleast 4")
            if size <= 3:
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")           

# Create the initial board randomly.
def get_board(size):
    board = []
    for i in range(size):
        k = random.sample(range(0,size-1),1)
        board = board + k
        i += 1
    print(board)
    return board
    
size = take_input()
board = get_board(size)
