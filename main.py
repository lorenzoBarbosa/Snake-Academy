from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.public_routes.cadastro_routes import router as cadastro_router
from routes.public_routes.home_routes import router as home_router
from routes.public_routes.login_routes import router as login_router
from routes.public_routes.detalhes_curso_routes import router as detalhes_curso_router
from routes.public_routes.confirmacao_cadastro_routes import router as confirmacao_cadastro_router
from routes.public_routes.cursos_routes import router as cursos_router
from routes.public_routes.recuperar_senha_routes import router as recuperar_senha_router
from routes.public_routes.restaurar_senha_routes import router as restaurar_senha_router
from routes.public_routes.validacao_email_routes import router as validacao_email_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(cadastro_router)
app.include_router(home_router)
app.include_router(login_router)
app.include_router(detalhes_curso_router)
app.include_router(confirmacao_cadastro_router)
app.include_router(cursos_router)
app.include_router(recuperar_senha_router)
app.include_router(restaurar_senha_router)
app.include_router(validacao_email_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)