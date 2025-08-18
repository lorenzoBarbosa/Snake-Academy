from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/cursos_matriculados/detalhes_curso_matriculado/modulos")
async def get_cursos_matriculados():
    response = templates.TemplateResponse("cliente/cursos_matriculados/modulos.html", {"request": {}})
    return response


    