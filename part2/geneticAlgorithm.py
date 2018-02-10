#This is for Genetic Algorithm

original_map = {}
""" Change these to be the correct values during runtime """
map_width = 5
map_height = 5

class map():
    def __init__(self, map_matrix):
        self.map_matrix = map_matrix
        self.fitness = self.fitness()

    def create_map(self):
        created_map = self.map_matrix
        return created_map

    def fitness(self):
        # Returns the integer fitness value
        # First fill in the map with the original
        formed_map = self.create_map()
        # Calculating from the original map side
        # Toxic waste
        # Scenic view
        # Calculating after placing the terrains

        # Industrial
        # Residential
        # Commercial
        pass

    def mutate(self):
        pass

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

