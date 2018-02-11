# This is for Genetic Algorithm
import random

original_map = {}
industrial = 'I'
commercial = 'C'
residential = 'R'
toxic = 'X'
scenic = 'S'


class map():
    def __init__(self, maprow, mapcol, original_map, map_matrix):
        self.map_matrix = map_matrix
        self.maprow = maprow
        self.mapcol = mapcol
        self.original_map = original_map
        self.fitness_score = 0
        # self.fitness()

    def __str__(self):
        string = ""
        for row in range(0, self.maprow):
            string = string + "\n|"
            for column in range(0, self.mapcol):
                # if isinstance(self.map_matrix[row, column], int):
                #     string = string + " |"
                # else:
                #     string = string + str(self.map_matrix[row, column]) + "|"
                if self.map_matrix[row, column] == 0:
                    string = string + " |"
                else:
                    string = string + str(self.map_matrix[row, column]) + "|"

        return string

    def cost_to_build(self):
        cost = 0
        print(self)
        for key, value in self.original_map.items():
            type = self.map_matrix[key]
            if type != 0 and  value != toxic and value != scenic:
                print("value "+str(value)+" type "+str(type))
                cost += value

        return cost

    def create_map(self):
        map = {}
        for i in range(0, self.maprow):
            for j in range(0, self.mapcol):
                if self.map_matrix[i, j] == 0:
                    map[i, j] = self.original_map[i, j]
                else:
                    map[i, j] = self.map_matrix[i, j]
        return map

    def fitness(self):
        # Returns the integer fitness value
        # First fill in the map with the original
        formed_map = self.create_map()
        build_cost = self.cost_to_build()
        i = 0  # i and j are for iterating through the matrix
        j = 0
        # Calculating from the original map side
        distance = 0
        unit_score = 0
        industrial_score = 0
        commercial_score = 0
        residential_score = 0
        toxic_score = 0
        scenic_score = 0
        for i in range(0, self.maprow):
            for j in range(0, self.mapcol):
                start = 0  # start of the loop in counting the number of tiles around a certain position
                end = 0
                if formed_map[i, j] == industrial:
                    distance = 2
                    unit_score = 3
                    industrial_score = industrial_score + \
                                       unit_score * self.find_terrain_in_distance(formed_map, distance, industrial, i,
                                                                                  j)
                elif formed_map[i, j] == commercial:
                    # For residence close to commercial
                    distance = 3
                    unit_score = 5
                    residential_c_commercial_score = unit_score * \
                                                     self.find_terrain_in_distance(formed_map, distance, residential, i,
                                                                                   j)
                    # For competition
                    distance = 2
                    unit_score = -5
                    commercial_c_commercial_score = unit_score * \
                                                    self.find_terrain_in_distance(formed_map, distance, commercial, i,
                                                                                  j)
                    commercial_score = commercial_score + residential_c_commercial_score + commercial_c_commercial_score
                elif formed_map[i, j] == residential:
                    # For industrial close to residential
                    distance = 3
                    unit_score = -5
                    industrial_c_residential_score = unit_score * \
                                                     self.find_terrain_in_distance(formed_map, distance, industrial, i,
                                                                                   j)
                    # For commercial close to residential
                    distance = 3
                    unit_score = 5
                    commercial_c_residential_score = unit_score * \
                                                     self.find_terrain_in_distance(formed_map, distance, commercial, i,
                                                                                   j)
                    residential_score = residential_score + \
                                        industrial_c_residential_score + commercial_c_residential_score
                elif formed_map[i, j] == toxic:
                    # For Industrial close to toxic
                    distance = 2
                    unit_score = -10
                    industrial_c_toxic_score = unit_score * \
                                               self.find_terrain_in_distance(formed_map, distance, industrial, i, j)
                    # For Commercial close to toxic
                    distance = 2
                    unit_score = -20
                    commercial_c_toxic_score = unit_score * \
                                               self.find_terrain_in_distance(formed_map, distance, commercial, i, j)
                    # For Residential close to toxic
                    distance = 2
                    unit_score = -20
                    residential_c_toxic_score = unit_score * \
                                                self.find_terrain_in_distance(formed_map, distance, residential, i, j)
                    toxic_score = toxic_score + \
                                  industrial_c_toxic_score + commercial_c_toxic_score + residential_c_toxic_score
                elif formed_map[i, j] == scenic:
                    # Residential close to scenic
                    distance = 2
                    unit_score = 10
                    residential_c_scenic_score = unit_score * \
                                                 self.find_terrain_in_distance(formed_map, distance, residential, i, j)
                    scenic_score = scenic_score + residential_c_scenic_score
        self.fitness_score = self.fitness_score + build_cost + \
                             toxic_score + scenic_score + industrial_score + residential_score + commercial_score
        print("build cost " + str(build_cost))
        print("toxic score " + str(toxic_score))
        print("scenic score " + str(scenic_score))
        print("industrial score " + str(industrial_score))
        print("residential score " + "commercial "+str(commercial_c_residential_score)+" industrial "+str(industrial_c_residential_score))
        print("commercial score " +"Comercial "+ str(commercial_c_commercial_score)+" residential "+str(residential_c_commercial_score))
        print("fitness score " + str(self.fitness_score))
        pass

    def mutate(self):
        rows = self.maprow - 1
        cols = self.mapcol - 1
        x1, y1 = random.randint(0, rows), random.randint(0, cols)
        x2, y2 = random.randint(0, rows), random.randint(0, cols)
        while self.original_map[x1, y1] == 'X' or self.original_map[x2, y2] == 'X' or self.map_matrix[x1, y1] == 0 or \
                self.map_matrix[x2, y2] == 0:
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

    def find_terrain_in_distance(self, my_map, distance, terrain, row, col):
        count = 0
        for i in range(-distance, +distance + 1):
            if (row + i) < 0 or (row + i) >= self.maprow:  # check for out of bound horizontally
                continue
            for j in range(-(distance - abs(i)), (distance - abs(i)) + 1):
                if (col + j) < 0 or (col + j) >= self.mapcol:  # check for out of bound vertically
                    continue
                if i == 0 and j == 0:  # check for the original position
                    continue
                if my_map[row + i, col + j] == terrain:
                    count = count + 1
                    # print("index "+ str(row+i) + " "+ str(col+j))
        return count
