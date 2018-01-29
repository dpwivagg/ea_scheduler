import heapq
import datetime
from copy import deepcopy

"""
Heapq.heappush: Add an item to the priority queue
Heapq.heappop: Remove the smallest item from the queue
"""

class gameBoard():
    def __init__(self, positionArray, actionCost=0):
        self.positionArray = positionArray
        self.actionCost = actionCost # This is g(n)
        self.heuristic = self.numberQueensAttacked() # This is h(n)
        # print(self.heuristic)

    def __lt__(self, other):
        return (self.actionCost + self.heuristic) < (other.actionCost + other.heuristic)

    def __eq__(self, other):
        return self.positionArray == other.positionArray

    def getChildren(self):
        firstCount = 0
        objectList = []
        while firstCount<len(self.positionArray):
            secondCount = 0
            while secondCount<len(self.positionArray):
                if secondCount != self.positionArray[firstCount]:
                    newPositionArray = deepcopy(self.positionArray)
                    newPositionArray[firstCount] = secondCount
                    aCost = self.actionCost + 10 + abs(secondCount-self.positionArray[firstCount])**2
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

        if numAttacks == 0:
            return numAttacks
        else:
            return numAttacks + 10


def astarRun(currentBoard):
    frontier = []
    explored = []
    # TODO: Need a list or something to backtrack the path (and compute effective branching factor)
    heapq.heappush(frontier, currentBoard)

    expansions = 0
    starttime = datetime.datetime.now()

    while frontier:
        # Pop the priority queue -- done
        # Evaluate the current board--is it the solution? -- done
        # Expand the current board -- done
        # Add expanded nodes to priority queue -- done
        board = heapq.heappop(frontier)

        # TODO: Add a failsafe for infinite loops, when there is no solution (as in 2x2 and 3x3)
        if board.heuristic == 0:
            endtime = datetime.datetime.now()
            print("Board found: " + str(board.positionArray))
            print("No. Boards Expanded: " + str(expansions))
            print("Time taken to solve: " + str(endtime - starttime))
            print("Cost of final board: " + str(board.actionCost))
            return board # Need to return some other stuff too

        else:
            expansions += 1
            for newBoard in board.getChildren():
                if newBoard not in explored:
                    explored.append(newBoard)
                    heapq.heappush(frontier, newBoard)

    pass

