from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/detalhes_curso/avaliacoes")
async def get_avaliacoes():
    response = templates.TemplateResponse("professor/cursos/detalhes_curso/avaliacoes.html", {"request": {}})
    return response