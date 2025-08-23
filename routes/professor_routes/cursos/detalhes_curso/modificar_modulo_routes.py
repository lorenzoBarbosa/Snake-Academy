from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes_curso/modificar_curso/modificar_modulo")
async def get_modificar_modulo():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/modificar_modulo.html", {"request": {}})
    return response