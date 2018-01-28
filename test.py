from astar import gameBoard

board = gameBoard([0,0,0], 5)
for i in board.getChildren():
    print(i.positionArray)