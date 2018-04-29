from functools import reduce

from FinalProject.shared_constants import *


class Person():
    def __init__(self, roles, eventIDs, availabilities):
        self.roles = roles # Roles is a dictionary contains the the key (String of role in shared constants and the data is the number of that role the person has been)
        roles[presenter] = 0
        roles[intro] = 0
        roles[lead] = 0
        roles[debrief] = 0
        #  No need for no role in person, because we do not use it to calculate heuristic
        self.eventIDs = eventIDs # List of Integers (event IDs)
        self.availabilities = availabilities # 2D array (events x times)
        self.heuristic = 0

    #  This might need to be changed
    def calc_heuristic(self):
        """THIS FUNCTION CANNOT BE USED WITHOUT INITIALIZING DATA IN THE PERSON CLASS"""
        h = 0

        # Calculate the time this person spent working
        time = reduce(lambda x, y: x + len(self.availabilities[y]), self.eventIDs)
        if time < 6:
            # Time is less than 6 half hours
            h -= 10
        elif time > 12:
            # Time is greater than 12 half hours
            h -= time
        else:
            h += 5

        # Calculate the number of roles
        h += 5 if len(self.roles) > len(self.eventIDs)/3 else -5

        # Calculate number of lead/presenter roles
        h += 5 if self.roles.count("PRESENTER") <= 2 else -5
        h += 5 if self.roles.count("LEAD") <= 2 else -5
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
        event_id.append(event_id)

    def remove_event(self, event_id):
        event_id.remove(event_id)

    #  get the list of event id, the person would be available for
    def get_available_event_id(self):
        events = []
        for i in range(len(self.availabilities)):
            if self.availabilities[i][0] != 0:
                events.append(i)
        return events

    def is_available(self, role, event_id):
        pass
        # TODO: Return a boolean, TRUE if person is available for given role, FALSE if not