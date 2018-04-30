# TODO: Form possible schedules
# TODO: Write a Schedule.__eq__ ()function
import random
from copy import deepcopy
from functools import total_ordering
from FinalProject.data_parser import read_data

@total_ordering
class Schedule():
    def __init__(self, persons, events):
        #  Persons is a dictionary of id and person object
        self.persons = persons
        #  Events is a dictionary of id and event object
        self.events = events
        self.heuristic = 0

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

        size = len(all_possible_schedules)
        best = max(all_possible_schedules)
        return best

    def form_random_schedule(self):

        pass

    def mutate(self):

        pass

    def get_RoleList(personID):
        roles = []
        allpeople = read_data()
        for person in allpeople:
            if person.id == personID:
                roles = person.getRoles()
        return roles

    def event_heuristic(self):
        h = 0
        count = 0
        event_persons = {}
        role_list = {}
        eventNum = int(len(self.events_avaibilities) / 6)

        for event in range(1, eventNum + 1):
            for timeslot in range(1, 7):
                # times from 9:00 to 11:00 : [2, 3, 4, 5]
                if timeslot in [2, 3, 4, 5]:
                    Num = len(self.events_avaibilities[(event, timeslot)])
                    if Num >= 4 and Num <= 7:
                        count += 1
            # if the number of people does not meet condition in any timeslot, take -5 penalty
            if count < 4:
                h -= 5
            else:
                h += 1
            count = 0

        # All five roles are filled
        # for event in range(1, eventNum + 1):
        #     for time in range(1, 7):
        #         persons = self.events_avaibilities[(event, time)]
        #         for i in persons:
        #             if i not in event_persons[event]:
        #                 event_persons[event].append(i)
        #
        #     # getRole????
        #     for k in event_persons[event]:
        #         list = self.get_RoleList(k)
        #         roleName = list[event-1]
        #         role_list[event].append(roleName)
        #
        #     presenterNum = role_list[event].count("PRESENTER")
        #     introNum = role_list[event].count("INTRO")
        #     leadNum = role_list[event].count("LEAD")
        #     debriefNum = role_list[event].count("DEBRIEF")
        #
        #     if presenterNum > 1 and introNum > 0 and leadNum > 0 and debriefNum > 0:
        #         h += 1
        #     else:
        #         h -= 5
        self.heuristic = h
        return h


    def mutate(self):

        return


    # TODO to be changed to form the new structure
    def cross_over(self,other, empty_persons):
        temporary_mid_event = {}
        for key, value in self.events_avaibilities:
            temporary_mid_event[key] = value
        for key, value in other.events_avaibilities:
            list = temporary_mid_event.get(key)
            for element in value:
                if element not in list:
                    list.add(element)

        persons1 = deepcopy(empty_persons)
        persons2 = deepcopy(empty_persons)
        event_availabilities_1 = {}
        event_availabilities_2 = {}
        for key, value in temporary_mid_event:
            eventID = key[0]
            list1 = []
            list2 = []
            for element in value:
                rand = random.random()
                if rand > 0.5:
                    list1.append(element)
                    persons1 = self.add_event_to_person(persons1, element, eventID)
                rand = random.random()
                if rand > 0.5:
                    list2.append(element)
                    persons2 = self.add_event_to_person(persons2, element, eventID)

            event_availabilities_1[key] = list1
            event_availabilities_2[key] = list2

        schedule1 = Schedule(persons1, event_availabilities_1)
        schedule2 = Schedule(persons2, event_availabilities_2)
        return schedule1, schedule2



