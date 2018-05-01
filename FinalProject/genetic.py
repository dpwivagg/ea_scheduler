# TODO: implement genetic algorithm and related methods


# TODO: run genetic
import time
import random
from copy import deepcopy
from itertools import chain

from FinalProject.schedule import Schedule


def run_genetic(original_copy, schedules=[], last_time=200, ):
    print("Run genetic algorithm")
    start_time = time.time()
    gen_list = []
    original_size = 100
    elite_size = 2
    cull_size = 2
    mutation_rate = 0.02   # The fraction for mutation 0.02 chance to mutate after crossover
    diff = 0

    #  Fill in the list
    while len(gen_list)<original_size:
        gen_list.append(randomly_form_schedule(original_copy))
    gen_list.sort(key=lambda x: x.heuristic,reverse=True)

    while diff < last_time:
        # Selection
        elite_list = list(chain(gen_list[0:(elite_size)]))
        # This is for forming the next generation (need to be selected)
        normal_list = list(chain(gen_list[0:(len(gen_list) - cull_size)]))
        # Currently have no use to store
        cull_list = list(chain(gen_list[(len(gen_list) - cull_size):]))
        # The probability distribution of the list
        probability_list = probability_distribution(normal_list)
        # Start to create  next generation
        gen_list = [] + elite_list

        # starts selection
        while (len(gen_list) < original_size):
            # selection with probability
            parents = random.choices(normal_list, weights=probability_list, k=2)
            parent1 = parents[0]
            parent2 = parents[1]
            # Cross over
            children = parent1.cross_over(parent2, original_copy)
            # check for mutation
            if random.random() < mutation_rate:
                children[0] = children[0].mutate(original_copy)
                children[1] = children[1].mutate(original_copy)
            # print(children[0])
            # print(children[1])
            gen_list = gen_list + children
        gen_list.sort(key=lambda x: x.heuristic, reverse=True)
        diff = float(time.time() - start_time)
        print(gen_list[0])
    print("Final state is:")
    print(gen_list[0])
    print("Heuristic " + str(gen_list[0].heuristic))
    print("actual time spent " + str(diff))

    return



def probability_distribution(schedule_list):
        total_count = 0
        min = schedule_list[0].heuristic
        probability_list = [None] * len(schedule_list)

        for schedule in schedule_list:
            if schedule.heuristic < min:
                min = schedule.heuristic
        for schedule in schedule_list:
            total_count += (schedule.heuristic - min)
        count = 0
        if total_count == 0:
            for schedule in schedule_list:
                probability_list[count] = 1 / len(schedule_list)  # Calculate the probability of
                count += 1
        else:
            for schedule in schedule_list:
                probability_list[count] = (schedule.heuristic - min) / total_count  # Calculate the probability of
                count += 1

        return probability_list


def randomly_form_schedule(original_copy):
    persons = deepcopy(original_copy.persons)
    events = deepcopy(original_copy.events)
    role_list = ["PRESENTER", "INTRO", "LEAD", "DEBRIEF", "NO_ROLE"]
    for personID in persons.keys():
        available_events = persons[personID].get_available_event_id()
        # print(str(personID))
        # print(available_events)
        randomNum = random.randint(1, int(len(available_events)))
        # randomSample = [ available_events[i] for i in sorted(random.sample(available_events), 4))]
        persons[personID].eventIDs = random.sample(available_events, randomNum)
        persons[personID].eventIDs.sort()
        # print(randomNum)
        # print(persons[personID].eventIDs)

        for item in persons[personID].eventIDs:
            x = random.randint(0, 4)
            persons[personID].roles[role_list[x]] += 1
            events[item].roles_filled[role_list[x]].append(personID)
            events[item].available_persons.remove(personID)
    newSchedule = Schedule(persons, events)
    return newSchedule