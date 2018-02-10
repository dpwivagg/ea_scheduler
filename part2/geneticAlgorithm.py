#This is for Genetic Algorithm

original_map = {}

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
        pass


def crossover(map1, map2):
    pass

