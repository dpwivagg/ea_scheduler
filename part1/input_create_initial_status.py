import random
from part1 import astar
from part1 import hill_climbing
# Input to define the board size.
# It won't permit the number of queens less than 4, because 3-queens problem will not have a solution.
from part1.hill_climbing import Queens


def take_input():

    size = 0
    algorithm = ""
    while True:
        while True:
            try:
                size = int(input('What is the size of the chessboard? n = \n'))
                if size == 1:
                    print('Trivial solution, choose a board size of atleast 4')
                if size <= 3:
                    print('Enter a value such that size>=4')
                    continue
                break
            except ValueError:
                print('Invalid value entered. Enter again')
        while True:
            try:
                algorithm = str(input('What algorithm do you want to use? a. AStat b.hill_climb\n'))
                if algorithm != 'a'and algorithm != 'b':
                    print('Enter a value from a or b')
                    continue
                else:
                    board = [random.randint(0, int(size) - 1) for i in range(0, int(size))]
                    print("Generated " + str(board))
                    if algorithm == 'a':
                        print("Running A*...")
                        ID = input('Want iterative deepening? Y/N \n')
                        while (ID != 'Y' and ID != 'N'):
                            ID = input("In valid input! Type in ans again. Want iterative deepening? Y/N \n")
                        astar.astarRun(board, ID)
                        break
                    elif algorithm == 'b':
                        print("Running Hill Climb...")
                        Queens(board)
                        break
            except ValueError:
                print("Invalid value entered. Enter again")
        ans = str(input('Do you want to play again? Y/N\n'))
        while ans!='Y'and ans!='N':
            ans= str(input('Please type in the correct value. Do you want to play again? Y/N \n'))
        if ans == 'N':
            break



# # Create the initial board randomly.

take_input()
# board = get_board(size)
