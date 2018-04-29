from FinalProject.shared_constants import *


class Event():
    def __init__(self, id, roles_filled):
        # A dictionary of key of roles and data is a list of person id which is assigned for this role
        # for example, key presenter has data of a list of [1001, 1034] representing the id of people in this role
        # Currently we have 5 roles,
        # presenter = "PRESENTER"
        # intro = "INTRO"
        # lead = "LEAD"
        # debrief = "DEBRIEF"
        # no_role = "NO_ROLE"
        self.id = id
        self.roles_filled = roles_filled
        roles_filled[presenter] = []
        roles_filled[intro] = []
        roles_filled[lead] = []
        roles_filled[debrief] = []
        roles_filled[no_role] = []
        self.heuristic = 0
        #  The list of id of persons who will be available for this event,
        # person id is removed when the person is assigned to roles and is added back to the list when he is removed from the roles
        self.available_persons = []

    def add_person_available(self, person_id):
        self.available_persons.append(person_id)

    def remove_person_available(self, person_id):
        self.available_persons.remove(person_id)

    #  TODO:This is needed for calculating the event heuristic
    def calc_heuristic(self):
        return

    # While we remove person from role, we add it back to available persons for future usage
    def remove_person_from_role(self, role, person_id):
        self.roles_filled[role].remove(person_id)
        self.available_persons.append(person_id)

    def add_person_to_role(self, role, person_id):
        self.roles_filled[role].append(person_id)
        self.available_persons.remove(person_id)






