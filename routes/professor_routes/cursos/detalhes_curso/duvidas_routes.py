from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes-curso/duvidas")
@requer_autenticacao(["professor"])
async def get_duvidas():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/duvidas.html", {"request": {}})
    return response