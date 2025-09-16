from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos")
@requer_autenticacao(["professor"])
async def get_cursos():
    response = templates.TemplateResponse("professor/cursos/cursos.html", {"request": {}})
    return response