# TODO: Form possible schedules
# TODO: Write a Schedule.__eq__ ()function
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

        return h





