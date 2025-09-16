from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/cursos-matriculados")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_cursos_matriculados():
    response = templates.TemplateResponse("cliente/cursos_matriculados.html", {"request": {}})
    return response


    