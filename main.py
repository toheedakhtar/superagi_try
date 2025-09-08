from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory='templates/')
@app.get('/')
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
@app.post('/api/data_handler')
def data_handler(data: str):
    processed_data = process_data(data)  # logic for data processing
    return {'result': processed_data}
