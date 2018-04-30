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



def start():
    role_list=["PRESENTER","INTRO","LEAD","DEBRIEF"]
    allpeople = read_data()
    allevents = {}
    for i in range(0, 21):
        event = Event(i, {})
        allevents[i] = event
    for personID in allpeople.keys():
        avaeventlist = []
        for i in range(0, 21):
            if allpeople[personID].availabilities[i][0] != 0:
                avaeventlist.append(i+1)
        # print(avaeventlist)
        x = random.randint(1,len(avaeventlist))
        allpeople[personID].eventIDs = random.sample(avaeventlist, x)
        allpeople[personID].eventIDs.sort()

        for j in range(len(allpeople[personID].eventIDs)):
            x = random.randint(0,3)
            allpeople[personID].roles[role_list[x]] += 1
            allevents[j].roles_filled[role_list[x]].append(personID)
            allevents[j].id = j+1
            # print(allevents[j].roles_filled)

        # print(personID)
        # print(allpeople[personID].roles)
        # print(allpeople[personID].eventIDs)
    # for i in range(21):
    #     print(allevents[i].id)
        # print(allevents[i].roles_filled)

start()