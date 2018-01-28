import heapq

from copy import deepcopy

"""
Heapq.heappush: Add an item to the priority queue
Heapq.heappop: Remove the smallest item from the queue
"""

class gameBoard():
    def __init__(self, positionArray, actionCost):
        self.positionArray = positionArray
        self.actionCost = actionCost # This is g(n)
        self.heuristic = self.numberQueensAttacked() + 10 # This is h(n)
        # print(self.heuristic)

    def __lt__(self, other):
        return (self.actionCost + self.heuristic) < (other.actionCost + other.heuristic)

    def getChildren(self):
        firstCount = 0
        objectList = []
        while firstCount<len(self.positionArray):
            secondCount = 0
            while secondCount<len(self.positionArray):
                if secondCount != self.positionArray[firstCount]:
                    newPositionArray = deepcopy(self.positionArray)
                    newPositionArray[firstCount] = secondCount
                    aCost = 10 + abs(secondCount-firstCount)*abs(secondCount-firstCount)
                    childBoard = gameBoard(newPositionArray,aCost)
                    objectList.append(childBoard)
                secondCount += 1
            firstCount += 1
        return objectList

    def numberQueensAttacked(self):
        # Fill in this function to return number of queens attacked
        numAttacks =0
        firstCount = 0
        while firstCount<len(self.positionArray):
            secondCount = firstCount + 1
            while secondCount<len(self.positionArray):
                if self.positionArray[firstCount]==self.positionArray[secondCount]:
                    numAttacks = numAttacks+1
                if (self.positionArray[firstCount]+(secondCount-firstCount))==self.positionArray[secondCount]:
                    numAttacks = numAttacks+1
                if (self.positionArray[firstCount]-(secondCount-firstCount))==self.positionArray[secondCount]:
                    numAttacks = numAttacks+1
                secondCount = secondCount+1
            firstCount = firstCount+1
        return numAttacks

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

