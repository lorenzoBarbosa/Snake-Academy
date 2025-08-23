from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/excluir_curso")
async def get_excluir_curso():
    response = templates.TemplateResponse("professor/cursos/excluir_curso.html", {"request": {}})
    return response