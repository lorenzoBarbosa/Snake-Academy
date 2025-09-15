from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cadastro-professor")
@requer_autenticacao(["cliente"])
async def get_cadastro_professor(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("professor/cadastro_professor.html", {"request": {request}, "usuario": usuario_logado})
    return response