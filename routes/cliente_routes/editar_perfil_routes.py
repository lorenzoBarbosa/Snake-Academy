from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/editar_perfil")
@requer_autenticacao(["cliente"])
async def get_editar_perfil(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("cliente/editar_perfil.html", {"request": request, "usuario": usuario_logado})
    return response


    