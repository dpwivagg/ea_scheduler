from functools import reduce

class Person():
    def __init__(self, id, roles, eventIDs, availabilities):
        self.id = id # Integer
        self.roles = roles # List of strings
        self.eventIDs = eventIDs # List of Integers (event IDs)
        self.availabilities = availabilities # 2D array (events x times)

    def calc_heuristic(self):
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


