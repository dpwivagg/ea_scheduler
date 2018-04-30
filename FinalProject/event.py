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

    def find_and_remove(self, person_id):
        for key, value in self.roles_filled.items():
            if person_id in value:
                self.roles_filled[key].remove(person_id)
                role = key
                break
            else:
                role = None
        self.available_persons.append(person_id)
        return role

    def add_to_any_role(self, person_id, person):
        print("Event ID:", self.id)
        if self.all_roles_filled():
            self.add_person_to_role("NO_ROLE",person_id)
            role = "NO_ROLE"
        else:
            if len(self.roles_filled[presenter]) < 2 and person.is_available("PRESENTER",self.id):
                self.add_person_to_role("PRESENTER",person_id)
                role = "PRESENTER"
            elif len(self.roles_filled[lead]) < 1 and person.is_available("LEAD",self.id):
                self.add_person_to_role("LEAD", person_id)
                role = "LEAD"
            elif len(self.roles_filled[debrief]) < 1 and person.is_available("DEBRIEF",self.id):
                self.add_person_to_role("DEBRIEF", person_id)
                role = "DEBRIEF"
            elif len(self.roles_filled[intro]) < 1 and person.is_available("INTRO",self.id):
                self.add_person_to_role("INTRO", person_id)
                role = "INTRO"
        return role


    # bool: True if all roles are filled, False if at least one role is not filled
    def all_roles_filled(self):
        p = len(self.roles_filled[presenter])
        i = len(self.roles_filled[intro])
        l = len(self.roles_filled[lead])
        d = len(self.roles_filled[debrief])
        return p == 2 and i == 1 and l == 1 and d == 1



