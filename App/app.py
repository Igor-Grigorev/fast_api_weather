from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import aiohttp
import json

app = FastAPI()

@app.get("/async")
def index():
    # res = requests.get("")
    return json.dumps({"async": "asd-asd"})

@app.get("/sync")
def index():
    # return json.dumps({"sync": "asd-asd"})
    return json.dumps("SomeAnsw")



app.mount("/", StaticFiles(directory="public", html=True))