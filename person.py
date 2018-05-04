from functools import reduce

from shared_constants import *


class Person():
    def __init__(self, availabilities):
        self.roles = {} # Roles is a dictionary contains the the key (String of role in shared constants and the data is the number of that role the person has been)
        self.roles[presenter] = 0
        self.roles[intro] = 0
        self.roles[lead] = 0
        self.roles[debrief] = 0
        self.roles[no_role] = 0
        #  We still need no role just for ease of use
        self.eventIDs = [] # List of Integers (event IDs)
        self.availabilities = availabilities # 2D array (events x times)

    #  This might need to be changed
    def calc_heuristic(self):
        h = 0
        # Calculate the time this person spent working
        time = reduce(lambda x, y: x + len(self.availabilities[int(y)]), self.eventIDs,0)
        eventcount = len(self.eventIDs)
        if time < 12 and eventcount < 3:
            # Time is less than 6 half hours
            h -= 25
        elif time > 35 and eventcount > 8:
            # Time is greater than 12 half hours
            h -= time + eventcount
        elif time > 35:
            h -= time - 10
        else:
            h += 10
        # Calculate number of lead/presenter roles
        h += 5 if self.roles["PRESENTER"] <= 4 else -5
        h += 5 if self.roles["LEAD"] <= 4 else -5
        return h

    def getRoles(self):
        return self.roles

    def add_role(self,role):
        self.roles[role] = self.roles[role] + 1

    #  remove roles by decreasing the number of the roles
    def remove_role(self, role):
        if self.roles[role] != 0:
            self.roles[role] = self.roles[role] - 1

    # Add event id to the event id list
    def add_event(self, event_id):
        self.eventIDs.append(event_id)

    def remove_event(self, event_id):
        self.eventIDs.remove(event_id)

    #  get the list of event id, the person would be available for
    def get_available_event_id(self):
        for i in range(len(self.availabilities)):
            if self.availabilities[i][0] != 0:
                yield i

    def is_available(self, role, event_id):
        if role == "PRESENTER":
            return True if 2 in self.availabilities[event_id] and 3 in self.availabilities[event_id] else False
        elif role == "LEAD":
            total = 0
            for i in range(0,7):
                total += i in self.availabilities[event_id]
            return True if total >= 4 else False
        elif role == "INTRO":
            return True if 3 in self.availabilities[event_id] and 4 in self.availabilities[event_id] else False
        elif role == "DEBRIEF":
            return True if 5 in self.availabilities[event_id] and 6 in self.availabilities[event_id] else False

    def check_correct(self, id):
        time = reduce(lambda x, y: x + len(self.availabilities[int(y)]), self.eventIDs, 0)
        if time > 35:
            print('Too many hours for person ', id, ':', time/2, "(", len(self.eventIDs), "events)")
        elif time < 9:
            print('Too few hours for person ', id, ':', time/2, "(", len(self.eventIDs), "events)")

        if self.roles["PRESENTER"] > 4:
            print('Too many presenter roles for person ', id, ':', self.roles["PRESENTER"])

        if self.roles["LEAD"] > 4:
            print('Too many lead roles for person ', id, ':', self.roles["LEAD"])

        return True