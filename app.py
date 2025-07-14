from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 
import json


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_FILE = "checkboxes.json"

@app.get("/state")
async def get_state():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return data
