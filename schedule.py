# TODO: Form possible schedules
# TODO: Write a Schedule.__eq__ ()function
import random
from copy import deepcopy
from datetime import datetime
from functools import total_ordering
from FinalProject.data_parser import read_data
from FinalProject.shared_constants import *


@total_ordering
class Schedule():
    def __init__(self, persons, events):
        #  Persons is a dictionary of id and person object
        self.persons = persons
        #  Events is a dictionary of id and event object
        self.events = events
        self.heuristic = 0
        self.calc_heuristic()

    def __eq__(self, other):
        return self.heuristic == other.heuristic

    def __ne__(self, other):
        return not (self.heuristic == other.heuristic)

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __str__(self):
        # TODO: Change this if we want a better command line representation of schedules
        return "Schedule with heuristic " + str(self.heuristic)

    # Calculate heuristic by event and person
    def calc_heuristic(self):
        heuristic = 0

        for eventID in self.events.keys():
            timeslot = {}
            count = 0
            for personID in self.persons.keys():
                if eventID in self.persons[personID].eventIDs:
                    for time in self.persons[personID].availabilities[eventID]:
                        if time not in timeslot.keys():
                            timeslot[time] = [personID]
                        else:
                            timeslot[time].append(personID)
            # print(str(eventID) + '\t' + str(timeslot))
            for i in timeslot.keys():
                if i in [2, 3, 4, 5]:
                    Num = len(timeslot[i])
                    if Num >= 4 and Num <= 7:
                        count += 1
            if count < 4:
                heuristic -= 5
            else:
                heuristic += 1

        for id, person in self.persons.items():
            heuristic = heuristic + person.calc_heuristic()

        for id, event in self.events.items():
            heuristic = heuristic + event.calc_heuristic()
        self.heuristic = heuristic


    def form_possible_schedules(self):
        # This should return the possible new formed schedule based on different algorithms
        start = datetime.now()
        all_possible_schedules = []
        for name, event in self.events.items():
            for id, person in self.persons.items():
                mutator = Schedule(deepcopy(self.persons),deepcopy(self.events))
                if id in event.available_persons:
                    # If they are available, try adding them to the event
                    role = mutator.events[name].add_to_any_role(id, person)
                    mutator.persons[id].add_event(name)
                    mutator.persons[id].add_role(role)

                else:
                    # Otherwise, try taking them out
                    role = mutator.events[name].find_and_remove(id)
                    if role is not None:
                        mutator.persons[id].remove_event(name)
                        mutator.persons[id].remove_role(role)
                all_possible_schedules.append(mutator)

        for a in all_possible_schedules:
            a.calc_heuristic()

        best = max(all_possible_schedules)
        print("Time cost ", (datetime.now()-start).total_seconds())
        return best

    def get_RoleList(personID):
        roles = []
        allpeople = read_data()
        for person in allpeople:
            if person.id == personID:
                roles = person.getRoles()
        return roles

    def mutate(self, original_copy):
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


    # TODO to be changed to form the new structure
    def cross_over(self,other, original_schedule):
        original_events = original_schedule.events
        original_persons = original_schedule.persons
        crossover_events1 = deepcopy(original_events)
        crossover_persons1 = deepcopy(original_persons)
        crossover_events2 = deepcopy(original_events)
        crossover_persons2 = deepcopy(original_persons)
        events1 = self.events
        events2 = other.events
        for i in range(21):
            original_available_persons = original_events[i].available_persons
            event1 = events1[i]
            event2 = events2[i]
            num_people = len(original_available_persons)
            swap_person_list = []
            # This -1 is for not swapping all people
            num_random_people = random.randint(1,num_people-1)
            # print("Random ", num_random_people)
            # print("Size ", num_people)
            for j in range(num_random_people):
                person_id = original_available_persons[random.randint(0,num_people-1)]
                while person_id in swap_person_list:
                    person_id = original_available_persons[random.randint(0,num_people-1)]
                swap_person_list.append(person_id)
        #     Now the person id we want to swap is found and we are trying to swap it.
            for person_id in original_available_persons:
                role1 = event1.find_role_by_person(person_id)
                role2 = event2.find_role_by_person(person_id)
                if person_id in swap_person_list:
                    if role1 != not_assigned:
                        crossover_events2[i].add_person_to_role(role1,person_id)
                        crossover_persons2[person_id].add_role(role1)
                        crossover_persons2[person_id].add_event(i)
                    if role2 != not_assigned:
                        crossover_events1[i].add_person_to_role(role2,person_id)
                        crossover_persons1[person_id].add_role(role2)
                        crossover_persons1[person_id].add_event(i)
                else:
                    if role2 != not_assigned:
                        crossover_events2[i].add_person_to_role(role2,person_id)
                        crossover_persons2[person_id].add_role(role2)
                        crossover_persons2[person_id].add_event(i)
                    if role1 != not_assigned:
                        crossover_events1[i].add_person_to_role(role1,person_id)
                        crossover_persons1[person_id].add_role(role1)
                        crossover_persons1[person_id].add_event(i)

        schedule1 = Schedule(crossover_persons1, crossover_events1)
        schedule2 = Schedule(crossover_persons2, crossover_events2)
        result_list = [schedule1, schedule2]
        return result_list

    # This is the cross over that fits
    def cross_over2(self):
        return

    # this changes the schedule to make there is only two presenters,
    # one lead, one intro, one debrief and several no_role
    def repair_schedule(self):
        for event_id, event in self.events:
            for role,person_ids in event.roles_filled:
                length = len(person_ids)
                if role == presenter:
                    if length > 2:
                        while length > 2:
                            index = random.randint(0,length-1)
                            # Start changing for the data
                            removed_person = person_ids[index]
                            event.remove_person_from_role(role,removed_person)
                            self.persons[removed_person].remove_event(event_id)
                            self.persons[removed_person].remove_role(role)
                            person_ids.remove(removed_person)
                            length = len(person_ids)
                    elif length < 2:
                        while length < 2:
                            return
                elif role != no_role and length > 1:
                    while length > 1:
                        index = random.randint(0,length-1)
                        # Start changing for the data
                        removed_person = person_ids[index]
                        event.remove_person_from_role(role,removed_person)
                        self.persons[removed_person].remove_event(event_id)
                        self.persons[removed_person].remove_role(role)
                        person_ids.remove(removed_person)
                        length = len(person_ids)


        return

    def check_correct(self):
        for name, event in self.events.items():
            event.check_correct()
        for id, person in self.persons.items():
            person.check_correct(id)