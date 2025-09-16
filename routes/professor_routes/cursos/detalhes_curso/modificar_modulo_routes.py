from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes-curso/modificar-curso/modificar-modulo")
@requer_autenticacao(["professor"])
async def get_modificar_modulo():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/modificar_modulo.html", {"request": {}})
    return response