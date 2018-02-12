from part1 import astar
import random

def run_astar():
    board_size = input("Enter board size: ")
    print("Randomly generating board...")
    board = [random.randint(0, board_size) for i in range(0, board_size)]
    print("Generated " + str(board))
    print("Running A*...")
    astar.astarRun(board)


run_astar()