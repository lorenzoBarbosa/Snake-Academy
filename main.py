from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.public_routes.cadastro_routes import router as cadastro_router
from routes.public_routes.home_routes import router as home_router
from routes.public_routes.login_routes import router as login_router
from routes.public_routes.curso_routes import router as curso_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(cadastro_router)
app.include_router(home_router)
app.include_router(login_router)
app.include_router(curso_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)