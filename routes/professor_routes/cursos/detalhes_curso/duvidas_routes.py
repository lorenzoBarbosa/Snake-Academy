from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes_curso/duvidas")
async def get_duvidas():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/duvidas.html", {"request": {}})
    return response