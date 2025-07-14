from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 
import json


app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

DATA_FILE = "checkboxes.json"


@app.get("/get-state")
async def get_state():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return data


@app.post("/set-state")
async def set_state(state: dict):
    with open(DATA_FILE, "w") as file:
        json.dump(state, file)