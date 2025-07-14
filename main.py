from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), 'static')
os.makedirs(static_dir, exist_ok=True)

# Copy the static files if not already present
for filename in ['style.css', 'script.js']:
    src = os.path.join(os.path.dirname(__file__), filename)
    dst = os.path.join(static_dir, filename)
    if os.path.exists(src) and not os.path.exists(dst):
        with open(src, 'r') as sf, open(dst, 'w') as df:
            df.write(sf.read())

app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_index():
    return FileResponse(os.path.join(os.path.dirname(__file__), 'index.html'))

