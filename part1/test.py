from part1 import astar
import random

def run_astar():
    board_size = input("Enter board size: ")
    print("Randomly generating board...")
    board = [random.randint(0, int(board_size)-1) for i in range(0, int(board_size))]
    print("Generated " + str(board))
    print("Running A*...")
    astar.astarRun(board)


run_astar()