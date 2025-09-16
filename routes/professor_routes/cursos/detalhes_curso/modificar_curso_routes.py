from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes-curso/modificar-curso")
@requer_autenticacao(["professor"])
async def get_modificar_curso():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/modificar_curso.html", {"request": {}})
    return response