#This is for Genetic Algorithm
import random

original_map = {}
""" Change these to be the correct values during runtime """
map_width = 5
map_height = 5

class map():
    def __init__(self, map_matrix):
        self.map_matrix = map_matrix
        self.fitness = self.fitness() - self.cost_to_build()

    def cost_to_build(self):
        cost = 0
        for key, value in original_map:
            type = self.map_matrix[key]
            if type == "C" or type == "R" or type == "I":
                cost += value

    def fitness(self):
        # Returns the integer fitness value
        pass

    def mutate(self):
        x1, y1 = random.randint(0, map_width), random.randint(0, map_height)
        x2, y2 = random.randint(0, map_width), random.randint(0, map_height)
        while original_map[x1, y1] == "X" or original_map[x2, y2] == "X":
            x1, y1 = random.randint(0, map_width), random.randint(0, map_height)
            x2, y2 = random.randint(0, map_width), random.randint(0, map_height)

        oldVal = self.map_matrix[x1, y1]
        newVal = self.map_matrix[x2, y2]
        self.map_matrix[x1, y1] = newVal
        self.map_matrix[x2, y2] = oldVal

    def crossover(self, other):
        first_new_map = {}
        second_new_map = {}
        for i in range(0, map_width//2):
            for j in range(0, map_height):
                first_new_map[i, j] = self.map_matrix[i, j]
                second_new_map[i, j] = other.map_matrix[i, j]

        for i in range(map_width//2, map_width):
            for j in range(0, map_height):
                first_new_map[i, j] = other.map_matrix[i, j]
                second_new_map[i, j] = self.map_matrix[i, j]


def crossover(map1, map2):
    pass

