from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.banner.banner_repo import *
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

banners = obter_todos_banners()

@router.get("/administrador")
@requer_autenticacao(["admin"])
async def get_administrador(request:Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("administrador/administrador.html", {"request": request, "usuario": usuario_logado, "banners": banners})
    return response
