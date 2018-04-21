
class Schedule():
    def __init__(self, persons, events_avaibilities, heuristic):
        self.persons = persons
        self.events_avaibilities = events_avaibilities
        self.heuristic = heuristic


    def cal_heuristic(self):
        heuristic = 0
        for person in self.persons:
            heuristic = heuristic+ person.calc_heuristic()
        self.heuristic = heuristic

    def form_possible_schedules(self):
        # This should return the possible new formed schedule based on different algorithms
        return



