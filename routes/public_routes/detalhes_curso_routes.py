from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/detalhes_curso")
async def get_curso():
    response = templates.TemplateResponse("publico/detalhes_curso.html", {"request": {}})
    return response


    