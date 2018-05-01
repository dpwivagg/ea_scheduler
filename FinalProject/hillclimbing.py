# TODO: implement hill climbing algorithm
import random
from FinalProject.person import Person
from FinalProject.schedule import Schedule
from FinalProject.event import Event
from FinalProject.data_parser import read_data
from datetime import datetime
from copy import deepcopy

# role_list=["PRESENTER","INTRO","LEAD","DEBRIEF"]
#
# def start():
#     person = Person({}, [], [])
#     allpeople = read_data()
#     # sch= Schedule([],{})
#     for person in allpeople.values():
#         avaeventlist = []
#         for i in range(0, 21):
#             if person.availabilities[i][0] != 0:
#                 avaeventlist.append(i+1)
#         # print(avaeventlist)
#         x = random.randint(1,len(avaeventlist))
#         person.eventIDs = random.sample(avaeventlist, x)
#         person.eventIDs.sort()
#
#         for j in range(len(person.eventIDs)):
#             x = random.randint(0,3)
#             person.roles[role_list[x]] += 1
#
#         print(person.roles)
#         print(person.eventIDs)
#
#     for i in range(1,22):
#         for j in range(1,7):
#             sch.events_avaibilities[i,j]=[]
#
#     for person in allpeople:
#         for i in range(len(person.eventIDs)):
#             event = person.eventIDs[i]
#             for j in range(len(person.availabilities[event-1])):
#                 time = person.availabilities[event-1][j]
#                 sch.events_avaibilities[event,time].append(person.id)
#                 if person.id not in sch.persons:
#                     sch.persons.append(person.id)
#
#     print(sch.persons, sch.events_avaibilities)
#     return sch.persons, sch.events_avaibilities

# def start(original_schedule):
#     role_list=["PRESENTER","INTRO","LEAD","DEBRIEF"]
#     allpeople = original_schedule.persons
#     allevents = original_schedule.events
#     # for i in range(0, 21):
#     #     event = Event(i, {})
#     #     allevents[i] = event
#     for personID in allpeople.keys():
#         avaeventlist = []
#         for i in range(0, 21):
#             if allpeople[personID].availabilities[i][0] != 0:
#                 avaeventlist.append(i+1)
#         # print(avaeventlist)
#         x = random.randint(1,len(avaeventlist))
#         allpeople[personID].eventIDs = random.sample(avaeventlist, x)
#         allpeople[personID].eventIDs.sort()
#
#         for j in range(len(allpeople[personID].eventIDs)):
#             x = random.randint(0,3)
#             allpeople[personID].roles[role_list[x]] += 1
#             allevents[j].roles_filled[role_list[x]].append(personID)
#             allevents[j].id = j+1
#             # print(allevents[j].roles_filled)
#
#     return allpeople, allevents
#
# a = start()

class Hill_Climb():

    def __init__(self, original_copy):
        self.original_copy = original_copy

    def hill_climbing(self):
        start_time = datetime.now()
        local_best = []
        time_cost = 0
        time = 180
        count = 0
        current_schedule = self.start()
        current_h = current_schedule.heuristic

        new_schedule = deepcopy(current_schedule.form_possible_schedules())
        new_h = new_schedule.heuristic

        while time_cost < time:
            while new_h >= current_h and time_cost < time :

                while new_h == current_h and time_cost < time:
                    if count <= 10:
                        count += 1
                        new_schedule = new_schedule.form_possible_schedules()
                        new_h = new_schedule.heuristic
                    else:
                        new_schedule = self.start()
                        print("random start because of a stage")
                        new_h = new_schedule.heuristic
                    time_cost = (datetime.now() - start_time).total_seconds()

                count = 0
                current_schedule = new_schedule
                current_h = new_h
                new_schedule = new_schedule.form_possible_schedules()
                new_h = new_schedule.heuristic
                print(str(new_h))

                time_cost = (datetime.now() - start_time).total_seconds()
            local_best.append((current_schedule, current_h))

            # restart if h < current_h
            current_schedule = self.start()
            current_h = current_schedule.heuristic

            new_schedule = current_schedule.form_possible_schedules()
            new_h = new_schedule.heuristic

        print(local_best)
        best_schedule = max(local_best)

        return best_schedule

    def start(self):
        persons = deepcopy(self.original_copy.persons)
        events = deepcopy(self.original_copy.events)
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

        # for i in events.keys():
        #     print(str(i) + str(events[i].roles_filled))
        #     print(str(i) + str(events[i].available_persons))
        #
        # for i in persons.keys():
        #     print(str(persons[i].eventIDs))
        #     print(str(persons[i].roles))

        newSchedule = Schedule(persons, events)
        return newSchedule








