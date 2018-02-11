import heapq
import datetime
from copy import deepcopy


"""
Heapq.heappush: Add an item to the priority queue
Heapq.heappop: Remove the smallest item from the queue
"""

class gameBoard():
    def __init__(self, positionArray, actionCost=0,parentBoard = None,heuristicOriginal = 0):
        self.positionArray = positionArray
        self.actionCost = actionCost # This is g(n)
        self.heuristic = self.numberQueensAttacked() # This is h(n)
        self.priorityQueueCost = heuristicOriginal + self.numberQueensAttacked()
        self.parentBoard = parentBoard
        # print(self.priorityQueueCost)

    def __lt__(self, other):
        # return (self.actionCost + self.heuristic) < (other.actionCost + other.heuristic)
        return self.priorityQueueCost< other.priorityQueueCost

    def __eq__(self, other):
        return self.positionArray == other.positionArray

    def __cmp__(self, other):
        return (self.priorityQueueCost> other.priorityQueueCost)-(self.priorityQueueCost< other.priorityQueueCost)

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return "gameBoard(%s)" % (self.positionArray)

    def __str__(self):
        string = ""
        for row in range(0, len(self.positionArray)):
            string = string + "\n|"
            for column in range(0, len(self.positionArray)):
                if row == self.positionArray[column]:
                    string = string + "Q|"
                else:
                    string = string + " |"

        return string

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
                    childBoard = gameBoard(newPositionArray,aCost,self,self.actionCost)
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


def astarRun(passBoard):
    currentBoard = gameBoard(passBoard)
    frontier = []
    explored = set()
    # TODO: Need a list or something to backtrack the path (and compute effective branching factor)
    solutionPath = []
    heapq.heappush(frontier, currentBoard)
    solution = None
    backTrackBoard = None
    expansions = 0
    starttime = datetime.datetime.now()
    board = None
    limit = 20
    while frontier:
        # Pop the priority queue -- done
        # Evaluate the current board--is it the solution? -- done
        # Expand the current board -- done
        # Add expanded nodes to priority queue -- done
        board = heapq.heappop(frontier)
        # print(board.priorityQueueCost)
        # TODO: Add a failsafe for infinite loops, when there is no solution (as in 2x2 and 3x3)
        # Is there any other place that needs a fail safe checks
        # We will have this in condition check before entering the algorithm.
        if board.heuristic == 0:
            endtime = datetime.datetime.now()
            print("Board found: " + str(board.positionArray))
            print(board);
            print("No. Boards Expanded: " + str(expansions))
            print("Time taken to solve: " + str(endtime - starttime))
            print("Cost of final board: " + str(board.actionCost))
            solution = board
            break
        else:
            expansions += 1
            # starttime = datetime.datetime.now()
            for newBoard in board.getChildren():
                if newBoard not in explored:
                    explored.add(newBoard)
                    heapq.heappush(frontier, newBoard)
            # endtime = datetime.datetime.now()
            # print(endtime - starttime)


    backTrackBoard = board
    if backTrackBoard is not None:
        while backTrackBoard.parentBoard:
            solutionPath.append(backTrackBoard)
            backTrackBoard = backTrackBoard.parentBoard
        solutionPath.append(backTrackBoard)
        solutionPath.reverse()

    if solutionPath is not None:
        print("Path Length: "+str(len(solutionPath)))
        print("Effective Branching Factor: " + str(expansions /len(solutionPath)));
        print("Path starts:")
        for aBoard in solutionPath:
             print(aBoard)
        print("Path ends.")
    else:
        print("No solution")
    return board  # Need to return some other stuff too


