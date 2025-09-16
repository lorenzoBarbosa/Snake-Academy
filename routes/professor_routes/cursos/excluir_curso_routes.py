from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/excluir-curso")
@requer_autenticacao(["professor"])
async def get_excluir_curso():
    response = templates.TemplateResponse("professor/cursos/excluir_curso.html", {"request": {}})
    return response