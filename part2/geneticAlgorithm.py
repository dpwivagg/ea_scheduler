# This is for Genetic Algorithm
import random
import datetime
import time
from itertools import chain
from collections import Counter
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
        self.fitness()

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
                    string = string + "0|"
                else:
                    string = string + str(self.map_matrix[row, column]) + "|"

        return string
    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return "gameBoard(%s)" % (self.map_matrix)
    def __cmp__(self, other):
        return (self.fitness_score> other.fitness_score)-(self.fitness_score< other.fitness_score)

    def cost_to_build(self):
        cost = 0
        for key, value in self.original_map.items():
            type = self.map_matrix[key]
            if type != 0 and  value != toxic and value != scenic:
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
                    # print("in commercial")
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
                    # print(
                    #     "commercial score "+str(commercial_score) + "Comercial " + str(commercial_c_commercial_score) + " residential " + str(
                    #         residential_c_commercial_score))
                elif formed_map[i, j] == residential:
                    # For industrial close to residential
                    # print("in residential")
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
                    # print("residential score " +str(residential_score)+" commercial " + str(
                    #     commercial_c_residential_score) + " industrial " + str(industrial_c_residential_score))
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
        self.fitness_score = self.fitness_score - build_cost + \
                             toxic_score + scenic_score + industrial_score + residential_score + commercial_score
        # print("build cost " + str(build_cost))
        # print("toxic score " + str(toxic_score))
        # print("scenic score " + str(scenic_score))
        # print("industrial score " + str(industrial_score))
        # print("residential score "+str(residential_score))
        # print("commercial score " +str(commercial_score))
        # print("fitness score " + str(self.fitness_score))
        pass

    def mutate(self):
        icount = 0
        ccount = 0
        rcount = 0
        for key, value in self.map_matrix.items():
            if value == industrial:
                icount += 1
            elif value == commercial:
                ccount += 1
            elif value == residential:
                rcount += 1

        map = randomly_form_generation(self.original_map, icount, ccount, rcount, self.maprow, self.mapcol)
        self.map_matrix = map.map_matrix
        self.fitness_score = map.fitness_score
        # rows = self.maprow - 1
        # cols = self.mapcol - 1
        # x1, y1 = random.randint(0, rows), random.randint(0, cols)
        # x2, y2 = random.randint(0, rows), random.randint(0, cols)
        # while self.original_map[x1, y1] == 'X' or self.original_map[x2, y2] == 'X' or self.map_matrix[x1, y1] == 0 or \
        #         self.map_matrix[x2, y2] == 0:
        #     x1, y1 = random.randint(0, rows), random.randint(0, cols)
        #     x2, y2 = random.randint(0, rows), random.randint(0, cols)
        #
        # oldVal = self.map_matrix[x1, y1]
        # newVal = self.map_matrix[x2, y2]
        # self.map_matrix[x1, y1] = newVal
        # self.map_matrix[x2, y2] = oldVal


    def crossover(self, other):
        parent1 = []
        parent2 = []

        first_new_map = {}
        second_new_map = {}

        bindex = 0
        cindex = 0
        rindex = 0
        iindex = 0

        for i in range(0, self.maprow):
            for j in range(0, self.mapcol):
                value = self.map_matrix[i, j]
                if value == industrial:
                    parent1.append("I" + str(iindex))
                    iindex += 1
                elif value == commercial:
                    parent1.append("C" + str(cindex))
                    cindex += 1
                elif value == residential:
                    parent1.append("R" + str(rindex))
                    rindex += 1
                elif value == "X":
                    parent1.append("X")
                else:
                    parent1.append("B" + str(bindex))
                    bindex += 1

        bindex = 0
        cindex = 0
        rindex = 0
        iindex = 0

        for i in range(0, self.maprow):
            for j in range(0, self.mapcol):
                value2 = other.map_matrix[i, j]
                if value2 == industrial:
                    parent2.append("I" + str(iindex))
                    iindex += 1
                elif value2 == commercial:
                    parent2.append("C" + str(cindex))
                    cindex += 1
                elif value2 == residential:
                    parent2.append("R" + str(rindex))
                    rindex += 1
                elif value2 == "X":
                    parent1.append("X")
                else:
                    parent2.append("B" + str(bindex))
                    bindex += 1

        start = random.randint(0, len(parent1) // 2)
        end = random.randint(0, len(parent1) // 2)

        child1 = parent1
        child2 = parent2

        for i in range(start, end):
            if parent1[i] == "X" or parent2[i] == "X":
                continue
            x = parent1.index(parent2[i])
            y = parent2.index(parent1[i])

            child1[i] = parent2[i]
            child2[i] = parent1[i]

            child1[x] = parent2[y]
            child2[y] = parent1[x]

        counter = 0
        for i in range(0, self.maprow):
            for j in range(0, self.mapcol):
                if "I" in child1[counter]:
                    first_new_map[i, j] = industrial
                elif "C" in child1[counter]:
                    first_new_map[i, j] = commercial
                elif "R" in child1[counter]:
                    first_new_map[i, j] = residential
                else:
                    first_new_map[i, j] = 0

                if "I" in child2[counter]:
                    second_new_map[i, j] = industrial
                elif "C" in child2[counter]:
                    second_new_map[i, j] = commercial
                elif "R" in child2[counter]:
                    second_new_map[i, j] = residential
                else:
                    second_new_map[i, j] = 0

                counter += 1

        first = map(self.maprow, self.mapcol, self.original_map, first_new_map)
        second = map(self.maprow, self.mapcol, self.original_map, second_new_map)
        result_list = []
        result_list.append(first)
        result_list.append(second)
        return result_list

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

def geneticRun(originalMap, maprow, mapcol, num_I, num_R, num_C, lastTime):
    last_time = lastTime # Time would always be set to 10s
    original_map = originalMap
    maprow = maprow
    mapcol = mapcol
    start_time = time.time()
    elite_list = []  # For storing the elite list
    normal_list = []
    cull_list = []
    gen_list = []
    original_size = 100
    elite_size = 2
    cull_size = 2
    cross_over_fraction = 0.6
    mutation_rate = 0.02   # The fraction for mutation 0.02 chance to mutate after crossover
    diff = 0
    # For the first time we always set the size to be 100
    if(maprow * mapcol)<5:
        elite_size = 1
        cull_size = 1
        original_size = 5

    # TODO:First need randomnize the amount of size of original size
    while len(gen_list)<original_size:
        gen_list.append(randomly_form_generation(original_map,num_I,num_R,num_C,maprow,mapcol))
    gen_list.sort(key=lambda x: x.fitness_score,reverse=True)
    # Now starts genetic
   # for i in range (0,1):
    while diff<last_time:
        # Selection
        elite_list = list(chain(gen_list[0:(elite_size)]))
        # This is for forming the next generation (need to be selected)
        normal_list = list(chain(gen_list[0:(len(gen_list)-cull_size)]))
        # Currently have no use to store
        cull_list = list(chain(gen_list[(len(gen_list)  -cull_size):]))
        # The probability distribution of the list
        probability_list = probability_distribution(normal_list)
        # Start to create  next generation
        gen_list = []+elite_list

        # starts selection
        while(len(gen_list)<original_size):
            # selection with probability
            parents = random.choices(normal_list,weights=probability_list,k=2)
            parent1 = parents[0]
            parent2 = parents[1]
            # Cross over
            children = parent1.crossover(parent2)
            # check for mutation
            if random.random() < mutation_rate:
                children[0].mutate()
                children[1].mutate()
            # print(children[0])
            # print(children[1])
            gen_list = gen_list + children
        gen_list.sort(key=lambda x: x.fitness_score,reverse = True)
        diff = float(time.time() - start_time)
    print("Final state is:")
    print( map(maprow,mapcol,original_map,gen_list[0].create_map()))
    print("fitness score " + str(gen_list[0].fitness_score))
    print("actual time spent " + str(diff))
    pass
# form a probability distribution
# TODO consider negetive values
def probability_distribution(map_list):
    total_count = 0
    min = map_list[0].fitness_score
    probability_list = [None]*len(map_list)

    for map in map_list:
        if map.fitness_score<min:
            min = map.fitness_score
    for map in map_list:
        total_count += (map.fitness_score-min)
    count = 0
    if total_count ==0:
        for map in map_list:
            probability_list[count] = 1 / len(map_list)  # Calculate the probability of
            count += 1
    else:
        for map in map_list:
            probability_list[count] = (map.fitness_score - min) / total_count  # Calculate the probability of
            count += 1

    return probability_list
# randomly form a new map based on the counts of different terrain
def randomly_form_generation(original_map,industrial_number,residential_number,commercial_number, maprow, mapcol):
    map_status = {}
    m = 0
    h = 0
    k = 0
    for i in range(maprow):
        for j in range(mapcol):
            map_status[i,j]=0

    # print(original_map)

    while m < industrial_number:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if original_map[random_row, random_col] == "X" or map_status[random_row, random_col] != 0:
            continue
        map_status[random_row, random_col] = "I"
        m += 1

    while h < residential_number:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if map_status[random_row, random_col] != 0 or original_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "R"
        h += 1

    while k < commercial_number:
        random_row = random.randint(0, maprow - 1)
        random_col = random.randint(0, mapcol - 1)
        if map_status[random_row, random_col] != 0 or original_map[random_row, random_col] == "X":
            continue
        map_status[random_row, random_col] = "C"
        k += 1
    map1 = map(maprow, mapcol,original_map, map_status)
    # print(map1)
    return map1