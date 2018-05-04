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

    new_schedule = current_schedule.choose_best_schedule()
    new_h = new_schedule.heuristic

    while time.time() < timeout:
        print("Time left: ", round(timeout - time.time()), "s")
        if new_h > current_h:
            current_h = new_h
            new_schedule = new_schedule.choose_best_schedule()
            new_h = new_schedule.heuristic
            print(new_schedule)
        elif new_h == current_h and count <= 10:
            new_schedule = new_schedule.choose_best_schedule()
            new_h = new_schedule.heuristic
            count += 1
            print(new_schedule)
        else:
            print("Restarting")
            local_best.append(new_schedule)
            new_schedule = random_restart(people, events)
            new_h = new_schedule.heuristic
            current_h = new_h - 10
            count = 0

    local_best.append(new_schedule)
    return max(local_best)

def random_restart(all_people, all_events):
    people = deepcopy(all_people)
    events = deepcopy(all_events)
    role_list = ["PRESENTER", "INTRO", "LEAD", "DEBRIEF", "NO_ROLE"]
    for ID, person in people.items():
        availability = [a for a in person.get_available_event_id()]
        randomNum = random.randint(1, 9 if len(availability) > 9 else len(availability))

        person.eventIDs = random.sample(availability, randomNum)
        person.eventIDs.sort()

        for eventID in person.eventIDs:
            role = events[eventID].add_to_any_role(ID, person)
            person.add_role(role)

    newSchedule = Schedule(people, events)
    return newSchedule
