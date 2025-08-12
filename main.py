from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.public_routes import router as public_router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(public_router)



if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)