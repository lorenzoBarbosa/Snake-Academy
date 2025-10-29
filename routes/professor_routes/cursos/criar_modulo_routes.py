from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso/criar-modulo")
@requer_autenticacao(["professor"])
async def get_criar_modulo(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("professor/cursos/criar_modulo.html", {"request": request, "usuario": usuario_logado})
    return response

@router.get("/professor/cursos/criar-curso/criar-aula")
@requer_autenticacao(["professor"])
async def get_criar_aula(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("professor/cursos/criar_aula.html", {"request": request, "usuario": usuario_logado})
    return response