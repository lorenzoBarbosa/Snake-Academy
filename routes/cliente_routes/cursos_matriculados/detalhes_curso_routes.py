from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/cursos_matriculados/detalhes_curso_matriculado")
async def get_detalhes_curso():
    response = templates.TemplateResponse("cliente/cursos_matriculados/detalhes_curso_matriculado.html", {"request": {}})
    return response


    