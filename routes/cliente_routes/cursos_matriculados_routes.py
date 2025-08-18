from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/cursos_matriculados")
async def get_cursos_matriculados():
    response = templates.TemplateResponse("cliente/cursos_matriculados.html", {"request": {}})
    return response


    