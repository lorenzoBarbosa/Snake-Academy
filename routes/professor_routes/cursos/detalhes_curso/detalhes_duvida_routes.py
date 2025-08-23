from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes_curso/duvidas/detalhes_duvida")
async def get_detalhes_duvida():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/detalhes_duvida.html", {"request": {}})
    return response