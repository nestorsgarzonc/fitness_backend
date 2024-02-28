from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from random import randrange
app = FastAPI()


CONST_DATA = {
    'stepsGoal': 4500,
    'caloriesGoal': 1800,
    'caloriesCounter': 1200,
    'waterGoal': 10,
    'waterCounter': 6,
    'heartRate': 95,
}

MAX_STEPS_RANDOM = 4500


class Steps(BaseModel):
    steps: int


class UserData(BaseModel):
    name: str
    stepsCounter: int
    stepsGoal: int
    caloriesGoal: int
    caloriesCounter: int
    waterGoal: int
    waterCounter: int
    heartRate: int


users = {
    '4312': {
        'name': 'Santiago Leon',
        'stepsCounter': randrange(MAX_STEPS_RANDOM)
    },
    '9812': {
        'name': 'Sebastian Beltran',
        'stepsCounter': randrange(MAX_STEPS_RANDOM)
    },
    '2018': {
        'name': 'Sofia Montoya',
        'stepsCounter': randrange(MAX_STEPS_RANDOM)
    },
}


def get_user_data(user_id: str):
    if (user_id not in users):
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id] | CONST_DATA


@app.get("/")
def read_root():
    return {"Hello": "Devs"}


@app.get("/api/user-info/{user_id}")
def get_user_info(user_id: str) -> UserData:
    return get_user_data(user_id)


@app.post("/api/add-steps/{user_id}")
def add(user_id: str, data: Steps) -> UserData:
    get_user_data(user_id)
    users[user_id]['stepsCounter'] += data.steps
    return users[user_id] | CONST_DATA
