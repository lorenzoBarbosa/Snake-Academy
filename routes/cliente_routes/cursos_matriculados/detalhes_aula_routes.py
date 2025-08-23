from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/cursos_matriculados/detalhes_curso/modulos/aulas/detalhes_aula")
async def get_detalhes_aula():
    response = templates.TemplateResponse("cliente/cursos_matriculados/detalhes_aula.html", {"request": {}})
    return response


    