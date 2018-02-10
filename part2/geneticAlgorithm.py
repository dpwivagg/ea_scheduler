#This is for Genetic Algorithm

original_map = {}
""" Change these to be the correct values during runtime """
map_width = 5
map_height = 5
industrial = 'I'
commercial = 'C'
residential = 'R'
toxic = 'X'
scenic = 'S'
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
        i = 0               # i and j are for iterating through the matrix
        j = 0
        # Calculating from the original map side
        distance = 0
        unit_score = 0
        industrial_score = 0
        commercial_score = 0
        residential_score = 0
        toxic_score = 0
        scenic_score = 0
        for i in range(0,map_height-1):
            for j in range(0,map_width-1):
                start = 0 #start of the loop in counting the number of tiles around a certain position
                end = 0
                if formed_map[i,j] == industrial:
                    distance = 2
                    unit_score = 3
                    industrial_score = industrial_score + \
                                       unit_score * find_terrain_in_distance(formed_map, distance, industrial, i, j)
                elif formed_map[i,j] == commercial:
                    # For residence close to commercial
                    distance = 3
                    unit_score = 5
                    residential_c_commercial_score = unit_score * \
                                                     find_terrain_in_distance(formed_map, distance, residential, i, j)
                    # For competition
                    distance = 2
                    unit_score = -5
                    commercial_c_commercial_score = unit_score * \
                                                    find_terrain_in_distance(formed_map, distance, commercial, i, j)
                    commercial_score = commercial_score + residential_c_commercial_score + commercial_c_commercial_score
                elif formed_map[i,j] == residential:
                    # For industrial close to residential
                    distance = 3
                    unit_score = -5
                    industrial_c_residential_score = unit_score * \
                                                     find_terrain_in_distance(formed_map, distance, industrial, i, j)
                    # For commercial close to residential
                    distance = 3
                    unit_score = 5
                    commercial_c_residential_score = unit_score * \
                                                     find_terrain_in_distance(formed_map, distance, commercial, i, j)
                    residential_score = residential_score + \
                                        industrial_c_residential_score + commercial_c_residential_score
                elif formed_map[i,j] == toxic:
                    # For Industrial close to toxic
                    distance = 2
                    unit_score = -10
                    industrial_c_toxic_score = unit_score * \
                                               find_terrain_in_distance(formed_map, distance, industrial, i, j)
                    # For Commercial close to toxic
                    distance = 2
                    unit_score = -20
                    commercial_c_toxic_score = unit_score * \
                                               find_terrain_in_distance(formed_map, distance, commercial, i, j)
                    # For Residential close to toxic
                    distance = 2
                    unit_score = -20
                    residential_c_toxic_score = unit_score * \
                                                find_terrain_in_distance(formed_map, distance, residential, i, j)
                    toxic_score = toxic_score + \
                                  industrial_c_toxic_score + commercial_c_toxic_score + residential_c_toxic_score
                elif formed_map[i,j] == scenic:
                    # Residential close to scenic
                    distance = 2
                    unit_score = 10
                    residential_c_scenic_score = unit_score * \
                                                 find_terrain_in_distance(formed_map, distance, residential, i, j)
                    scenic_score = scenic_score + residential_c_scenic_score
        self.fitness = self.fitness +\
                       toxic_score + scenic_score + industrial_score + residential_score + commercial_score
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

def find_terrain_in_distance(my_map, distance, terrain, row, col):
    count = 0
    for i in range(-distance,+distance):
        if (row+i)<0 or (row+i)>= map_height:    # check for out of bound horizontally
            continue
        for j in range (-i,i):
            if (col+j)<0 or (col+j)>= map_width: # check for out of bound vertically
                continue
            if i == 0 and j == 0:   # check for the original position
                continue
            if my_map[i,j] == terrain:
                count = count + 1
    return count
