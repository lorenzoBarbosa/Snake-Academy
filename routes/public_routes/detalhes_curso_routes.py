from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.curso import curso_repo
from data.curso.curso_model import Curso
from data.usuario import usuario_repo
from util.auth_decorator import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/detalhes_curso/{curso_id}")
async def get_curso(request: Request, curso_id: int, usuario_logado: dict = None):
    rota = get_image_filename("nossos_cursos", curso_id)
    curso = curso_repo.obter_curso_por_id(curso_id)
    response = templates.TemplateResponse("publico/detalhes_curso.html", {"request": request, "usuario": usuario_logado, "curso": curso, "rota": rota})
    return response


    