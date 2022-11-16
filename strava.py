import requests
import urllib3
from utils import convert_seconds_to_hours, activity_types

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def refresh_token():
    auth_url = 'https://www.strava.com/oauth/token'
    payload = {
        'client_id': '',
        'client_secret': '',
        'refresh_token': '',
        'grant_type': 'refresh_token',
        'f': 'json'
    }

    response = requests.post(auth_url, data=payload, verify=False)
    return response.json()['access_token']


def get_my_activities():
    access_token = refresh_token()
    url = 'https://www.strava.com/api/v3/athlete/activities'
    headers = {"Authorization": "Bearer " + access_token}
    params = {
        'per_page': 200,
        'page': 1
    }
    response = requests.get(url, headers=headers, params=params)

    return response.json()


def get_profile():
    access_token = refresh_token()
    url = 'https://www.strava.com/api/v3/athlete'
    headers = {"Authorization": "Bearer " + access_token}
    response = requests.get(url, headers=headers)

    return response.json()


def calculate_all_rides_duration():
    activities = get_my_activities()
    rides = list(filter(lambda ride: ride['type'] == 'Ride', activities))
    duration = 0
    for i in range(len(rides)):
        duration = duration + rides[i]['moving_time']

    # print(duration)

    return convert_seconds_to_hours


def calculate_all_runs_duration():
    activities = get_my_activities()
    rides = list(filter(lambda ride: ride['type'] == 'Run', activities))
    duration = 0
    for i in range(len(rides)):
        duration = duration + rides[i]['moving_time']

    print(duration)

    return convert_seconds_to_hours(duration)


def calculate_activity_duration():
    activities = get_my_activities()

    act_types = activity_types(activities)
    arr = []
    result = {}
    for act_type in act_types:
        duration = 0
        actions = list(filter(lambda action: action['type'] == act_type, activities))
        for i in range(len(actions)):
            duration = duration + actions[i]['moving_time']
            # result[act_type] = duration

        result['name'] = act_type
        result['count'] = len(actions)
        result['duration'] = duration
        arr.append(result)

    return result
