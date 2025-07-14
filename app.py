import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 
import json


DATA_FILE = "checkboxes.json"


async def lifespan(app: FastAPI):
    async def reset_loop():
        while True:
            now = datetime.now()
            next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
            wait_time = (next_midnight - now).total_seconds()
            await asyncio.sleep(wait_time)

            with open(DATA_FILE, "w") as file:
                json.dump({"morning": False, "day": False, "evening": False}, file)
    
    asyncio.create_task(reset_loop())
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/get-state")
async def get_state():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return data


@app.post("/set-state")
async def set_state(state: dict):
    with open(DATA_FILE, "w") as file:
        json.dump(state, file)
