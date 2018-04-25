# TODO: Form possible schedules
# TODO: Write a Schedule.__eq__ ()function
import random
from copy import deepcopy
from functools import total_ordering


@total_ordering
class Schedule():
    def __init__(self, persons, events_avaibilities):
        self.persons = persons
        self.events_avaibilities = events_avaibilities
        self.heuristic = 0

    def __eq__(self, other):
        return self.heuristic == other.heuristic

    def __ne__(self, other):
        return not (self.heuristic == other.heuristic)

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def calc_heuristic(self):
        heuristic = 0
        for person in self.persons:
            heuristic = heuristic + person.calc_heuristic()
        self.heuristic = heuristic

    def form_possible_schedules(self):
        # This should return the possible new formed schedule based on different algorithms
        all_possible_schedules = []
        for key, value in self.events_avaibilities.items():
            for counter, person in enumerate(self.persons):
                mutator = deepcopy(self)
                if person in self.events_avaibilities(key):
                    mutator.events_avaibilities(key).remove(person)
                    mutator.persons[counter].eventIDs.remove(key[1])
                else:
                    mutator.events_avaibilities(key).append(person)
                all_possible_schedules.append(mutator)

        best = max(all_possible_schedules)
        return best

    def form_random_schedule(self):

        pass

    def mutate(self):

        pass

    def event_heuristic(self):
        h = 0
        count = 0
        event_persons = {}
        role_list = {}

        # At least 4 people but no more than 7 people are present at all times from 9:00 to 11:00
        for event in self.events_avaibilities.keys():
            for time in self.events_avaibilities[event].keys():
                # times from 9:00 to 11:00 : [2, 3, 4, 5]
                if time in [2, 3, 4, 5]:
                        Num = len(self.events_avaibilities[event][time])
                        if Num >= 4 and Num <= 7:
                            count += 1
            # if the number of peopel does not meet condition in any timeslot, take -5 penalty
            if count < 4 :
                h -= 5
            else:
                h += 1
            count = 0

        # All five roles are filled
        for event in self.events_avaibilities.keys():
            event_dict = self.events_avaibilities[event]

            for time in event_dict.keys():
                persons = event_dict[time]
                for i in persons:
                    if i not in event_persons[event]:
                        event_persons[event].append(i)

            # Not sure using the class "Person" is correct or not here,
            for k in event_persons[event]:
                list = k.getRoles()
                roleName = list[event-1]
                role_list[event].append(roleName)

            presenterNum = role_list[event].count("PRESENTER")
            introNum = role_list[event].count("INTRO")
            leadNum = role_list[event].count("LEAD")
            debriefNum = role_list[event].count("DEBRIEF")

            if presenterNum > 1 and introNum > 0 and leadNum > 0 and debriefNum > 0:
                h += 1
            else:
                h -= 5
        self.heuristic = h
        return h



    def mutate(self):

        return

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

    def add_event_to_person(self, persons, id, event_id):
        for person in persons:
            if id == person.id:
                if event_id not in person.eventIDs:
                    person.eventIDs.append(event_id)
        return persons


