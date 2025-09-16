from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/cursos-matriculados/detalhes-curso-matriculado")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_detalhes_curso():
    response = templates.TemplateResponse("cliente/cursos_matriculados/detalhes_curso_matriculado.html", {"request": {}})
    return response


    