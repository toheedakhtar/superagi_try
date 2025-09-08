from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def read_index():
    with open('frontend/index.html') as f:
        return f.read()
