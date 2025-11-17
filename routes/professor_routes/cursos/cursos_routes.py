from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos")
@requer_autenticacao(["professor"])
async def get_cursos(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("professor/cursos/cursos.html", {"request": request, "usuario_logado": usuario_logado})
    return response