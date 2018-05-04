from copy import deepcopy
from datetime import datetime
from functools import total_ordering
from data_parser import read_data
from shared_constants import *

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
        # TODO: Change this if you want a better command line representation of schedules
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
        all_possible_schedules = []
        for name, event in self.events.items():
            for id, person in self.persons.items():
                mutator = Schedule(dict(self.persons), dict(self.events))
                mutator.persons[id] = deepcopy(person)
                mutator.events[name] = deepcopy(event)
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
        return best

    def get_RoleList(personID):
        roles = []
        allpeople = read_data()
        for person in allpeople:
            if person.id == personID:
                roles = person.getRoles()
        return roles

    def check_correct(self):
        for name, event in self.events.items():
            event.check_correct()
        for id, person in self.persons.items():
            person.check_correct(id)

    def disp(self):
        for name, event in self.events:
            for ID, person in event.roles_filled:
                pass