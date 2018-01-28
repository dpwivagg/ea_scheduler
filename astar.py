import heapq
"""
Heapq.heappush: Add an item to the priority queue
Heapq.heappop: Remove the smallest item from the queue
"""

class gameBoard():
    def __init__(self, positionArray, actionCost):
        self.positionArray = positionArray
        self.actionCost = actionCost # This is g(n)
        self.heuristic = self.numberQueensAttacked() + 10 # This is h(n)

    def __lt__(self, other):
        return (self.actionCost + self.heuristic) < (other.actionCost + other.heuristic)

    def getChildren(self):
        pass

    def numberQueensAttacked(self):
        # Fill in this function to return number of queens attacked
        return self.positionArray

def astar(currentBoard):
    frontier = []
    heapq.heappush(frontier, currentBoard)

    while frontier:
        # Pop the priority queue -- done
        # Evaluate the current board--is it the solution? -- done
        # Expand the current board -- done
        # Add expanded nodes to priority queue -- done
        board = heapq.heappop(frontier)
        if board.heuristic == 0:
            print("Board found")
            return board # Need to return some other stuff too

        else:
            heapq.heappush(frontier, (newBoard for newBoard in board.getChildren()))

    pass

