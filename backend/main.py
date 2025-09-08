from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

templates = Jinja2Templates(directory="frontend/pages")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return templates.TemplateResponse("index.html", {"request": None})

@app.get("/api/about-content")
def get_about_content():
    return {
        "vision_statement": "Our vision statement...",
        "mission_statement": "Our mission statement...",
        "directors_message": "A message from our director..."
    }
