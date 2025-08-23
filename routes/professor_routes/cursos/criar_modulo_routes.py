from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar_curso/criar_modulo")
async def get_criar_modulo():
    response = templates.TemplateResponse("professor/cursos/criar_modulo.html", {"request": {}})
    return response