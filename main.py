from fastapi import FastAPI, responses
app = FastAPI()
@app.get("/")
async def read_root():
    return responses.FileResponse("index.html")
