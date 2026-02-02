from fastapi import FastAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def home():
    return HTMLResponse()
