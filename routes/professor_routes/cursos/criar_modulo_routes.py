from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso/criar-modulo")
@requer_autenticacao(["professor"])
async def get_criar_modulo():
    response = templates.TemplateResponse("professor/cursos/criar_modulo.html", {"request": {}})
    return response