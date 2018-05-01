# dic = { "presenter": [], "lead":[2,8,9],"no_role":[1,2,3] }
# print(dic)
# a = []
# # a.append(dic.values())
# for key in dic.keys():
#     a.append(dic[key])
# print(a)
# h = 0
# for key in dic.keys():
#     if key != 'no_role':
#         if len(dic[key]) < 1:
#             h -= 5
#             break
# print (h)

# class Employee():
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@comapny.com"
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
# employee1 = Employee("Ying", "Fang", 50000)
# employee2 = Employee("Mengdi", "Li", 60000)
#
# print(employee1.email)

import random
from FinalProject.person import Person
from FinalProject.schedule import Schedule
from FinalProject.event import Event
from FinalProject.data_parser import read_data
from datetime import datetime

allpeople = read_data()
event = {}

for PID in allpeople.keys():
    ava = allpeople[PID].availabilities
    for i in range(21):
        if ava[i] != 0:
            if i not in event.keys():
                event[i] = []
                event[i].append(ava[i])
            else:
                event[i].append(ava[i])
for item in event.keys():
    print(str(event[item]) + '\n')

def start():
    role_list=["PRESENTER","INTRO","LEAD","DEBRIEF","NO_ROLE"]
    allpeople = read_data()
    allevents = {}
    # for i in allpeople.keys():
    #     print(str(allpeople[i].availabilities))
    for i in range(1, 22):
        event = Event(i, {})
        allevents[i] = event
    for personID in allpeople.keys():
        avaeventlist = []
        for i in range(0, 21):
            if allpeople[personID].availabilities[i][0] != 0:
                avaeventlist.append(i+1)
        # print(avaeventlist)
        x = random.randint(0,len(avaeventlist))
        allpeople[personID].eventIDs = random.sample(avaeventlist, x)
        allpeople[personID].eventIDs.sort()

        for j in range(len(allpeople[personID].eventIDs)):
            x = random.randint(0,4)
            allpeople[personID].roles[role_list[x]] += 1
            allevents[j+1].roles_filled[role_list[x]].append(personID)
            allevents[j+1].id = j+1
            # print("Event " + str(j) + str(allevents[j].roles_filled))

        # print(personID)
        # print(allpeople[personID].roles)
        # print(allpeople[personID].eventIDs)

    # for i in range(1, 22):
    #     print(allevents[i].id)
    #     print(allevents[i].roles_filled)
    return allpeople, allevents

# start()