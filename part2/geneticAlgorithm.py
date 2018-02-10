#This is for Genetic Algorithm
import random

class map():
    def __init__(self, maprow, mapcol, original_map, map_matrix):
        self.map_matrix = map_matrix
        self.maprow = maprow
        self.mapcol = mapcol
        self.original_map = original_map
        #self.fitness = self.fitness() - self.cost_to_build()

    def __str__(self):
        string = ""
        for row in range(0, self.maprow):
            string = string + "\n|"
            for column in range(0, self.mapcol):
                if self.map_matrix[row, column] == 0:
                    string = string + " |"
                else:
                    string = string + self.map_matrix[row, column] + "|"

        return string

    def cost_to_build(self):
        cost = 0
        for key, value in self.original_map:
            type = self.map_matrix[key]
            if not type == 0:
                cost += value

        return cost

    def fitness(self):
        # Returns the integer fitness value
        pass

    def mutate(self):
        rows = self.maprow - 1
        cols = self.mapcol - 1
        x1, y1 = random.randint(0, rows), random.randint(0, cols)
        x2, y2 = random.randint(0, rows), random.randint(0, cols)
        while self.original_map[x1, y1] == 'X' or self.original_map[x2, y2] == 'X' or self.map_matrix[x1, y1] == 0 or self.map_matrix[x2, y2] == 0:
            x1, y1 = random.randint(0, rows), random.randint(0, cols)
            x2, y2 = random.randint(0, rows), random.randint(0, cols)

        oldVal = self.map_matrix[x1, y1]
        newVal = self.map_matrix[x2, y2]
        self.map_matrix[x1, y1] = newVal
        self.map_matrix[x2, y2] = oldVal

    def crossover(self, other):
        first_new_map = {}
        second_new_map = {}
        for i in range(0, self.maprow // 2):
            for j in range(0, self.mapcol):
                first_new_map[i, j] = self.map_matrix[i, j]
                second_new_map[i, j] = other.map_matrix[i, j]

        for i in range(self.maprow // 2, self.maprow):
            for j in range(0, self.mapcol):
                first_new_map[i, j] = other.map_matrix[i, j]
                second_new_map[i, j] = self.map_matrix[i, j]

