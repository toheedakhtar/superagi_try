import os
print("Hello")
from fastapi import FastAPI, responses
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
async def read_root():
    return responses.HTMLResponse(open("static/index.html").read())
