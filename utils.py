import time

def convert_seconds_to_hours(seconds):
    return seconds / 60 / 60


def activity_types(all_activities):
    activity_set = set()
    for activity in all_activities:
        activity_set.add(activity['type'])
    return
