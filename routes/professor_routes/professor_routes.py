from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor")
@requer_autenticacao(["professor", "admin"])
async def get_professor(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("professor/professor.html", {"request": request, "usuario": usuario_logado})
    return response