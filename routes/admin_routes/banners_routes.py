from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.banner.banner_repo import *
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners")
@requer_autenticacao(["admin"])
async def get_banners(request:Request, usuario_logado: dict = None):
    banners = obter_todos_banners()
    response = templates.TemplateResponse("admin/banners/banners.html", {"request": request, "usuario": usuario_logado, "banners": banners})
    return response