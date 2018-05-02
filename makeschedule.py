# TODO: implement hill climbing algorithm
import random
from schedule import Schedule
import time
from copy import deepcopy

def makeschedule(people, events, end_time):
    local_best = []
    count = 0
    timeout = time.time() + end_time

    current_schedule = random_restart(people, events)
    current_h = current_schedule.heuristic

    new_schedule = current_schedule.form_possible_schedules()
    new_h = new_schedule.heuristic

    while time.time() < timeout:
        if new_h > current_h:
            current_h = new_h
            new_schedule = new_schedule.form_possible_schedules()
            new_h = new_schedule.heuristic
            print(new_schedule)
        elif new_h == current_h and count <= 10:
            new_schedule = new_schedule.form_possible_schedules()
            new_h = new_schedule.heuristic
            count += 1
        else:
            local_best.append(new_schedule)
            new_schedule = random_restart(people, events)
            new_h = new_schedule.heuristic
            current_h = new_h - 10
            count = 0

    return max(local_best)

def random_restart(all_people, all_events):
    people = deepcopy(all_people)
    events = deepcopy(all_events)
    role_list = ["PRESENTER", "INTRO", "LEAD", "DEBRIEF", "NO_ROLE"]
    for ID, person in people.items():
        availability = person.get_available_event_id()
        randomNum = random.randint(1, int(len(availability)))

        person.eventIDs = random.sample(availability, randomNum)
        person.eventIDs.sort()

        for eventID in person.eventIDs:
            x = random.randint(0, 4)
            if events[eventID].is_role_filled(role_list[x]):
                person.roles["NO_ROLE"] += 1
                events[eventID].add_person_to_role("NO_ROLE",ID)
            else:
                person.roles[role_list[x]] += 1
                events[eventID].add_person_to_role(role_list[x],ID)

    newSchedule = Schedule(people, events)
    return newSchedule
