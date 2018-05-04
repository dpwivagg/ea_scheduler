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
        return "Schedule with heuristic " + str(self.heuristic)

    # Calculate heuristic by event and person
    def calc_heuristic(self):
        heuristic = 0
        for id, person in self.persons.items():
            heuristic += person.calc_heuristic()

        for id, event in self.events.items():
            heuristic += event.calc_heuristic(self.persons)
        self.heuristic = heuristic


    def choose_best_schedule(self):
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

    def check_correct(self):
        for name, event in self.events.items():
            event.check_correct()
        for id, person in self.persons.items():
            person.check_correct(id)
