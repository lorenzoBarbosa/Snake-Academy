from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso")
@requer_autenticacao(["professor"])
async def get_criar_curso():
    response = templates.TemplateResponse("professor/cursos/criar_curso.html", {"request": {}})
    return response