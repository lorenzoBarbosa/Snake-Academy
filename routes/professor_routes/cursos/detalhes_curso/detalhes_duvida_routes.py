from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes-curso/duvidas/detalhes-duvida")
@requer_autenticacao(["professor"])
async def get_detalhes_duvida():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/detalhes_duvida.html", {"request": {}})
    return response