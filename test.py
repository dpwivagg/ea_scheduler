import astar

board = astar.gameBoard([0,0,0,0,0,0,0,0])

# for b in board.getChildren():
#     print(b.positionArray)
astar.astarRun(board)