import os
import uvicorn
from fastapi import FastAPI
from strava import get_my_activities, get_profile, calculate_all_rides_duration, calculate_all_runs_duration, calculate_activity_duration
from utils import activity_types

app = FastAPI()

# start server: uvicorn main:app --reload


@app.get('/')
async def root():
    return {'Message': 'Hello there!'}


@app.get('/profile')
async def get_profile():
    profile = get_profile()

    return profile


@app.get('/activity/{number}')
async def get_activity(number: int):
    activities = get_my_activities()
    return activities[number]


@app.get('/activities')
async def get_all_activities():
    return get_my_activities()


@app.get('/stats')
async def get_stats():
    return calculate_activity_duration()


@app.get('/my_activity_types')
async def get_activity_types():
    return activity_types(get_my_activities())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
