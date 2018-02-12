from part1 import astar
import random

def run_astar():
    board_size = input("Enter board size: ")
    ID = input("Want iterative deepening? Y/N ")
    while(ID != 'Y' and ID != 'N'):
        ID = input("In valid input! Type in ans again. Want iterative deepening? Y/N ")
    print("Randomly generating board...")
    board = [random.randint(0, int(board_size)-1) for i in range(0, int(board_size))]
    print("Generated " + str(board))
    print("Running A*...")
    astar.astarRun(board,ID)


run_astar()