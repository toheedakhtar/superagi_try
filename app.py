from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount('/static', StaticFiles(directory='clone/superagi_try/static'), name='static')
@app.get('/', response_class=HTMLResponse)
async def read_index():
    with open('clone/superagi_try/index.html') as f:
        return f.read()
