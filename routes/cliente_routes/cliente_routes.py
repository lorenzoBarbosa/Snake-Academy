from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente")
@requer_autenticacao(["cliente"])
async def get_cliente(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse("cliente/cliente.html", {"request": request, "usuario": usuario_logado})
