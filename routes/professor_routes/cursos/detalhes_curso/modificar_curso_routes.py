from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes_curso/modificar")
async def get_modificar_curso():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/modificar_curso.html", {"request": {}})
    return response